#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.capture_mode import CaptureMode
from com.alipay.ams.api.model.in_store_payment_scenario import InStorePaymentScenario
from com.alipay.ams.api.model.presentment_mode import PresentmentMode


class PaymentFactor(object):
    def __init__(self):
        self.__is_payment_evaluation = None
        self.__in_store_payment_scenario = None  # type: InStorePaymentScenario
        self.__presentment_mode = None  # type: PresentmentMode
        self.__capture_mode = None  # type: CaptureMode
        self.__is_authorization = None

    @property
    def is_payment_evaluation(self):
        return self.__is_payment_evaluation

    @is_payment_evaluation.setter
    def is_payment_evaluation(self, value):
        self.__is_payment_evaluation = value

    @property
    def in_store_payment_scenario(self):
        return self.__in_store_payment_scenario

    @in_store_payment_scenario.setter
    def in_store_payment_scenario(self, value):
        self.__in_store_payment_scenario = value

    @property
    def presentment_mode(self):
        return self.__presentment_mode

    @presentment_mode.setter
    def presentment_mode(self, value):
        self.__presentment_mode = value

    @property
    def is_authorization(self):
        return self.__is_authorization

    @is_authorization.setter
    def is_authorization(self, value):
        self.__is_authorization = value

    @property
    def capture_mode(self):
        return self.__capture_mode

    @capture_mode.setter
    def capture_mode(self, value):
        self.__capture_mode = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "is_payment_evaluation") and self.__is_payment_evaluation:
            params['isPaymentEvaluation'] = self.is_payment_evaluation

        if hasattr(self, "in_store_payment_scenario") and self.in_store_payment_scenario:
            params['inStorePaymentScenario'] = self.in_store_payment_scenario

        if hasattr(self, "presentment_mode") and self.presentment_mode:
            params['presentmentMode'] = self.presentment_mode

        if hasattr(self, "is_authorization") and self.is_authorization:
            params['isAuthorization'] = self.is_authorization

        if hasattr(self, "capture_mode") and self.capture_mode:
            params['captureMode'] = self.capture_mode

        return params
