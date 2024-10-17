#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.buyer import Buyer
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayPayConsultRequest(AlipayRequest):

    def __init__(self):
        super(AlipayPayConsultRequest, self).__init__(AntomPathConstants.CONSULT_PAYMENT_PATH)
        self.__product_code = None  # type:ProductCodeType
        self.__payment_amount = None  # type:Amount
        self.__allowed_payment_methods = None
        self.__blocked_payment_methods = None
        self.__region = None
        self.__customer_id = None
        self.__reference_user_id = None
        self.__env = None  # type:Env
        self.__extend_info = None
        self.__user_region = None
        self.__payment_factor = None  # type:PaymentFactor
        self.__settlement_strategy = None  # type:SettlementStrategy
        self.__merchant = None  # type:Merchant
        self.__allowed_psp_regions = None
        self.__merchant_region = None
        self.__merchant_account_id = None
        self.__allowed_payment_method_regions = None
        self.__buyer = None  # type:Buyer

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    @property
    def payment_amount(self):
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def allowed_payment_methods(self):
        return self.__allowed_payment_methods

    @allowed_payment_methods.setter
    def allowed_payment_methods(self, value):
        self.__allowed_payment_methods = value

    @property
    def blocked_payment_methods(self):
        return self.__blocked_payment_methods

    @blocked_payment_methods.setter
    def blocked_payment_methods(self, value):
        self.__blocked_payment_methods = value

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def reference_user_id(self):
        return self.__reference_user_id

    @reference_user_id.setter
    def reference_user_id(self, value):
        self.__reference_user_id = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    @property
    def user_region(self):
        return self.__user_region

    @user_region.setter
    def user_region(self, value):
        self.__user_region = value

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
    def merchant(self):
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value

    @property
    def allowed_psp_regions(self):
        return self.__allowed_psp_regions

    @allowed_psp_regions.setter
    def allowed_psp_regions(self, value):
        self.__allowed_psp_regions = value

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def merchant_account_id(self):
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value

    @property
    def allowed_payment_method_regions(self):
        return self.__allowed_payment_method_regions

    @allowed_payment_method_regions.setter
    def allowed_payment_method_regions(self, value):
        self.__allowed_payment_method_regions = value

    @property
    def buyer(self):
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code:
            params['productCode'] = self.product_code

        if hasattr(self, "payment_amount") and self.payment_amount:
            params['paymentAmount'] = self.payment_amount

        if hasattr(self, "allowed_payment_methods") and self.allowed_payment_methods:
            params['allowedPaymentMethods'] = self.allowed_payment_methods

        if hasattr(self, "blocked_payment_methods") and self.blocked_payment_methods:
            params['blockedPaymentMethods'] = self.blocked_payment_methods

        if hasattr(self, "region") and self.region:
            params['region'] = self.region

        if hasattr(self, "customer_id") and self.customer_id:
            params['customerId'] = self.customer_id

        if hasattr(self, "reference_user_id") and self.reference_user_id:
            params['referenceUserId'] = self.reference_user_id

        if hasattr(self, "env") and self.env:
            params['env'] = self.env

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "user_region") and self.user_region:
            params['userRegion'] = self.user_region

        if hasattr(self, "payment_factor") and self.payment_factor:
            params['paymentFactor'] = self.payment_factor

        if hasattr(self, "settlement_strategy") and self.settlement_strategy:
            params['settlementStrategy'] = self.settlement_strategy

        if hasattr(self, "merchant") and self.merchant:
            params['merchant'] = self.merchant

        if hasattr(self, "allowed_psp_regions") and self.allowed_psp_regions:
            params['allowedPspRegions'] = self.allowed_psp_regions

        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region

        if hasattr(self, "merchant_account_id") and self.merchant_account_id:
            params['merchantAccountId'] = self.merchant_account_id

        if hasattr(self, "allowed_payment_method_regions") and self.allowed_payment_method_regions:
            params['allowedPaymentMethodRegions'] = self.allowed_payment_method_regions

        if hasattr(self, "buyer") and self.buyer:
            params['buyer'] = self.buyer

        return params
