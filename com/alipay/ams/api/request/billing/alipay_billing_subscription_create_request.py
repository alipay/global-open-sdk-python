import json
from com.alipay.ams.api.model.price_item import PriceItem
from com.alipay.ams.api.model.billing_subscription_create_trial_settings import BillingSubscriptionCreateTrialSettings
from com.alipay.ams.api.model.billing_subscription_create_discount import BillingSubscriptionCreateDiscount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionCreateRequest, self).__init__("/ams/api/v1/billing/subscription/create") 

        self.__subscription_request_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__customer_email = None  # type: str
        self.__price_items = None  # type: [PriceItem]
        self.__trial_settings = None  # type: BillingSubscriptionCreateTrialSettings
        self.__discounts = None  # type: [BillingSubscriptionCreateDiscount]
        self.__payment_behavior = None  # type: str
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__billing_cycle_anchor = None  # type: str
        self.__cancel_at = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__description = None  # type: str
        self.__subscription_notify_url = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def subscription_request_id(self):
        """
        The subscription request id. Maximum length: 64 characters.
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
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
    def customer_email(self):
        """
        The email address of the customer. Maximum length: 256 characters. Note: See documentation for details.
        """
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, value):
        self.__customer_email = value
    @property
    def price_items(self):
        """
        The price items.
        """
        return self.__price_items

    @price_items.setter
    def price_items(self, value):
        self.__price_items = value
    @property
    def trial_settings(self):
        """Gets the trial_settings of this AlipayBillingSubscriptionCreateRequest.
        
        """
        return self.__trial_settings

    @trial_settings.setter
    def trial_settings(self, value):
        self.__trial_settings = value
    @property
    def discounts(self):
        """
        The discounts applied. Note: See documentation for details.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value
    @property
    def payment_behavior(self):
        """
        The payment behavior.
        """
        return self.__payment_behavior

    @payment_behavior.setter
    def payment_behavior(self, value):
        self.__payment_behavior = value
    @property
    def collection_method(self):
        """
        The collection method.
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
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def cancel_at(self):
        """
        The cancel at.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
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
    def description(self):
        """
        The description. Maximum length: 500 characters. Note: See documentation for details.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def subscription_notify_url(self):
        """
        The subscription notify url. Maximum length: 512 characters.
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Note: See documentation for details.
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
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_email") and self.customer_email is not None:
            params['customerEmail'] = self.customer_email
        if hasattr(self, "price_items") and self.price_items is not None:
            params['priceItems'] = self.price_items
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        if hasattr(self, "payment_behavior") and self.payment_behavior is not None:
            params['paymentBehavior'] = self.payment_behavior
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "days_until_due") and self.days_until_due is not None:
            params['daysUntilDue'] = self.days_until_due
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "cancel_at") and self.cancel_at is not None:
            params['cancelAt'] = self.cancel_at
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "subscription_notify_url") and self.subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.subscription_notify_url
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerEmail' in response_body:
            self.__customer_email = response_body['customerEmail']
        if 'priceItems' in response_body:
            self.__price_items = []
            for item in response_body['priceItems']:
                obj = PriceItem()
                obj.parse_rsp_body(item)
                self.__price_items.append(obj)
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingSubscriptionCreateTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = BillingSubscriptionCreateDiscount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'paymentBehavior' in response_body:
            self.__payment_behavior = response_body['paymentBehavior']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'cancelAt' in response_body:
            self.__cancel_at = response_body['cancelAt']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'subscriptionNotifyUrl' in response_body:
            self.__subscription_notify_url = response_body['subscriptionNotifyUrl']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
