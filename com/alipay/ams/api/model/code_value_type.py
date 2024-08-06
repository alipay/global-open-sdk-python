#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class CodeValueType(Enum):
    BARCODE = "BARCODE"
    QRCODE = "QRCODE"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CodeValueType.BARCODE.value == value:
            return CodeValueType.BARCODE
        elif CodeValueType.QRCODE.value == value:
            return CodeValueType.QRCODE
        else:
            return None
