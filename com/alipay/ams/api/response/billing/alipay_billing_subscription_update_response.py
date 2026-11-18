import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.subscription_item import SubscriptionItem



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__subscription_items = None  # type: [SubscriptionItem]
        self.__proration_invoice_id = None  # type: str
        self.__proration_invoice_amount = None  # type: int
        self.__proration_invoice_currency = None  # type: str
        self.__credit_note_id = None  # type: str
        self.__credit_note_amount = None  # type: int
        self.__credit_note_currency = None  # type: str
        self.__pending_update = None  # type: bool
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionUpdateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def status(self):
        """
        The subscription status after the update. PAST_DUE means the latest renewal payment failed and collection retry is in progress. PAUSED means payment collection is suspended and can be entered by setting statusChange.action to PAUSE. CANCELLED means the subscription remains active until the current period ends and can be reverted before then by setting cancelAtPeriodEnd to false. TERMINATED is a permanent final state. Maximum length: 20 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def subscription_items(self):
        """
        The subscription items. Note: See documentation for details.
        """
        return self.__subscription_items

    @subscription_items.setter
    def subscription_items(self, value):
        self.__subscription_items = value
    @property
    def proration_invoice_id(self):
        """
        The proration invoice id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__proration_invoice_id

    @proration_invoice_id.setter
    def proration_invoice_id(self, value):
        self.__proration_invoice_id = value
    @property
    def proration_invoice_amount(self):
        """
        The proration invoice amount in the smallest currency unit. Returned together with prorationInvoiceId.
        """
        return self.__proration_invoice_amount

    @proration_invoice_amount.setter
    def proration_invoice_amount(self, value):
        self.__proration_invoice_amount = value
    @property
    def proration_invoice_currency(self):
        """
        The currency of prorationInvoiceAmount as a three-letter ISO 4217 code.
        """
        return self.__proration_invoice_currency

    @proration_invoice_currency.setter
    def proration_invoice_currency(self, value):
        self.__proration_invoice_currency = value
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
    def credit_note_amount(self):
        """
        The credit note amount in the smallest currency unit. Returned together with creditNoteId.
        """
        return self.__credit_note_amount

    @credit_note_amount.setter
    def credit_note_amount(self, value):
        self.__credit_note_amount = value
    @property
    def credit_note_currency(self):
        """
        The currency of creditNoteAmount as a three-letter ISO 4217 code.
        """
        return self.__credit_note_currency

    @credit_note_currency.setter
    def credit_note_currency(self, value):
        self.__credit_note_currency = value
    @property
    def pending_update(self):
        """
        Whether a payment-gated upgrade or quantity increase is staged but not yet effective. When true, subscriptionItems can still describe the currently effective items.
        """
        return self.__pending_update

    @pending_update.setter
    def pending_update(self, value):
        self.__pending_update = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "subscription_items") and self.subscription_items is not None:
            params['subscriptionItems'] = self.subscription_items
        if hasattr(self, "proration_invoice_id") and self.proration_invoice_id is not None:
            params['prorationInvoiceId'] = self.proration_invoice_id
        if hasattr(self, "proration_invoice_amount") and self.proration_invoice_amount is not None:
            params['prorationInvoiceAmount'] = self.proration_invoice_amount
        if hasattr(self, "proration_invoice_currency") and self.proration_invoice_currency is not None:
            params['prorationInvoiceCurrency'] = self.proration_invoice_currency
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "credit_note_amount") and self.credit_note_amount is not None:
            params['creditNoteAmount'] = self.credit_note_amount
        if hasattr(self, "credit_note_currency") and self.credit_note_currency is not None:
            params['creditNoteCurrency'] = self.credit_note_currency
        if hasattr(self, "pending_update") and self.pending_update is not None:
            params['pendingUpdate'] = self.pending_update
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayBillingSubscriptionUpdateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'subscriptionItems' in response_body:
            self.__subscription_items = []
            for item in response_body['subscriptionItems']:
                obj = SubscriptionItem()
                obj.parse_rsp_body(item)
                self.__subscription_items.append(obj)
        if 'prorationInvoiceId' in response_body:
            self.__proration_invoice_id = response_body['prorationInvoiceId']
        if 'prorationInvoiceAmount' in response_body:
            self.__proration_invoice_amount = response_body['prorationInvoiceAmount']
        if 'prorationInvoiceCurrency' in response_body:
            self.__proration_invoice_currency = response_body['prorationInvoiceCurrency']
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'creditNoteAmount' in response_body:
            self.__credit_note_amount = response_body['creditNoteAmount']
        if 'creditNoteCurrency' in response_body:
            self.__credit_note_currency = response_body['creditNoteCurrency']
        if 'pendingUpdate' in response_body:
            self.__pending_update = response_body['pendingUpdate']
