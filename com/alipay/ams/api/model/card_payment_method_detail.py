#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.card_brand import CardBrand
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address


class CardPaymentMethodDetail(object):

    def __init__(self):
        self.__card_token = None
        self.__card_no = None
        self.__brand = None
        self.__card_issuer = None
        self.__country_issue = None
        self.__inst_user_name = None
        self.__expiry_year = None
        self.__expiry_month = None
        self.__billing_address = None
        self.__mask = None
        self.__last4 = None
        self.__payment_method_detail_metadata = None

    @property
    def card_token(self):
        return self.__card_token

    @property
    def card_no(self):
        return self.__card_no

    @property
    def brand(self):
        return self.__brand

    @property
    def card_issuer(self):
        return self.__card_issuer

    @property
    def country_issue(self):
        return self.__country_issue

    @property
    def inst_user_name(self):
        return self.__inst_user_name

    @property
    def expiry_year(self):
        return self.__expiry_year

    @property
    def expiry_month(self):
        return self.__expiry_month

    @property
    def billing_address(self):
        return self.__billing_address

    @property
    def mask(self):
        return self.__mask

    @property
    def last4(self):
        return self.__last4

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata

    def parse_rsp_body(self, card_payment_method_detail_body):
        if type(card_payment_method_detail_body) == str:
            card_payment_method_detail_body = json.loads(card_payment_method_detail_body)

        if 'cardToken' in card_payment_method_detail_body:
            self.__card_token = card_payment_method_detail_body['cardToken']

        if 'cardNo' in card_payment_method_detail_body:
            self.__card_no = card_payment_method_detail_body['cardNo']

        if 'brand' in card_payment_method_detail_body:
            card_no = CardBrand.value_of(card_payment_method_detail_body['brand'])
            self.__card_no = card_no

        if 'cardIssuer' in card_payment_method_detail_body:
            self.__card_issuer = card_payment_method_detail_body['cardIssuer']

        if 'countryIssue' in card_payment_method_detail_body:
            self.__country_issue = card_payment_method_detail_body['countryIssue']

        if 'instUserName' in card_payment_method_detail_body:
            inst_user_name = UserName()
            inst_user_name.parse_rsp_body(card_payment_method_detail_body['instUserName'])
            self.__inst_user_name = inst_user_name

        if 'expiryYear' in card_payment_method_detail_body:
            self.__expiry_year = card_payment_method_detail_body['expiryYear']

        if 'expiryMonth' in card_payment_method_detail_body:
            self.__expiry_month = card_payment_method_detail_body['expiryMonth']

        if 'billingAddress' in card_payment_method_detail_body:
            billing_address = Address()
            billing_address.parse_rsp_body(card_payment_method_detail_body['billingAddress'])
            self.__billing_address = billing_address

        if 'mask' in card_payment_method_detail_body:
            self.__mask = card_payment_method_detail_body['mask']

        if 'last4' in card_payment_method_detail_body:
            self.__last4 = card_payment_method_detail_body['last4']

        if 'paymentMethodDetailMetadata' in card_payment_method_detail_body:
            self.__payment_method_detail_metadata = card_payment_method_detail_body['paymentMethodDetailMetadata']

