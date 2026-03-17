import json
from com.alipay.ams.api.model.refund_from_method import RefundFromMethod
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateDirectRefundRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateDirectRefundRequest, self).__init__("/ams/aba/funds/createDirectRefund") 

        self.__payment_id = None  # type: str
        self.__refund_request_id = None  # type: str
        self.__reference_refund_id = None  # type: str
        self.__refund_from_method = None  # type: RefundFromMethod
        self.__refund_from_amount = None  # type: Amount
        self.__memo = None  # type: str
        self.__remark = None  # type: str
        self.__refund_reason = None  # type: str
        self.__refund_notify_url = None  # type: str
        

    @property
    def payment_id(self):
        """
        The unique ID assigned by Antom for the original payment to be refunded.  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def refund_request_id(self):
        """
        The unique ID assigned by the merchant to identify a refund request.  More information:  This field is an API idempotency field. The merchant uses the refundRequestId field for idempotency control. For requests that are initiated with the same value of refundRequestId and reach a final status (S or F), the same result is to be returned for the request.  Maximum length: 64 characters
        """
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value
    @property
    def reference_refund_id(self):
        """
        The unique ID to identify a refund, which is assigned by the merchant that directly provides services or goods to the customer.  Note: Specify this field if this value is needed for internal use or reconciliation.  More information:  Maximum length: 64 characters
        """
        return self.__reference_refund_id

    @reference_refund_id.setter
    def reference_refund_id(self, value):
        self.__reference_refund_id = value
    @property
    def refund_from_method(self):
        """Gets the refund_from_method of this AlipayCreateDirectRefundRequest.
        
        """
        return self.__refund_from_method

    @refund_from_method.setter
    def refund_from_method(self, value):
        self.__refund_from_method = value
    @property
    def refund_from_amount(self):
        """Gets the refund_from_amount of this AlipayCreateDirectRefundRequest.
        
        """
        return self.__refund_from_amount

    @refund_from_amount.setter
    def refund_from_amount(self, value):
        self.__refund_from_amount = value
    @property
    def memo(self):
        """
        The memo for the refund request.  Note: Specify this field if you want to provide additional information about the refund.  More information:  Maximum length: 256 characters
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def remark(self):
        """
        The remark for the refund request.  Note: Specify this field if you want to provide additional remarks about the refund.  More information:  Maximum length: 256 characters
        """
        return self.__remark

    @remark.setter
    def remark(self, value):
        self.__remark = value
    @property
    def refund_reason(self):
        """
        The refund reason.  Note: Specify this field if you want to provide the refund reason to the user and payment method.  More information:  Maximum length: 256 characters
        """
        return self.__refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self.__refund_reason = value
    @property
    def refund_notify_url(self):
        """
        The URL that is used to receive the refund result notification. The URL must be either specified in the request or set in Antom Dashboard.  Note: Specify this field if you want to receive an asynchronous notification of the refund result. If the refund notification URL is specified in both the request and Antom Dashboard, the value specified in the request takes precedence.  More information:  Maximum length: 1024 characters
        """
        return self.__refund_notify_url

    @refund_notify_url.setter
    def refund_notify_url(self, value):
        self.__refund_notify_url = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "refund_request_id") and self.refund_request_id is not None:
            params['refundRequestId'] = self.refund_request_id
        if hasattr(self, "reference_refund_id") and self.reference_refund_id is not None:
            params['referenceRefundId'] = self.reference_refund_id
        if hasattr(self, "refund_from_method") and self.refund_from_method is not None:
            params['refundFromMethod'] = self.refund_from_method
        if hasattr(self, "refund_from_amount") and self.refund_from_amount is not None:
            params['refundFromAmount'] = self.refund_from_amount
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "remark") and self.remark is not None:
            params['remark'] = self.remark
        if hasattr(self, "refund_reason") and self.refund_reason is not None:
            params['refundReason'] = self.refund_reason
        if hasattr(self, "refund_notify_url") and self.refund_notify_url is not None:
            params['refundNotifyUrl'] = self.refund_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'refundRequestId' in response_body:
            self.__refund_request_id = response_body['refundRequestId']
        if 'referenceRefundId' in response_body:
            self.__reference_refund_id = response_body['referenceRefundId']
        if 'refundFromMethod' in response_body:
            self.__refund_from_method = RefundFromMethod()
            self.__refund_from_method.parse_rsp_body(response_body['refundFromMethod'])
        if 'refundFromAmount' in response_body:
            self.__refund_from_amount = Amount()
            self.__refund_from_amount.parse_rsp_body(response_body['refundFromAmount'])
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'remark' in response_body:
            self.__remark = response_body['remark']
        if 'refundReason' in response_body:
            self.__refund_reason = response_body['refundReason']
        if 'refundNotifyUrl' in response_body:
            self.__refund_notify_url = response_body['refundNotifyUrl']
