import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxInquireCalculationRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxInquireCalculationRequest, self).__init__("/ams/api/v1/tax/inquireCalculation") 

        self.__tax_calculation_id = None  # type: str
        self.__tax_calculation_request_id = None  # type: str
        self.__payment_request_id = None  # type: str
        

    @property
    def tax_calculation_id(self):
        """
        The tax calculation ID returned by a successful calculate request. Specify exactly one of taxCalculationId, taxCalculationRequestId, and paymentRequestId. Maximum length: 64 characters.
        """
        return self.__tax_calculation_id

    @tax_calculation_id.setter
    def tax_calculation_id(self, value):
        self.__tax_calculation_id = value
    @property
    def tax_calculation_request_id(self):
        """
        The original tax calculation request ID. Use this field to recover an unknown, timed-out, or lost calculate response. Specify exactly one query key. Maximum length: 64 characters.
        """
        return self.__tax_calculation_request_id

    @tax_calculation_request_id.setter
    def tax_calculation_request_id(self, value):
        self.__tax_calculation_request_id = value
    @property
    def payment_request_id(self):
        """
        The payment request ID associated with the tax calculation. Use this field only when the payment references the calculation. Specify exactly one query key. Maximum length: 64 characters.
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "tax_calculation_id") and self.tax_calculation_id is not None:
            params['taxCalculationId'] = self.tax_calculation_id
        if hasattr(self, "tax_calculation_request_id") and self.tax_calculation_request_id is not None:
            params['taxCalculationRequestId'] = self.tax_calculation_request_id
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'taxCalculationId' in response_body:
            self.__tax_calculation_id = response_body['taxCalculationId']
        if 'taxCalculationRequestId' in response_body:
            self.__tax_calculation_request_id = response_body['taxCalculationRequestId']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
