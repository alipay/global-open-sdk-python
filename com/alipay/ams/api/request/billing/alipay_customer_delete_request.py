import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCustomerDeleteRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomerDeleteRequest, self).__init__("/ams/api/v1/billing/customer/delete") 

        self.__customer_id = None  # type: str
        

    @property
    def customer_id(self):
        """
        System-generated customer ID to delete. Cannot be empty. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
