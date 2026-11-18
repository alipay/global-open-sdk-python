import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.subscription_info import SubscriptionInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireSubscriptionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__subscription = None  # type: SubscriptionInfo
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireSubscriptionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscription(self):
        """Gets the subscription of this AlipayInquireSubscriptionResponse.
        
        """
        return self.__subscription

    @subscription.setter
    def subscription(self, value):
        self.__subscription = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription") and self.subscription is not None:
            params['subscription'] = self.subscription
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireSubscriptionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscription' in response_body:
            self.__subscription = SubscriptionInfo()
            self.__subscription.parse_rsp_body(response_body['subscription'])
