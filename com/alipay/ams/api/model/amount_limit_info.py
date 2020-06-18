#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount_limit import AmountLimit


class AmountLimitInfo(object):
    def __init__(self):
        self.__single_limit = None
        self.__day_limit = None
        self.__month_limit = None

    @property
    def single_limit(self):
        return self.__single_limit

    @property
    def day_limit(self):
        return self.__day_limit

    @property
    def month_limit(self):
        return self.__month_limit

    def parse_rsp_body(self, amount_limit_info_body):
        if type(amount_limit_info_body) == str:
            amount_limit_info_body = json.loads(amount_limit_info_body)

        if 'singleLimit' in amount_limit_info_body:
            single_limit = AmountLimit()
            single_limit.parse_rsp_body(amount_limit_info_body['singleLimit'])
            self.__single_limit = single_limit

        if 'dayLimit' in amount_limit_info_body:
            day_amount = AmountLimit()
            day_amount.parse_rsp_body(amount_limit_info_body['dayLimit'])
            self.__day_limit = day_amount

        if 'monthLimit' in amount_limit_info_body:
            month_amount = AmountLimit()
            month_amount.parse_rsp_body(amount_limit_info_body['monthLimit'])
            self.__month_limit = month_amount
