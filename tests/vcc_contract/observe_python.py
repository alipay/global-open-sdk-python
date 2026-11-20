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
    types = dict(re.findall(r'self\.__(\w+)\s*=.*?# type:\s*([^\n]+)', text))
    keys = dict((prop, key) for key, prop in re.findall(r"params\[['\"]([^'\"]+)['\"]\]\s*=\s*self\.(\w+)", text))
    return types, keys


def sample(typ):
    if typ.startswith('['): return ['HKD', 'USD']
    if typ.startswith('{'): return {'probe': 'value'}
    if typ == 'str': return 'probe'
    if typ == 'int': return 0
    if typ == 'float': return 0.0
    if typ == 'bool': return False
    return make(typ)


def wire(obj):
    return json.loads(json.dumps(obj.to_ams_dict(), default=lambda value: value.to_ams_dict()))


req = json.load(sys.stdin)
models = {}
for name in req['models']:
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
    models[name] = {'type': 'object', 'properties': props}

for name in ['ApplyCardPaymentPreference', 'CardPaymentPreference']:
    empty = make(name)
    assert wire(empty) == {}
    empty.currency_order = []
    assert wire(empty)['currencyOrder'] == []
    empty.currency_order = ['HKD', 'USD']
    assert wire(empty)['currencyOrder'] == ['HKD', 'USD']
    empty.currency_order = None
    assert 'currencyOrder' not in wire(empty)  # existing SDK null omission, not fabricated null support

create = make('AlipayApplyCardRequest')
control = make('ApplyCardAuthorizationControl')
create.authorization_control = control
assert wire(create)['authorizationControl'] == {}
control.payment_preference = make('ApplyCardPaymentPreference')
assert wire(create)['authorizationControl']['paymentPreference'] == {}
for name, prefix in [('AlipayInquireCardDetailResponse', []), ('AlipayInquireCardSensitiveInfoResponse', ['cardDetail'])]:
    payload = {'authorizationControl': {'paymentPreference': {'currencyOrder': ['HKD', 'USD']}}}
    if prefix: payload = {'cardDetail': payload}
    obj = make(name); obj.parse_rsp_body(json.dumps(payload))
    restored = wire(obj)
    nested = restored['cardDetail'] if prefix else restored
    assert nested['authorizationControl']['paymentPreference']['currencyOrder'] == ['HKD', 'USD']

bindings = []
for stem in ['ApplyCard', 'InquireCardDetail', 'InquireCardSensitiveInfo']:
    obj = make('Alipay' + stem + 'Request')
    # Real base stores the path/method as private attributes; getters are public SDK API.
    path = obj.path
    method = obj.http_method.value
    response = cls('Alipay' + stem + 'Response')
    bindings.append({'path': path, 'method': method, 'request': obj.__class__.__name__, 'response': response.__name__})
json.dump({'models': models, 'bindings': bindings, 'wire_checks': len(models),
           'evidence': ['Real Python model setters, to_ams_dict and parse_rsp_body; ordered/empty arrays and empty/omitted policy; nested sensitive parsing']}, sys.stdout)
