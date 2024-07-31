#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class PaymentMethodCategoryType(Enum):
    WALLET = "WALLET"
    CARD = "CARD"
    ALIPAY_PLUS = "ALIPAY_PLUS"
    BANK_TRANSFER = "BANK_TRANSFER"
    MOBILE_BANKING_APP = "MOBILE_BANKING_APP"
    ONLINE_BANKING = "ONLINE_BANKING"
    OTC = "OTC"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodCategoryType.WALLET.value == value:
            return PaymentMethodCategoryType.WALLET
        elif PaymentMethodCategoryType.CARD.value == value:
            return PaymentMethodCategoryType.CARD
        else:
            return None
