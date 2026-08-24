import json
from com.alipay.ams.api.model.inquiry_rate_condition import InquiryRateCondition



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryRateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryRateRequest, self).__init__("/ams/api/v1/aba/funds/inquireRate") 

        self.__rate_condition_list = None  # type: [InquiryRateCondition]
        self.__test_request_id = None  # type: str
        

    @property
    def rate_condition_list(self):
        """Gets the rate_condition_list of this AlipayInquiryRateRequest.
        
        """
        return self.__rate_condition_list

    @rate_condition_list.setter
    def rate_condition_list(self, value):
        self.__rate_condition_list = value
    @property
    def test_request_id(self):
        """
        5.14测试
        """
        return self.__test_request_id

    @test_request_id.setter
    def test_request_id(self, value):
        self.__test_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "rate_condition_list") and self.rate_condition_list is not None:
            params['rateConditionList'] = self.rate_condition_list
        if hasattr(self, "test_request_id") and self.test_request_id is not None:
            params['testRequestId'] = self.test_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'rateConditionList' in response_body:
            self.__rate_condition_list = []
            for item in response_body['rateConditionList']:
                obj = InquiryRateCondition()
                obj.parse_rsp_body(item)
                self.__rate_condition_list.append(obj)
        if 'testRequestId' in response_body:
            self.__test_request_id = response_body['testRequestId']
