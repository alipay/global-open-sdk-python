#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.disable_reason_type import DisableReasonType
from com.alipay.ams.api.model.amount_limit_info import AmountLimitInfo
from com.alipay.ams.api.model.installment import Installment
from com.alipay.ams.api.model.logo import Logo
from com.alipay.ams.api.model.paymentOptionDetail import PaymentOptionDetail
from com.alipay.ams.api.model.payment_method_category_type import PaymentMethodCategoryType
from com.alipay.ams.api.model.promotion_info import PromotionInfo


class PaymentOption(object):

    def __init__(self):
        self.__payment_method_type = None
        self.__payment_method_category = None  # type: PaymentMethodCategoryType
        self.__enabled = None
        self.__preferred = None
        self.__disable_reason = None  # type: DisableReasonType
        self.__amount_limit_info_map = None
        self.__supported_currencies = None
        self.__payment_option_detail = None  # type: PaymentOptionDetail
        self.__extend_info = None
        self.__logo = None  # type: Logo
        self.__promo_names = None
        self.__installment = None  # type: Installment
        self.__promotion_infos = None  # type: list[PromotionInfo]
        self.__payment_method_region = None  # type: list[str]

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @property
    def payment_method_category(self):
        return self.__payment_method_category

    @property
    def enabled(self):
        return self.__enabled

    @property
    def preferred(self):
        return self.__preferred

    @property
    def disable_reason(self):
        return self.__disable_reason

    @property
    def amount_limit_info_map(self):
        return self.__amount_limit_info_map

    @property
    def supported_currencies(self):
        return self.__supported_currencies

    @property
    def payment_option_detail(self):
        return self.__payment_option_detail

    @property
    def extend_info(self):
        return self.__extend_info

    @property
    def logo(self):
        return self.__logo

    @property
    def promo_names(self):
        return self.__promo_names

    @property
    def installment(self):
        return self.__installment

    @property
    def promotion_infos(self):
        return self.__promotion_infos

    def parse_rsp_body(self, payment_option_body):
        if type(payment_option_body) == str:
            payment_option_body = json.loads(payment_option_body)

        if 'paymentMethodType' in payment_option_body:
            self.__payment_method_type = payment_option_body['paymentMethodType']

        if 'paymentMethodCategory' in payment_option_body:
            payment_method_category = PaymentMethodCategoryType.value_of(payment_option_body['paymentMethodCategory'])
            self.__payment_method_category = payment_method_category

        if 'enabled' in payment_option_body:
            self.__enabled = payment_option_body['enabled']

        if 'preferred' in payment_option_body:
            self.__preferred = payment_option_body['preferred']

        if 'disableReason' in payment_option_body:
            self.__disable_reason = payment_option_body['disableReason']

        if 'amountLimitInfoMap' in payment_option_body:
            amount_limit_info_map = dict()
            for key, value in payment_option_body['amountLimitInfoMap']:
                amount_limit_info = AmountLimitInfo()
                amount_limit_info.parse_rsp_body(value)
                amount_limit_info_map[key] = amount_limit_info
            self.__amount_limit_info_map = amount_limit_info_map

        if 'supportedCurrencies' in payment_option_body:
            self.__supported_currencies = payment_option_body['supportedCurrencies']

        if 'paymentOptionDetail' in payment_option_body:
            self.__payment_option_detail = payment_option_body['paymentOptionDetail']

        if 'extendInfo' in payment_option_body:
            self.__extend_info = payment_option_body['extendInfo']

        if 'logo' in payment_option_body:
            self.__logo = payment_option_body['logo']

        if 'promoNames' in payment_option_body:
            self.__promo_names = payment_option_body['promoNames']

        if 'installment' in payment_option_body:
            self.__installment = payment_option_body['installment']

        if 'promotionInfos' in payment_option_body:
            promotion_infos = list()
            for promotion_info_body in payment_option_body['promotionInfos']:
                promotion_info = PromotionInfo()
                promotion_info.parse_rsp_body(promotion_info_body)
                promotion_infos.append(promotion_info)
            self.__promotion_infos = promotion_infos
