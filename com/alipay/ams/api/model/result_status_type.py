#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class ResultStatusType(Enum):
    S = "S"
    F = "F"
    U = "U"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ResultStatusType.S.value == value:
            return ResultStatusType.S
        elif ResultStatusType.F.value == value:
            return ResultStatusType.F
        elif ResultStatusType.U.value == value:
            return ResultStatusType.U
        else:
            return None
