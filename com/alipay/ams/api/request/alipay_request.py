#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.http_method import HttpMethod


class AlipayRequest(object):

    def __init__(self):
        self.__path = None
        self.__key_version = None
        self.__http_method = HttpMethod.POST

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def key_version(self):
        return self.__key_version

    @key_version.setter
    def key_version(self, value):
        self.__key_version = value

    @property
    def http_method(self):
        return self.__http_method

    @http_method.setter
    def http_method(self, value):
        self.__http_method = value






