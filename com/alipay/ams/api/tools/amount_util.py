from __future__ import absolute_import

import re

from ._amount_rules import get_rules

try:
    _STRING_TYPES = (basestring,)
except NameError:
    _STRING_TYPES = (str,)

_CURRENCY = re.compile(r"^[A-Z]{3}\Z")
_AMOUNT = re.compile(r"^[0-9]+(?:\.[0-9]+)?\Z")
_VALUE = re.compile(r"^[0-9]+\Z")


def to_amount(amount, currency):
    minor_unit = _minor_unit(currency)
    _require_string(amount, "amount")
    if not _AMOUNT.match(amount):
        _fail("INVALID_AMOUNT_FORMAT", "amount must be an unsigned ASCII decimal string")
    parts = amount.split(".", 1)
    whole = parts[0]
    fraction = parts[1] if len(parts) == 2 else ""
    if len(fraction) > minor_unit:
        if any(character != "0" for character in fraction[minor_unit:]):
            _fail("EXCESS_PRECISION", "amount exceeds the currency minor unit")
        fraction = fraction[:minor_unit]
    fraction += "0" * (minor_unit - len(fraction))
    value = (whole + fraction).lstrip("0") or "0"
    _validate_canonical(value, currency)
    return value


def from_amount(value, currency):
    minor_unit = _minor_unit(currency)
    _validate_value_format(value)
    canonical = value.lstrip("0") or "0"
    if minor_unit == 0:
        return canonical
    padded = canonical.rjust(minor_unit + 1, "0")
    return padded[:-minor_unit] + "." + padded[-minor_unit:]


def validate(value, currency):
    _minor_unit(currency)
    _validate_value_format(value)
    _validate_canonical(value, currency)


def _minor_unit(currency):
    _require_string(currency, "currency")
    if not _CURRENCY.match(currency):
        _fail("INVALID_CURRENCY", "currency must be three uppercase ASCII letters")
    currencies, _ = get_rules()
    if currency not in currencies:
        _fail("UNKNOWN_CURRENCY", "currency is not present in the ISO snapshot")
    minor_unit = currencies[currency].get("minorUnit")
    if minor_unit is None:
        _fail("UNSUPPORTED_MINOR_UNIT", "currency has no numeric minor unit")
    if isinstance(minor_unit, bool) or not isinstance(minor_unit, int) or minor_unit < 0 or minor_unit > 4:
        raise RuntimeError("RULE_DATA_ERROR: invalid minor unit")
    return minor_unit


def _validate_value_format(value):
    _require_string(value, "value")
    if not _VALUE.match(value):
        _fail("INVALID_VALUE_FORMAT", "value must contain ASCII digits only")
    if len(value) > 16:
        _fail("VALUE_TOO_LONG", "value exceeds 16 digits")


def _validate_canonical(value, currency):
    if not value.strip("0"):
        _fail("AMOUNT_NOT_POSITIVE", "value must be greater than zero")
    if len(value) > 16:
        _fail("VALUE_TOO_LONG", "value exceeds 16 digits")
    _, constraints = get_rules()
    constraint = constraints.get(currency)
    if constraint:
        multiple = constraint.get("minorValueMultiple")
        if not isinstance(multiple, _STRING_TYPES) or not re.match(r"^10*\Z", multiple):
            raise RuntimeError("RULE_DATA_ERROR: invalid amount constraint")
        if not value.endswith(multiple[1:]):
            _fail("RULE_VIOLATION", "value does not satisfy the Antom currency constraint")


def _require_string(value, name):
    if not isinstance(value, _STRING_TYPES):
        raise TypeError("INVALID_ARGUMENT_TYPE: {0} must be a string".format(name))


def _fail(category, detail):
    raise ValueError("{0}: {1}".format(category, detail))
