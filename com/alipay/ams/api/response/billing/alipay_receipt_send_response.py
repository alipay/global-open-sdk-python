import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayReceiptSendResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__receipt_id = None  # type: str
        self.__send_status = None  # type: str
        self.__hosted_receipt_url = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayReceiptSendResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def receipt_id(self):
        """
        The receipt ID. Maximum length: 64 characters.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def send_status(self):
        """
        The email sending status. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__send_status

    @send_status.setter
    def send_status(self, value):
        self.__send_status = value
    @property
    def hosted_receipt_url(self):
        """
        The hosted receipt url. Maximum length: 2048 characters.
        """
        return self.__hosted_receipt_url

    @hosted_receipt_url.setter
    def hosted_receipt_url(self, value):
        self.__hosted_receipt_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        if hasattr(self, "hosted_receipt_url") and self.hosted_receipt_url is not None:
            params['hostedReceiptUrl'] = self.hosted_receipt_url
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayReceiptSendResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
        if 'hostedReceiptUrl' in response_body:
            self.__hosted_receipt_url = response_body['hostedReceiptUrl']
