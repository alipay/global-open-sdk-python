import json
from com.alipay.ams.api.model.datetime import datetime
from com.alipay.ams.api.model.datetime import datetime
from com.alipay.ams.api.model.subscription_status import SubscriptionStatus
from com.alipay.ams.api.model.period_type import PeriodType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireSubscriptionListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireSubscriptionListRequest, self).__init__("/ams/api/v1/subscriptions/inquireSubscriptionList") 

        self.__merchant_account_id = None  # type: str
        self.__start_time_from = None  # type: datetime
        self.__start_time_to = None  # type: datetime
        self.__statuses = None  # type: [SubscriptionStatus]
        self.__payment_method_types = None  # type: [str]
        self.__currencies = None  # type: [str]
        self.__period_types = None  # type: [PeriodType]
        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        

    @property
    def merchant_account_id(self):
        """
        A unique ID to identify a specific merchant account.
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def start_time_from(self):
        """
        Filter Subscriptions with a start date after the specified date. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. Default if not provided: 7 days ago.
        """
        return self.__start_time_from

    @start_time_from.setter
    def start_time_from(self, value):
        self.__start_time_from = value
    @property
    def start_time_to(self):
        """
        Filter Subscriptions with a start date before the specified date. The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. Default if not provided: current time.
        """
        return self.__start_time_to

    @start_time_to.setter
    def start_time_to(self, value):
        self.__start_time_to = value
    @property
    def statuses(self):
        """
        Filter Subscriptions whose status matches any value in the list. Default if not provided: Get all subscriptions whose status is in [ACTIVE, CANCELLED, TERMINATED].
        """
        return self.__statuses

    @statuses.setter
    def statuses(self, value):
        self.__statuses = value
    @property
    def payment_method_types(self):
        """
        Filter Subscriptions whose payment method matches any value in the list. See Payment methods to check the valid values. Default if not provided: Subscriptions of all payment method are returned.
        """
        return self.__payment_method_types

    @payment_method_types.setter
    def payment_method_types(self, value):
        self.__payment_method_types = value
    @property
    def currencies(self):
        """
        Filter Subscriptions whose currency matches any value in the list. The transaction currency, which is a 3-letter currency code that follows the ISO 4217 standard. Default if not provided: Subscriptions of all currency are returned.
        """
        return self.__currencies

    @currencies.setter
    def currencies(self, value):
        self.__currencies = value
    @property
    def period_types(self):
        """
        Filter Subscriptions whose periodType matches any value in the list. Default if not provided: Subscriptions of all periodType are returned.
        """
        return self.__period_types

    @period_types.setter
    def period_types(self, value):
        self.__period_types = value
    @property
    def current_page(self):
        """
        Current page number. Default if not provided: Get all subscriptions in page 1.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        Page size. Default if not provided: Page size of 10.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "start_time_from") and self.start_time_from is not None:
            params['startTimeFrom'] = self.start_time_from
        if hasattr(self, "start_time_to") and self.start_time_to is not None:
            params['startTimeTo'] = self.start_time_to
        if hasattr(self, "statuses") and self.statuses is not None:
            params['statuses'] = self.statuses
        if hasattr(self, "payment_method_types") and self.payment_method_types is not None:
            params['paymentMethodTypes'] = self.payment_method_types
        if hasattr(self, "currencies") and self.currencies is not None:
            params['currencies'] = self.currencies
        if hasattr(self, "period_types") and self.period_types is not None:
            params['periodTypes'] = self.period_types
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'startTimeFrom' in response_body:
            self.__start_time_from = response_body['startTimeFrom']
        if 'startTimeTo' in response_body:
            self.__start_time_to = response_body['startTimeTo']
        if 'statuses' in response_body:
            self.__statuses = []
            for item in response_body['statuses']:
                self.__statuses.append(item)
        if 'paymentMethodTypes' in response_body:
            self.__payment_method_types = response_body['paymentMethodTypes']
        if 'currencies' in response_body:
            self.__currencies = response_body['currencies']
        if 'periodTypes' in response_body:
            self.__period_types = []
            for item in response_body['periodTypes']:
                self.__period_types.append(item)
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
