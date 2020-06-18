#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class WalletPaymentMethodType(Enum):
    TRUEMONEY = "TRUEMONEY"
    ALIPAY_HK = "ALIPAY_HK"
    TNG = "TNG"
    ALIPAY_CN = "ALIPAY_CN"
    GCASH = "GCASH"
    DANA = "DANA"
    KAKAOPAY = "KAKAOPAY"
    BKASH = "BKASH"
    EASYPAISA = "EASYPAISA"
    CONNECT_WALLET = "CONNECT_WALLET"

    def to_ams_dict(self):
        return self.name
