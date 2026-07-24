import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.billing_subscription_inquire_details_trial_settings import BillingSubscriptionInquireDetailsTrialSettings
from com.alipay.ams.api.model.billing_subscription_inquire_details_pause_collection import BillingSubscriptionInquireDetailsPauseCollection
from com.alipay.ams.api.model.billing_subscription_inquire_details_cancellation_details import BillingSubscriptionInquireDetailsCancellationDetails
from com.alipay.ams.api.model.subscription_item import SubscriptionItem
from com.alipay.ams.api.model.discount import Discount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__subscription_request_id = None  # type: str
        self.__created_at = None  # type: str
        self.__status = None  # type: str
        self.__current_period_start = None  # type: str
        self.__current_period_end = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__cancel_at_period_end = None  # type: bool
        self.__canceled_at = None  # type: str
        self.__trial_start = None  # type: str
        self.__trial_end = None  # type: str
        self.__trial_settings = None  # type: BillingSubscriptionInquireDetailsTrialSettings
        self.__pause_collection = None  # type: BillingSubscriptionInquireDetailsPauseCollection
        self.__cancel_at = None  # type: str
        self.__collection_method = None  # type: str
        self.__days_until_due = None  # type: int
        self.__cancellation_details = None  # type: BillingSubscriptionInquireDetailsCancellationDetails
        self.__termination_reason = None  # type: str
        self.__description = None  # type: str
        self.__default_payment_method = None  # type: str
        self.__subscription_items = None  # type: [SubscriptionItem]
        self.__discounts = None  # type: [Discount]
        self.__metadata = None  # type: {str: (str,)}
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionInquireDetailsResponse.
        
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
    def subscription_request_id(self):
        """
        The subscription request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def created_at(self):
        """
        The created at.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value
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
    def current_period_start(self):
        """
        The current period start.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def current_period_end(self):
        """
        The current period end.
        """
        return self.__current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self.__current_period_end = value
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
    def cancel_at_period_end(self):
        """
        The cancel at period end.
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
    def trial_start(self):
        """
        The trial start. Note: See documentation for details.
        """
        return self.__trial_start

    @trial_start.setter
    def trial_start(self, value):
        self.__trial_start = value
    @property
    def trial_end(self):
        """
        The trial end. Note: See documentation for details.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value
    @property
    def trial_settings(self):
        """Gets the trial_settings of this AlipayBillingSubscriptionInquireDetailsResponse.
        
        """
        return self.__trial_settings

    @trial_settings.setter
    def trial_settings(self, value):
        self.__trial_settings = value
    @property
    def pause_collection(self):
        """Gets the pause_collection of this AlipayBillingSubscriptionInquireDetailsResponse.
        
        """
        return self.__pause_collection

    @pause_collection.setter
    def pause_collection(self, value):
        self.__pause_collection = value
    @property
    def cancel_at(self):
        """
        The cancel at. Note: See documentation for details.
        """
        return self.__cancel_at

    @cancel_at.setter
    def cancel_at(self, value):
        self.__cancel_at = value
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
    def cancellation_details(self):
        """Gets the cancellation_details of this AlipayBillingSubscriptionInquireDetailsResponse.
        
        """
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = value
    @property
    def termination_reason(self):
        """
        The termination reason. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__termination_reason

    @termination_reason.setter
    def termination_reason(self, value):
        self.__termination_reason = value
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
    def default_payment_method(self):
        """
        The default payment method token. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, value):
        self.__default_payment_method = value
    @property
    def subscription_items(self):
        """
        The subscription items. Maximum length: 20 characters.
        """
        return self.__subscription_items

    @subscription_items.setter
    def subscription_items(self, value):
        self.__subscription_items = value
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
    def metadata(self):
        """
        Custom metadata for special use cases. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "created_at") and self.created_at is not None:
            params['createdAt'] = self.created_at
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "cancel_at_period_end") and self.cancel_at_period_end is not None:
            params['cancelAtPeriodEnd'] = self.cancel_at_period_end
        if hasattr(self, "canceled_at") and self.canceled_at is not None:
            params['canceledAt'] = self.canceled_at
        if hasattr(self, "trial_start") and self.trial_start is not None:
            params['trialStart'] = self.trial_start
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        if hasattr(self, "trial_settings") and self.trial_settings is not None:
            params['trialSettings'] = self.trial_settings
        if hasattr(self, "pause_collection") and self.pause_collection is not None:
            params['pauseCollection'] = self.pause_collection
        if hasattr(self, "cancel_at") and self.cancel_at is not None:
            params['cancelAt'] = self.cancel_at
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "days_until_due") and self.days_until_due is not None:
            params['daysUntilDue'] = self.days_until_due
        if hasattr(self, "cancellation_details") and self.cancellation_details is not None:
            params['cancellationDetails'] = self.cancellation_details
        if hasattr(self, "termination_reason") and self.termination_reason is not None:
            params['terminationReason'] = self.termination_reason
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "default_payment_method") and self.default_payment_method is not None:
            params['defaultPaymentMethod'] = self.default_payment_method
        if hasattr(self, "subscription_items") and self.subscription_items is not None:
            params['subscriptionItems'] = self.subscription_items
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayBillingSubscriptionInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'createdAt' in response_body:
            self.__created_at = response_body['createdAt']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'cancelAtPeriodEnd' in response_body:
            self.__cancel_at_period_end = response_body['cancelAtPeriodEnd']
        if 'canceledAt' in response_body:
            self.__canceled_at = response_body['canceledAt']
        if 'trialStart' in response_body:
            self.__trial_start = response_body['trialStart']
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
        if 'trialSettings' in response_body:
            self.__trial_settings = BillingSubscriptionInquireDetailsTrialSettings()
            self.__trial_settings.parse_rsp_body(response_body['trialSettings'])
        if 'pauseCollection' in response_body:
            self.__pause_collection = BillingSubscriptionInquireDetailsPauseCollection()
            self.__pause_collection.parse_rsp_body(response_body['pauseCollection'])
        if 'cancelAt' in response_body:
            self.__cancel_at = response_body['cancelAt']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'daysUntilDue' in response_body:
            self.__days_until_due = response_body['daysUntilDue']
        if 'cancellationDetails' in response_body:
            self.__cancellation_details = BillingSubscriptionInquireDetailsCancellationDetails()
            self.__cancellation_details.parse_rsp_body(response_body['cancellationDetails'])
        if 'terminationReason' in response_body:
            self.__termination_reason = response_body['terminationReason']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'defaultPaymentMethod' in response_body:
            self.__default_payment_method = response_body['defaultPaymentMethod']
        if 'subscriptionItems' in response_body:
            self.__subscription_items = []
            for item in response_body['subscriptionItems']:
                obj = SubscriptionItem()
                obj.parse_rsp_body(item)
                self.__subscription_items.append(obj)
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = Discount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
