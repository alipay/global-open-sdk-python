import json
from com.alipay.ams.api.model.amount import Amount




class CreditNoteSummary:
    def __init__(self):
        
        self.__credit_note_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__type = None  # type: str
        self.__status = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__reason = None  # type: str
        self.__effective_date = None  # type: str
        self.__refund_status = None  # type: str
        self.__voided_at = None  # type: str
        self.__refunded_at = None  # type: str
        self.__created_at = None  # type: str
        

    @property
    def credit_note_id(self):
        """
        The credit note ID. Maximum length: 64 characters.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
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
    def type(self):
        """
        The type. Maximum length: 32 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def status(self):
        """
        The current status. Maximum length: 32 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def total_amount(self):
        """Gets the total_amount of this CreditNoteSummary.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def reason(self):
        """
        The reason for the status change. Maximum length: 32 characters.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def effective_date(self):
        """
        The effective date. Maximum length: 29 characters.
        """
        return self.__effective_date

    @effective_date.setter
    def effective_date(self, value):
        self.__effective_date = value
    @property
    def refund_status(self):
        """
        The refund status. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__refund_status

    @refund_status.setter
    def refund_status(self, value):
        self.__refund_status = value
    @property
    def voided_at(self):
        """
        The voided at. Maximum length: 29 characters.
        """
        return self.__voided_at

    @voided_at.setter
    def voided_at(self, value):
        self.__voided_at = value
    @property
    def refunded_at(self):
        """
        The refunded at. Maximum length: 29 characters.
        """
        return self.__refunded_at

    @refunded_at.setter
    def refunded_at(self, value):
        self.__refunded_at = value
    @property
    def created_at(self):
        """
        The created at. Maximum length: 29 characters.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "effective_date") and self.effective_date is not None:
            params['effectiveDate'] = self.effective_date
        if hasattr(self, "refund_status") and self.refund_status is not None:
            params['refundStatus'] = self.refund_status
        if hasattr(self, "voided_at") and self.voided_at is not None:
            params['voidedAt'] = self.voided_at
        if hasattr(self, "refunded_at") and self.refunded_at is not None:
            params['refundedAt'] = self.refunded_at
        if hasattr(self, "created_at") and self.created_at is not None:
            params['createdAt'] = self.created_at
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'effectiveDate' in response_body:
            self.__effective_date = response_body['effectiveDate']
        if 'refundStatus' in response_body:
            self.__refund_status = response_body['refundStatus']
        if 'voidedAt' in response_body:
            self.__voided_at = response_body['voidedAt']
        if 'refundedAt' in response_body:
            self.__refunded_at = response_body['refundedAt']
        if 'createdAt' in response_body:
            self.__created_at = response_body['createdAt']
