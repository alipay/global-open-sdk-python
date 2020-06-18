#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class PaymentMethodCategoryType(Enum):
    WALLET = "WALLET"
    CARD = "CARD"

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

