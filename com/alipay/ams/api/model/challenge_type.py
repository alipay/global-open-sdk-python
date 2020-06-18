#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class ChallengeType(Enum):
    SMS_OTP = "SMS_OTP"
    PLAINTEXT_CARD_NO = "PLAINTEXT_CARD_NO"
    CARD_EXPIRE_DATE = "CARD_EXPIRE_DATE"

    def to_ams_dict(self):
        return self.name
