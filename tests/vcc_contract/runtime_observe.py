"""Observe live Python models and exercise their real serialize/parse methods."""
import ast, importlib, json, pathlib, re,sys
root=pathlib.Path.cwd();sys.path.insert(0,str(root));request=json.load(sys.stdin)
files={};classes={};metadata={}
for path in (root/'com/alipay/ams/api').rglob('*.py'):
 if '__' in path.name:continue
 for name in re.findall(r'^class\s+(\w+)',path.read_text(),re.M):files[name]=path

def load(name):
 if name not in classes:
  path=files[name];mod=importlib.import_module('.'.join(path.relative_to(root).with_suffix('').parts));classes[name]=getattr(mod,name)
 return classes[name]

def instance(name):
 cls=load(name)
 return cls("{}") if name.endswith("Response") else cls()

def properties(name):
 if name in metadata:return metadata[name]
 cls=load(name);text=files[name].read_text();tree=ast.parse(text);node=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name==name)
 types=dict(re.findall(r'self\.__(\w+)\s*=\s*None\s*#\s*type:\s*([^\n]+)',text))
 keys={}
 for method in node.body:
  if isinstance(method,ast.FunctionDef) and method.name=='to_ams_dict':
   for assn in ast.walk(method):
    if isinstance(assn,ast.Assign) and len(assn.targets)==1 and isinstance(assn.targets[0],ast.Subscript):
     target=assn.targets[0]
     if isinstance(target.value,ast.Name) and target.value.id=='params' and isinstance(target.slice,ast.Constant):
      # Find the property accessed by the SDK serializer itself.
      attrs=[n.attr for n in ast.walk(assn.value) if isinstance(n,ast.Attribute) and isinstance(n.value,ast.Name) and n.value.id=='self']
      if attrs:keys[target.slice.value]=attrs[0]
 result={}
 for key,attr in keys.items():
  assert isinstance(getattr(cls,attr,None),property),(name,key,attr)
  assert attr in types,(name,attr)
  result[key]=(attr,types[attr].strip())
 metadata[name]=result;return result

def shape(t):
 t=t.strip()
 if t in ['str','string','datetime','datetime.datetime']:return {'type':'string'}
 if t in ['int','long']:return {'type':'integer'}
 if t in ['bool']:return {'type':'boolean'}
 if t in ['float','double','decimal.Decimal']:return {'type':'number'}
 if t.startswith('['):return {'type':'array','items':shape(t[1:-1])}
 if t.startswith('{'):return {'type':'object','additionalProperties':shape(t.split(':',1)[1].strip().strip('(){} ,')),'properties':{}}
 if t in ['object','dict']:return {'type':'object','properties':{}}
 return {'$ref':'#/components/schemas/'+t.split('.')[-1]}

def sample(t,depth=0):
 s=shape(t)
 if depth>8:return None
 if s.get('type')=='string':return 'USD'
 if s.get('type')=='integer':return 0
 if s.get('type')=='number':return 0.0
 if s.get('type')=='boolean':return False
 if s.get('type')=='array':return ['HKD','USD'] if t[1:-1].strip()=='str' else [sample(t[1:-1],depth+1)]
 if s.get('type')=='object':return {'key':'value'}
 name=s['$ref'].rsplit('/',1)[-1];v=instance(name)
 if name not in request['models']:return v
 for key,(attr,ty) in properties(name).items():setattr(v,attr,sample(ty,depth+1))
 return v

def encode(v):
 if hasattr(v,'to_ams_dict'):return v.to_ams_dict()
 raise TypeError(type(v).__name__)
models={}
for name in request['models']:
 props=properties(name);value=instance(name)
 for key,(attr,t) in props.items():setattr(value,attr,sample(t))
 wire=json.loads(json.dumps(value,default=encode));assert set(wire)==set(props),(name,wire,props)
 parsed=instance(name);parsed.parse_rsp_body(json.dumps(wire));again=json.loads(json.dumps(parsed,default=encode));assert again==wire,(name,wire,again)
 # The serializer and parser must preserve an ordered array, including empty input.
 if 'currencyOrder' in props:
  attr=props['currencyOrder'][0]
  for order in [['HKD','USD'],['USD','HKD'],[]]:
   setattr(value,attr,order);w=json.loads(json.dumps(value,default=encode));assert w['currencyOrder']==order;parsed.parse_rsp_body(json.dumps(w));assert getattr(parsed,attr)==order
 models[name]={'type':'object','properties':{key:shape(t) for key,(attr,t) in props.items()}}
bindings={}
for target in request['operations']:
 op=target.split(' ',1)[1].split('/requestBody',1)[0].split('/responses',1)[0].rsplit('/',1)[1]
 name='Alipay'+op[0].upper()+op[1:]+'Request';cls=load(name);v=cls();text=files[name].read_text();paths=re.findall(r'"(/ams/api/[^"\n]+)"',text);assert len(set(paths))==1
 response=name[:-7]+'Response';load(response) # verifies actual response model is loadable
 bindings[op]={'path':paths[0],'request':type(v).__name__,'response':load(response).__name__}
print(json.dumps({'models':models,'bindings':bindings,'evidence':['Live property/setter access; SDK to_ams_dict and parse_rsp_body roundtrip for every model member; ordered/nonordered/empty arrays; existing false and zero values']}))
