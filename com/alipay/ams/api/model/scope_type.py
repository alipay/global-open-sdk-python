#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class ScopeType(Enum):
    BASE_USER_INFO = "BASE_USER_INFO"
    AGREEMENT_PAY = "AGREEMENT_PAY"
    USER_INFO = "USER_INFO"
    USER_LOGIN_ID = "USER_LOGIN_ID"
    HASH_LOGIN_ID = "HASH_LOGIN_ID"
    SEND_OTP = "SEND_OTP"
    TAOBAO_REBIND = "TAOBAO_REBIND"

    def to_ams_dict(self):
        return self.name
