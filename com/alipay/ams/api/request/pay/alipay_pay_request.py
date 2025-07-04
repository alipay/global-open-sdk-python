#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.credit_pay_plan import CreditPayPlan
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.subscription_info import SubscriptionInfo
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayPayRequest(AlipayRequest):

    def __init__(self):
        super(AlipayPayRequest, self).__init__(AntomPathConstants.PAYMENT_PATH)
        self.__product_code = None  # type: ProductCodeType
        self.__payment_request_id = None
        self.__order = None  # type: Order
        self.__payment_amount = None  # type: Amount
        self.__pay_to_method = None  # type: PaymentMethod
        self.__payment_method = None  # type: PaymentMethod
        self.__payment_expiry_time = None
        self.__payment_redirect_url = None
        self.__payment_notify_url = None
        self.__is_authorization = None
        self.__payment_verification_data = None
        self.__payment_factor = None  # type: PaymentFactor
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__extend_info = None
        self.__env = None  # type: Env
        self.__merchant_region = None
        self.__app_id = None
        self.__merchant_account_id = None
        self.__user_region = None
        self.__credit_pay_plan = None  # type: CreditPayPlan
        self.__subscription_info = None # type: SubscriptionInfo

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def app_id(self):
        return self.__app_id

    @app_id.setter
    def app_id(self, value):
        self.__app_id = value

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
    def pay_to_method(self):
        return self.__pay_to_method

    @pay_to_method.setter
    def pay_to_method(self, value):
        self.__pay_to_method = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def payment_expiry_time(self):
        return self.__payment_expiry_time

    @payment_expiry_time.setter
    def payment_expiry_time(self, value):
        self.__payment_expiry_time = value

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
    def is_authorization(self):
        return self.__is_authorization

    @is_authorization.setter
    def is_authorization(self, value):
        self.__is_authorization = value

    @property
    def payment_verification_data(self):
        return self.__payment_verification_data

    @payment_verification_data.setter
    def payment_verification_data(self, value):
        self.__payment_verification_data = value

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
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    @property
    def merchant_account_id(self):
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value

    @property
    def user_region(self):
        return self.__user_region

    @user_region.setter
    def user_region(self, value):
        self.__user_region = value

    @property
    def credit_pay_plan(self):
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value

    @property
    def subscription_info(self):
        return self.__subscription_info

    @subscription_info.setter
    def subscription_info(self, value):
        self.__subscription_info = value

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

        if hasattr(self, "pay_to_method") and self.pay_to_method:
            params['payToMethod'] = self.pay_to_method

        if hasattr(self, "payment_method") and self.payment_method:
            params['paymentMethod'] = self.payment_method

        if hasattr(self, "payment_expiry_time") and self.payment_expiry_time:
            params['paymentExpiryTime'] = self.payment_expiry_time

        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url:
            params['paymentRedirectUrl'] = self.payment_redirect_url

        if hasattr(self, "payment_notify_url") and self.payment_notify_url:
            params['paymentNotifyUrl'] = self.payment_notify_url

        if hasattr(self, "is_authorization") and self.is_authorization:
            params['isAuthorization'] = self.is_authorization

        if hasattr(self, "payment_verification_data") and self.payment_verification_data:
            params['paymentVerificationData'] = self.payment_verification_data

        if hasattr(self, "payment_factor") and self.payment_factor:
            params['paymentFactor'] = self.payment_factor

        if hasattr(self, "settlement_strategy") and self.settlement_strategy:
            params['settlementStrategy'] = self.settlement_strategy

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "env") and self.env:
            params['env'] = self.env

        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region

        if hasattr(self, "app_id") and self.app_id:
            params['appId'] = self.app_id

        if hasattr(self, "merchant_account_id") and self.merchant_account_id:
            params['merchantAccountId'] = self.merchant_account_id

        if hasattr(self, "user_region") and self.user_region:
            params['userRegion'] = self.user_region

        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan:
            params['creditPayPlan'] = self.credit_pay_plan

        if hasattr(self, "subscription_info") and self.subscription_info:
            params['subscriptionInfo'] = self.subscription_info

        return params
