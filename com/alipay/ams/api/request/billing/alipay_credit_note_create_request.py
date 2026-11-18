import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.credit_note_create_item import CreditNoteCreateItem
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditNoteCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditNoteCreateRequest, self).__init__("/ams/api/v1/billing/creditNote/create") 

        self.__credit_note_request_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__type = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__items = None  # type: [CreditNoteCreateItem]
        self.__refund_amount = None  # type: Amount
        self.__refund_destination = None  # type: str
        self.__reason = None  # type: str
        self.__reason_description = None  # type: str
        self.__memo = None  # type: str
        self.__email_type = None  # type: str
        self.__language = None  # type: str
        self.__effective_date = None  # type: str
        self.__metadata = None  # type: str
        self.__credit_note_notify_url = None  # type: str
        

    @property
    def credit_note_request_id(self):
        """
        The credit note request id. Maximum length: 64 characters.
        """
        return self.__credit_note_request_id

    @credit_note_request_id.setter
    def credit_note_request_id(self, value):
        self.__credit_note_request_id = value
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
        The type. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def total_amount(self):
        """Gets the total_amount of this AlipayCreditNoteCreateRequest.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def items(self):
        """
        The credit note items. Item-level quantity and itemAmount follow the conditional rules documented by CreditNoteCreateItem.
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this AlipayCreditNoteCreateRequest.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
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
    def reason(self):
        """
        The reason for the status change. Maximum length: 32 characters.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def reason_description(self):
        """
        The detailed description of the reason. Maximum length: 512 characters.
        """
        return self.__reason_description

    @reason_description.setter
    def reason_description(self, value):
        self.__reason_description = value
    @property
    def memo(self):
        """
        The memo. Maximum length: 512 characters.
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def email_type(self):
        """
        The email type. Maximum length: 16 characters.
        """
        return self.__email_type

    @email_type.setter
    def email_type(self, value):
        self.__email_type = value
    @property
    def language(self):
        """
        The language. Maximum length: 10 characters. Note: See documentation for details.
        """
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
    @property
    def effective_date(self):
        """
        The effective date. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__effective_date

    @effective_date.setter
    def effective_date(self, value):
        self.__effective_date = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Maximum length: 65535 characters. The value must be a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def credit_note_notify_url(self):
        """
        The URL that receives credit note notifications. Maximum length: 2048 characters.
        """
        return self.__credit_note_notify_url

    @credit_note_notify_url.setter
    def credit_note_notify_url(self, value):
        self.__credit_note_notify_url = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_note_request_id") and self.credit_note_request_id is not None:
            params['creditNoteRequestId'] = self.credit_note_request_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "items") and self.items is not None:
            params['items'] = self.items
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refund_destination") and self.refund_destination is not None:
            params['refundDestination'] = self.refund_destination
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "reason_description") and self.reason_description is not None:
            params['reasonDescription'] = self.reason_description
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "email_type") and self.email_type is not None:
            params['emailType'] = self.email_type
        if hasattr(self, "language") and self.language is not None:
            params['language'] = self.language
        if hasattr(self, "effective_date") and self.effective_date is not None:
            params['effectiveDate'] = self.effective_date
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "credit_note_notify_url") and self.credit_note_notify_url is not None:
            params['creditNoteNotifyUrl'] = self.credit_note_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditNoteRequestId' in response_body:
            self.__credit_note_request_id = response_body['creditNoteRequestId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'items' in response_body:
            self.__items = []
            for item in response_body['items']:
                obj = CreditNoteCreateItem()
                obj.parse_rsp_body(item)
                self.__items.append(obj)
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundDestination' in response_body:
            self.__refund_destination = response_body['refundDestination']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'reasonDescription' in response_body:
            self.__reason_description = response_body['reasonDescription']
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'emailType' in response_body:
            self.__email_type = response_body['emailType']
        if 'language' in response_body:
            self.__language = response_body['language']
        if 'effectiveDate' in response_body:
            self.__effective_date = response_body['effectiveDate']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'creditNoteNotifyUrl' in response_body:
            self.__credit_note_notify_url = response_body['creditNoteNotifyUrl']
