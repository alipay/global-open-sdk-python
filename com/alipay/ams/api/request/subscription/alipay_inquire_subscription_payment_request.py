import json
from com.alipay.ams.api.model.payment_status import PaymentStatus



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireSubscriptionPaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireSubscriptionPaymentRequest, self).__init__("/ams/api/v1/subscriptions/inquireSubscriptionPayment") 

        self.__merchant_account_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__payment_statuses = None  # type: [PaymentStatus]
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
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def payment_statuses(self):
        """
        Filter Transactions whose status matches any value in the list. Default if not provided: Transactions of all status are returned.
        """
        return self.__payment_statuses

    @payment_statuses.setter
    def payment_statuses(self, value):
        self.__payment_statuses = value
    @property
    def current_page(self):
        """
        Current page number. Default if not provided: Get all transactions in page 1.
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
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "payment_statuses") and self.payment_statuses is not None:
            params['paymentStatuses'] = self.payment_statuses
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
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'paymentStatuses' in response_body:
            self.__payment_statuses = []
            for item in response_body['paymentStatuses']:
                self.__payment_statuses.append(item)
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
