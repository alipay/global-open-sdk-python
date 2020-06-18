#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Shipping(object):

    def __init__(self):
        self.__shipping_name = None
        self.__shipping_address = None
        self.__shipping_carrier = None
        self.__shipping_phone_no = None

    @property
    def shipping_name(self):
        return self.__shipping_name

    @shipping_name.setter
    def shipping_name(self, value):
        self.__shipping_name = value

    @property
    def shipping_address(self):
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value

    @property
    def shipping_carrier(self):
        return self.__shipping_carrier

    @shipping_carrier.setter
    def shipping_carrier(self, value):
        self.__shipping_carrier = value

    @property
    def shipping_phone_no(self):
        return self.__shipping_phone_no

    @shipping_phone_no.setter
    def shipping_phone_no(self, value):
        self.__shipping_phone_no = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "shipping_name") and self.shipping_name:
            params['shippingName'] = self.shipping_name

        if hasattr(self, "shipping_address") and self.shipping_address:
            params['shippingAddress'] = self.shipping_address

        if hasattr(self, "shipping_carrier") and self.shipping_carrier:
            params['shippingCarrier'] = self.shipping_carrier

        if hasattr(self, "shipping_phone_no") and self.shipping_phone_no:
            params['shippingPhoneNo'] = self.shipping_phone_no

        return params
