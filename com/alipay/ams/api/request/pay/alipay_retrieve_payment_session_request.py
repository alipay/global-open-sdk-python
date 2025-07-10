import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayRetrievePaymentSessionRequest(AlipayRequest):

    def __init__(self):
        super(AlipayRetrievePaymentSessionRequest, self).__init__(AntomPathConstants.RETRIEVE_PATH)
        self.__payment_request_id = None


    @property
    def payment_request_id(self):
        return self.__payment_request_id


    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value


    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_request_id") and self.__payment_request_id:
            params['payment_request_id'] = self.__payment_request_id
        return params