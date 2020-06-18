#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Env(object):
    def __init__(self):
        self.__terminal_type = None
        self.__os_type = None
        self.__user_agent = None
        self.__device_token_id = None
        self.__client_ip = None
        self.__cookie_id = None
        self.__store_terminal_id = None
        self.__store_terminal_request_time = None
        self.__extend_info = None

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

        return params

