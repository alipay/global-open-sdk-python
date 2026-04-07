import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.subscription_transaction import SubscriptionTransaction
from com.alipay.ams.api.model.paginator import Paginator



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireSubscriptionPaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payments = None  # type: [SubscriptionTransaction]
        self.__paginator = None  # type: Paginator
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireSubscriptionPaymentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payments(self):
        """
        List of transactions of the specified subscriptionId. Can be EMPTY if no criteria match or subscriptionId is not exists.
        """
        return self.__payments

    @payments.setter
    def payments(self, value):
        self.__payments = value
    @property
    def paginator(self):
        """Gets the paginator of this AlipayInquireSubscriptionPaymentResponse.
        
        """
        return self.__paginator

    @paginator.setter
    def paginator(self, value):
        self.__paginator = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payments") and self.payments is not None:
            params['payments'] = self.payments
        if hasattr(self, "paginator") and self.paginator is not None:
            params['paginator'] = self.paginator
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireSubscriptionPaymentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'payments' in response_body:
            self.__payments = []
            for item in response_body['payments']:
                obj = SubscriptionTransaction()
                obj.parse_rsp_body(item)
                self.__payments.append(obj)
        if 'paginator' in response_body:
            self.__paginator = Paginator()
            self.__paginator.parse_rsp_body(response_body['paginator'])
