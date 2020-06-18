#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class CustomerBelongsTo(Enum):
    TRUEMONEY = "TRUEMONEY"
    ALIPAY_HK = "ALIPAY_HK"
    TNG = "TNG"
    ALIPAY_CN = "ALIPAY_CN"
    GCASH = "GCASH"
    DANA = "DANA"
    KAKAOPAY = "KAKAOPAY"
    BKASH = "BKASH"
    EASYPAISA = "EASYPAISA"

    def to_ams_dict(self):
        return self.name
