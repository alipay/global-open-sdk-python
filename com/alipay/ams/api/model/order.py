#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Order(object):

    def __init__(self):
        self.__reference_order_id = None
        self.__order_description = None
        self.__order_amount = None
        self.__merchant = None
        self.__goods = None
        self.__shipping = None
        self.__buyer = None
        self.__env = None
        self.__extend_info = None

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

        return params

