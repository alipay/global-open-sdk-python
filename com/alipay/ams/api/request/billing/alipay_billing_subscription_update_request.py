import json
from com.alipay.ams.api.model.price_item_change import PriceItemChange
from com.alipay.ams.api.model.billing_subscription_update_pause_collection import BillingSubscriptionUpdatePauseCollection
from com.alipay.ams.api.model.billing_subscription_update_trial_settings import BillingSubscriptionUpdateTrialSettings



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionUpdateRequest, self).__init__("/ams/api/v1/billing/subscription/update") 

        self.__subscription_id = None  # type: str
        self.__price_item_changes = None  # type: [PriceItemChange]
        self.__proration_behavior = None  # type: str
        self.__proration_date = None  # type: str
        self.__pause_collection = None  # type: BillingSubscriptionUpdatePauseCollection
        self.__billing_cycle_anchor = None  # type: str
        self.__trial_settings = None  # type: BillingSubscriptionUpdateTrialSettings
        self.__cancel_at_period_end = None  # type: bool
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__default_payment_method = None  # type: str
        self.__description = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        

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
        The proration behavior. Maximum length: 18 characters.
        """
        return self.__proration_behavior

    @proration_behavior.setter
    def proration_behavior(self, value):
        self.__proration_behavior = value
    @property
    def proration_date(self):
        """
        The proration date.
        """
        return self.__proration_date

    @proration_date.setter
    def proration_date(self, value):
        self.__proration_date = value
    @property
    def pause_collection(self):
        """Gets the pause_collection of this AlipayBillingSubscriptionUpdateRequest.
        
        """
        return self.__pause_collection

    @pause_collection.setter
    def pause_collection(self, value):
        self.__pause_collection = value
    @property
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor. Maximum length: 9 characters.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
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
    def default_payment_method(self):
        """
        The default payment method token. Maximum length: 64 characters.
        """
        return self.__default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, value):
        self.__default_payment_method = value
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
        Custom metadata for special use cases.
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
        if hasattr(self, "proration_date") and self.proration_date is not None:
            params['prorationDate'] = self.proration_date
        if hasattr(self, "pause_collection") and self.pause_collection is not None:
            params['pauseCollection'] = self.pause_collection
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "days_until_due") and self.days_until_due is not None:
            params['daysUntilDue'] = self.days_until_due
        if hasattr(self, "default_payment_method") and self.default_payment_method is not None:
            params['defaultPaymentMethod'] = self.default_payment_method
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
        if 'prorationDate' in response_body:
            self.__proration_date = response_body['prorationDate']
        if 'pauseCollection' in response_body:
            self.__pause_collection = BillingSubscriptionUpdatePauseCollection()
            self.__pause_collection.parse_rsp_body(response_body['pauseCollection'])
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingSubscriptionUpdateTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
        if 'defaultPaymentMethod' in response_body:
            self.__default_payment_method = response_body['defaultPaymentMethod']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
