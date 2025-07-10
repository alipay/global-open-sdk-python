#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.buyer import Buyer
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.gaming import Gaming
from com.alipay.ams.api.model.goods import Goods
from com.alipay.ams.api.model.lodging import Lodging
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.shipping import Shipping
from com.alipay.ams.api.model.transit import Transit


class Order(object):

    def __init__(self):
        self.__reference_order_id = None
        self.__order_description = None
        self.__order_amount = None
        self.__merchant = None  # type: Merchant
        self.__goods = None  # type: list[Goods]
        self.__shipping = None  # type: Shipping
        self.__buyer = None  # type: Buyer
        self.__env = None  # type: Env
        self.__extend_info = None
        self.__transit = None  # type: Transit
        self.lodging = None  # type: Lodging
        self.__gaming = None  # type: Gaming
        self.__order_created_time = None
        self.__need_declaration = None
        self.__order_discount_amount = None # type: Amount
        self.__sub_total_order_amount = None # type: Amount

    @property
    def reference_order_id(self):
        return self.__reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, value):
        self.__reference_order_id = value

    @property
    def order_description(self):
        return self.__order_description

    @order_description.setter
    def order_description(self, value):
        self.__order_description = value

    @property
    def order_amount(self):
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value

    @property
    def merchant(self):
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods = value

    @property
    def shipping(self):
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value

    @property
    def buyer(self):
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value

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
    def transit(self):
        return self.__transit

    @transit.setter
    def transit(self, value):
        self.__transit = value

    @property
    def lodging(self):
        return self.__lodging

    @lodging.setter
    def lodging(self, value):
        self.__lodging = value

    @property
    def gaming(self):
        return self.__gaming

    @gaming.setter
    def gaming(self, value):
        self.__gaming = value

    @property
    def order_created_time(self):
        return self.__order_created_time

    @order_created_time.setter
    def order_created_time(self, value):
        self.__order_created_time = value
    @property
    def need_declaration(self):
        return self.__need_declaration

    @need_declaration.setter
    def need_declaration(self, value):
        self.__need_declaration = value

    @property
    def order_discount_amount(self):
        return self.__order_discount_amount

    @order_discount_amount.setter
    def order_discount_amount(self, value):
        self.__order_discount_amount = value


    @property
    def sub_total_order_amount(self):
        return self.__sub_total_order_amount

    @sub_total_order_amount.setter
    def sub_total_order_amount(self, value):
        self.__sub_total_order_amount = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_order_id") and self.reference_order_id:
            params['referenceOrderId'] = self.reference_order_id

        if hasattr(self, "order_description") and self.order_description:
            params['orderDescription'] = self.order_description

        if hasattr(self, "order_amount") and self.order_amount:
            params['orderAmount'] = self.order_amount

        if hasattr(self, "merchant") and self.merchant:
            params['merchant'] = self.merchant

        if hasattr(self, "goods") and self.goods:
            params['goods'] = self.goods

        if hasattr(self, "shipping") and self.shipping:
            params['shipping'] = self.shipping

        if hasattr(self, "buyer") and self.buyer:
            params['buyer'] = self.buyer

        if hasattr(self, "env") and self.env:
            params['env'] = self.env

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "transit") and self.transit:
            params['transit'] = self.transit

        if hasattr(self, "lodging") and self.lodging:
            params['lodging'] = self.lodging

        if hasattr(self, "gaming") and self.gaming:
            params['gaming'] = self.gaming

        if hasattr(self, "order_created_time") and self.order_created_time:
            params['orderCreatedTime'] = self.order_created_time

        if hasattr(self, "need_declaration") and self.need_declaration:
            params['needDeclaration'] = self.need_declaration

        if hasattr(self, "order_discount_amount") and self.order_discount_amount:
            params['orderDiscountAmount'] = self.order_discount_amount

        if hasattr(self, "sub_total_order_amount") and self.sub_total_order_amount:
            params['subTotalOrderAmount'] = self.sub_total_order_amount

        return params
