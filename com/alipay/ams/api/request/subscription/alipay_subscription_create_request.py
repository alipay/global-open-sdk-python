import json
from com.alipay.ams.api.model.customized_info import CustomizedInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.trial import Trial



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySubscriptionCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionCreateRequest, self).__init__("/ams/api/v1/subscriptions/create") 

        self.__customized_info = None  # type: CustomizedInfo
        self.__merchant_account_id = None  # type: str
        self.__allow_accumulate = None  # type: bool
        self.__max_accumulate_amount = None  # type: Amount
        self.__subscription_request_id = None  # type: str
        self.__subscription_description = None  # type: str
        self.__subscription_redirect_url = None  # type: str
        self.__subscription_start_time = None  # type: str
        self.__subscription_end_time = None  # type: str
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_expiry_time = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__subscription_notification_url = None  # type: str
        self.__payment_notification_url = None  # type: str
        self.__order_info = None  # type: OrderInfo
        self.__payment_amount = None  # type: Amount
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__env = None  # type: Env
        self.__trials = None  # type: [Trial]
        

    @property
    def customized_info(self):
        """Gets the customized_info of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__customized_info

    @customized_info.setter
    def customized_info(self, value):
        self.__customized_info = value
    @property
    def merchant_account_id(self):
        """
        The merchant account ID
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def allow_accumulate(self):
        """
        Whether to allow accumulate payment amount
        """
        return self.__allow_accumulate

    @allow_accumulate.setter
    def allow_accumulate(self, value):
        self.__allow_accumulate = value
    @property
    def max_accumulate_amount(self):
        """Gets the max_accumulate_amount of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__max_accumulate_amount

    @max_accumulate_amount.setter
    def max_accumulate_amount(self, value):
        self.__max_accumulate_amount = value
    @property
    def subscription_request_id(self):
        """
        The unique ID assigned by a merchant to identify a subscription request. Antom uses this field for idempotency control.    More information:  This field is an API idempotency field.For subscription requests that are initiated with the same value of subscriptionRequestId and reach a final status of S or F, the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def subscription_description(self):
        """
        The description of the subscription, used for displaying user consumption records and other actions.   More information:  Maximum length: 256 characters
        """
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value
    @property
    def subscription_redirect_url(self):
        """
        The merchant page URL that the user is redirected to after authorizing the subscription.   More information:  Maximum length: 2048 characters 
        """
        return self.__subscription_redirect_url

    @subscription_redirect_url.setter
    def subscription_redirect_url(self, value):
        self.__subscription_redirect_url = value
    @property
    def subscription_start_time(self):
        """
        The date and time when the subscription becomes active.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_end_time(self):
        """
        The date and time when the subscription ends.  Note: Specify this parameter when you want to designate the subscription end time.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def period_rule(self):
        """Gets the period_rule of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def subscription_expiry_time(self):
        """
        A specific date and time after which the created subscription expires. When the subscription expires, the order must be terminated. The default value of this parameter is 30 minutes after the subscription creation request is sent.  Note: Specify this parameter if you want to designate the subscription creation expiration time. The specified payment expiration time must be less than 48 hours after the subscription request is sent.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def subscription_notification_url(self):
        """
        The URL that is used to receive the subscription result notification.   You can also configure the subscription notification URL in Antom Dashboard. If you specify this URL in both this API and Antom Dashboard, the URL configured in the API takes precedence.    Only one subscription notification URL can be configured in Antom Dashboard.  More information:  Maximum length: 2048 characters
        """
        return self.__subscription_notification_url

    @subscription_notification_url.setter
    def subscription_notification_url(self, value):
        self.__subscription_notification_url = value
    @property
    def payment_notification_url(self):
        """
        The URL that is used to receive the payment result notification for each subscription period.  You can also configure the subscription notification URL in Antom Dashboard. If you specify this URL in both this API and Antom Dashboard, the URL configured in the API takes precedence.    You can only configure one subscription notification URL in Antom Dashboard.  More information:  Maximum length: 2048 characters 
        """
        return self.__payment_notification_url

    @payment_notification_url.setter
    def payment_notification_url(self, value):
        self.__payment_notification_url = value
    @property
    def order_info(self):
        """Gets the order_info of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__order_info

    @order_info.setter
    def order_info(self, value):
        self.__order_info = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def settlement_strategy(self):
        """Gets the settlement_strategy of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value
    @property
    def env(self):
        """Gets the env of this AlipaySubscriptionCreateRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def trials(self):
        """
        The list of trial information of a subscription.    Note: Specify this parameter if the subscription includes any trial periods.
        """
        return self.__trials

    @trials.setter
    def trials(self, value):
        self.__trials = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customized_info") and self.customized_info is not None:
            params['customizedInfo'] = self.customized_info
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "allow_accumulate") and self.allow_accumulate is not None:
            params['allowAccumulate'] = self.allow_accumulate
        if hasattr(self, "max_accumulate_amount") and self.max_accumulate_amount is not None:
            params['maxAccumulateAmount'] = self.max_accumulate_amount
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "subscription_description") and self.subscription_description is not None:
            params['subscriptionDescription'] = self.subscription_description
        if hasattr(self, "subscription_redirect_url") and self.subscription_redirect_url is not None:
            params['subscriptionRedirectUrl'] = self.subscription_redirect_url
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "subscription_expiry_time") and self.subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.subscription_expiry_time
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "subscription_notification_url") and self.subscription_notification_url is not None:
            params['subscriptionNotificationUrl'] = self.subscription_notification_url
        if hasattr(self, "payment_notification_url") and self.payment_notification_url is not None:
            params['paymentNotificationUrl'] = self.payment_notification_url
        if hasattr(self, "order_info") and self.order_info is not None:
            params['orderInfo'] = self.order_info
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "settlement_strategy") and self.settlement_strategy is not None:
            params['settlementStrategy'] = self.settlement_strategy
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "trials") and self.trials is not None:
            params['trials'] = self.trials
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customizedInfo' in response_body:
            self.__customized_info = CustomizedInfo()
            self.__customized_info.parse_rsp_body(response_body['customizedInfo'])
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'allowAccumulate' in response_body:
            self.__allow_accumulate = response_body['allowAccumulate']
        if 'maxAccumulateAmount' in response_body:
            self.__max_accumulate_amount = Amount()
            self.__max_accumulate_amount.parse_rsp_body(response_body['maxAccumulateAmount'])
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'subscriptionDescription' in response_body:
            self.__subscription_description = response_body['subscriptionDescription']
        if 'subscriptionRedirectUrl' in response_body:
            self.__subscription_redirect_url = response_body['subscriptionRedirectUrl']
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'subscriptionExpiryTime' in response_body:
            self.__subscription_expiry_time = response_body['subscriptionExpiryTime']
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'subscriptionNotificationUrl' in response_body:
            self.__subscription_notification_url = response_body['subscriptionNotificationUrl']
        if 'paymentNotificationUrl' in response_body:
            self.__payment_notification_url = response_body['paymentNotificationUrl']
        if 'orderInfo' in response_body:
            self.__order_info = OrderInfo()
            self.__order_info.parse_rsp_body(response_body['orderInfo'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'settlementStrategy' in response_body:
            self.__settlement_strategy = SettlementStrategy()
            self.__settlement_strategy.parse_rsp_body(response_body['settlementStrategy'])
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'trials' in response_body:
            self.__trials = []
            for item in response_body['trials']:
                obj = Trial()
                obj.parse_rsp_body(item)
                self.__trials.append(obj)
