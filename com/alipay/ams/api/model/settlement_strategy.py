#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SettlementStrategy(object):
    def __init__(self):
        self.__settlement_currency = None

    @property
    def settlement_currency(self):
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settlement_currency") and self.settlement_currency:
            params['settlementCurrency'] = self.settlement_currency

        return params
