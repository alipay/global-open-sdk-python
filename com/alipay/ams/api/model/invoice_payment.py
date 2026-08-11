import json
from com.alipay.ams.api.model.amount import Amount




class InvoicePayment:
    def __init__(self):
        
        self.__invoice_payment_id = None  # type: str
        self.__attempt_no = None  # type: int
        self.__payment_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__pay_to_request_id = None  # type: str
        self.__pay_to_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_order_status = None  # type: str
        self.__payment_method = None  # type: str
        self.__error_code = None  # type: str
        self.__error_message = None  # type: str
        self.__retry_reason = None  # type: str
        self.__payment_time = None  # type: str
        self.__next_retry_at = None  # type: str
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        

    @property
    def invoice_payment_id(self):
        """
        Payment record ID. Unique identifier for this payment attempt. Cannot be null. Maximum length: 64 characters.
        """
        return self.__invoice_payment_id

    @invoice_payment_id.setter
    def invoice_payment_id(self, value):
        self.__invoice_payment_id = value
    @property
    def attempt_no(self):
        """
        Attempt number (1-based). Incremented for each retry. Minimum value: 1. Cannot be null.
        """
        return self.__attempt_no

    @attempt_no.setter
    def attempt_no(self, value):
        self.__attempt_no = value
    @property
    def payment_request_id(self):
        """
        Outbound payment request ID (idempotency key). May be null or omitted for offline confirmations. Maximum length: 128 characters.
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def payment_id(self):
        """
        External payment transaction ID. May be null or omitted for failed or processing attempts. Maximum length: 64 characters.
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def pay_to_request_id(self):
        """
        Order request ID. May be null or omitted if not applicable. Maximum length: 128 characters.
        """
        return self.__pay_to_request_id

    @pay_to_request_id.setter
    def pay_to_request_id(self, value):
        self.__pay_to_request_id = value
    @property
    def pay_to_id(self):
        """
        Order ID. May be null or omitted if not applicable. Maximum length: 64 characters.
        """
        return self.__pay_to_id

    @pay_to_id.setter
    def pay_to_id(self, value):
        self.__pay_to_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this InvoicePayment.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_order_status(self):
        """
        Payment status. Allowed values: &#x60;SUCCESS&#x60; - payment completed; &#x60;PROCESSING&#x60; - awaiting an asynchronous result; &#x60;FAILED&#x60; - payment failed; &#x60;CLOSED&#x60; - payment permanently closed or cancelled. Cannot be null. Maximum length: 32 characters.
        """
        return self.__payment_order_status

    @payment_order_status.setter
    def payment_order_status(self, value):
        self.__payment_order_status = value
    @property
    def payment_method(self):
        """
        Payment method used for this attempt. Allowed values include &#x60;CARD&#x60;, &#x60;BANK_TRANSFER&#x60;, &#x60;WALLET&#x60;, and &#x60;OFFLINE&#x60;. May be null or omitted when no payment method was recorded. Maximum length: 32 characters.
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def error_code(self):
        """
        Error code from the payment gateway. May be null or omitted for successful payments. Maximum length: 64 characters.
        """
        return self.__error_code

    @error_code.setter
    def error_code(self, value):
        self.__error_code = value
    @property
    def error_message(self):
        """
        Error message from the payment gateway. May be null or omitted for successful payments. Maximum length: 256 characters.
        """
        return self.__error_message

    @error_message.setter
    def error_message(self, value):
        self.__error_message = value
    @property
    def retry_reason(self):
        """
        Reason for retry. May be null or omitted if no retry is scheduled. Maximum length: 64 characters.
        """
        return self.__retry_reason

    @retry_reason.setter
    def retry_reason(self, value):
        self.__retry_reason = value
    @property
    def payment_time(self):
        """
        ISO 8601 timestamp of successful payment. May be null or omitted for failed or processing attempts. Maximum length: 29 characters.
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def next_retry_at(self):
        """
        ISO 8601 timestamp of the next scheduled retry. May be null or omitted if no retry is scheduled. Maximum length: 29 characters.
        """
        return self.__next_retry_at

    @next_retry_at.setter
    def next_retry_at(self, value):
        self.__next_retry_at = value
    @property
    def gmt_create(self):
        """
        ISO 8601 timestamp of record creation. Cannot be null. Maximum length: 29 characters.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        ISO 8601 timestamp of the last record update. Cannot be null. Maximum length: 29 characters.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_payment_id") and self.invoice_payment_id is not None:
            params['invoicePaymentId'] = self.invoice_payment_id
        if hasattr(self, "attempt_no") and self.attempt_no is not None:
            params['attemptNo'] = self.attempt_no
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "pay_to_request_id") and self.pay_to_request_id is not None:
            params['payToRequestId'] = self.pay_to_request_id
        if hasattr(self, "pay_to_id") and self.pay_to_id is not None:
            params['payToId'] = self.pay_to_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_order_status") and self.payment_order_status is not None:
            params['paymentOrderStatus'] = self.payment_order_status
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "error_code") and self.error_code is not None:
            params['errorCode'] = self.error_code
        if hasattr(self, "error_message") and self.error_message is not None:
            params['errorMessage'] = self.error_message
        if hasattr(self, "retry_reason") and self.retry_reason is not None:
            params['retryReason'] = self.retry_reason
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "next_retry_at") and self.next_retry_at is not None:
            params['nextRetryAt'] = self.next_retry_at
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoicePaymentId' in response_body:
            self.__invoice_payment_id = response_body['invoicePaymentId']
        if 'attemptNo' in response_body:
            self.__attempt_no = response_body['attemptNo']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'payToRequestId' in response_body:
            self.__pay_to_request_id = response_body['payToRequestId']
        if 'payToId' in response_body:
            self.__pay_to_id = response_body['payToId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentOrderStatus' in response_body:
            self.__payment_order_status = response_body['paymentOrderStatus']
        if 'paymentMethod' in response_body:
            self.__payment_method = response_body['paymentMethod']
        if 'errorCode' in response_body:
            self.__error_code = response_body['errorCode']
        if 'errorMessage' in response_body:
            self.__error_message = response_body['errorMessage']
        if 'retryReason' in response_body:
            self.__retry_reason = response_body['retryReason']
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'nextRetryAt' in response_body:
            self.__next_retry_at = response_body['nextRetryAt']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']
