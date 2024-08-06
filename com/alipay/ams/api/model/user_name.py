#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class UserName(object):

    def __init__(self):
        self.__first_name = None
        self.__middle_name = None
        self.__last_name = None
        self.__full_name = None

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "first_name") and self.first_name:
            params['firstName'] = self.first_name

        if hasattr(self, "middle_name") and self.middle_name:
            params['middleName'] = self.middle_name

        if hasattr(self, "last_name") and self.last_name:
            params['lastName'] = self.last_name

        if hasattr(self, "full_name") and self.full_name:
            params['fullName'] = self.full_name

        return params

    def parse_rsp_body(self, user_name_body):
        if type(user_name_body) == str:
            user_name_body = json.loads(user_name_body)

        if 'firstName' in user_name_body:
            self.__first_name = user_name_body['firstName']

        if 'middleName' in user_name_body:
            self.__middle_name = user_name_body['middleName']

        if 'lastName' in user_name_body:
            self.__last_name = user_name_body['lastName']

        if 'fullName' in user_name_body:
            self.__full_name = user_name_body['fullName']
