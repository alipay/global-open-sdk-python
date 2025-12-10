import json
from com.alipay.ams.api.model.funding_type import FundingType




class PaymentMethod:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_id = None  # type: str
        self.__funding = None  # type: FundingType
        self.__customer_id = None  # type: str
        self.__extend_info = None  # type: str
        self.__require_issuer_authentication = None  # type: bool
        self.__payment_method_meta_data = None  # type: {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
        

    @property
    def payment_method_type(self):
        """
        The payment method type that is included in payment method options. By specifying the value of this parameter, you can receive the cashier URL of the specified payment method returned by Alipay. See Payment methods to check the valid values.  More information:  Maximum length: 64 characters
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_id(self):
        """
        The unique ID that is used to identify a payment method. The value of this parameter is that of cardToken obtained from the notifyPayment or inquiryPayment API.   Specify this parameter when the value of paymentMethodType is CARD.  More information:  Maximum length: 128 characters
        """
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value
    @property
    def funding(self):
        """Gets the funding of this PaymentMethod.
        
        """
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value
    @property
    def customer_id(self):
        """
        The unique ID to identify a buyer.  Note: Specify this field if you have the information. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def extend_info(self):
        """
        Extended information.  Note: Specify this field if you need to use the extended information.  More information:  Maximum length: 2048 characters
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def require_issuer_authentication(self):
        """
        Indicates whether Korean card transactions require authentication from the issuing bank. Valid values are:  true: indicates that Korean card transactions require authentication from the issuing bank. false: indicates that Korean card transactions do not require authentication from the issuing bank. The same applies when you do not specify this parameter or the value is empty. Specify this parameter when all the following conditions are met:  The value of paymentMethodType is CARD. The value of paymentMethodRegion is KR. The Korean card transactions require issuer authentication.
        """
        return self.__require_issuer_authentication

    @require_issuer_authentication.setter
    def require_issuer_authentication(self, value):
        self.__require_issuer_authentication = value
    @property
    def payment_method_meta_data(self):
        """
        Additional information required for some specific payment methods.  
        """
        return self.__payment_method_meta_data

    @payment_method_meta_data.setter
    def payment_method_meta_data(self, value):
        self.__payment_method_meta_data = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_id") and self.payment_method_id is not None:
            params['paymentMethodId'] = self.payment_method_id
        if hasattr(self, "funding") and self.funding is not None:
            params['funding'] = self.funding
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "require_issuer_authentication") and self.require_issuer_authentication is not None:
            params['requireIssuerAuthentication'] = self.require_issuer_authentication
        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data is not None:
            params['paymentMethodMetaData'] = self.payment_method_meta_data
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodId' in response_body:
            self.__payment_method_id = response_body['paymentMethodId']
        if 'funding' in response_body:
            funding_temp = FundingType.value_of(response_body['funding'])
            self.__funding = funding_temp
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'requireIssuerAuthentication' in response_body:
            self.__require_issuer_authentication = response_body['requireIssuerAuthentication']
        if 'paymentMethodMetaData' in response_body:
            self.__payment_method_meta_data = response_body['paymentMethodMetaData']
