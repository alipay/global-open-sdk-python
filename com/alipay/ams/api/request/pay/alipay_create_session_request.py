from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCreateSessionRequest(AlipayRequest):

    def __init__(self):
        super(AlipayCreateSessionRequest, self).__init__()
        self.__product_code = None
        self.__payment_request_id = None
        self.__order = None
        self.__payment_amount = None
        self.__payment_method = None
        self.__payment_session_expiry_time = None
        self.__payment_redirect_url = None
        self.__payment_notify_url = None
        self.__payment_factor = None
        self.__settlement_strategy = None
        self.__env = None
        self.__merchant_region = None
        self.__credit_pay_plan = None
        self.__enable_installment_collection = None


    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def payment_amount(self):
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def payment_session_expiry_time(self):
        return self.__payment_session_expiry_time

    @payment_session_expiry_time.setter
    def payment_session_expiry_time(self, value):
        self.__payment_session_expiry_time = value

    @property
    def payment_redirect_url(self):
        return self.__payment_redirect_url

    @payment_redirect_url.setter
    def payment_redirect_url(self, value):
        self.__payment_redirect_url = value

    @property
    def payment_notify_url(self):
        return self.__payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self.__payment_notify_url = value

    @property
    def payment_factor(self):
        return self.__payment_factor

    @payment_factor.setter
    def payment_factor(self, value):
        self.__payment_factor = value

    @property
    def settlement_strategy(self):
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value;

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value;

    @property
    def credit_pay_plan(self):
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value;

    @property
    def enable_installment_collection(self):
        return self.__enable_installment_collection

    @enable_installment_collection.setter
    def enable_installment_collection(self, value):
        self.__enable_installment_collection = value;


    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code:
            params['productCode'] = self.product_code
        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "order") and self.order:
            params['order'] = self.order.__to_ams_dict()
        if hasattr(self, "payment_amount") and self.payment_amount:
            params['paymentAmount'] = self.payment_amount.__to_ams_dict()
        if hasattr(self, "payment_method") and self.payment_method:
            params['paymentMethod'] = self.payment_method.__to_ams_dict()
        if hasattr(self, "payment_session_expiry_time") and self.payment_session_expiry_time:
            params['paymentSessionExpiryTime'] = self.payment_session_expiry_time
        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url:
            params['paymentRedirectUrl'] = self.payment_redirect_url
        if hasattr(self, "payment_notify_url") and self.payment_notify_url:
            params['paymentNotifyUrl'] = self.payment_notify_url
        if hasattr(self, "payment_factor") and self.payment_factor:
            params['paymentFactor'] = self.payment_factor.__to_ams_dict()
        if hasattr(self, "settlement_strategy") and self.settlement_strategy:
            params['settlementStrategy'] = self.settlement_strategy.__to_ams_dict()
        if hasattr(self, "env") and self.env:
            params['env'] = self.env.__to_ams_dict()
        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan:
            params['creditPayPlan'] = self.credit_pay_plan.__to_ams_dict()
        if hasattr(self, "enable_installment_collection") and self.enable_installment_collection:
            params['enableInstallmentCollection'] = self.enable_installment_collection

        return params