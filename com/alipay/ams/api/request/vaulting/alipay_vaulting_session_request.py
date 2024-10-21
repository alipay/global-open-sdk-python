import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayVaultingSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVaultingSessionRequest, self).__init__(AntomPathConstants.CREATE_VAULTING_SESSION_PATH)
        self.__payment_method_type = None
        self.__vaulting_request_id = None
        self.__vaulting_notification_url = None
        self.__redirect_url = None
        self.__merchant_region = None
        self.__is_3D_s_authentication = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @property
    def vaulting_request_id(self):
        return self.__vaulting_request_id

    @property
    def vaulting_notification_url(self):
        return self.__vaulting_notification_url

    @property
    def redirect_url(self):
        return self.__redirect_url

    @property
    def merchant_region(self):
        return self.__merchant_region

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value

    @vaulting_notification_url.setter
    def vaulting_notification_url(self, value):
        self.__vaulting_notification_url = value

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def is_3D_s_authentication(self):
        return self.__is_3D_s_authentication

    @is_3D_s_authentication.setter
    def is_3D_s_authentication(self, value):
        self.__is_3D_s_authentication = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "vaulting_request_id") and self.vaulting_request_id:
            params['vaultingRequestId'] = self.vaulting_request_id
        if hasattr(self, "vaulting_notification_url") and self.vaulting_notification_url:
            params['vaultingNotificationUrl'] = self.vaulting_notification_url
        if hasattr(self, "redirect_url") and self.redirect_url:
            params['redirectUrl'] = self.redirect_url
        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "is_3D_s_authentication") and self.is_3D_s_authentication:
            params['is3DSAuthentication'] = self.is_3D_s_authentication

        return params
