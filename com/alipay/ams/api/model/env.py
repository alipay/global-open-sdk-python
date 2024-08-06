#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.browser_info import BrowserInfo
from com.alipay.ams.api.model.os_type import OsType
from com.alipay.ams.api.model.terminal_type import TerminalType


class Env(object):
    def __init__(self):
        self.__terminal_type = None  # type: TerminalType
        self.__os_type = None  # type: OsType
        self.__user_agent = None
        self.__device_token_id = None
        self.__client_ip = None
        self.__cookie_id = None
        self.__store_terminal_id = None
        self.__store_terminal_request_time = None
        self.__extend_info = None
        self.__browser_info = None  # type: BrowserInfo
        self.__color_depth = None
        self.__screen_height = None
        self.__screen_width = None
        self.__time_zone_offset = None
        self.__device_brand = None
        self.__device_model = None
        self.__device_language = None
        self.__device_id = None

    @property
    def terminal_type(self):
        return self.__terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self.__terminal_type = value

    @property
    def os_type(self):
        return self.__os_type

    @os_type.setter
    def os_type(self, value):
        self.__os_type = value

    @property
    def user_agent(self):
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value

    @property
    def device_token_id(self):
        return self.__device_token_id

    @device_token_id.setter
    def device_token_id(self, value):
        self.__device_token_id = value

    @property
    def client_ip(self):
        return self.__client_ip

    @client_ip.setter
    def client_ip(self, value):
        self.__client_ip = value

    @property
    def cookie_id(self):
        return self.__cookie_id

    @cookie_id.setter
    def cookie_id(self, value):
        self.__cookie_id = value

    @property
    def store_terminal_id(self):
        return self.__store_terminal_id

    @store_terminal_id.setter
    def store_terminal_id(self, value):
        self.__store_terminal_id = value

    @property
    def store_terminal_request_time(self):
        return self.__store_terminal_request_time

    @store_terminal_request_time.setter
    def store_terminal_request_time(self, value):
        self.__store_terminal_request_time = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    @property
    def browser_info(self):
        return self.__browser_info

    @browser_info.setter
    def browser_info(self, value):
        self.__browser_info = value

    @property
    def color_depth(self):
        return self.__color_depth

    @color_depth.setter
    def color_depth(self, value):
        self.__color_depth = value

    @property
    def screen_height(self):
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, value):
        self.__screen_height = value

    @property
    def screen_width(self):
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, value):
        self.__screen_width = value

    @property
    def time_zone_offset(self):
        return self.__time_zone_offset

    @time_zone_offset.setter
    def time_zone_offset(self, value):
        self.__time_zone_offset = value

    @property
    def device_brand(self):
        return self.__device_brand

    @device_brand.setter
    def device_brand(self, value):
        self.__device_brand = value

    @property
    def device_model(self):
        return self.__device_model

    @device_model.setter
    def device_model(self, value):
        self.__device_model = value

    @property
    def device_language(self):
        return self.__device_language

    @device_language.setter
    def device_language(self, value):
        self.__device_language = value

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__device_id = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "terminal_type") and self.terminal_type:
            params['terminalType'] = self.terminal_type

        if hasattr(self, "os_type") and self.os_type:
            params['osType'] = self.os_type

        if hasattr(self, "user_agent") and self.user_agent:
            params['userAgent'] = self.user_agent

        if hasattr(self, "device_token_id ") and self.device_token_id:
            params['deviceTokenId'] = self.device_token_id

        if hasattr(self, "client_ip") and self.client_ip:
            params['clientIp'] = self.client_ip

        if hasattr(self, "cookie_id") and self.cookie_id:
            params['cookieId'] = self.cookie_id

        if hasattr(self, "store_terminal_id") and self.store_terminal_id:
            params['storeTerminalId'] = self.store_terminal_id

        if hasattr(self, "store_terminal_request_time") and self.store_terminal_request_time:
            params['storeTerminalRequestTime'] = self.store_terminal_request_time

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "browser_info") and self.browser_info:
            params['browserInfo'] = self.browser_info

        if hasattr(self, "color_depth") and self.color_depth:
            params['colorDepth'] = self.color_depth

        if hasattr(self, "screen_height") and self.screen_height:
            params['screenHeight'] = self.screen_height

        if hasattr(self, "screen_width") and self.screen_width:
            params['screenWidth'] = self.screen_width

        if hasattr(self, "time_zone_offset") and self.time_zone_offset:
            params['timeZoneOffset'] = self.time_zone_offset

        if hasattr(self, "device_brand") and self.device_brand:
            params['deviceBrand'] = self.device_brand

        if hasattr(self, "device_model") and self.device_model:
            params['deviceModel'] = self.device_model

        if hasattr(self, "device_language") and self.device_language:
            params['deviceLanguage'] = self.device_language

        if hasattr(self, "device_id") and self.device_id:
            params['deviceId'] = self.device_id

        return params
