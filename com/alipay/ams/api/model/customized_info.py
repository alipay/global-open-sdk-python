


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class CustomizedInfo(object):
    def __init__(self):
        self.__customized_field1 = None
        self.__customized_field2 = None
        self.__customized_field3 = None
        self.__customized_field4 = None
        self.__customized_field5 = None


    @property
    def customized_field1(self):
        return self.__customized_field1

    @customized_field1.setter
    def customized_field1(self, value):
        self.__customized_field1 = value

    @property
    def customized_field2(self):
        return self.__customized_field2

    @customized_field2.setter
    def customized_field2(self, value):
        self.__customized_field2 = value


    @property
    def customized_field3(self):
        return self.__customized_field3

    @customized_field3.setter
    def customized_field3(self, value):
        self.__customized_field3 = value


    @property
    def customized_field4(self):
        return self.__customized_field4

    @customized_field4.setter
    def customized_field4(self, value):
        self.__customized_field4 = value

    @property
    def customized_field5(self):
        return self.__customized_field5

    @customized_field5.setter
    def customized_field5(self, value):
        self.__customized_field5 = value





    def parse_rsp_body(self, CustomizedInfo_body):
        if type(CustomizedInfo_body) == str:
            CustomizedInfo_body = json.loads(CustomizedInfo_body)

        if 'customized_field1' in CustomizedInfo_body:
            self.__customized_field1= CustomizedInfo_body['customized_field1']

        if 'customized_field2' in CustomizedInfo_body:
            self.__customized_field2= CustomizedInfo_body['customized_field2']

        if 'customized_field3' in CustomizedInfo_body:
            self.__customized_field3= CustomizedInfo_body['customized_field3']

        if 'customized_field4' in CustomizedInfo_body:
            self.__customized_field4= CustomizedInfo_body['customized_field4']

        if 'customized_field5' in CustomizedInfo_body:
            self.__customized_field5= CustomizedInfo_body['customized_field5']
