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

    @property
    def account_display_name(self):
        return self.__account_display_name

    @property
    def disable_reason(self):
        return self.__disable_reason

    @property
    def ayment_method_detail_metadata(self):
        return self.__ayment_method_detail_metadata

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


