import json




class PaymentMethodInfo:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_detail = None  # type: str
        self.__enabled = None  # type: bool
        self.__preferred = None  # type: bool
        self.__extend_info = None  # type: str
        

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this PaymentMethodInfo.
        
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_detail(self):
        """Gets the payment_method_detail of this PaymentMethodInfo.
        
        """
        return self.__payment_method_detail

    @payment_method_detail.setter
    def payment_method_detail(self, value):
        self.__payment_method_detail = value
    @property
    def enabled(self):
        """Gets the enabled of this PaymentMethodInfo.
        
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value
    @property
    def preferred(self):
        """Gets the preferred of this PaymentMethodInfo.
        
        """
        return self.__preferred

    @preferred.setter
    def preferred(self, value):
        self.__preferred = value
    @property
    def extend_info(self):
        """Gets the extend_info of this PaymentMethodInfo.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_detail") and self.payment_method_detail is not None:
            params['paymentMethodDetail'] = self.payment_method_detail
        if hasattr(self, "enabled") and self.enabled is not None:
            params['enabled'] = self.enabled
        if hasattr(self, "preferred") and self.preferred is not None:
            params['preferred'] = self.preferred
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodDetail' in response_body:
            self.__payment_method_detail = response_body['paymentMethodDetail']
        if 'enabled' in response_body:
            self.__enabled = response_body['enabled']
        if 'preferred' in response_body:
            self.__preferred = response_body['preferred']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
