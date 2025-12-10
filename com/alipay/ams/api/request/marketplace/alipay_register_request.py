import json
from com.alipay.ams.api.model.settlement_info import SettlementInfo
from com.alipay.ams.api.model.merchant_info import MerchantInfo
from com.alipay.ams.api.model.payment_method import PaymentMethod



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayRegisterRequest(AlipayRequest):
    def __init__(self):
        super(AlipayRegisterRequest, self).__init__("/ams/api/v1/merchants/register") 

        self.__registration_request_id = None  # type: str
        self.__settlement_infos = None  # type: [SettlementInfo]
        self.__merchant_info = None  # type: MerchantInfo
        self.__payment_methods = None  # type: [PaymentMethod]
        

    @property
    def registration_request_id(self):
        """
        The unique ID that is assigned by the marketplace to identify a registration request. Alipay uses this field for idempotence control.  More information:  This field is an API idempotency field.For registration requests that are initiated with the same value of registrationRequestId and reach a final status (resultStatus &#x3D; S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__registration_request_id

    @registration_request_id.setter
    def registration_request_id(self, value):
        self.__registration_request_id = value
    @property
    def settlement_infos(self):
        """
        The list of sub-merchants&#39; settlement information. One settlement currency corresponds to one settlement bank account.  More information:  Maximum size: 10 elements
        """
        return self.__settlement_infos

    @settlement_infos.setter
    def settlement_infos(self, value):
        self.__settlement_infos = value
    @property
    def merchant_info(self):
        """Gets the merchant_info of this AlipayRegisterRequest.
        
        """
        return self.__merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        self.__merchant_info = value
    @property
    def payment_methods(self):
        """
        The payment method that is used to collect the payment by the merchant or acquirer. The payment method must be already supportd by the platform merchant before they can be assigned for sub-merchants.  More information:  Maximum length: 100 characters
        """
        return self.__payment_methods

    @payment_methods.setter
    def payment_methods(self, value):
        self.__payment_methods = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "registration_request_id") and self.registration_request_id is not None:
            params['registrationRequestId'] = self.registration_request_id
        if hasattr(self, "settlement_infos") and self.settlement_infos is not None:
            params['settlementInfos'] = self.settlement_infos
        if hasattr(self, "merchant_info") and self.merchant_info is not None:
            params['merchantInfo'] = self.merchant_info
        if hasattr(self, "payment_methods") and self.payment_methods is not None:
            params['paymentMethods'] = self.payment_methods
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'registrationRequestId' in response_body:
            self.__registration_request_id = response_body['registrationRequestId']
        if 'settlementInfos' in response_body:
            self.__settlement_infos = []
            for item in response_body['settlementInfos']:
                obj = SettlementInfo()
                obj.parse_rsp_body(item)
                self.__settlement_infos.append(obj)
        if 'merchantInfo' in response_body:
            self.__merchant_info = MerchantInfo()
            self.__merchant_info.parse_rsp_body(response_body['merchantInfo'])
        if 'paymentMethods' in response_body:
            self.__payment_methods = []
            for item in response_body['paymentMethods']:
                obj = PaymentMethod()
                obj.parse_rsp_body(item)
                self.__payment_methods.append(obj)
