#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class GrantType(Enum):
    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    REFRESH_TOKEN = "REFRESH_TOKEN"

    def to_ams_dict(self):
        return self.name
