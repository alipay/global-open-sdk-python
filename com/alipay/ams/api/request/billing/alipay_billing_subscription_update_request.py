import json
from com.alipay.ams.api.model.price_item_change import PriceItemChange
from com.alipay.ams.api.model.billing_trial_settings import BillingTrialSettings
from com.alipay.ams.api.model.billing_subscription_cancellation_details import BillingSubscriptionCancellationDetails



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionUpdateRequest, self).__init__("/ams/api/v1/billing/subscription/update") 

        self.__subscription_id = None  # type: str
        self.__price_item_changes = None  # type: [PriceItemChange]
        self.__proration_behavior = None  # type: str
        self.__reset_billing_cycle_anchor = None  # type: bool
        self.__trial_settings = None  # type: BillingTrialSettings
        self.__cancel_at_period_end = None  # type: bool
        self.__cancel_at = None  # type: str
        self.__cancellation_details = None  # type: BillingSubscriptionCancellationDetails
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__description = None  # type: str
        self.__metadata = None  # type: str
        

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
    def price_item_changes(self):
        """
        The price item changes.
        """
        return self.__price_item_changes

    @price_item_changes.setter
    def price_item_changes(self, value):
        self.__price_item_changes = value
    @property
    def proration_behavior(self):
        """
        Controls when the subscription update takes effect. Valid values are ALWAYS_INVOICE and NONE. ALWAYS_INVOICE applies the change immediately and generates an invoice or credit note for the prorated difference. NONE defers the change until the next billing cycle without generating a proration invoice. The default value is NONE.
        """
        return self.__proration_behavior

    @proration_behavior.setter
    def proration_behavior(self, value):
        self.__proration_behavior = value
    @property
    def reset_billing_cycle_anchor(self):
        """
        Whether to reset the billing cycle anchor when the update takes effect.
        """
        return self.__reset_billing_cycle_anchor

    @reset_billing_cycle_anchor.setter
    def reset_billing_cycle_anchor(self, value):
        self.__reset_billing_cycle_anchor = value
    @property
    def trial_settings(self):
        """Gets the trial_settings of this AlipayBillingSubscriptionUpdateRequest.
        
        """
        return self.__trial_settings

    @trial_settings.setter
    def trial_settings(self, value):
        self.__trial_settings = value
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
    def cancel_at(self):
        """
        The time when the subscription is scheduled for cancellation in ISO 8601 format.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
    @property
    def cancellation_details(self):
        """Gets the cancellation_details of this AlipayBillingSubscriptionUpdateRequest.
        
        """
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = value
    @property
    def collection_method(self):
        """
        The collection method. Maximum length: 22 characters.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def days_until_due(self):
        """
        The days until due. Note: See documentation for details.
        """
        return self.__days_until_due

    @days_until_due.setter
    def days_until_due(self, value):
        self.__days_until_due = value
    @property
    def description(self):
        """
        The description. Maximum length: 500 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def metadata(self):
        """
        Custom metadata encoded as a JSON object string. When provided, the value fully replaces the existing metadata. When omitted, the existing value is unchanged.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "price_item_changes") and self.price_item_changes is not None:
            params['priceItemChanges'] = self.price_item_changes
        if hasattr(self, "proration_behavior") and self.proration_behavior is not None:
            params['prorationBehavior'] = self.proration_behavior
        if hasattr(self, "reset_billing_cycle_anchor") and self.reset_billing_cycle_anchor is not None:
            params['resetBillingCycleAnchor'] = self.reset_billing_cycle_anchor
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "cancel_at") and self.cancel_at is not None:
            params['cancelAt'] = self.cancel_at
        if hasattr(self, "cancellation_details") and self.cancellation_details is not None:
            params['cancellationDetails'] = self.cancellation_details
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "days_until_due") and self.days_until_due is not None:
            params['daysUntilDue'] = self.days_until_due
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'priceItemChanges' in response_body:
            self.__price_item_changes = []
            for item in response_body['priceItemChanges']:
                obj = PriceItemChange()
                obj.parse_rsp_body(item)
                self.__price_item_changes.append(obj)
        if 'prorationBehavior' in response_body:
            self.__proration_behavior = response_body['prorationBehavior']
        if 'resetBillingCycleAnchor' in response_body:
            self.__reset_billing_cycle_anchor = response_body['resetBillingCycleAnchor']
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'cancelAt' in response_body:
            self.__cancel_at = response_body['cancelAt']
        if 'cancellationDetails' in response_body:
            self.__cancellation_details = BillingSubscriptionCancellationDetails()
            self.__cancellation_details.parse_rsp_body(response_body['cancellationDetails'])
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
