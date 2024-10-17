import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayMerchantRegistrationRequest(AlipayRequest):

    def __init__(self):
        super(AlipayMerchantRegistrationRequest, self).__init__(AntomPathConstants.MERCHANTS_REGISTRATION_PATH)
        self.__product_codes = None
        self.__registration_request_id = None
        self.__registration_notify_url = None
        self.__merchant_info = None
        self.__pass_through_info = None

    @property
    def product_codes(self):
        return self.__product_codes

    @product_codes.setter
    def product_codes(self, value):
        self.__product_codes = value

    @property
    def registration_request_id(self):
        return self.__registration_request_id

    @registration_request_id.setter
    def registration_request_id(self, value):
        self.__registration_request_id = value

    @property
    def registration_notify_url(self):
        return self.__registration_notify_url

    @registration_notify_url.setter
    def registration_notify_url(self, value):
        self.__registration_notify_url = value

    @property
    def merchant_info(self):
        return self.__merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        self.__merchant_info = value

    @property
    def pass_through_info(self):
        return self.__pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self.__pass_through_info = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=10)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_codes") and self.product_codes:
            params['productCodes'] = self.product_codes

        if hasattr(self, "registration_request_id") and self.registration_request_id:
            params['registrationRequestId'] = self.registration_request_id

        if hasattr(self, "registration_notify_url") and self.registration_notify_url:
            params['registrationNotifyURL'] = self.registration_notify_url

        if hasattr(self, "merchant_info") and self.merchant_info:
            params['merchantInfo'] = self.merchant_info

        if hasattr(self, "pass_through_info") and self.pass_through_info:
            params['passThroughInfo'] = self.pass_through_info

        return params
