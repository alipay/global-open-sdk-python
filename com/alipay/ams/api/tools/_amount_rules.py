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
        if root.get("schemaVersion") != 1:
            raise RuntimeError("unsupported schema")
        currencies = root.get("currencies")
        constraints = root.get("antomConstraints")
        if not isinstance(currencies, dict) or not isinstance(constraints, dict):
            raise RuntimeError("invalid structure")
        _RULES = (_freeze(currencies), _freeze(constraints))
        return _RULES
    except RuntimeError as exception:
        raise RuntimeError("RULE_DATA_ERROR: {0}".format(exception))
    except Exception as exception:
        raise RuntimeError("RULE_DATA_ERROR: unable to load amount currency rules: {0}".format(exception))
