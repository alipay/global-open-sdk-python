import json
from com.alipay.ams.api.model.price_item import PriceItem
from com.alipay.ams.api.model.billing_trial_settings import BillingTrialSettings
from com.alipay.ams.api.model.billing_discount import BillingDiscount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionCreateRequest, self).__init__("/ams/api/v1/billing/subscription/create") 

        self.__subscription_request_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__customer_email = None  # type: str
        self.__price_items = None  # type: [PriceItem]
        self.__trial_settings = None  # type: BillingTrialSettings
        self.__discounts = None  # type: [BillingDiscount]
        self.__payment_behavior = None  # type: str
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__cancel_at = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__description = None  # type: str
        self.__subscription_notify_url = None  # type: str
        self.__metadata = None  # type: str
        

    @property
    def subscription_request_id(self):
        """
        Idempotency key. Unique per merchant. This field is an idempotent field. Not null. Idempotent replay (2026-08-06 code-verified): if a request is repeated with the same &#x60;subscriptionRequestId&#x60;, the API returns SUCCESS together with the previously created subscription and its latest invoice - no new subscription is created
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def customer_id(self):
        """
        Existing customer ID. References a customer already created in your account. Mutually optional with &#x60;customerEmail&#x60; - you must provide at least one. If both are provided, &#x60;customerId&#x60; takes precedence. Can be null
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_email(self):
        """
        Customer email address. Use this when you don&#39;t yet have a &#x60;customerId&#x60; - Antom will create a new customer with this email. If a customer with this email already exists under your merchant account, a &#x60;CUSTOMER_EMAIL_DUPLICATED&#x60; error is returned - use the existing customer&#39;s &#x60;customerId&#x60; instead. Mutually optional with &#x60;customerId&#x60;. Must be a valid email format. Can be null
        """
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, value):
        self.__customer_email = value
    @property
    def price_items(self):
        """
        List of price items. The list must contain 1 to 20 items.
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
        Pre-bound discounts. Currently limited to exactly 1 item (the previous maximum of 10 no longer applies) - sending more than one discount item returns PARAM_ILLEGAL. Can be null
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value
    @property
    def payment_behavior(self):
        """
        Payment attempt behavior. See Enum Behavior Reference for detailed behavior per value. Default: ALLOW_INCOMPLETE. Not null
        """
        return self.__payment_behavior

    @payment_behavior.setter
    def payment_behavior(self, value):
        self.__payment_behavior = value
    @property
    def collection_method(self):
        """
        Collection method. CHARGE_AUTOMATICALLY - charges automatically at each billing cycle. SEND_INVOICE - emails invoice; customer pays manually. Default: CHARGE_AUTOMATICALLY. Not null
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def days_until_due(self):
        """
        Days to pay invoices. Range: 1-365, default: 30. Can be null
        """
        return self.__days_until_due

    @days_until_due.setter
    def days_until_due(self, value):
        self.__days_until_due = value
    @property
    def cancel_at(self):
        """
        Pre-schedule cancellation. ISO 8601 with timezone offset, must be future. Can be null
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
    @property
    def cancel_at_period_end(self):
        """
        Whether to automatically cancel the subscription when the current billing period ends. If not specified, defaults to false. Can be null
        """
        return self.__cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self.__cancel_at_period_end = value
    @property
    def description(self):
        """
        Subscription description, displayable to customer. PII caution: should not contain personal data (names, emails) - use structured fields for customer information. No HTML tags. Can be null. Server-side fallback (2026-07-29 SA): when blank, the WALLET payment paths send &#x60;Subscription {subscriptionId} payment&#x60; as the A+ APS &#x60;orderDescription&#x60; (mandatory downstream) - no contract change, field stays optional
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def subscription_notify_url(self):
        """
        Subscription status notification URL. Valid URL. Can be null
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value
    @property
    def metadata(self):
        """
        Key-value extension data as a JSON-encoded string. Keys max 64 chars, values max 512 chars. Maximum size: 20 pairs. PII prohibition applies - must not contain personal data (names, emails, IDs). Use structured fields for PII. Can be null The value must be a valid JSON object string.
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
            self.__trial_settings = BillingTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = BillingDiscount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'paymentBehavior' in response_body:
            self.__payment_behavior = response_body['paymentBehavior']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
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
