import json
from com.alipay.ams.api.model.billing_trial_settings import BillingTrialSettings
from com.alipay.ams.api.model.billing_discount import BillingDiscount




class BillingSubscription:
    def __init__(self):
        
        self.__customer_id = None  # type: str
        self.__trial_settings = None  # type: BillingTrialSettings
        self.__payment_behavior = None  # type: str
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__cancel_at = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__description = None  # type: str
        self.__discounts = None  # type: [BillingDiscount]
        self.__default_payment_method = None  # type: str
        self.__allow_promotion_code = None  # type: bool
        self.__subscription_notify_url = None  # type: str
        

    @property
    def customer_id(self):
        """
        The customer ID.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def trial_settings(self):
        """Gets the trial_settings of this BillingSubscription.
        
        """
        return self.__trial_settings

    @trial_settings.setter
    def trial_settings(self, value):
        self.__trial_settings = value
    @property
    def payment_behavior(self):
        """
        Payment behavior.
        """
        return self.__payment_behavior

    @payment_behavior.setter
    def payment_behavior(self, value):
        self.__payment_behavior = value
    @property
    def collection_method(self):
        """
        Collection method.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def days_until_due(self):
        """
        Number of days until due.
        """
        return self.__days_until_due

    @days_until_due.setter
    def days_until_due(self, value):
        self.__days_until_due = value
    @property
    def cancel_at(self):
        """
        Cancellation time.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
    @property
    def cancel_at_period_end(self):
        """
        Whether to cancel at period end.
        """
        return self.__cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self.__cancel_at_period_end = value
    @property
    def description(self):
        """
        Description.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def discounts(self):
        """
        Discounts applied to the subscription.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value
    @property
    def default_payment_method(self):
        """
        The default payment method for this subscription. It takes precedence over the customer-level default. Maximum length: 64 characters.
        """
        return self.__default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, value):
        self.__default_payment_method = value
    @property
    def allow_promotion_code(self):
        """
        Whether to allow promotion codes.
        """
        return self.__allow_promotion_code

    @allow_promotion_code.setter
    def allow_promotion_code(self, value):
        self.__allow_promotion_code = value
    @property
    def subscription_notify_url(self):
        """
        The URL for subscription notifications.
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
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
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        if hasattr(self, "default_payment_method") and self.default_payment_method is not None:
            params['defaultPaymentMethod'] = self.default_payment_method
        if hasattr(self, "allow_promotion_code") and self.allow_promotion_code is not None:
            params['allowPromotionCode'] = self.allow_promotion_code
        if hasattr(self, "subscription_notify_url") and self.subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.subscription_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
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
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = BillingDiscount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'defaultPaymentMethod' in response_body:
            self.__default_payment_method = response_body['defaultPaymentMethod']
        if 'allowPromotionCode' in response_body:
            self.__allow_promotion_code = response_body['allowPromotionCode']
        if 'subscriptionNotifyUrl' in response_body:
            self.__subscription_notify_url = response_body['subscriptionNotifyUrl']
