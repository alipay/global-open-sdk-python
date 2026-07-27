import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.billing_subscription_cancel_cancellation_details import BillingSubscriptionCancelCancellationDetails



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionCancelResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__cancellation_reason = None  # type: str
        self.__cancellation_details = None  # type: BillingSubscriptionCancelCancellationDetails
        self.__canceled_at = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__credit_note_id = None  # type: str
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
    def cancellation_reason(self):
        """
        The cancellation reason. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__cancellation_reason

    @cancellation_reason.setter
    def cancellation_reason(self, value):
        self.__cancellation_reason = value
    @property
    def cancellation_details(self):
        """Gets the cancellation_details of this AlipayBillingSubscriptionCancelResponse.
        
        """
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = value
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
        The credit note ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "cancellation_reason") and self.cancellation_reason is not None:
            params['cancellationReason'] = self.cancellation_reason
        if hasattr(self, "cancellation_details") and self.cancellation_details is not None:
            params['cancellationDetails'] = self.cancellation_details
        if hasattr(self, "canceled_at") and self.canceled_at is not None:
            params['canceledAt'] = self.canceled_at
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
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
        if 'cancellationReason' in response_body:
            self.__cancellation_reason = response_body['cancellationReason']
        if 'cancellationDetails' in response_body:
            self.__cancellation_details = BillingSubscriptionCancelCancellationDetails()
            self.__cancellation_details.parse_rsp_body(response_body['cancellationDetails'])
        if 'canceledAt' in response_body:
            self.__canceled_at = response_body['canceledAt']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
