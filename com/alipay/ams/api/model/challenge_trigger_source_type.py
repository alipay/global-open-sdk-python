#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class ChallengeTriggerSourceType(Enum):
    AMS = "AMS"
    CHANNEL = "CHANNEL"

    def to_ams_dict(self):
        return self.name
