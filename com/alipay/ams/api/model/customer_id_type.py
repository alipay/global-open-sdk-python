#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class CustomerIdType(Enum):
    EMAIL = "EMAIL"
    USER_ID = "USER_ID"
    MOBILE_NO = "MOBILE_NO"
    AUTH_CODE = "AUTH_CODE"

    def to_ams_dict(self):
        return self.name
