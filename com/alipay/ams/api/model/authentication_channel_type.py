#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class AuthenticationChannelType(Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"

    def to_ams_dict(self):
        return self.name
