import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.subscription_info import SubscriptionInfo
from com.alipay.ams.api.model.paginator import Paginator



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireSubscriptionListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__subscriptions = None  # type: [SubscriptionInfo]
        self.__paginator = None  # type: Paginator
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireSubscriptionListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscriptions(self):
        """
        List of subscriptions that match the criteria.
        """
        return self.__subscriptions

    @subscriptions.setter
    def subscriptions(self, value):
        self.__subscriptions = value
    @property
    def paginator(self):
        """Gets the paginator of this AlipayInquireSubscriptionListResponse.
        
        """
        return self.__paginator

    @paginator.setter
    def paginator(self, value):
        self.__paginator = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscriptions") and self.subscriptions is not None:
            params['subscriptions'] = self.subscriptions
        if hasattr(self, "paginator") and self.paginator is not None:
            params['paginator'] = self.paginator
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireSubscriptionListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptions' in response_body:
            self.__subscriptions = []
            for item in response_body['subscriptions']:
                obj = SubscriptionInfo()
                obj.parse_rsp_body(item)
                self.__subscriptions.append(obj)
        if 'paginator' in response_body:
            self.__paginator = Paginator()
            self.__paginator.parse_rsp_body(response_body['paginator'])
