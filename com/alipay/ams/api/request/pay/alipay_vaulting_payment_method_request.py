import json
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.customized_info import CustomizedInfo



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayVaultingPaymentMethodRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVaultingPaymentMethodRequest, self).__init__("/ams/api/v1/vaults/vaultPaymentMethod") 

        self.__merchant_account_id = None  # type: str
        self.__metadata = None  # type: str
        self.__vaulting_request_id = None  # type: str
        self.__vaulting_notification_url = None  # type: str
        self.__redirect_url = None  # type: str
        self.__merchant_region = None  # type: str
        self.__payment_method_detail = None  # type: PaymentMethodDetail
        self.__env = None  # type: Env
        self.__vaulting_currency = None  # type: str
        self.__customized_info = None  # type: CustomizedInfo
        

    @property
    def merchant_account_id(self):
        """
        一点集成场景使用
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def metadata(self):
        """
        商户使用，Json Format，用于提交元数据信息
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def vaulting_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a card vaulting request.   More information:  This field is an API idempotency field.For vaulting requests that are initiated with the same value of vaultingRequestId and reach a final status of S or F, the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__vaulting_request_id

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value
    @property
    def vaulting_notification_url(self):
        """
        The URL that is used to receive the vaulting result notification.   More information:  Maximum length: 2048 characters
        """
        return self.__vaulting_notification_url

    @vaulting_notification_url.setter
    def vaulting_notification_url(self, value):
        self.__vaulting_notification_url = value
    @property
    def redirect_url(self):
        """
        The merchant page URL that the buyer is redirected to after the vaulting process is completed.  More information:  Maximum length: 2048 characters 
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value
    @property
    def merchant_region(self):
        """
        The country or region where the merchant operates the business. The value of this parameter is a 2-letter country or region code based on the ISO 3166 Country Codes standard.   Some possible values are US, SG, HK, PK, JP, CN, BR, AU, and MY.  Note: Specify this parameter when you use the Global Acquirer Gateway (GAGW) product.  More information:  Maximum length: 2 characters
        """
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value
    @property
    def payment_method_detail(self):
        """Gets the payment_method_detail of this AlipayVaultingPaymentMethodRequest.
        
        """
        return self.__payment_method_detail

    @payment_method_detail.setter
    def payment_method_detail(self, value):
        self.__payment_method_detail = value
    @property
    def env(self):
        """Gets the env of this AlipayVaultingPaymentMethodRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def vaulting_currency(self):
        """Gets the vaulting_currency of this AlipayVaultingPaymentMethodRequest.
        
        """
        return self.__vaulting_currency

    @vaulting_currency.setter
    def vaulting_currency(self, value):
        self.__vaulting_currency = value
    @property
    def customized_info(self):
        """Gets the customized_info of this AlipayVaultingPaymentMethodRequest.
        
        """
        return self.__customized_info

    @customized_info.setter
    def customized_info(self, value):
        self.__customized_info = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "vaulting_request_id") and self.vaulting_request_id is not None:
            params['vaultingRequestId'] = self.vaulting_request_id
        if hasattr(self, "vaulting_notification_url") and self.vaulting_notification_url is not None:
            params['vaultingNotificationUrl'] = self.vaulting_notification_url
        if hasattr(self, "redirect_url") and self.redirect_url is not None:
            params['redirectUrl'] = self.redirect_url
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "payment_method_detail") and self.payment_method_detail is not None:
            params['paymentMethodDetail'] = self.payment_method_detail
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "vaulting_currency") and self.vaulting_currency is not None:
            params['vaultingCurrency'] = self.vaulting_currency
        if hasattr(self, "customized_info") and self.customized_info is not None:
            params['customizedInfo'] = self.customized_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'vaultingRequestId' in response_body:
            self.__vaulting_request_id = response_body['vaultingRequestId']
        if 'vaultingNotificationUrl' in response_body:
            self.__vaulting_notification_url = response_body['vaultingNotificationUrl']
        if 'redirectUrl' in response_body:
            self.__redirect_url = response_body['redirectUrl']
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
        if 'paymentMethodDetail' in response_body:
            self.__payment_method_detail = PaymentMethodDetail()
            self.__payment_method_detail.parse_rsp_body(response_body['paymentMethodDetail'])
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'vaultingCurrency' in response_body:
            self.__vaulting_currency = response_body['vaultingCurrency']
        if 'customizedInfo' in response_body:
            self.__customized_info = CustomizedInfo()
            self.__customized_info.parse_rsp_body(response_body['customizedInfo'])
