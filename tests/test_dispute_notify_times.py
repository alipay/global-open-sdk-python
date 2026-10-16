import json
import unittest

from com.alipay.ams.api.request.notify.alipay_dispute_notify import AlipayDisputeNotify


class DisputeNotifyTimesTest(unittest.TestCase):
    def test_event_times_preserve_offsets(self):
        cases = [
            ("DISPUTE_CANCELLED", "disputeCancelledTime", "dispute_cancelled_time", "2026-08-03T03:56:00+00:00"),
            ("DEFENSE_SUPPLIED", "defenseSuppliedTime", "defense_supplied_time", "2022-09-22T01:10:05-07:00"),
        ]
        for event, camel, snake, value in cases:
            for key in (camel, snake):
                notify = AlipayDisputeNotify(json.dumps({"disputeId": "d1", "disputeNotificationType": event, key: value}))
                self.assertEqual(value, getattr(notify, snake))
                self.assertEqual("d1", notify.dispute_id)
                other = "defense_supplied_time" if snake == "dispute_cancelled_time" else "dispute_cancelled_time"
                self.assertIsNone(getattr(notify, other))

    def test_legacy_and_null(self):
        for body in ({"disputeId": "legacy", "disputeTime": "2022-09-20T23:41:32-07:00"},
                     {"disputeCancelledTime": None, "defenseSuppliedTime": None}):
            notify = AlipayDisputeNotify(json.dumps(body))
            self.assertIsNone(notify.dispute_cancelled_time)
            self.assertIsNone(notify.defense_supplied_time)
            self.assertEqual(body.get("disputeTime"), notify.dispute_time)

    def test_camel_case_keeps_existing_precedence(self):
        notify = AlipayDisputeNotify(json.dumps({
            "disputeCancelledTime": "2026-08-03T03:56:00+00:00", "dispute_cancelled_time": "fallback",
            "defenseSuppliedTime": None, "defense_supplied_time": "fallback"}))
        self.assertEqual("2026-08-03T03:56:00+00:00", notify.dispute_cancelled_time)
        self.assertIsNone(notify.defense_supplied_time)


if __name__ == "__main__":
    unittest.main()
