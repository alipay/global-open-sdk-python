import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.merchant_info import MerchantInfo
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.settlement_info import SettlementInfo
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayRegisterRequest(AlipayRequest):
    def __init__(self):
        super(AlipayRegisterRequest,self).__init__(AntomPathConstants.MARKETPLACE_REGISTER_PATH)
        self.__registration_request_id = None
        self.__settlement_infos = None #type: list[SettlementInfo]
        self.__merchant_info = None #type: MerchantInfo
        self.__payment_methods = None #type: list[PaymentMethod]

    @property
    def registration_request_id(self):
        return self.__registration_request_id

    @registration_request_id.setter
    def registration_request_id(self, value):
        self.__registration_request_id = value

    @property
    def settlement_infos(self):
        return self.__settlement_infos

    @settlement_infos.setter
    def settlement_infos(self, value):
        self.__settlement_infos = value

    @property
    def merchant_info(self):
        return self.__merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        self.__merchant_info = value

    @property
    def payment_methods(self):
        return self.__payment_methods

    @payment_methods.setter
    def payment_methods(self, value):
        self.__payment_methods = value


    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, 'registration_request_id') and self.registration_request_id:
            params['registrationRequestId'] = self.registration_request_id
        if hasattr(self, 'settlement_infos') and self.settlement_infos:
            params['settlementInfos'] = self.settlement_infos
        if hasattr(self, 'merchant_info') and self.merchant_info:
            params['merchantInfo'] = self.merchant_info
        if hasattr(self, 'payment_methods') and self.payment_methods:
            params['paymentMethods'] = self.payment_methods
        return params
