import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxInquireTransactionListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxInquireTransactionListRequest, self).__init__("/ams/api/v1/tax/inquireTransactionList") 

        self.__tax_calculation_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__refund_id = None  # type: str
        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        

    @property
    def tax_calculation_id(self):
        """
        The unique ID assigned by Antom to identify a tax calculation. Exactly one of taxCalculationId, paymentId, and refundId must be provided. Omit the unused query keys; do not send them with null values. Maximum length: 64 characters.
        """
        return self.__tax_calculation_id

    @tax_calculation_id.setter
    def tax_calculation_id(self, value):
        self.__tax_calculation_id = value
    @property
    def payment_id(self):
        """
        The unique ID assigned by Antom to identify a payment. Exactly one of taxCalculationId, paymentId, and refundId must be provided. Omit the unused query keys; do not send them with null values. Maximum length: 64 characters.
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def refund_id(self):
        """
        The unique ID assigned by Antom to identify a refund. Exactly one of taxCalculationId, paymentId, and refundId must be provided. Omit the unused query keys; do not send them with null values. Maximum length: 64 characters.
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def current_page(self):
        """
        The current page number.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The number of records per page.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "tax_calculation_id") and self.tax_calculation_id is not None:
            params['taxCalculationId'] = self.tax_calculation_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'taxCalculationId' in response_body:
            self.__tax_calculation_id = response_body['taxCalculationId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
