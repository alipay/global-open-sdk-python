#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.delivery_estimate import DeliveryEstimate
from com.alipay.ams.api.model.user_name import UserName


class Shipping(object):

    def __init__(self):
        self.__shipping_name = None  # type:UserName
        self.__shipping_address = None  # type:Address
        self.__shipping_carrier = None
        self.__shipping_phone_no = None
        self.__shipping_number = None
        self.__ship_to_email = None
        self.__notes = None
        self.__shipping_fee_id = None
        self.__shipping_fee = None # type: Amount
        self.__shipping_description = None
        self.__delivery_estimate = None # type: DeliveryEstimate


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


    @property
    def shipping_number(self):
        return self.__shipping_number

    @shipping_number.setter
    def shipping_number(self, value):
        self.__shipping_number = value


    @property
    def ship_to_email(self):
        return self.__ship_to_email

    @ship_to_email.setter
    def ship_to_email(self, value):
        self.__ship_to_email = value


    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value



    @property
    def shipping_fee_id(self):
        return self.__shipping_fee_id

    @shipping_fee_id.setter
    def shipping_fee_id(self, value):
        self.__shipping_fee_id = value

    @property
    def shipping_fee(self):
        return self.__shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        self.__shipping_fee = value

    @property
    def shipping_description(self):
        return self.__shipping_description

    @shipping_description.setter
    def shipping_description(self, value):
        self.__shipping_description = value


    @property
    def delivery_estimate(self):
        return self.__delivery_estimate

    @delivery_estimate.setter
    def delivery_estimate(self, value):
        self.__delivery_estimate = value



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

        if hasattr(self, "shipping_number") and self.shipping_number:
            params['shippingNumber'] = self.shipping_number
        if hasattr(self, "ship_to_email") and self.ship_to_email:
            params['shipToEmail'] = self.ship_to_email
        if hasattr(self, "notes") and self.notes:
            params['notes'] = self.notes
        if hasattr(self, "shipping_fee_id") and self.shipping_fee_id:
            params['shippingFeeId'] = self.shipping_fee_id
        if hasattr(self, "shipping_fee") and self.shipping_fee:
            params['shippingFee'] = self.shipping_fee
        if hasattr(self, "shipping_description") and self.shipping_description:
            params['shippingDescription'] = self.shipping_description
        if hasattr(self, "delivery_estimate") and self.delivery_estimate:
            params['deliveryEstimate'] = self.delivery_estimate

        return params
