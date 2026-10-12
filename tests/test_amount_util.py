from __future__ import absolute_import

import json
import os
import unittest

from com.alipay.ams.api.tools.amount_util import from_amount, to_amount, validate
from com.alipay.ams.api.tools._amount_rules import get_rules


class AmountUtilTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.join(os.path.dirname(__file__), "resources", "amount-conversion-test-cases.json")
        with open(path, "r") as stream:
            cls.vectors = json.load(stream)

    def test_shared_vectors(self):
        for vector in self.vectors["toAmount"]:
            self._check(vector, lambda: to_amount(vector["amount"], vector["currency"]))
        for vector in self.vectors["fromAmount"]:
            self._check(vector, lambda: from_amount(vector["value"], vector["currency"]))
        for vector in self.vectors["validate"]:
            self._check(vector, lambda: validate(vector["value"], vector["currency"]))

    def test_dynamic_types_are_rejected(self):
        invalid_values = [1, 1.0, True, None]
        if bytes is not str:
            invalid_values.append(b"1")
        for value in invalid_values:
            with self._assert_raises_pattern(TypeError, "^INVALID_ARGUMENT_TYPE:"):
                to_amount(value, "USD")
        with self._assert_raises_pattern(TypeError, "^INVALID_ARGUMENT_TYPE:"):
            validate("1", 123)

    def test_successful_outbound_vectors_round_trip_exactly(self):
        for vector in self.vectors["toAmount"]:
            if "result" in vector:
                value = vector["result"]
                self.assertEqual(value, to_amount(from_amount(value, vector["currency"]), vector["currency"]))

    def test_trailing_newline_is_rejected(self):
        with self._assert_raises_pattern(ValueError, "^INVALID_AMOUNT_FORMAT:"):
            to_amount("1\n", "USD")

    def test_rules_are_immutable(self):
        with self.assertRaises(TypeError):
            get_rules()[0]["USD"] = {"minorUnit": 0}

    def _check(self, vector, call):
        if "error" in vector:
            with self._assert_raises_pattern(ValueError, "^" + vector["error"] + ":"):
                call()
        else:
            actual = call()
            if "result" in vector:
                self.assertEqual(vector["result"], actual, vector["name"])

    def _assert_raises_pattern(self, exception, pattern):
        method = getattr(self, "assertRaisesRegex", None)
        if method is None:
            method = self.assertRaisesRegexp
        return method(exception, pattern)


if __name__ == "__main__":
    unittest.main()
