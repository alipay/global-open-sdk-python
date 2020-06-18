#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.result_status_type import ResultStatusType


class Result(object):
    def __init__(self):
        self.__result_code = None
        self.__result_message = None
        self.__result_status = None

    @property
    def result_code(self):
        return self.__result_code

    @property
    def result_message(self):
        return self.__result_message

    @property
    def result_status(self):
        return self.__result_status

    def parse_rsp_body(self, result_body):
        if type(result_body) == str:
            result_body = json.loads(result_body)

        if 'resultCode' in result_body:
            self.__result_code = result_body['resultCode']

        if 'resultMessage' in result_body:
            self.__result_message = result_body['resultMessage']

        if 'resultStatus' in result_body:
            result_status = ResultStatusType.value_of(result_body['resultStatus'])
            self.__result_status = result_status
