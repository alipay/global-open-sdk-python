import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceReviseResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__new_invoice_id = None  # type: str
        self.__voided_invoice_id = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceReviseResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def new_invoice_id(self):
        """
        The new invoice id. Maximum length: 64 characters.
        """
        return self.__new_invoice_id

    @new_invoice_id.setter
    def new_invoice_id(self, value):
        self.__new_invoice_id = value
    @property
    def voided_invoice_id(self):
        """
        The voided invoice id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__voided_invoice_id

    @voided_invoice_id.setter
    def voided_invoice_id(self, value):
        self.__voided_invoice_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "new_invoice_id") and self.new_invoice_id is not None:
            params['newInvoiceId'] = self.new_invoice_id
        if hasattr(self, "voided_invoice_id") and self.voided_invoice_id is not None:
            params['voidedInvoiceId'] = self.voided_invoice_id
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceReviseResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'newInvoiceId' in response_body:
            self.__new_invoice_id = response_body['newInvoiceId']
        if 'voidedInvoiceId' in response_body:
            self.__voided_invoice_id = response_body['voidedInvoiceId']
