import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.settlement_detail import SettlementDetail
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySettleRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySettleRequest, self).__init__(AntomPathConstants.MARKETPLACE_SETTLE_PATH)
        self.__settlement_request_id = None
        self.__payment_id = None
        self.__settlement_details = None #type: list[SettlementDetail]

    @property
    def settlement_request_id(self):
        return self.__settlement_request_id

    @settlement_request_id.setter
    def settlement_request_id(self, value):
        self.__settlement_request_id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def settlement_details(self):
        return self.__settlement_details

    @settlement_details.setter
    def settlement_details(self, value):
        self.__settlement_details = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, 'settlement_request_id') and self.__settlement_request_id:
            params['settlementRequestId'] = self.__settlement_request_id
        if hasattr(self, 'payment_id') and self.__payment_id:
            params['paymentId'] = self.__payment_id
        if hasattr(self, 'settlement_details') and self.__settlement_details:
            params['settlementDetails'] = self.__settlement_details
        return params