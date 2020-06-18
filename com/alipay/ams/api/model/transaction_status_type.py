#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class TransactionStatusType(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    PROCESSING = "PROCESSING"
    CANCELLED = "CANCELLED"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TransactionStatusType.SUCCESS.value == value:
            return TransactionStatusType.SUCCESS
        elif TransactionStatusType.FAIL.value == value:
            return TransactionStatusType.FAIL
        elif TransactionStatusType.PROCESSING.value == value:
            return TransactionStatusType.PROCESSING
        elif TransactionStatusType.CANCELLED.value == value:
            return TransactionStatusType.CANCELLED
        else:
            return None
