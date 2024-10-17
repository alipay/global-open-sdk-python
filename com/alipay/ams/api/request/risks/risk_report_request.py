import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class RiskReportRequest(AlipayRequest):

    def __init__(self):
        super(RiskReportRequest, self).__init__(AntomPathConstants.RISK_REPORT_PATH)
        self.__reference_transaction_id = None
        self.__report_reason = None
        self.__risk_type = None
        self.__risk_occurrence_time = None

    @property
    def reference_transaction_id(self):
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value

    @property
    def report_reason(self):
        return self.__report_reason

    @report_reason.setter
    def report_reason(self, value):
        self.__report_reason = value

    @property
    def risk_type(self):
        return self.__risk_type

    @risk_type.setter
    def risk_type(self, value):
        self.__risk_type = value

    @property
    def risk_occurrence_time(self):
        return self.__risk_occurrence_time

    @risk_occurrence_time.setter
    def risk_occurrence_time(self, value):
        self.__risk_occurrence_time = value

    def to_ams_dict(self):
        ams_dict = super(RiskReportRequest, self)

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__reference_transaction_id is not None:
            params['referenceTransactionId'] = self.__reference_transaction_id
        if self.__report_reason is not None:
            params['reportReason'] = self.__report_reason
        if self.__risk_type is not None:
            params['riskType'] = self.__risk_type
        if self.__risk_occurrence_time is not None:
            params['riskOccurrenceTime'] = self.__risk_occurrence_time
        return params