import ast
import importlib
import inspect
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path.cwd()))
catalog = {}
for path in Path('com/alipay/ams/api').rglob('*.py'):
    for name in re.findall(r'^class (\w+)', path.read_text(), re.M):
        catalog[name] = path


def cls(name):
    path = catalog[name]
    return getattr(importlib.import_module('.'.join(path.with_suffix('').parts)), name)


def make(name):
    target = cls(name)
    required = [p for p in inspect.signature(target).parameters.values()
                if p.default is inspect.Parameter.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    return target('{}') if required else target()


def shape(typ):
    typ = typ.strip()
    if typ.startswith('['):
        return {'type': 'array', 'items': shape(typ[1:-1])}
    if typ.startswith('{'):
        return {'type': 'object', 'additionalProperties': {'type': 'string'}, 'properties': {}}
    if typ in {'str', 'int', 'float', 'bool'}:
        return {'type': {'str': 'string', 'int': 'integer', 'float': 'number', 'bool': 'boolean'}[typ]}
    return {'$ref': '#/components/schemas/' + typ}


def info(name):
    text = catalog[name].read_text()
    types = {k:v.replace(', none_type','') for k,v in re.findall(r'self\.__(\w+)\s*=.*?# type:\s*([^\n]+)', text)}
    keys = dict((prop, key) for key, prop in re.findall(r"params\[['\"]([^'\"]+)['\"]\]\s*=\s*self\.(\w+)", text))
    return types, keys


def sample(typ):
    if typ.startswith('['): return [sample(typ[1:-1]), sample(typ[1:-1])]
    if typ.startswith('{'): return {'probe': 'value'}
    if typ == 'str': return 'probe'
    if typ == 'int': return 0
    if typ == 'float': return 0.0
    if typ == 'bool': return False
    import enum
    target=cls(typ)
    if issubclass(target, enum.Enum): return next(iter(target))
    return make(typ)


def wire(obj):
    return json.loads(json.dumps(obj.to_ams_dict(), default=lambda value: value.to_ams_dict()))


req = json.load(sys.stdin)
models = {}
for target in req['models']:
    name = target.rsplit('/', 1)[-1]
    types, keys = info(name)
    assert set(types) == set(keys), (name, types, keys)
    obj = make(name)
    props = {}
    for attr, typ in types.items():
        setattr(obj, attr, sample(typ))
        props[keys[attr]] = shape(typ)
    body = wire(obj)
    assert set(body) == set(props), (name, body, props)
    restored = make(name)
    restored.parse_rsp_body(json.dumps(body))
    assert wire(restored) == body, (name, 'roundtrip')
    models[target] = {'type': 'object', 'properties': props}


evidence = []
if 'ConsultBuyer' in catalog:
    for value in ('true', 'false'):
        buyer = make('ConsultBuyer')
        buyer.buyer_access_group_flag = value
        assert wire(buyer)['buyerAccessGroupFlag'] == value
        assert isinstance(wire(buyer)['buyerAccessGroupFlag'], str)
        request = make('AlipayPayConsultRequest')
        request.buyer = buyer
        assert wire(request)['buyer']['buyerAccessGroupFlag'] == value
    buyer.buyer_access_group_flag = None
    assert 'buyerAccessGroupFlag' not in wire(buyer)
    evidence.append('Actual consult request serializes buyer true/false as strings; unset/null flag omitted')
for name in catalog:
    if not name.endswith('Response') or 'credit_note_ids' not in info(name)[0]:
        continue
    for data in ({}, {'creditNoteIds':None}, {'creditNoteId':'cn_a','creditNoteIds':['cn_a'],'creditNoteAmount':'3000','creditNoteCurrency':'USD'}, {'creditNoteIds':['cn_a','cn_z'],'creditNoteAmount':'8000','creditNoteCurrency':'USD'}, {'creditNoteIds':[]}):
        obj = make(name); obj.parse_rsp_body(json.dumps(data)); actual = wire(obj)
        for key, value in data.items():
            if value is not None:
                assert actual[key] == value, (name, key, value, actual)
    evidence.append('Actual subscription response parses single/multi/empty/absent/null lists, preserves ID order, scalar and string amount')
paths = {key.split(' ',1)[1].split('/requestBody/',1)[0].split('/responses/',1)[0] for key in req['operation_keys']}
bindings = []
for name, path in catalog.items():
    if not name.endswith('Request') or name == 'AlipayRequest':
        continue
    if not any(p in path.read_text() for p in paths):
        continue
    try:
        obj = make(name)
        if obj.path not in paths: continue
        response = cls(name[:-7]+'Response')
        bindings.append({'path':obj.path, 'method':obj.http_method.value, 'request':name, 'response':response.__name__})
    except (AttributeError, TypeError, KeyError):
        continue
json.dump({'models':models,'bindings':bindings,'wire_checks':len(models),'evidence':evidence},sys.stdout)
