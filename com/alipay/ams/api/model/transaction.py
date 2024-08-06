#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.model.transaction_type import TransactionType


class Transaction(object):

    def __init__(self):
        self.__transaction_result = None
        self.__transaction_id = None
        self.__transaction_type = None  # type:TransactionType
        self.__transaction_status = None  # type:TransactionStatusType
        self.__transaction_amount = None  # type:Amount
        self.__transaction_request_id = None
        self.__transaction_time = None

    @property
    def transaction_result(self):
        return self.__transaction_result

    @property
    def transaction_id(self):
        return self.__transaction_id

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def transaction_status(self):
        return self.__transaction_status

    @property
    def transaction_amount(self):
        return self.__transaction_amount

    @property
    def transaction_request_id(self):
        return self.__transaction_request_id

    @property
    def transaction_time(self):
        return self.__transaction_time

    def parse_rsp_body(self, transaction_body):
        if type(transaction_body) == str:
            transaction_body = json.loads(transaction_body)

        if 'transactionResult' in transaction_body:
            transaction_result = Result()
            transaction_result.parse_rsp_body(transaction_body['transactionResult'])
            self.__transaction_result = transaction_result

        if 'transactionId' in transaction_body:
            self.__transaction_id = transaction_body['transactionId']

        if 'transactionType' in transaction_body:
            transaction_type = TransactionType.value_of(transaction_body['transactionType'])
            self.__transaction_type = transaction_type

        if 'transactionStatus' in transaction_body:
            transaction_status = TransactionStatusType.value_of(transaction_body['transactionStatus'])
            self.__transaction_status = transaction_status

        if 'transactionAmount' in transaction_body:
            transaction_amount = Amount()
            transaction_amount.parse_rsp_body(transaction_body['transactionAmount'])
            self.__transaction_amount = transaction_amount

        if 'transactionRequestId' in transaction_body:
            self.__transaction_request_id = transaction_body['transactionRequestId']

        if 'transactionTime' in transaction_body:
            self.__transaction_time = transaction_body['transactionTime']
