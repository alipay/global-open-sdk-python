import json
import re
import unittest
from pathlib import Path

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.event_merchant_info import EventMerchantInfo
from com.alipay.ams.api.request.notify.alipay_card_transaction_event_notify import (
    AlipayCardTransactionEventNotify,
)


class CardTransactionEventNotifyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads(
            (Path(__file__).parent / "resources/card-transaction-event-notify.json").read_text()
        )

    def test_all_fields_and_nested_models(self):
        fields = ["eventId","lifecycleId","eventType","authTime","authExpireTime","authType","authCode","failureReason","status","balanceType","transactionTime","billType","outAmount","inAmount","exchangeCurrencyPair","exchangeRate","transactionAmount","assetId","maskedCardNo","cardProduct","merchantInfo","metadata"]
        self.assertEqual(22, len([
            name for name, value in vars(AlipayCardTransactionEventNotify).items()
            if isinstance(value, property)
        ]))
        for fixture in self.fixtures:
            with self.subTest(fixture=fixture["name"]):
                body = dict(fixture["body"], futureField={"ignored": True})
                notify = AlipayCardTransactionEventNotify(json.dumps(body))
                for key in fields:
                    name = re.sub(r"[A-Z]", lambda match: "_" + match[0].lower(), key)
                    value = getattr(notify, name)
                    expected = fixture["body"].get(key)
                    if key in ("outAmount", "inAmount", "transactionAmount") and expected is not None:
                        self.assertIsInstance(value, Amount)
                        self.assertEqual(expected, value.to_ams_dict())
                        self.assertIsInstance(value.value, str)
                    elif key == "merchantInfo" and expected is not None:
                        self.assertIsInstance(value, EventMerchantInfo)
                        self.assertEqual(expected, value.to_ams_dict())
                    else:
                        self.assertEqual(expected, value)
                self.assertFalse(hasattr(notify, "event"))
                self.assertFalse(hasattr(notify, "future_field"))

    def test_capture_and_auth_preserve_profile(self):
        auth = AlipayCardTransactionEventNotify(json.dumps(self.fixtures[0]["body"]))
        self.assertIsNone(auth.auth_time)
        capture = AlipayCardTransactionEventNotify(json.dumps(self.fixtures[1]["body"]))
        self.assertEqual("0", capture.out_amount.value)
        self.assertEqual("USD", capture.out_amount.currency)
        self.assertEqual("30000", capture.transaction_amount.value)
        self.assertEqual("2026-07-09T10:35:10+00:00", capture.auth_time)
        self.assertEqual("ANTOM_BIZ_ACCOUNT", capture.balance_type)
        self.assertIsNone(capture.in_amount)

    def test_setters_follow_notify_convention(self):
        notify = AlipayCardTransactionEventNotify("{}")
        notify.event_id = "setter"
        self.assertEqual("setter", notify.event_id)
        self.assertIsNone(notify.metadata)


if __name__ == "__main__":
    unittest.main()
