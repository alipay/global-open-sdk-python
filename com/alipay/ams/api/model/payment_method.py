import json




class PaymentMethod:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_id = None  # type: str
        self.__payment_method_meta_data = None  # type: {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
        self.__customer_id = None  # type: str
        self.__extend_info = None  # type: str
        self.__require_issuer_authentication = None  # type: bool
        

    @property
    def payment_method_type(self):
        """
        The payment method that is used to accept the subscription payment. See Payment methods to check the valid values.    Note: Card payment method is not currently supported when you work with Antom as your acquirer.  More information:  Maximum length: 64 characters
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_id(self):
        """
        The unique ID that is used to identify a payment method.  Pass the corresponding token to this field when the user has a bound payment method.  More information:  Maximum length: 128 characters 
        """
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value
    @property
    def payment_method_meta_data(self):
        """Gets the payment_method_meta_data of this PaymentMethod.
        
        """
        return self.__payment_method_meta_data

    @payment_method_meta_data.setter
    def payment_method_meta_data(self, value):
        self.__payment_method_meta_data = value
    @property
    def customer_id(self):
        """Gets the customer_id of this PaymentMethod.
        
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def extend_info(self):
        """Gets the extend_info of this PaymentMethod.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def require_issuer_authentication(self):
        """Gets the require_issuer_authentication of this PaymentMethod.
        
        """
        return self.__require_issuer_authentication

    @require_issuer_authentication.setter
    def require_issuer_authentication(self, value):
        self.__require_issuer_authentication = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_id") and self.payment_method_id is not None:
            params['paymentMethodId'] = self.payment_method_id
        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data is not None:
            params['paymentMethodMetaData'] = self.payment_method_meta_data
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "require_issuer_authentication") and self.require_issuer_authentication is not None:
            params['requireIssuerAuthentication'] = self.require_issuer_authentication
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodId' in response_body:
            self.__payment_method_id = response_body['paymentMethodId']
        if 'paymentMethodMetaData' in response_body:
            self.__payment_method_meta_data = response_body['paymentMethodMetaData']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'requireIssuerAuthentication' in response_body:
            self.__require_issuer_authentication = response_body['requireIssuerAuthentication']
