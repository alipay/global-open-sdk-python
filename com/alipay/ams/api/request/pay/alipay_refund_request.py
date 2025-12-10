import json
from com.alipay.ams.api.model.customized_info import CustomizedInfo
from com.alipay.ams.api.model.refund_to_bank_info import RefundToBankInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.refund_detail import RefundDetail



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayRefundRequest(AlipayRequest):
    def __init__(self):
        super(AlipayRefundRequest, self).__init__("/ams/api/v1/payments/refund") 

        self.__metadata = None  # type: str
        self.__customized_info = None  # type: CustomizedInfo
        self.__capture_id = None  # type: str
        self.__refund_to_bank_info = None  # type: RefundToBankInfo
        self.__refund_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__reference_refund_id = None  # type: str
        self.__refund_amount = None  # type: Amount
        self.__refund_reason = None  # type: str
        self.__refund_notify_url = None  # type: str
        self.__is_async_refund = None  # type: bool
        self.__extend_info = None  # type: str
        self.__refund_details = None  # type: [RefundDetail]
        self.__refund_source_account_no = None  # type: str
        

    @property
    def metadata(self):
        """
        Additional metadata about the refund request
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def customized_info(self):
        """Gets the customized_info of this AlipayRefundRequest.
        
        """
        return self.__customized_info

    @customized_info.setter
    def customized_info(self, value):
        self.__customized_info = value
    @property
    def capture_id(self):
        """Gets the capture_id of this AlipayRefundRequest.
        
        """
        return self.__capture_id

    @capture_id.setter
    def capture_id(self, value):
        self.__capture_id = value
    @property
    def refund_to_bank_info(self):
        """Gets the refund_to_bank_info of this AlipayRefundRequest.
        
        """
        return self.__refund_to_bank_info

    @refund_to_bank_info.setter
    def refund_to_bank_info(self, value):
        self.__refund_to_bank_info = value
    @property
    def refund_request_id(self):
        """
        The unique ID assigned by the merchant to identify a refund request.  More information:  This field is an API idempotency field.The merchant uses the refundRequestId field for idempotency control. For payment requests that are initiated with the same value of refundRequestId and reach a final status (S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value
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
    def reference_refund_id(self):
        """
        The unique ID to identify a refund, which is assigned by the merchant that directly provides services or goods to the customer.  Note: Specify this field if this value is needed for internal use or reconciliation.  More information:  Maximum length: 64 characters 
        """
        return self.__reference_refund_id

    @reference_refund_id.setter
    def reference_refund_id(self, value):
        self.__reference_refund_id = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this AlipayRefundRequest.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
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
    @property
    def is_async_refund(self):
        """Gets the is_async_refund of this AlipayRefundRequest.
        
        """
        return self.__is_async_refund

    @is_async_refund.setter
    def is_async_refund(self, value):
        self.__is_async_refund = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayRefundRequest.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def refund_details(self):
        """Gets the refund_details of this AlipayRefundRequest.
        
        """
        return self.__refund_details

    @refund_details.setter
    def refund_details(self, value):
        self.__refund_details = value
    @property
    def refund_source_account_no(self):
        """Gets the refund_source_account_no of this AlipayRefundRequest.
        
        """
        return self.__refund_source_account_no

    @refund_source_account_no.setter
    def refund_source_account_no(self, value):
        self.__refund_source_account_no = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "customized_info") and self.customized_info is not None:
            params['customizedInfo'] = self.customized_info
        if hasattr(self, "capture_id") and self.capture_id is not None:
            params['captureId'] = self.capture_id
        if hasattr(self, "refund_to_bank_info") and self.refund_to_bank_info is not None:
            params['refundToBankInfo'] = self.refund_to_bank_info
        if hasattr(self, "refund_request_id") and self.refund_request_id is not None:
            params['refundRequestId'] = self.refund_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "reference_refund_id") and self.reference_refund_id is not None:
            params['referenceRefundId'] = self.reference_refund_id
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refund_reason") and self.refund_reason is not None:
            params['refundReason'] = self.refund_reason
        if hasattr(self, "refund_notify_url") and self.refund_notify_url is not None:
            params['refundNotifyUrl'] = self.refund_notify_url
        if hasattr(self, "is_async_refund") and self.is_async_refund is not None:
            params['isAsyncRefund'] = self.is_async_refund
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "refund_details") and self.refund_details is not None:
            params['refundDetails'] = self.refund_details
        if hasattr(self, "refund_source_account_no") and self.refund_source_account_no is not None:
            params['refundSourceAccountNo'] = self.refund_source_account_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'customizedInfo' in response_body:
            self.__customized_info = CustomizedInfo()
            self.__customized_info.parse_rsp_body(response_body['customizedInfo'])
        if 'captureId' in response_body:
            self.__capture_id = response_body['captureId']
        if 'refundToBankInfo' in response_body:
            self.__refund_to_bank_info = RefundToBankInfo()
            self.__refund_to_bank_info.parse_rsp_body(response_body['refundToBankInfo'])
        if 'refundRequestId' in response_body:
            self.__refund_request_id = response_body['refundRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'referenceRefundId' in response_body:
            self.__reference_refund_id = response_body['referenceRefundId']
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundReason' in response_body:
            self.__refund_reason = response_body['refundReason']
        if 'refundNotifyUrl' in response_body:
            self.__refund_notify_url = response_body['refundNotifyUrl']
        if 'isAsyncRefund' in response_body:
            self.__is_async_refund = response_body['isAsyncRefund']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'refundDetails' in response_body:
            self.__refund_details = []
            for item in response_body['refundDetails']:
                obj = RefundDetail()
                obj.parse_rsp_body(item)
                self.__refund_details.append(obj)
        if 'refundSourceAccountNo' in response_body:
            self.__refund_source_account_no = response_body['refundSourceAccountNo']
