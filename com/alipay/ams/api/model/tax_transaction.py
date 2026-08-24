import json




class TaxTransaction:
    def __init__(self):
        
        self.__tax_transaction_id = None  # type: str
        self.__tax_calculation_id = None  # type: str
        self.__type = None  # type: str
        self.__tax_amount = None  # type: str
        self.__currency = None  # type: str
        self.__status = None  # type: str
        self.__failure_reason = None  # type: str
        self.__tax_date = None  # type: str
        self.__posted_at = None  # type: str
        self.__reference_payment_id = None  # type: str
        self.__reference_refund_id = None  # type: str
        

    @property
    def tax_transaction_id(self):
        """
        The unique ID assigned by Antom to identify a tax transaction. Maximum length: 64 characters.
        """
        return self.__tax_transaction_id

    @tax_transaction_id.setter
    def tax_transaction_id(self, value):
        self.__tax_transaction_id = value
    @property
    def tax_calculation_id(self):
        """
        The unique ID assigned by Antom to identify a tax calculation. Maximum length: 64 characters.
        """
        return self.__tax_calculation_id

    @tax_calculation_id.setter
    def tax_calculation_id(self, value):
        self.__tax_calculation_id = value
    @property
    def type(self):
        """
        The type. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def tax_amount(self):
        """
        The non-negative tax amount in the smallest currency unit, without leading zeros. For TRANSACTION and REVERSAL records, this value is always a positive absolute amount. Reconcile a business scope by subtracting the sum of REVERSAL amounts from the sum of TRANSACTION amounts. Maximum length: 19 characters.
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def currency(self):
        """
        The 3-letter currency code that follows the ISO 4217 standard. This field is returned together with taxAmount. Maximum length: 3 characters.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def failure_reason(self):
        """
        The failure reason. Maximum length: 256 characters. Note: See documentation for details.
        """
        return self.__failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self.__failure_reason = value
    @property
    def tax_date(self):
        """
        The tax date. Maximum length: 32 characters.
        """
        return self.__tax_date

    @tax_date.setter
    def tax_date(self, value):
        self.__tax_date = value
    @property
    def posted_at(self):
        """
        The time when the tax transaction was posted. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__posted_at

    @posted_at.setter
    def posted_at(self, value):
        self.__posted_at = value
    @property
    def reference_payment_id(self):
        """
        The reference payment ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__reference_payment_id

    @reference_payment_id.setter
    def reference_payment_id(self, value):
        self.__reference_payment_id = value
    @property
    def reference_refund_id(self):
        """
        The reference refund ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__reference_refund_id

    @reference_refund_id.setter
    def reference_refund_id(self, value):
        self.__reference_refund_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "tax_transaction_id") and self.tax_transaction_id is not None:
            params['taxTransactionId'] = self.tax_transaction_id
        if hasattr(self, "tax_calculation_id") and self.tax_calculation_id is not None:
            params['taxCalculationId'] = self.tax_calculation_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "failure_reason") and self.failure_reason is not None:
            params['failureReason'] = self.failure_reason
        if hasattr(self, "tax_date") and self.tax_date is not None:
            params['taxDate'] = self.tax_date
        if hasattr(self, "posted_at") and self.posted_at is not None:
            params['postedAt'] = self.posted_at
        if hasattr(self, "reference_payment_id") and self.reference_payment_id is not None:
            params['referencePaymentId'] = self.reference_payment_id
        if hasattr(self, "reference_refund_id") and self.reference_refund_id is not None:
            params['referenceRefundId'] = self.reference_refund_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'taxTransactionId' in response_body:
            self.__tax_transaction_id = response_body['taxTransactionId']
        if 'taxCalculationId' in response_body:
            self.__tax_calculation_id = response_body['taxCalculationId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'taxAmount' in response_body:
            self.__tax_amount = response_body['taxAmount']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'failureReason' in response_body:
            self.__failure_reason = response_body['failureReason']
        if 'taxDate' in response_body:
            self.__tax_date = response_body['taxDate']
        if 'postedAt' in response_body:
            self.__posted_at = response_body['postedAt']
        if 'referencePaymentId' in response_body:
            self.__reference_payment_id = response_body['referencePaymentId']
        if 'referenceRefundId' in response_body:
            self.__reference_refund_id = response_body['referenceRefundId']
