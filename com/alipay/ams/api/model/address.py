#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class Address(object):
    def __init__(self):
        self.__region = None
        self.__state = None
        self.__city = None
        self.__address1 = None
        self.__address2 = None
        self.__zip_code = None
        self.__label = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def address1(self):
        return self.__address1

    @address1.setter
    def address1(self, value):
        self.__address1 = value

    @property
    def address2(self):
        return self.__address2

    @address2.setter
    def address2(self, value):
        self.__address2 = value

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        self.__zip_code = value

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "region") and self.region:
            params['region'] = self.region

        if hasattr(self, "state") and self.state:
            params['state'] = self.state

        if hasattr(self, "city") and self.city:
            params['city'] = self.city

        if hasattr(self, "address1 ") and self.address1:
            params['address1'] = self.address1

        if hasattr(self, "address2") and self.address2:
            params['address2'] = self.address2

        if hasattr(self, "zip_code") and self.zip_code:
            params['zipCode'] = self.zip_code

        if hasattr(self, "label") and self.label:
            params['label'] = self.label

        return params

    def parse_rsp_body(self, address_body):
        if type(address_body) == str:
            address_body = json.loads(address_body)

        if 'region' in address_body:
            self.__region = address_body['region']

        if 'state' in address_body:
            self.__state = address_body['state']

        if 'city' in address_body:
            self.__city = address_body['city']

        if 'address1' in address_body:
            self.__address1 = address_body['address1']

        if 'address2' in address_body:
            self.__address2 = address_body['address2']

        if 'zipCode' in address_body:
            self.__zip_code = address_body['zipCode']

        if 'label' in address_body:
            self.__label = address_body['label']
