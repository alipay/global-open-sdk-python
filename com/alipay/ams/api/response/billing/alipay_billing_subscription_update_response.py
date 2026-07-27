import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.billing_subscription_update_pause_collection import BillingSubscriptionUpdatePauseCollection
from com.alipay.ams.api.model.billing_subscription_update_trial_settings import BillingSubscriptionUpdateTrialSettings
from com.alipay.ams.api.model.subscription_item import SubscriptionItem



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__pause_collection = None  # type: BillingSubscriptionUpdatePauseCollection
        self.__trial_settings = None  # type: BillingSubscriptionUpdateTrialSettings
        self.__subscription_items = None  # type: [SubscriptionItem]
        self.__proration_invoice_id = None  # type: str
        self.__credit_note_id = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__canceled_at = None  # type: str
        self.__proration_date = None  # type: str
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
        The current status. Maximum length: 20 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor. Note: See documentation for details.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def pause_collection(self):
        """Gets the pause_collection of this AlipayBillingSubscriptionUpdateResponse.
        
        """
        return self.__pause_collection

    @pause_collection.setter
    def pause_collection(self, value):
        self.__pause_collection = value
    @property
    def trial_settings(self):
        """Gets the trial_settings of this AlipayBillingSubscriptionUpdateResponse.
        
        """
        return self.__trial_settings

    @trial_settings.setter
    def trial_settings(self, value):
        self.__trial_settings = value
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
    def credit_note_id(self):
        """
        The credit note ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value
    @property
    def cancel_at_period_end(self):
        """
        The cancel at period end. Note: See documentation for details.
        """
        return self.__cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self.__cancel_at_period_end = value
    @property
    def canceled_at(self):
        """
        The canceled at. Note: See documentation for details.
        """
        return self.__canceled_at

    @canceled_at.setter
    def canceled_at(self, value):
        self.__canceled_at = value
    @property
    def proration_date(self):
        """
        The proration date. Note: See documentation for details.
        """
        return self.__proration_date

    @proration_date.setter
    def proration_date(self, value):
        self.__proration_date = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "pause_collection") and self.pause_collection is not None:
            params['pauseCollection'] = self.pause_collection
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
        if hasattr(self, "subscription_items") and self.subscription_items is not None:
            params['subscriptionItems'] = self.subscription_items
        if hasattr(self, "proration_invoice_id") and self.proration_invoice_id is not None:
            params['prorationInvoiceId'] = self.proration_invoice_id
        if hasattr(self, "credit_note_id") and self.credit_note_id is not None:
            params['creditNoteId'] = self.credit_note_id
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "canceled_at") and self.canceled_at is not None:
            params['canceledAt'] = self.canceled_at
        if hasattr(self, "proration_date") and self.proration_date is not None:
            params['prorationDate'] = self.proration_date
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
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'pauseCollection' in response_body:
            self.__pause_collection = BillingSubscriptionUpdatePauseCollection()
            self.__pause_collection.parse_rsp_body(response_body['pauseCollection'])
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingSubscriptionUpdateTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'subscriptionItems' in response_body:
            self.__subscription_items = []
            for item in response_body['subscriptionItems']:
                obj = SubscriptionItem()
                obj.parse_rsp_body(item)
                self.__subscription_items.append(obj)
        if 'prorationInvoiceId' in response_body:
            self.__proration_invoice_id = response_body['prorationInvoiceId']
        if 'creditNoteId' in response_body:
            self.__credit_note_id = response_body['creditNoteId']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'canceledAt' in response_body:
            self.__canceled_at = response_body['canceledAt']
        if 'prorationDate' in response_body:
            self.__proration_date = response_body['prorationDate']
