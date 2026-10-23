from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.model.dispute_defense_file import DisputeDefenseFile


class AlipayDefenseDocumentNotify(AlipayNotify):
    """Notification that a defense material is ready to download."""

    def __init__(self, notify_body):
        super(AlipayDefenseDocumentNotify, self).__init__()
        self.__dispute_id = None
        self.__notify_time = None
        self.__defense_file = None
        self.__win_rate_level = None
        self.__recommended_evidence = None
        self.__suggestions_for_improvement = None
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
    def defense_file(self):
        """Metadata of the generated material; the file body is not included."""
        return self.__defense_file

    @property
    def win_rate_level(self):
        """Optional predicted win-rate level of this material."""
        return self.__win_rate_level

    @property
    def recommended_evidence(self):
        """Optional evidence tags mapped to requirement descriptions."""
        return self.__recommended_evidence

    @property
    def suggestions_for_improvement(self):
        """Optional suggestions for improving the defense material."""
        return self.__suggestions_for_improvement

    def __parse_notify_body(self, notify_body):
        body = super(AlipayDefenseDocumentNotify, self).parse_notify_body(notify_body)
        self.__dispute_id = body.get("disputeId")
        self.__notify_time = body.get("notifyTime")
        metadata = body.get("defenseFile")
        if metadata is not None:
            self.__defense_file = DisputeDefenseFile()
            self.__defense_file.file_name = metadata.get("fileName")
            self.__defense_file.file_format = metadata.get("fileFormat")
            self.__defense_file.file_md5 = metadata.get("fileMd5")
        self.__win_rate_level = body.get("winRateLevel")
        self.__recommended_evidence = body.get("recommendedEvidence")
        self.__suggestions_for_improvement = body.get("suggestionsForImprovement")
