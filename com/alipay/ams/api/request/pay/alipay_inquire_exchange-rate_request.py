#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import List

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.currency_pair import CurrencyPair
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayInquireExchangeRateRequest(AlipayRequest):

    def __init__(self):
        super(AlipayInquireExchangeRateRequest, self).__init__(
            AntomPathConstants.PAYMENT_INQUIRE_EXCHANGE_RATE_PATH
        )
        self.__merchant_account_id = None
        self.__payment_currency = None
        self.__currency_pairs = None  # type: List[CurrencyPair]
        self.__sell_currency = None
        self.__buy_currency = None
        self.__product_code = None  # type: ProductCodeType

    @property
    def merchant_account_id(self):
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value

    @property
    def payment_currency(self):
        return self.__payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self.__payment_currency = value

    @property
    def currency_pairs(self):
        return self.__currency_pairs

    @currency_pairs.setter
    def currency_pairs(self, value):
        self.__currency_pairs = value

    @property
    def sell_currency(self):
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value

    @property
    def buy_currency(self):
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id:
            params["merchantAccountId"] = self.merchant_account_id

        if hasattr(self, "payment_currency") and self.payment_currency:
            params["paymentCurrency"] = self.payment_currency

        if hasattr(self, "currency_pairs") and self.currency_pairs:
            params["currencyPairs"] = [
                currency_pair.to_ams_dict() for currency_pair in self.currency_pairs
            ]

        if hasattr(self, "sell_currency") and self.sell_currency:
            params["sellCurrency"] = self.sell_currency

        if hasattr(self, "buy_currency") and self.buy_currency:
            params["buyCurrency"] = self.buy_currency

        if hasattr(self, "extend_info") and self.extend_info:
            params["extendInfo"] = self.extend_info

        if hasattr(self, "product_code") and self.product_code:
            params["productCode"] = self.product_code

        return params
