import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceSendResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__send_status = None  # type: str
        self.__hosted_invoice_url = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceSendResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def send_status(self):
        """
        The email sending status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__send_status

    @send_status.setter
    def send_status(self, value):
        self.__send_status = value
    @property
    def hosted_invoice_url(self):
        """
        The hosted invoice url. Maximum length: 2048 characters.
        """
        return self.__hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, value):
        self.__hosted_invoice_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        if hasattr(self, "hosted_invoice_url") and self.hosted_invoice_url is not None:
            params['hostedInvoiceUrl'] = self.hosted_invoice_url
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceSendResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
        if 'hostedInvoiceUrl' in response_body:
            self.__hosted_invoice_url = response_body['hostedInvoiceUrl']
