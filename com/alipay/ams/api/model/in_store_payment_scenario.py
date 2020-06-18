#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class InStorePaymentScenario(Enum):
    PaymentCode = "PaymentCode"
    OrderCode = "OrderCode"
    EntryCode = "EntryCode"

    def to_ams_dict(self):
        return self.name
