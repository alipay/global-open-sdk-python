#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.delivery_method_type import DeliveryMethodType


class Goods(object):
    def __init__(self):
        self.__reference_goods_id = None
        self.__goods_name = None
        self.__goods_category = None
        self.__goods_brand = None
        self.__goods_unit_amount = None  # type:Amount
        self.__goods_quantity = None
        self.__goods_sku_name = None
        self.__delivery_method_type = None  # type:DeliveryMethodType

    @property
    def reference_goods_id(self):
        return self.__reference_goods_id

    @reference_goods_id.setter
    def reference_goods_id(self, value):
        self.__reference_goods_id = value

    @property
    def goods_name(self):
        return self.__goods_name

    @goods_name.setter
    def goods_name(self, value):
        self.__goods_name = value

    @property
    def goods_category(self):
        return self.__goods_category

    @goods_category.setter
    def goods_category(self, value):
        self.__goods_category = value

    @property
    def goods_brand(self):
        return self.__goods_brand

    @goods_brand.setter
    def goods_brand(self, value):
        self.__goods_brand = value

    @property
    def goods_unit_amount(self):
        return self.__goods_unit_amount

    @goods_unit_amount.setter
    def goods_unit_amount(self, value):
        self.__goods_unit_amount = value

    @property
    def goods_quantity(self):
        return self.__goods_quantity

    @goods_quantity.setter
    def goods_quantity(self, value):
        self.__goods_quantity = value

    @property
    def goods_sku_name(self):
        return self.__goods_sku_name

    @goods_sku_name.setter
    def goods_sku_name(self, value):
        self.__goods_sku_name = value

    @property
    def delivery_method_type(self):
        return self.__delivery_method_type

    @delivery_method_type.setter
    def delivery_method_type(self, value):
        self.__delivery_method_type = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_goods_id") and self.reference_goods_id:
            params['referenceGoodsId'] = self.reference_goods_id

        if hasattr(self, "goods_name") and self.goods_name:
            params['goodsName'] = self.goods_name

        if hasattr(self, "goods_category") and self.goods_category:
            params['goodsCategory'] = self.goods_category

        if hasattr(self, "goods_brand") and self.goods_brand:
            params['goodsBrand'] = self.goods_brand

        if hasattr(self, "goods_unit_amount") and self.goods_unit_amount:
            params['goodsUnitAmount'] = self.goods_unit_amount

        if hasattr(self, "goods_quantity") and self.goods_quantity:
            params['goodsQuantity'] = self.goods_quantity

        if hasattr(self, "goods_sku_name") and self.goods_sku_name:
            params['goodsSkuName'] = self.goods_sku_name

        if hasattr(self, "delivery_method_type") and self.delivery_method_type:
            params['deliveryMethodType'] = self.delivery_method_type

        return params
