import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.subscription_item import SubscriptionItem
from com.alipay.ams.api.model.billing_discount import BillingDiscount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__subscription_request_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__current_period_start = None  # type: str
        self.__current_period_end = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__trial_start = None  # type: str
        self.__trial_end = None  # type: str
        self.__cancel_at = None  # type: str
        self.__description = None  # type: str
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__subscription_items = None  # type: [SubscriptionItem]
        self.__discounts = None  # type: [BillingDiscount]
        self.__subscription_notify_url = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscription_request_id(self):
        """
        Idempotency key echo-back. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def subscription_id(self):
        """
        Created subscription ID. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def customer_id(self):
        """
        The customer this subscription belongs to. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def invoice_id(self):
        """
        ID of the draft Invoice created alongside the subscription. Returned when subscription creation generates an invoice (i.e., non-zero amount or trial with invoice). Can be null Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def status(self):
        """
        Subscription status after creation. Possible values at creation: INCOMPLETE (first payment pending), TRIALING (trial configured). ACTIVE can only appear after Step 2 (&#x60;payments/pay&#x60;) succeeds and is never returned at creation (2026-08-06 code-verified darksite audit). Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def current_period_start(self):
        """
        Billing period start. ISO 8601 with timezone offset. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def current_period_end(self):
        """
        Billing period end. ISO 8601 with timezone offset. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self.__current_period_end = value
    @property
    def billing_cycle_anchor(self):
        """
        Billing cycle anchor - the reference point all future billing periods are measured from. System-derived, not merchant-writable (it was withdrawn from the request; see the request table). Derivation: without a trial -&gt; the subscription creation timestamp (NOW); with a trial -&gt; the trial end date (&#x60;trialEnd&#x60;), so the first paid cycle begins when the trial ends. The anchor always describes the full, uncapped cycle - setting &#x60;cancelAt&#x60; inside the first period shortens &#x60;currentPeriodEnd&#x60; but leaves &#x60;billingCycleAnchor&#x60; unchanged. ISO 8601 with timezone offset. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def trial_start(self):
        """
        Trial start. ISO 8601 with timezone offset Returned only when result.resultCode is SUCCESS.
        """
        return self.__trial_start

    @trial_start.setter
    def trial_start(self, value):
        self.__trial_start = value
    @property
    def trial_end(self):
        """
        Trial end. ISO 8601 with timezone offset Returned only when result.resultCode is SUCCESS.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value
    @property
    def cancel_at(self):
        """
        Scheduled cancellation timestamp Returned only when result.resultCode is SUCCESS.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
    @property
    def description(self):
        """
        Subscription description echo-back. No HTML tags Returned only when result.resultCode is SUCCESS.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def collection_method(self):
        """
        Collection method echo-back. Not null Returned only when result.resultCode is SUCCESS.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def days_until_due(self):
        """
        Days until invoice due Returned only when result.resultCode is SUCCESS.
        """
        return self.__days_until_due

    @days_until_due.setter
    def days_until_due(self, value):
        self.__days_until_due = value
    @property
    def subscription_items(self):
        """
        The created subscription items, one for each request &#x60;priceItems&#x60; entry. A successful response contains at most 20 items.
        """
        return self.__subscription_items

    @subscription_items.setter
    def subscription_items(self, value):
        self.__subscription_items = value
    @property
    def discounts(self):
        """
        Discount preference echo-back from request - at most 1 item, matching the request limit. Not Antom-generated data - echoed as provided by merchant in request Returned only when result.resultCode is SUCCESS.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value
    @property
    def subscription_notify_url(self):
        """
        Subscription notification URL echo-back Returned only when result.resultCode is SUCCESS.
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "trial_start") and self.trial_start is not None:
            params['trialStart'] = self.trial_start
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        if hasattr(self, "cancel_at") and self.cancel_at is not None:
            params['cancelAt'] = self.cancel_at
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "days_until_due") and self.days_until_due is not None:
            params['daysUntilDue'] = self.days_until_due
        if hasattr(self, "subscription_items") and self.subscription_items is not None:
            params['subscriptionItems'] = self.subscription_items
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        if hasattr(self, "subscription_notify_url") and self.subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.subscription_notify_url
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayBillingSubscriptionCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'trialStart' in response_body:
            self.__trial_start = response_body['trialStart']
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
        if 'cancelAt' in response_body:
            self.__cancel_at = response_body['cancelAt']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
        if 'subscriptionItems' in response_body:
            self.__subscription_items = []
            for item in response_body['subscriptionItems']:
                obj = SubscriptionItem()
                obj.parse_rsp_body(item)
                self.__subscription_items.append(obj)
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = BillingDiscount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'subscriptionNotifyUrl' in response_body:
            self.__subscription_notify_url = response_body['subscriptionNotifyUrl']
