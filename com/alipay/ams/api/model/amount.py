#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class Amount(object):
    def __init__(self, currency=None, value=None):
        self.__currency = currency
        self.__value = value

    @property
    def currency(self):
        return self.__currency

    @property
    def value(self):
        return self.__value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency") and self.currency:
            params['currency'] = self.currency

        if hasattr(self, "value") and self.value:
            params['value'] = self.value

        return params

    def parse_rsp_body(self, amount_body):
        if type(amount_body) == str:
            amount_body = json.loads(amount_body)

        if 'currency' in amount_body:
            self.__currency = amount_body['currency']

        if 'value' in amount_body:
            self.__value = amount_body['value']

