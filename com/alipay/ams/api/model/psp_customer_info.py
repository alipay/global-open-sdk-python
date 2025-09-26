import json




class PspCustomerInfo:
    def __init__(self):
        
        self.__psp_name = None  # type: str
        self.__psp_customer_id = None  # type: str
        self.__display_customer_id = None  # type: str
        self.__display_customer_name = None  # type: str
        self.__customer2088_id = None  # type: str
        self.__extend_info = None  # type: str
        

    @property
    def psp_name(self):
        """
        The name of Alipay+ payment methods.  Note: This field is returned when the Alipay+ payment methods can provide the related information.  More information:  Maximum length: 64 characters
        """
        return self.__psp_name

    @psp_name.setter
    def psp_name(self, value):
        self.__psp_name = value
    @property
    def psp_customer_id(self):
        """
        The customer ID of Alipay+ payment methods.  Note: This field is returned when the Alipay+ payment methods can provide the related information.  More information:  Maximum length: 64 characters
        """
        return self.__psp_customer_id

    @psp_customer_id.setter
    def psp_customer_id(self, value):
        self.__psp_customer_id = value
    @property
    def display_customer_id(self):
        """
        The customer ID used for display. For example, loginId.  Note: This field is returned when the Alipay+ payment methods can provide the related information.  More information:  Maximum length: 64 characters
        """
        return self.__display_customer_id

    @display_customer_id.setter
    def display_customer_id(self, value):
        self.__display_customer_id = value
    @property
    def display_customer_name(self):
        """Gets the display_customer_name of this PspCustomerInfo.
        
        """
        return self.__display_customer_name

    @display_customer_name.setter
    def display_customer_name(self, value):
        self.__display_customer_name = value
    @property
    def customer2088_id(self):
        """Gets the customer2088_id of this PspCustomerInfo.
        
        """
        return self.__customer2088_id

    @customer2088_id.setter
    def customer2088_id(self, value):
        self.__customer2088_id = value
    @property
    def extend_info(self):
        """Gets the extend_info of this PspCustomerInfo.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "psp_name") and self.psp_name is not None:
            params['pspName'] = self.psp_name
        if hasattr(self, "psp_customer_id") and self.psp_customer_id is not None:
            params['pspCustomerId'] = self.psp_customer_id
        if hasattr(self, "display_customer_id") and self.display_customer_id is not None:
            params['displayCustomerId'] = self.display_customer_id
        if hasattr(self, "display_customer_name") and self.display_customer_name is not None:
            params['displayCustomerName'] = self.display_customer_name
        if hasattr(self, "customer2088_id") and self.customer2088_id is not None:
            params['customer2088Id'] = self.customer2088_id
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'pspName' in response_body:
            self.__psp_name = response_body['pspName']
        if 'pspCustomerId' in response_body:
            self.__psp_customer_id = response_body['pspCustomerId']
        if 'displayCustomerId' in response_body:
            self.__display_customer_id = response_body['displayCustomerId']
        if 'displayCustomerName' in response_body:
            self.__display_customer_name = response_body['displayCustomerName']
        if 'customer2088Id' in response_body:
            self.__customer2088_id = response_body['customer2088Id']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
