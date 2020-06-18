#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class TransactionType(Enum):
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    CAPTURE = "CAPTURE"
    CANCEL = "CANCEL"
    AUTHORIZATION = "AUTHORIZATION"
    VOID = "VOID"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TransactionType.PAYMENT.value == value:
            return TransactionType.PAYMENT
        elif TransactionType.REFUND.value == value:
            return TransactionType.REFUND
        elif TransactionType.CAPTURE.value == value:
            return TransactionType.CAPTURE
        elif TransactionType.CANCEL.value == value:
            return TransactionType.CANCEL
        elif TransactionType.AUTHORIZATION.value == value:
            return TransactionType.AUTHORIZATION
        elif TransactionType.VOID.value == value:
            return TransactionType.VOID
        else:
            return None
