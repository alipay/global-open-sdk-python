import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayVaultingPaymentMethodRequest(AlipayRequest):
    
    def __init__(self):
        super(AlipayVaultingPaymentMethodRequest, self).__init__(AntomPathConstants.VAULT_PAYMENT_METHOD_PATH)
        self.__vaulting_request_id = None
        self.__vaulting_notification_url = None
        self.__redirect_url = None
        self.__merchant_region = None
        self.__payment_method_detail = None # type: PaymentMethodDetail
        self.__env = None # type: Env

    @property
    def vaulting_request_id(self):
        return self.__vaulting_request_id

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value

    @property
    def vaulting_notification_url(self):
        return self.__vaulting_notification_url

    @vaulting_notification_url.setter
    def vaulting_notification_url(self, value):
        self.__vaulting_notification_url = value

    @property
    def redirect_url(self):
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def payment_method_detail(self):
        return self.__payment_method_detail

    @payment_method_detail.setter
    def payment_method_detail(self, value):
        self.__payment_method_detail = value
    @property
    def env(self):
        return self.__env
    @env.setter
    def env(self, value):
        self.__env = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__vaulting_request_id is not None:
            params['vaultingRequestId'] = self.__vaulting_request_id
        if self.__vaulting_notification_url is not None:
            params['vaultingNotificationUrl'] = self.__vaulting_notification_url
        if self.__redirect_url is not None:
            params['redirectUrl'] = self.__redirect_url
        if self.__merchant_region is not None:
            params['merchantRegion'] = self.__merchant_region
        if self.__payment_method_detail is not None:
            params['paymentMethodDetail'] = self.__payment_method_detail.to_ams_dict()
        if self.__env is not None:
            params['env'] = self.__env.to_ams_dict()
        return params