#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class RiskScoreType(Enum):
    NSF_SCORE = "NSF_SCORE"
    FRAUD_SCORE = "FRAUD_SCORE"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if RiskScoreType.NSF_SCORE.value == value:
            return RiskScoreType.NSF_SCORE
        elif RiskScoreType.FRAUD_SCORE.value == value:
            return RiskScoreType.FRAUD_SCORE
        else:
            return None
