#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class ProductCodeType(Enum):
    AGREEMENT_PAYMENT = "AGREEMENT_PAYMENT"
    IN_STORE_PAYMENT = "IN_STORE_PAYMENT"
    CASHIER_PAYMENT = "CASHIER_PAYMENT"

    def to_ams_dict(self):
        return self.name
