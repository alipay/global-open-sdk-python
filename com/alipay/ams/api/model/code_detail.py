#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.code_value_type import CodeValueType
from com.alipay.ams.api.model.display_type import DisplayType


class CodeDetail(object):
    def __init__(self):
        self.__code_value_type = None  # type:CodeValueType
        self.__code_value = None
        self.__display_type = None  # type:DisplayType

    @property
    def code_value_type(self):
        return self.__code_value_type

    @code_value_type.setter
    def code_value_type(self, value):
        self.__code_value_type = value

    @property
    def code_value(self):
        return self.__code_value

    @code_value.setter
    def code_value(self, value):
        self.__code_value = value

    @property
    def display_type(self):
        return self.__display_type

    @display_type.setter
    def display_type(self, value):
        self.__display_type = value

    def parse_rsp_body(self, code_detail_body):
        if type(code_detail_body) == str:
            code_detail_body = json.loads(code_detail_body)

        if 'codeValueType' in code_detail_body:
            code_value_type = CodeValueType.value_of(code_detail_body['codeValueType'])
            self.__code_value_type = code_value_type

        if 'codeValue' in code_detail_body:
            self.__code_value = code_detail_body['codeValue']

        if 'displayType' in code_detail_body:
            display_type = DisplayType.value_of(code_detail_body['displayType'])
            self.__display_type = display_type
