import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayRefundQueryRequest(AlipayRequest):

    def __init__(self):
        super(AlipayRefundQueryRequest, self).__init__(
            AntomPathConstants.INQUIRY_REFUND_PATH
        )
        self.__refund_request_id = None
        self.__refund_id = None
        self.__merchant_account_id = None

    @property
    def refund_request_id(self):
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value

    @property
    def refund_id(self):
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value

    @property
    def merchant_account_id(self):
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "refund_request_id") and self.refund_request_id:
            params["refundRequestId"] = self.refund_request_id
        if hasattr(self, "refund_id") and self.refund_id:
            params["refundId"] = self.refund_id
        if hasattr(self, "merchant_account_id") and self.merchant_account_id:
            params["merchantAccountId"] = self.merchant_account_id
        return params
