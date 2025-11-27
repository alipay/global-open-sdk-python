#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from com.alipay.ams.api.model.result import Result


class AlipayResponse(object):
    def __init__(self):
        self.__result = None

    @property
    def result(self):
        return self.__result

    def parse_rsp_body(self, rsp_body):
        response = json.loads(rsp_body)
        if "result" in response:
            result = Result()
            result.parse_rsp_body(response["result"])
            self.__result = result
        return response
