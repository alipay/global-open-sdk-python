import json
from com.alipay.ams.api.model.code_detail import CodeDetail




class OrderCodeForm:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__expire_time = None  # type: str
        self.__code_details = None  # type: [CodeDetail]
        self.__extend_info = None  # type: str
        

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this OrderCodeForm.
        
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def expire_time(self):
        """
        Expiry time of the order code information.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__expire_time

    @expire_time.setter
    def expire_time(self, value):
        self.__expire_time = value
    @property
    def code_details(self):
        """
        Details about the code.  More information:  Maximum size: 4 elements
        """
        return self.__code_details

    @code_details.setter
    def code_details(self, value):
        self.__code_details = value
    @property
    def extend_info(self):
        """
        Extended information.  Note: This field is returned when extended information exists.  More information:  Maximum length: 2048 characters
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "expire_time") and self.expire_time is not None:
            params['expireTime'] = self.expire_time
        if hasattr(self, "code_details") and self.code_details is not None:
            params['codeDetails'] = self.code_details
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'expireTime' in response_body:
            self.__expire_time = response_body['expireTime']
        if 'codeDetails' in response_body:
            self.__code_details = []
            for item in response_body['codeDetails']:
                obj = CodeDetail()
                obj.parse_rsp_body(item)
                self.__code_details.append(obj)
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
