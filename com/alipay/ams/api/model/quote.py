#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class Quote(object):
    def __init__(self):
        self.__quote_id = None
        self.__quote_currency_pair = None
        self.__quote_price = None
        self.__quote_start_time = None
        self.__quote_expiry_time = None
        self.__guaranteed = None
        self.__exchange_amount = None #type: Amount

    @property
    def quote_id(self):
        return self.__quote_id

    @quote_id.setter
    def quote_id(self, value):
        self.__quote_id = value

    @property
    def quote_currency_pair(self):
        return self.__quote_currency_pair

    @quote_currency_pair.setter
    def quote_currency_pair(self, value):
        self.__quote_currency_pair = value

    @property
    def quote_price(self):
        return self.__quote_price

    @quote_price.setter
    def quote_price(self, value):
        self.__quote_price = value

    @property
    def quote_start_time(self):
        return self.__quote_start_time

    @quote_start_time.setter
    def quote_start_time(self, value):
        self.__quote_start_time = value

    @property
    def quote_expiry_time(self):
        return self.__quote_start_time

    @quote_expiry_time.setter
    def quote_start_time(self, value):
        self.__quote_expiry_time = value

    @property
    def guaranteed(self):
        return self.__guaranteed

    @guaranteed.setter
    def guaranteed(self, value):
        self.__guaranteed = value

    @property
    def exchange_amount(self):
        return self.__exchange_amount

    @exchange_amount.setter
    def exchange_amount(self, value):
        self.__exchange_amount = value

    def parse_rsp_body(self, quote_body):
        if type(quote_body) == str:
            quote_body = json.loads(quote_body)

        if 'quoteId' in quote_body:
            self.__quote_id = quote_body['quoteId']

        if 'quoteCurrencyPair' in quote_body:
            self.__quote_currency_pair = quote_body['quoteCurrencyPair']

        if 'quotePrice' in quote_body:
            self.__quote_price = quote_body['quotePrice']

        if 'quoteStartTime' in quote_body:
            self.__quote_start_time = quote_body['quoteStartTime']

        if 'quoteExpiryTime' in quote_body:
            self.__quote_expiry_time = quote_body['quoteExpiryTime']

        if 'guaranteed' in quote_body:
            self.__guaranteed = quote_body['guaranteed']


        if 'exchangeAmount' in quote_body:
            self.__exchange_amount = Amount()
            self.__exchange_amount.parse_rsp_body(quote_body['exchangeAmount'])
