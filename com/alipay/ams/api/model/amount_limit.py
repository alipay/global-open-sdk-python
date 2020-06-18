#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class AmountLimit(object):
    def __init__(self):
        self.__max_amount = None
        self.__min_amount = None
        self.__remain_amount = None

    @property
    def max_amount(self):
        return self.__max_amount

    @property
    def min_amount(self):
        return self.__min_amount

    @property
    def remain_amount(self):
        return self.__remain_amount

    def parse_rsp_body(self, amount_limit_body):
        if type(amount_limit_body) == str:
            amount_limit_body = json.loads(amount_limit_body)

        if 'maxAmount' in amount_limit_body:
            max_amount = Amount()
            max_amount.parse_rsp_body(amount_limit_body['maxAmount'])
            self.__max_amount = max_amount

        if 'minAmount' in amount_limit_body:
            min_amount = Amount()
            min_amount.parse_rsp_body(amount_limit_body['minAmount'])
            self.__min_amount = min_amount

        if 'remainAmount' in amount_limit_body:
            remain_amount = Amount()
            remain_amount.parse_rsp_body(amount_limit_body['remainAmount'])
            self.__remain_amount = remain_amount
