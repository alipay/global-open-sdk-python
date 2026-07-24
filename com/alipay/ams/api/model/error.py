import json




class Error:
    def __init__(self):
        
        self.__index = None  # type: int
        self.__group_index = None  # type: int
        self.__event_name = None  # type: str
        self.__idempotency_key = None  # type: str
        self.__customer_id = None  # type: str
        self.__error_code = None  # type: str
        

    @property
    def index(self):
        """
        The index.
        """
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value
    @property
    def group_index(self):
        """
        The group index. Note: See documentation for details.
        """
        return self.__group_index

    @group_index.setter
    def group_index(self, value):
        self.__group_index = value
    @property
    def event_name(self):
        """
        The event name. Maximum length: 128 characters.
        """
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value
    @property
    def idempotency_key(self):
        """
        The idempotency key. Maximum length: 128 characters.
        """
        return self.__idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, value):
        self.__idempotency_key = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 128 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def error_code(self):
        """
        The error code. Maximum length: 64 characters.
        """
        return self.__error_code

    @error_code.setter
    def error_code(self, value):
        self.__error_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "index") and self.index is not None:
            params['index'] = self.index
        if hasattr(self, "group_index") and self.group_index is not None:
            params['groupIndex'] = self.group_index
        if hasattr(self, "event_name") and self.event_name is not None:
            params['eventName'] = self.event_name
        if hasattr(self, "idempotency_key") and self.idempotency_key is not None:
            params['idempotencyKey'] = self.idempotency_key
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "error_code") and self.error_code is not None:
            params['errorCode'] = self.error_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'index' in response_body:
            self.__index = response_body['index']
        if 'groupIndex' in response_body:
            self.__group_index = response_body['groupIndex']
        if 'eventName' in response_body:
            self.__event_name = response_body['eventName']
        if 'idempotencyKey' in response_body:
            self.__idempotency_key = response_body['idempotencyKey']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'errorCode' in response_body:
            self.__error_code = response_body['errorCode']
