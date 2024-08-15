#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class PspCustomerInfo(object):
    def __init__(self):
        self.__psp_name = None
        self.__psp_customer_id = None
        self.__display_customer_id = None
        self.__display_customer_name = None
        self.__customer_2088_id = None
        self.__extend_info = None

    @property
    def psp_name(self):
        return self.__psp_name

    @psp_name.setter
    def psp_name(self, value):
        self.__psp_name = value

    @property
    def psp_customer_id(self):
        return self.__psp_customer_id

    @psp_customer_id.setter
    def psp_customer_id(self, value):
        self.__psp_customer_id = value

    @property
    def display_customer_id(self):
        return self.__display_customer_id

    @display_customer_id.setter
    def display_customer_id(self, value):
        self.__display_customer_id = value

    @property
    def display_customer_name(self):
        return self.__display_customer_name

    @display_customer_name.setter
    def display_customer_name(self, value):
        self.__display_customer_name = value

    @property
    def customer_2088_id(self):
        return self.__customer_2088_id

    @customer_2088_id.setter
    def customer_2088_id(self, value):
        self.__customer_2088_id = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def parse_rsp_body(self, psp_customer_info_body):
        if type(psp_customer_info_body) == str:
            psp_customer_info_body = json.loads(psp_customer_info_body)
        if 'pspName' in psp_customer_info_body:
            self.__psp_name = psp_customer_info_body['pspName']
        if 'pspCustomerId' in psp_customer_info_body:
            self.__psp_customer_id = psp_customer_info_body['pspCustomerId']
        if 'displayCustomerId' in psp_customer_info_body:
            self.__display_customer_id = psp_customer_info_body['displayCustomerId']
        if 'displayCustomerName' in psp_customer_info_body:
            self.__display_customer_name = psp_customer_info_body['displayCustomerName']
        if 'customer2088Id' in psp_customer_info_body:
            self.__customer_2088_id = psp_customer_info_body['customer2088Id']
        if 'extendInfo' in psp_customer_info_body:
            self.__extend_info = psp_customer_info_body['extendInfo']
