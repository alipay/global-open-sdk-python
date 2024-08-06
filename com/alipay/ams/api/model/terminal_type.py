#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class TerminalType(Enum):
    WEB = "WEB"
    WAP = "WAP"
    APP = "APP"

    def to_ams_dict(self):
        return self.name
