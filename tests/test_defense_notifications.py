import json
import unittest
from com.alipay.ams.api.request.notify.alipay_defense_strategy_suggestion_notify import AlipayDefenseStrategySuggestionNotify
from com.alipay.ams.api.request.notify.alipay_defense_document_notify import AlipayDefenseDocumentNotify

STRATEGY = '{"disputeId":"d1","notifyTime":"2026-10-22T01:02:03.123+08:00","winRateLevel":"FUTURE","evidenceList":[{"evidenceTag":"FUTURE_TAG","obtained":false,"winRateContribution":"FUTURE"},{"evidenceTag":"ORDER_INFORMATION","obtained":true}],"cardholderDisputeReason":"Reason","defenseStrategyDescription":"Supply evidence","futureField":{"ignored":true}}'
DOCUMENT = '{"disputeId":"d1","notifyTime":"2026-10-22T01:02:03.123+08:00","defenseFile":{"fileName":"defense.pdf","fileFormat":"FUTURE","fileMd5":"5d41402abc4b2a76b9719d911017c592"},"winRateLevel":"FUTURE","recommendedEvidence":{"FUTURE_TAG":"提供材料","ORDER_INFORMATION":"Order proof"},"suggestionsForImprovement":"Add proof"}'

class DefenseNotificationsTest(unittest.TestCase):
    def test_strategy(self):
        n = AlipayDefenseStrategySuggestionNotify(STRATEGY)
        self.assertEqual(n.dispute_id, 'd1')
        self.assertEqual(n.notify_time, '2026-10-22T01:02:03.123+08:00')
        self.assertEqual(n.win_rate_level, 'FUTURE')
        self.assertEqual(n.cardholder_dispute_reason, 'Reason')
        self.assertEqual(n.defense_strategy_description, 'Supply evidence')
        self.assertIs(n.evidence_list[0].obtained, False)
        self.assertIs(n.evidence_list[1].obtained, True)
        self.assertEqual(n.evidence_list[0].evidence_tag, 'FUTURE_TAG')
        self.assertEqual(n.evidence_list[0].win_rate_contribution, 'FUTURE')
        self.assertIsNone(n.evidence_list[1].win_rate_contribution)

    def test_document(self):
        n = AlipayDefenseDocumentNotify(DOCUMENT)
        self.assertEqual(n.dispute_id, 'd1')
        self.assertEqual(n.notify_time, '2026-10-22T01:02:03.123+08:00')
        self.assertEqual(n.defense_file.file_name, 'defense.pdf')
        self.assertEqual(n.defense_file.file_format, 'FUTURE')
        self.assertEqual(n.defense_file.file_md5, '5d41402abc4b2a76b9719d911017c592')
        self.assertEqual(n.win_rate_level, 'FUTURE')
        self.assertEqual(n.recommended_evidence['FUTURE_TAG'], '提供材料')
        self.assertEqual(n.suggestions_for_improvement, 'Add proof')

    def test_missing_and_null_optionals(self):
        for val in ({}, {'winRateLevel': None, 'recommendedEvidence': None, 'suggestionsForImprovement': None}):
            n = AlipayDefenseDocumentNotify(json.dumps(val))
            self.assertIsNone(n.win_rate_level)
            self.assertIsNone(n.recommended_evidence)
            self.assertIsNone(n.suggestions_for_improvement)
            self.assertIsNone(n.defense_file)
        n = AlipayDefenseStrategySuggestionNotify('{"evidenceList":[{"evidenceTag":"X"}]}')
        self.assertIsNone(n.evidence_list[0].obtained)
        self.assertIsNone(n.cardholder_dispute_reason)

if __name__ == '__main__':
    unittest.main()
