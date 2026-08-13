import json
from com.alipay.ams.api.model.result_info import ResultInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionCancelResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__canceled_at = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__credit_note_id = None  # type: str
        self.__credit_note_amount = None  # type: int
        self.__credit_note_currency = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionCancelResponse.
        
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
        The current status. Maximum length: 20 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def canceled_at(self):
        """
        The canceled at.
        """
        return self.__canceled_at

    @canceled_at.setter
    def canceled_at(self, value):
        self.__canceled_at = value
    @property
    def cancel_at_period_end(self):
        """
        The cancel at period end.
        """
        return self.__cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self.__cancel_at_period_end = value
    @property
    def credit_note_id(self):
        """
        The generated credit note ID. Returned for an immediate termination that generates prorated credit. Maximum length: 64 characters.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value
    @property
    def credit_note_amount(self):
        """
        The credit amount in the smallest currency unit. Returned together with &#x60;creditNoteId&#x60; and &#x60;creditNoteCurrency&#x60;.
        """
        return self.__credit_note_amount

    @credit_note_amount.setter
    def credit_note_amount(self, value):
        self.__credit_note_amount = value
    @property
    def credit_note_currency(self):
        """
        The three-letter ISO 4217 currency code for &#x60;creditNoteAmount&#x60;. Returned together with &#x60;creditNoteId&#x60;. Maximum length: 3 characters.
        """
        return self.__credit_note_currency

    @credit_note_currency.setter
    def credit_note_currency(self, value):
        self.__credit_note_currency = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "canceled_at") and self.canceled_at is not None:
            params['canceledAt'] = self.canceled_at
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "credit_note_amount") and self.credit_note_amount is not None:
            params['creditNoteAmount'] = self.credit_note_amount
        if hasattr(self, "credit_note_currency") and self.credit_note_currency is not None:
            params['creditNoteCurrency'] = self.credit_note_currency
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayBillingSubscriptionCancelResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'canceledAt' in response_body:
            self.__canceled_at = response_body['canceledAt']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'creditNoteAmount' in response_body:
            self.__credit_note_amount = response_body['creditNoteAmount']
        if 'creditNoteCurrency' in response_body:
            self.__credit_note_currency = response_body['creditNoteCurrency']
