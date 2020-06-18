#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PaymentMethod(object):
    def __init__(self):
        self.__payment_method_id = None
        self.__payment_method_type = None
        self.__payment_method_meta_data = None
        self.__customer_id = None
        self.__extend_info = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value

    @property
    def payment_method_id(self):
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self , value):
        self.__payment_method_id = value

    @property
    def payment_method_meta_data(self):
        return self.__payment_method_meta_data

    @payment_method_meta_data.setter
    def payment_method_meta_data(self, value):
        self.__payment_method_meta_data = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type:
            params['paymentMethodType'] = self.payment_method_type

        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data:
            params['paymentMethodMetaData'] = self.payment_method_meta_data

        if hasattr(self, "customer_id") and self.customer_id:
            params['customerId'] = self.customer_id

        if hasattr(self, "payment_method_id") and self.payment_method_id:
            params['paymentMethodId'] = self.payment_method_id

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        return params
