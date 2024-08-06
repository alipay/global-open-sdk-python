#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class PaymentMethodDetailType(Enum):
    CARD = "CARD"
    EXTERNALACCOUNT = "EXTERNALACCOUNT"
    COUPON = "COUPON"
    DISCOUNT = "DISCOUNT"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodDetailType.CARD.value == value:
            return PaymentMethodDetailType.CARD
        elif PaymentMethodDetailType.EXTERNALACCOUNT.value == value:
            return PaymentMethodDetailType.EXTERNALACCOUNT
        elif PaymentMethodDetailType.COUPON.value == value:
            return PaymentMethodDetailType.COUPON
        elif PaymentMethodDetailType.DISCOUNT.value == value:
            return PaymentMethodDetailType.DISCOUNT
        else:
            return None
