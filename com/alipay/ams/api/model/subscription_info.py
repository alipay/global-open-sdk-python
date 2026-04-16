import json
from com.alipay.ams.api.model.subscription_status import SubscriptionStatus
from com.alipay.ams.api.model.period_type import PeriodType
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.trial_plan import TrialPlan
from com.alipay.ams.api.model.trial import Trial
from com.alipay.ams.api.model.amount import Amount




class SubscriptionInfo:
    def __init__(self):
        
        self.__subscription_id = None  # type: str
        self.__description = None  # type: str
        self.__subscription_description = None  # type: str
        self.__status = None  # type: SubscriptionStatus
        self.__subscription_start_time = None  # type: str
        self.__subscription_end_time = None  # type: str
        self.__period_type = None  # type: PeriodType
        self.__period_count = None  # type: int
        self.__period_rule = None  # type: PeriodRule
        self.__current_period_start = None  # type: str
        self.__current_period_end = None  # type: str
        self.__current_phase_no = None  # type: int
        self.__payment_method = None  # type: PaymentMethod
        self.__payment_amount = None  # type: Amount
        self.__last_update_time = None  # type: str
        self.__related_subscription_id = None  # type: str
        self.__trial_plan = None  # type: TrialPlan
        self.__trials = None  # type: [Trial]
        self.__subscription_notify_url = None  # type: str
        self.__subscription_expiry_time = None  # type: str
        self.__allow_retry = None  # type: bool
        self.__max_amount_floor = None  # type: Amount
        

    @property
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def description(self):
        """
        The description of the subscription, used for displaying user consumption records and other actions.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def subscription_description(self):
        """
        Description of the subscription plan
        """
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value
    @property
    def status(self):
        """Gets the status of this SubscriptionInfo.
        
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def subscription_start_time(self):
        """
        The date and time when the subscription becomes active. The value follows the ISO 8601 standard format.
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_end_time(self):
        """
        The date and time when the subscription ends. The value follows the ISO 8601 standard format. The subscriptionEndTime can be NULL.
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def period_type(self):
        """Gets the period_type of this SubscriptionInfo.
        
        """
        return self.__period_type

    @period_type.setter
    def period_type(self, value):
        self.__period_type = value
    @property
    def period_count(self):
        """
        The number of times the period type repeats in one subscription cycle. For example, a periodCount of 2 with periodType MONTH means the subscription period is 2 months.
        """
        return self.__period_count

    @period_count.setter
    def period_count(self, value):
        self.__period_count = value
    @property
    def period_rule(self):
        """Gets the period_rule of this SubscriptionInfo.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def current_period_start(self):
        """
        Start time of current period.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def current_period_end(self):
        """
        End time of current period.
        """
        return self.__current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self.__current_period_end = value
    @property
    def current_phase_no(self):
        """
        Indicates current phase of subscription period, start from 1.
        """
        return self.__current_phase_no

    @current_phase_no.setter
    def current_phase_no(self, value):
        self.__current_phase_no = value
    @property
    def payment_method(self):
        """Gets the payment_method of this SubscriptionInfo.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this SubscriptionInfo.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def last_update_time(self):
        """
        DateTime when the subscription is changed using the Change/Update API.
        """
        return self.__last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self.__last_update_time = value
    @property
    def related_subscription_id(self):
        """
        When merchants use Change API, a new subscription is created base on the current one. This field stores the ID of the original subscription and represents the relationship between the old and new subscription.
        """
        return self.__related_subscription_id

    @related_subscription_id.setter
    def related_subscription_id(self, value):
        self.__related_subscription_id = value
    @property
    def trial_plan(self):
        """Gets the trial_plan of this SubscriptionInfo.
        
        """
        return self.__trial_plan

    @trial_plan.setter
    def trial_plan(self, value):
        self.__trial_plan = value
    @property
    def trials(self):
        """
        List of trial periods for the subscription
        """
        return self.__trials

    @trials.setter
    def trials(self, value):
        self.__trials = value
    @property
    def subscription_notify_url(self):
        """
        URL for subscription notifications
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value
    @property
    def subscription_expiry_time(self):
        """
        Expiry time of the subscription in ISO 8601 format
        """
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value
    @property
    def allow_retry(self):
        """
        Field is used only in the PIX recurrence scenario.  Whether to allow a retry in the event that a recurring payment fails due to insufficient balance.
        """
        return self.__allow_retry

    @allow_retry.setter
    def allow_retry(self, value):
        self.__allow_retry = value
    @property
    def max_amount_floor(self):
        """Gets the max_amount_floor of this SubscriptionInfo.
        
        """
        return self.__max_amount_floor

    @max_amount_floor.setter
    def max_amount_floor(self, value):
        self.__max_amount_floor = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "subscription_description") and self.subscription_description is not None:
            params['subscriptionDescription'] = self.subscription_description
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "period_type") and self.period_type is not None:
            params['periodType'] = self.period_type
        if hasattr(self, "period_count") and self.period_count is not None:
            params['periodCount'] = self.period_count
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "current_phase_no") and self.current_phase_no is not None:
            params['currentPhaseNo'] = self.current_phase_no
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "last_update_time") and self.last_update_time is not None:
            params['lastUpdateTime'] = self.last_update_time
        if hasattr(self, "related_subscription_id") and self.related_subscription_id is not None:
            params['relatedSubscriptionId'] = self.related_subscription_id
        if hasattr(self, "trial_plan") and self.trial_plan is not None:
            params['trialPlan'] = self.trial_plan
        if hasattr(self, "trials") and self.trials is not None:
            params['trials'] = self.trials
        if hasattr(self, "subscription_notify_url") and self.subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.subscription_notify_url
        if hasattr(self, "subscription_expiry_time") and self.subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.subscription_expiry_time
        if hasattr(self, "allow_retry") and self.allow_retry is not None:
            params['allowRetry'] = self.allow_retry
        if hasattr(self, "max_amount_floor") and self.max_amount_floor is not None:
            params['maxAmountFloor'] = self.max_amount_floor
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'subscriptionDescription' in response_body:
            self.__subscription_description = response_body['subscriptionDescription']
        if 'status' in response_body:
            status_temp = SubscriptionStatus.value_of(response_body['status'])
            self.__status = status_temp
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'periodType' in response_body:
            period_type_temp = PeriodType.value_of(response_body['periodType'])
            self.__period_type = period_type_temp
        if 'periodCount' in response_body:
            self.__period_count = response_body['periodCount']
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'currentPhaseNo' in response_body:
            self.__current_phase_no = response_body['currentPhaseNo']
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'lastUpdateTime' in response_body:
            self.__last_update_time = response_body['lastUpdateTime']
        if 'relatedSubscriptionId' in response_body:
            self.__related_subscription_id = response_body['relatedSubscriptionId']
        if 'trialPlan' in response_body:
            self.__trial_plan = TrialPlan()
            self.__trial_plan.parse_rsp_body(response_body['trialPlan'])
        if 'trials' in response_body:
            self.__trials = []
            for item in response_body['trials']:
                obj = Trial()
                obj.parse_rsp_body(item)
                self.__trials.append(obj)
        if 'subscriptionNotifyUrl' in response_body:
            self.__subscription_notify_url = response_body['subscriptionNotifyUrl']
        if 'subscriptionExpiryTime' in response_body:
            self.__subscription_expiry_time = response_body['subscriptionExpiryTime']
        if 'allowRetry' in response_body:
            self.__allow_retry = response_body['allowRetry']
        if 'maxAmountFloor' in response_body:
            self.__max_amount_floor = Amount()
            self.__max_amount_floor.parse_rsp_body(response_body['maxAmountFloor'])
