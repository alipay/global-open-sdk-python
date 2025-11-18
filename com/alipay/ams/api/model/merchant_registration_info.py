from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.logo import Logo
from com.alipay.ams.api.model.registration_detail import RegistrationDetail
from com.alipay.ams.api.model.web_site import WebSite


class MerchantRegistrationInfo(object):
    def __init__(self):
        self.__reference_merchant_id = None
        self.__merchant_display_name = None
        self.__merchant_mcc = None
        self.__logo = None  # type: Logo
        self.__websites = None  # type: list[WebSite]
        self.__merchant_address = None  # type: Address
        self.__registration_detail = None  # type: RegistrationDetail

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def merchant_display_name(self):
        return self.__merchant_display_name

    @merchant_display_name.setter
    def merchant_display_name(self, value):
        self.__merchant_display_name = value

    @property
    def merchant_mcc(self):
        return self.__merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self.__merchant_mcc = value

    @property
    def logo(self):
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    @property
    def websites(self):
        return self.__websites

    @websites.setter
    def websites(self, value):
        self.__websites = value

    @property
    def merchant_address(self):
        return self.__merchant_address

    @merchant_address.setter
    def merchant_address(self, value):
        self.__merchant_address = value

    @property
    def registration_detail(self):
        return self.__registration_detail

    @registration_detail.setter
    def registration_detail(self, value):
        self.__registration_detail = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id:
            params["referenceMerchantId"] = self.reference_merchant_id

        if hasattr(self, "merchant_display_name") and self.merchant_display_name:
            params["merchantDisplayName"] = self.merchant_display_name

        if hasattr(self, "merchant_mcc") and self.merchant_mcc:
            params["merchantMCC"] = self.merchant_mcc

        if hasattr(self, "logo") and self.logo:
            params["logo"] = self.logo

        if hasattr(self, "websites") and self.websites:
            params["websites"] = self.websites

        if hasattr(self, "merchant_address") and self.merchant_address:
            params["merchantAddress"] = self.merchant_address

        if hasattr(self, "registration_detail") and self.registration_detail:
            params["registrationDetail"] = self.registration_detail

        return params
