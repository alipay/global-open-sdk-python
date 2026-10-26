import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.ams_inquiry_payment_result import AmsInquiryPaymentResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireBatchPaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__batch_payment_request_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_create_time = None  # type: str
        self.__payment_method_type = None  # type: str
        self.__redirect_action_form = None  # type: RedirectActionForm
        self.__psp_customer_info = None  # type: PspCustomerInfo
        self.__payment_time = None  # type: str
        self.__auth_expirytime = None  # type: str
        self.__customs_declaration_amount = None  # type: Amount
        self.__payment_results = None  # type: [AmsInquiryPaymentResult]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireBatchPaymentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def batch_payment_request_id(self):
        """
        Echo of queried batch ID (maximum 64 characters), returned when result.resultStatus is S.
        """
        return self.__batch_payment_request_id

    @batch_payment_request_id.setter
    def batch_payment_request_id(self, value):
        self.__batch_payment_request_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayInquireBatchPaymentResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_create_time(self):
        """
        Batch payment creation time in ISO 8601 format, returned on successful inquiry.
        """
        return self.__payment_create_time

    @payment_create_time.setter
    def payment_create_time(self, value):
        self.__payment_create_time = value
    @property
    def payment_method_type(self):
        """
        Payment method type (maximum 64 characters), for example ALIPAY_CN; returned with Checkout Page integration.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def redirect_action_form(self):
        """Gets the redirect_action_form of this AlipayInquireBatchPaymentResponse.
        
        """
        return self.__redirect_action_form

    @redirect_action_form.setter
    def redirect_action_form(self, value):
        self.__redirect_action_form = value
    @property
    def psp_customer_info(self):
        """Gets the psp_customer_info of this AlipayInquireBatchPaymentResponse.
        
        """
        return self.__psp_customer_info

    @psp_customer_info.setter
    def psp_customer_info(self, value):
        self.__psp_customer_info = value
    @property
    def payment_time(self):
        """
        ISO 8601 time when the batch payment reached final success; the start of cancellation and refund eligibility periods.
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def auth_expirytime(self):
        """
        Authorization expiration time, returned when paymentMethodType is CARD.
        """
        return self.__auth_expirytime

    @auth_expirytime.setter
    def auth_expirytime(self, value):
        self.__auth_expirytime = value
    @property
    def customs_declaration_amount(self):
        """Gets the customs_declaration_amount of this AlipayInquireBatchPaymentResponse.
        
        """
        return self.__customs_declaration_amount

    @customs_declaration_amount.setter
    def customs_declaration_amount(self, value):
        self.__customs_declaration_amount = value
    @property
    def payment_results(self):
        """
        Sub-order payment summaries, returned when result.resultStatus is S.
        """
        return self.__payment_results

    @payment_results.setter
    def payment_results(self, value):
        self.__payment_results = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "batch_payment_request_id") and self.batch_payment_request_id is not None:
            params['batchPaymentRequestId'] = self.batch_payment_request_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_create_time") and self.payment_create_time is not None:
            params['paymentCreateTime'] = self.payment_create_time
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "redirect_action_form") and self.redirect_action_form is not None:
            params['redirectActionForm'] = self.redirect_action_form
        if hasattr(self, "psp_customer_info") and self.psp_customer_info is not None:
            params['pspCustomerInfo'] = self.psp_customer_info
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "auth_expirytime") and self.auth_expirytime is not None:
            params['authExpirytime'] = self.auth_expirytime
        if hasattr(self, "customs_declaration_amount") and self.customs_declaration_amount is not None:
            params['customsDeclarationAmount'] = self.customs_declaration_amount
        if hasattr(self, "payment_results") and self.payment_results is not None:
            params['paymentResults'] = self.payment_results
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireBatchPaymentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'batchPaymentRequestId' in response_body:
            self.__batch_payment_request_id = response_body['batchPaymentRequestId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentCreateTime' in response_body:
            self.__payment_create_time = response_body['paymentCreateTime']
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'redirectActionForm' in response_body:
            self.__redirect_action_form = RedirectActionForm()
            self.__redirect_action_form.parse_rsp_body(response_body['redirectActionForm'])
        if 'pspCustomerInfo' in response_body:
            self.__psp_customer_info = PspCustomerInfo()
            self.__psp_customer_info.parse_rsp_body(response_body['pspCustomerInfo'])
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'authExpirytime' in response_body:
            self.__auth_expirytime = response_body['authExpirytime']
        if 'customsDeclarationAmount' in response_body:
            self.__customs_declaration_amount = Amount()
            self.__customs_declaration_amount.parse_rsp_body(response_body['customsDeclarationAmount'])
        if 'paymentResults' in response_body:
            self.__payment_results = []
            for item in response_body['paymentResults']:
                obj = AmsInquiryPaymentResult()
                obj.parse_rsp_body(item)
                self.__payment_results.append(obj)
