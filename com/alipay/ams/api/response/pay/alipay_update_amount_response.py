import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayUpdateAmountResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__update_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__amount = None  # type: Amount
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayUpdateAmountResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def update_request_id(self):
        """
        The unique ID that is assigned by the merchant to identify an updateAmount request. More information: Maximum length: 64 characters
        """
        return self.__update_request_id

    @update_request_id.setter
    def update_request_id(self, value):
        self.__update_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  More information: Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def amount(self):
        """Gets the amount of this AlipayUpdateAmountResponse.
        
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "update_request_id") and self.update_request_id is not None:
            params['updateRequestId'] = self.update_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayUpdateAmountResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'updateRequestId' in response_body:
            self.__update_request_id = response_body['updateRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'amount' in response_body:
            self.__amount = Amount()
            self.__amount.parse_rsp_body(response_body['amount'])
