#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class ExternalPaymentMethodDetail(object):

    def __init__(self):
        self.__asset_token = None
        self.__account_display_name = None
        self.__disable_reason = None
        self.__payment_method_detail_metadata = None

    @property
    def asset_token(self):
        return self.__asset_token

    @asset_token.setter
    def asset_token(self, value):
        self.__asset_token = value

    @property
    def account_display_name(self):
        return self.__account_display_name


    @account_display_name.setter
    def account_display_name(self, value):
        self.__account_display_name = value

    @property
    def disable_reason(self):
        return self.__disable_reason


    @disable_reason.setter
    def disable_reason(self, value):
        self.__disable_reason = value

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value

    def parse_rsp_body(self, external_payment_method_detail_body):
        if type(external_payment_method_detail_body) == str:
            external_payment_method_detail_body = json.loads(external_payment_method_detail_body)

        if 'assetToken' in external_payment_method_detail_body:
            self.__asset_token = external_payment_method_detail_body['assetToken']

        if 'accountDisplayName' in external_payment_method_detail_body:
            self.__account_display_name = external_payment_method_detail_body['accountDisplayName']

        if 'disableReason' in external_payment_method_detail_body:
            self.__disable_reason = external_payment_method_detail_body['disableReason']

        if 'paymentMethodDetailMetadata' in external_payment_method_detail_body:
            self.__payment_method_detail_metadata = external_payment_method_detail_body['paymentMethodDetailMetadata']

    def to_ams_dict(self):
        params = dict()
        if self.asset_token:
            params['assetToken'] = self.asset_token
        if self.account_display_name:
            params['accountDisplayName'] = self.account_display_name
        if self.disable_reason:
            params['disableReason'] = self.disable_reason
        if self.payment_method_detail_metadata:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata

        return params