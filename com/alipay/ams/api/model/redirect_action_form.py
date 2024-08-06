#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.method_type import MethodType


class RedirectActionForm(object):

    def __init__(self):
        self.__method = None  # type:MethodType
        self.__parameters = None
        self.__redirect_url = None
        self.__action_form_type = None

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        self.__parameters = value

    @property
    def redirect_url(self):
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value

    @property
    def action_form_type(self):
        return self.__action_form_type

    @action_form_type.setter
    def action_form_type(self, value):
        self.__action_form_type = value

    def parse_rsp_body(self, redirect_action_form_body):
        if type(redirect_action_form_body) == str:
            redirect_action_form_body = json.loads(redirect_action_form_body)

        if 'method' in redirect_action_form_body:
            self.__method = redirect_action_form_body['method']

        if 'parameters' in redirect_action_form_body:
            self.__parameters = redirect_action_form_body['parameters']

        if 'redirectUrl' in redirect_action_form_body:
            self.__redirect_url = redirect_action_form_body['redirectUrl']

        if 'actionFormType' in redirect_action_form_body:
            self.__action_form_type = redirect_action_form_body['actionFormType']
