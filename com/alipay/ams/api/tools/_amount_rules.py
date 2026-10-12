from __future__ import absolute_import

import json
import pkgutil

_RULES = None


class _FrozenDict(dict):
    def _immutable(self, *args, **kwargs):
        raise TypeError("amount currency rules are immutable")

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    pop = _immutable
    popitem = _immutable
    setdefault = _immutable
    update = _immutable


def _freeze(value):
    if isinstance(value, dict):
        return _FrozenDict((key, _freeze(item)) for key, item in value.items())
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def get_rules():
    global _RULES
    if _RULES is not None:
        return _RULES
    try:
        data = pkgutil.get_data(__package__, "resources/amount-currency-rules.json")
        if data is None:
            raise RuntimeError("resource is missing")
        root = json.loads(data.decode("utf-8"))
        if not isinstance(root, dict) or type(root.get("schemaVersion")) is not int or root["schemaVersion"] != 1:
            raise RuntimeError("unsupported schema")
        currencies = root.get("currencies")
        constraints = root.get("antomConstraints")
        if not isinstance(currencies, dict) or not currencies or not isinstance(constraints, dict):
            raise RuntimeError("invalid structure")
        for rule in currencies.values():
            if not isinstance(rule, dict) or type(rule.get("minorUnit")) is not int or not 0 <= rule["minorUnit"] <= 4:
                raise RuntimeError("invalid minor unit")
        for constraint in constraints.values():
            if not isinstance(constraint, dict):
                raise RuntimeError("invalid amount constraint")
            multiple = constraint.get("minorValueMultiple")
            if not isinstance(multiple, str) or not multiple.startswith("1") or multiple[1:].strip("0"):
                raise RuntimeError("invalid amount constraint")
        _RULES = (_freeze(currencies), _freeze(constraints))
        return _RULES
    except RuntimeError as exception:
        raise RuntimeError("RULE_DATA_ERROR: {0}".format(exception))
    except Exception as exception:
        raise RuntimeError("RULE_DATA_ERROR: unable to load amount currency rules") from exception
