#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.address import Address


class Merchant(object):
    def __init__(self):
        self.__reference_merchant_id = None
        self.__merchant_mcc = None
        self.__merchant_name = None
        self.__merchant_display_name = None
        self.__merchant_address = None  # type: Address
        self.__merchant_register_date = None
        self.__merchant_type = None  # type: MerchantType
        self.__store = None

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def merchant_mcc(self):
        return self.__merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self.__merchant_mcc = value

    @property
    def merchant_name(self):
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value

    @property
    def merchant_display_name(self):
        return self.__merchant_display_name

    @merchant_display_name.setter
    def merchant_display_name(self, value):
        self.__merchant_display_name = value

    @property
    def merchant_address(self):
        return self.__merchant_address

    @merchant_address.setter
    def merchant_address(self, value):
        self.__merchant_address = value

    @property
    def merchant_register_date(self):
        return self.__merchant_register_date

    @merchant_register_date.setter
    def merchant_register_date(self, value):
        self.__merchant_register_date = value

    @property
    def merchant_type(self):
        return self.__merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self.__merchant_type = value

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, value):
        self.__store = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id:
            params['referenceMerchantId'] = self.reference_merchant_id

        if hasattr(self, "merchant_mcc") and self.merchant_mcc:
            params['merchantMCC'] = self.merchant_mcc

        if hasattr(self, "merchant_name") and self.merchant_name:
            params['merchantName'] = self.merchant_name

        if hasattr(self, "merchant_display_name") and self.merchant_display_name:
            params['merchantDisplayName'] = self.merchant_display_name

        if hasattr(self, "merchant_address") and self.merchant_address:
            params['merchantAddress'] = self.merchant_address

        if hasattr(self, "merchant_register_date") and self.merchant_register_date:
            params['merchantRegisterDate'] = self.merchant_register_date

        if hasattr(self, "merchant_type") and self.merchant_type:
            params['merchantType'] = self.merchant_type

        if hasattr(self, "store") and self.store:
            params['store'] = self.store

        return params
