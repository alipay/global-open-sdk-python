#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class UserIdentityType(Enum):
    WALLET_TOKEN = "WALLET_TOKEN"

    def to_ams_dict(self):
        return self.name
