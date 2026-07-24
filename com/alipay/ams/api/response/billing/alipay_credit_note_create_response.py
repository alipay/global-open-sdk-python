import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.credit_note_create_items import CreditNoteCreateItems



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditNoteCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__credit_note_id = None  # type: str
        self.__credit_note_request_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__type = None  # type: str
        self.__status = None  # type: str
        self.__customer_id = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__refund_amount = None  # type: Amount
        self.__refund_status = None  # type: str
        self.__refund_id = None  # type: str
        self.__reason = None  # type: str
        self.__reason_description = None  # type: str
        self.__refund_destination = None  # type: str
        self.__items = None  # type: CreditNoteCreateItems
        self.__memo = None  # type: str
        self.__effective_date = None  # type: str
        self.__issued_at = None  # type: str
        self.__refunded_at = None  # type: str
        self.__voided_at = None  # type: str
        self.__created_at = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditNoteCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def credit_note_id(self):
        """
        The credit note ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value
    @property
    def credit_note_request_id(self):
        """
        The credit note request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__credit_note_request_id

    @credit_note_request_id.setter
    def credit_note_request_id(self, value):
        self.__credit_note_request_id = value
    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def type(self):
        """
        The type. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def status(self):
        """
        The current status. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def total_amount(self):
        """Gets the total_amount of this AlipayCreditNoteCreateResponse.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this AlipayCreditNoteCreateResponse.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
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
    def refund_id(self):
        """
        The refund id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def reason(self):
        """
        The reason for the status change. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def reason_description(self):
        """
        The detailed description of the reason. Maximum length: 512 characters. Note: See documentation for details.
        """
        return self.__reason_description

    @reason_description.setter
    def reason_description(self, value):
        self.__reason_description = value
    @property
    def refund_destination(self):
        """
        The refund destination. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__refund_destination

    @refund_destination.setter
    def refund_destination(self, value):
        self.__refund_destination = value
    @property
    def items(self):
        """Gets the items of this AlipayCreditNoteCreateResponse.
        
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def memo(self):
        """
        The memo. Maximum length: 512 characters. Note: See documentation for details.
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def effective_date(self):
        """
        The effective date. Note: See documentation for details.
        """
        return self.__effective_date

    @effective_date.setter
    def effective_date(self, value):
        self.__effective_date = value
    @property
    def issued_at(self):
        """
        The issued at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value
    @property
    def refunded_at(self):
        """
        The refunded at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__refunded_at

    @refunded_at.setter
    def refunded_at(self, value):
        self.__refunded_at = value
    @property
    def voided_at(self):
        """
        The voided at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__voided_at

    @voided_at.setter
    def voided_at(self, value):
        self.__voided_at = value
    @property
    def created_at(self):
        """
        The created at. Note: See documentation for details.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "credit_note_request_id") and self.credit_note_request_id is not None:
            params['creditNoteRequestId'] = self.credit_note_request_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refund_status") and self.refund_status is not None:
            params['refundStatus'] = self.refund_status
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "reason_description") and self.reason_description is not None:
            params['reasonDescription'] = self.reason_description
        if hasattr(self, "refund_destination") and self.refund_destination is not None:
            params['refundDestination'] = self.refund_destination
        if hasattr(self, "items") and self.items is not None:
            params['items'] = self.items
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "effective_date") and self.effective_date is not None:
            params['effectiveDate'] = self.effective_date
        if hasattr(self, "issued_at") and self.issued_at is not None:
            params['issuedAt'] = self.issued_at
        if hasattr(self, "refunded_at") and self.refunded_at is not None:
            params['refundedAt'] = self.refunded_at
        if hasattr(self, "voided_at") and self.voided_at is not None:
            params['voidedAt'] = self.voided_at
        if hasattr(self, "created_at") and self.created_at is not None:
            params['createdAt'] = self.created_at
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditNoteCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'creditNoteRequestId' in response_body:
            self.__credit_note_request_id = response_body['creditNoteRequestId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundStatus' in response_body:
            self.__refund_status = response_body['refundStatus']
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'reasonDescription' in response_body:
            self.__reason_description = response_body['reasonDescription']
        if 'refundDestination' in response_body:
            self.__refund_destination = response_body['refundDestination']
        if 'items' in response_body:
            self.__items = CreditNoteCreateItems()
            self.__items.parse_rsp_body(response_body['items'])
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'effectiveDate' in response_body:
            self.__effective_date = response_body['effectiveDate']
        if 'issuedAt' in response_body:
            self.__issued_at = response_body['issuedAt']
        if 'refundedAt' in response_body:
            self.__refunded_at = response_body['refundedAt']
        if 'voidedAt' in response_body:
            self.__voided_at = response_body['voidedAt']
        if 'createdAt' in response_body:
            self.__created_at = response_body['createdAt']
