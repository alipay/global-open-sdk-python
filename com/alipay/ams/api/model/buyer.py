#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Buyer(object):

    def __init__(self):
        self.__reference_buyer_id = None
        self.__buyer_name = None
        self.__buyer_phone_no = None
        self.__buyer_email = None

    @property
    def reference_buyer_id(self):
        return self.__reference_buyer_id

    @reference_buyer_id.setter
    def reference_buyer_id(self, value):
        self.__reference_buyer_id = value

    @property
    def buyer_name(self):
        return self.__buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self.__buyer_name = value

    @property
    def buyer_phone_no(self):
        return self.__buyer_phone_no

    @buyer_phone_no.setter
    def buyer_phone_no(self, value):
        self.__buyer_phone_no = value

    @property
    def buyer_email(self):
        return self.__buyer_email

    @buyer_email.setter
    def buyer_email(self, value):
        self.__buyer_email = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_buyer_id") and self.reference_buyer_id:
            params['referenceBuyerId'] = self.reference_buyer_id

        if hasattr(self, "buyer_name") and self.buyer_name:
            params['buyerName'] = self.buyer_name

        if hasattr(self, "buyer_phone_no") and self.buyer_phone_no:
            params['buyerPhoneNo'] = self.buyer_phone_no

        if hasattr(self, "buyer_email") and self.buyer_email:
            params['buyerEmail'] = self.buyer_email

        return params
