import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.billing_subscription_price_item import BillingSubscriptionPriceItem




class Subscription:
    def __init__(self):
        
        self.__subscription_id = None  # type: str
        self.__subscription_request_id = None  # type: str
        self.__status = None  # type: str
        self.__customer_id = None  # type: str
        self.__description = None  # type: str
        self.__billing_mode = None  # type: str
        self.__current_period_start = None  # type: str
        self.__current_period_end = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__canceled_at = None  # type: str
        self.__cancel_at = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__trial_start = None  # type: str
        self.__trial_end = None  # type: str
        self.__subtotal = None  # type: Amount
        self.__discount_amount = None  # type: Amount
        self.__total_amount = None  # type: Amount
        self.__price_items = None  # type: [BillingSubscriptionPriceItem]
        self.__termination_reason = None  # type: str
        self.__create_time = None  # type: str
        

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
    def subscription_request_id(self):
        """
        The original idempotency key used to create the subscription. Maximum length: 64 characters.
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
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
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def description(self):
        """
        The subscription description. Maximum length: 500 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def billing_mode(self):
        """
        The billing mode. Valid values are LICENSED, METERED, and MIXED. Maximum length: 8 characters.
        """
        return self.__billing_mode

    @billing_mode.setter
    def billing_mode(self, value):
        self.__billing_mode = value
    @property
    def current_period_start(self):
        """
        The start of the current billing period in ISO 8601 format.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def current_period_end(self):
        """
        The end of the current billing period in ISO 8601 format.
        """
        return self.__current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self.__current_period_end = value
    @property
    def cancel_at_period_end(self):
        """
        Whether the subscription is scheduled to be canceled at the end of the current period.
        """
        return self.__cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, value):
        self.__cancel_at_period_end = value
    @property
    def canceled_at(self):
        """
        The cancellation time in ISO 8601 format.
        """
        return self.__canceled_at

    @canceled_at.setter
    def canceled_at(self, value):
        self.__canceled_at = value
    @property
    def cancel_at(self):
        """
        The scheduled cancellation time in ISO 8601 format.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
    @property
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor in ISO 8601 format.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def trial_start(self):
        """
        The trial start time in ISO 8601 format.
        """
        return self.__trial_start

    @trial_start.setter
    def trial_start(self, value):
        self.__trial_start = value
    @property
    def trial_end(self):
        """
        The trial end time in ISO 8601 format.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value
    @property
    def subtotal(self):
        """Gets the subtotal of this Subscription.
        
        """
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
    @property
    def discount_amount(self):
        """Gets the discount_amount of this Subscription.
        
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value
    @property
    def total_amount(self):
        """Gets the total_amount of this Subscription.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def price_items(self):
        """
        The subscription price items.
        """
        return self.__price_items

    @price_items.setter
    def price_items(self, value):
        self.__price_items = value
    @property
    def termination_reason(self):
        """
        The termination reason. Returned when the status is TERMINATED. Maximum length: 64 characters.
        """
        return self.__termination_reason

    @termination_reason.setter
    def termination_reason(self, value):
        self.__termination_reason = value
    @property
    def create_time(self):
        """
        The subscription creation time in ISO 8601 format. List results are sorted by this field in descending order by default.
        """
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "billing_mode") and self.billing_mode is not None:
            params['billingMode'] = self.billing_mode
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "canceled_at") and self.canceled_at is not None:
            params['canceledAt'] = self.canceled_at
        if hasattr(self, "cancel_at") and self.cancel_at is not None:
            params['cancelAt'] = self.cancel_at
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "trial_start") and self.trial_start is not None:
            params['trialStart'] = self.trial_start
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        if hasattr(self, "subtotal") and self.subtotal is not None:
            params['subtotal'] = self.subtotal
        if hasattr(self, "discount_amount") and self.discount_amount is not None:
            params['discountAmount'] = self.discount_amount
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "price_items") and self.price_items is not None:
            params['priceItems'] = self.price_items
        if hasattr(self, "termination_reason") and self.termination_reason is not None:
            params['terminationReason'] = self.termination_reason
        if hasattr(self, "create_time") and self.create_time is not None:
            params['createTime'] = self.create_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'billingMode' in response_body:
            self.__billing_mode = response_body['billingMode']
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'canceledAt' in response_body:
            self.__canceled_at = response_body['canceledAt']
        if 'cancelAt' in response_body:
            self.__cancel_at = response_body['cancelAt']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'trialStart' in response_body:
            self.__trial_start = response_body['trialStart']
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
        if 'subtotal' in response_body:
            self.__subtotal = Amount()
            self.__subtotal.parse_rsp_body(response_body['subtotal'])
        if 'discountAmount' in response_body:
            self.__discount_amount = Amount()
            self.__discount_amount.parse_rsp_body(response_body['discountAmount'])
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'priceItems' in response_body:
            self.__price_items = []
            for item in response_body['priceItems']:
                obj = BillingSubscriptionPriceItem()
                obj.parse_rsp_body(item)
                self.__price_items.append(obj)
        if 'terminationReason' in response_body:
            self.__termination_reason = response_body['terminationReason']
        if 'createTime' in response_body:
            self.__create_time = response_body['createTime']
