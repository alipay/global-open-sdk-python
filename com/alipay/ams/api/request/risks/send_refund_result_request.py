import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class SendRefundResultRequest(AlipayRequest):
    def __init__(self):
        super(SendRefundResultRequest, self).__init__(
            AntomPathConstants.RISK_SEND_REFUND_RESULT_PATH
        )
        self.__reference_transaction_id = None
        self.__reference_refund_id = None
        self.__actual_refund_amount = None
        self.__refund_records = None  # type: list: RefundRecord

    @property
    def reference_transaction_id(self):
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value

    @property
    def reference_refund_id(self):
        return self.__reference_refund_id

    @reference_refund_id.setter
    def reference_refund_id(self, value):
        self.__reference_refund_id = value

    @property
    def actual_refund_amount(self):
        return self.__actual_refund_amount

    @actual_refund_amount.setter
    def actual_refund_amount(self, value):
        self.__actual_refund_amount = value

    @property
    def refund_records(self):
        return self.__refund_records

    @refund_records.setter
    def refund_records(self, value):
        self.__refund_records = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__reference_transaction_id is not None:
            params["referenceTransactionId"] = self.__reference_transaction_id
        if self.__reference_refund_id is not None:
            params["referenceRefundId"] = self.__reference_refund_id
        if self.__actual_refund_amount is not None:
            params["actualRefundAmount"] = self.__actual_refund_amount.to_ams_dict()
        if self.__refund_records is not None:
            params["refundRecords"] = [
                record.to_ams_dict() for record in self.__refund_records
            ]
        return params
