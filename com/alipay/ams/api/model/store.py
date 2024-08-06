#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.address import Address


class Store(object):
    def __init__(self):
        self.__reference_store_id = None
        self.__store_name = None
        self.__store_mcc = None
        self.__store_display_name = None
        self.__store_terminal_id = None
        self.__store_operator_id = None
        self.__store_address = None  # type: Address
        self.__store_phone_no = None

    @property
    def reference_store_id(self):
        return self.__reference_store_id

    @reference_store_id.setter
    def reference_store_id(self, value):
        self.__reference_store_id = value

    @property
    def store_name(self):
        return self.__store_name

    @store_name.setter
    def store_name(self, value):
        self.__store_name = value

    @property
    def store_mcc(self):
        return self.__store_mcc

    @store_mcc.setter
    def store_mcc(self, value):
        self.__store_mcc = value

    @property
    def store_display_name(self):
        return self.__store_display_name

    @store_display_name.setter
    def store_display_name(self, value):
        self.__store_display_name = value

    @property
    def store_terminal_id(self):
        return self.__store_terminal_id

    @store_terminal_id.setter
    def store_terminal_id(self, value):
        self.__store_terminal_id = value

    @property
    def store_operator_id(self):
        return self.__store_operator_id

    @store_operator_id.setter
    def store_operator_id(self, value):
        self.__store_operator_id = value

    @property
    def store_address(self):
        return self.__store_address

    @store_address.setter
    def store_address(self, value):
        self.__store_address = value

    @property
    def store_phone_no(self):
        return self.__store_phone_no

    @store_phone_no.setter
    def store_phone_no(self, value):
        self.__store_phone_no = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_store_id") and self.reference_store_id:
            params['referenceStoreId'] = self.reference_store_id

        if hasattr(self, "store_name") and self.store_name:
            params['storeName'] = self.store_name

        if hasattr(self, "store_mcc") and self.store_mcc:
            params['storeMCC'] = self.store_mcc

        if hasattr(self, "store_display_name") and self.store_display_name:
            params['storeDisplayName'] = self.store_display_name

        if hasattr(self, "store_terminal_id") and self.store_terminal_id:
            params['storeTerminalId'] = self.store_terminal_id

        if hasattr(self, "store_operator_id") and self.store_operator_id:
            params['storeOperatorId'] = self.store_operator_id

        if hasattr(self, "store_address") and self.store_address:
            params['storeAddress'] = self.store_address

        if hasattr(self, "store_phone_no") and self.store_phone_no:
            params['storePhoneNo'] = self.store_phone_no

        return params
