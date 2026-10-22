from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.model.dispute_evidence_recommendation import DisputeEvidenceRecommendation


class AlipayDefenseStrategySuggestionNotify(AlipayNotify):
    """Defense strategy and recommended evidence for a dispute."""

    def __init__(self, notify_body):
        super(AlipayDefenseStrategySuggestionNotify, self).__init__()
        self.__dispute_id = None
        self.__notify_time = None
        self.__win_rate_level = None
        self.__evidence_list = None
        self.__cardholder_dispute_reason = None
        self.__defense_strategy_description = None
        self.__parse_notify_body(notify_body)

    @property
    def dispute_id(self):
        """Dispute ID."""
        return self.__dispute_id

    @property
    def notify_time(self):
        """Notification time as an ISO 8601 string with timezone."""
        return self.__notify_time

    @property
    def win_rate_level(self):
        """Predicted win-rate level: HIGH, MEDIUM or LOW."""
        return self.__win_rate_level

    @property
    def evidence_list(self):
        """Recommended evidence items, from 1 to 32 entries."""
        return self.__evidence_list

    @property
    def cardholder_dispute_reason(self):
        """Optional cardholder dispute reason."""
        return self.__cardholder_dispute_reason

    @property
    def defense_strategy_description(self):
        """Suggested defense strategy."""
        return self.__defense_strategy_description

    def __parse_notify_body(self, notify_body):
        body = super(AlipayDefenseStrategySuggestionNotify, self).parse_notify_body(notify_body)
        self.__dispute_id = body.get("disputeId")
        self.__notify_time = body.get("notifyTime")
        self.__win_rate_level = body.get("winRateLevel")
        items = body.get("evidenceList")
        if items is not None:
            self.__evidence_list = []
            for item in items:
                evidence = DisputeEvidenceRecommendation()
                evidence.evidence_tag = item.get("evidenceTag")
                evidence.obtained = item.get("obtained")
                evidence.win_rate_contribution = item.get("winRateContribution")
                self.__evidence_list.append(evidence)
        self.__cardholder_dispute_reason = body.get("cardholderDisputeReason")
        self.__defense_strategy_description = body.get("defenseStrategyDescription")
