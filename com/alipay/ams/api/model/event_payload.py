import json




class EventPayload:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__customer_id = None  # type: str
        

    @property
    def value(self):
        """
        The value of the amount as a positive integer in the smallest currency unit. Maximum length: 32 characters.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 128 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'value' in response_body:
            self.__value = response_body['value']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
