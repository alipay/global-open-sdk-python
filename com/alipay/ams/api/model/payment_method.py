#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from com.alipay.ams.api.model.funding_type import FundingType


class PaymentMethod(object):
    def __init__(self):
        self.__payment_method_id = None
        self.__payment_method_type = None
        self.__payment_method_meta_data = None #type: map
        self.__customer_id = None
        self.__extend_info = None
        self.__require_issuer_authentication = None #type: bool
        self.funding = None #type: FundingType

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value

    @property
    def payment_method_id(self):
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value

    @property
    def payment_method_meta_data(self):
        return self.__payment_method_meta_data

    @payment_method_meta_data.setter
    def payment_method_meta_data(self, value):
        self.__payment_method_meta_data = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    @property
    def require_issuer_authentication(self):
        return self.__require_issuer_authentication
    @require_issuer_authentication.setter
    def require_issuer_authentication(self, value):
        self.__require_issuer_authentication = value

    @property
    def funding(self):
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type:
            params['paymentMethodType'] = self.payment_method_type

        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data:
            params['paymentMethodMetaData'] = self.payment_method_meta_data

        if hasattr(self, "customer_id") and self.customer_id:
            params['customerId'] = self.customer_id

        if hasattr(self, "payment_method_id") and self.payment_method_id:
            params['paymentMethodId'] = self.payment_method_id

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "require_issuer_authentication") and self.require_issuer_authentication:
            params['requireIssuerAuthentication'] = self.require_issuer_authentication

        if hasattr(self, "funding") and self.funding:
            params['funding'] = self.funding

        return params

    def parse_rsp_body(self, response_body):
        if type(response_body) == str:
            response_body = json.loads(response_body)

        if 'paymentMethodType' in response_body:
            self.transfer_from_method = response_body['paymentMethodType']
        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data:
            self.payment_method_meta_data = response_body['paymentMethodMetaData']
        if 'customerId' in response_body:
            self.customer_id = response_body['customerId']
        if 'paymentMethodId' in response_body:
            self.payment_method_id = response_body['paymentMethodId']
        if 'extendInfo' in response_body:
            self.extend_info = response_body['extendInfo']
        if 'requireIssuerAuthentication' in response_body:
            self.require_issuer_authentication = response_body['requireIssuerAuthentication']
        if 'funding' in response_body:
            self.funding = response_body['funding']