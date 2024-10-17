import json

from com.alipay.ams.api.model.agreement_info import AgreementInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCreateSessionRequest(AlipayRequest):

    def __init__(self):
        super(AlipayCreateSessionRequest, self).__init__(AntomPathConstants.CREATE_SESSION_PATH)
        self.__product_code = None  # type:ProductCodeType
        self.__payment_request_id = None
        self.__order = None  # type:Order
        self.__payment_amount = None  # type:Amount
        self.__payment_method = None  # type:PaymentMethod
        self.__payment_session_expiry_time = None
        self.__payment_redirect_url = None
        self.__payment_notify_url = None
        self.__payment_factor = None
        self.__settlement_strategy = None  # type:SettlementStrategy
        self.__env = None  # type:Env
        self.__merchant_region = None
        self.__credit_pay_plan = None
        self.__enable_installment_collection = None
        self.__agreement_info = None  # type:AgreementInfo
        self.__product_scene = None

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
        self.__env = value

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def credit_pay_plan(self):
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value

    @property
    def enable_installment_collection(self):
        return self.__enable_installment_collection

    @enable_installment_collection.setter
    def enable_installment_collection(self, value):
        self.__enable_installment_collection = value

    @property
    def agreement_info(self):
        return self.__agreement_info

    @agreement_info.setter
    def agreement_info(self, value):
        self.__agreement_info = value

    @property
    def product_scene(self):
        return self.__product_scene

    @product_scene.setter
    def product_scene(self, value):
        self.__product_scene = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code:
            params['productCode'] = self.product_code
        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "order") and self.order:
            params['order'] = self.order
        if hasattr(self, "payment_amount") and self.payment_amount:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_method") and self.payment_method:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "payment_session_expiry_time") and self.payment_session_expiry_time:
            params['paymentSessionExpiryTime'] = self.payment_session_expiry_time
        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url:
            params['paymentRedirectUrl'] = self.payment_redirect_url
        if hasattr(self, "payment_notify_url") and self.payment_notify_url:
            params['paymentNotifyUrl'] = self.payment_notify_url
        if hasattr(self, "payment_factor") and self.payment_factor:
            params['paymentFactor'] = self.payment_factor
        if hasattr(self, "settlement_strategy") and self.settlement_strategy:
            params['settlementStrategy'] = self.settlement_strategy
        if hasattr(self, "env") and self.env:
            params['env'] = self.env
        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan:
            params['creditPayPlan'] = self.credit_pay_plan
        if hasattr(self, "enable_installment_collection") and self.enable_installment_collection:
            params['enableInstallmentCollection'] = self.enable_installment_collection
        if hasattr(self, "agreement_info") and self.agreement_info:
            params['agreementInfo'] = self.agreement_info
        if hasattr(self, "product_scene") and self.product_scene:
            params['productScene'] = self.product_scene

        return params
