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

    RABBIT_LINE_PAY = "RABBIT_LINE_PAY"

    PAYPAY = "PAYPAY"

    BOOST = "BOOST"

    GRABPAY_MY = "GRABPAY_MY"

    MAYA = "MAYA"

    GRABPAY_PH = "GRABPAY_PH"

    GRABPAY_SG = "GRABPAY_SG"

    NAVERPAY = "NAVERPAY"

    JKOPAY = "JKOPAY"

    KPLUS = "KPLUS"

    DIRECT_DEBIT_SIAMCOMMERCIALBANK = "DIRECT_DEBIT_SIAMCOMMERCIALBANK"

    DIRECT_DEBIT_KRUNGTHAIBANK = "DIRECT_DEBIT_KRUNGTHAIBANK"

    ZALOPAY = "ZALOPAY"

    DIRECTDEBIT_YAPILY = "DIRECTDEBIT_YAPILY "

    def to_ams_dict(self):
        return self.name
