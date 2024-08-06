#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.risk_score_detail import RiskScoreDetail
from com.alipay.ams.api.model.risk_score_type import RiskScoreType


class RiskScoreResult(object):

    def __init__(self):
        self.__risk_score_type = None  # type: RiskScoreType
        self.__risk_score = None
        self.__risk_score_details = None  # type: list[RiskScoreDetail]

    @property
    def risk_score_type(self):
        return self.__risk_score_type

    @risk_score_type.setter
    def risk_score_type(self, value):
        self.__risk_score_type = value

    @property
    def risk_score(self):
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, value):
        self.__risk_score = value

    @property
    def risk_score_details(self):
        return self.__risk_score_details

    @risk_score_details.setter
    def risk_score_details(self, value):
        self.__risk_score_details = value

    def parse_rsp_body(self, risk_score_result_body):
        if type(risk_score_result_body) == str:
            risk_score_result_body = json.loads(risk_score_result_body)

        if 'riskScoreType' in risk_score_result_body:
            risk_score_type = RiskScoreType.value_of(risk_score_result_body['riskScoreType'])
            self.__risk_score_type = risk_score_type

        if 'riskScore' in risk_score_result_body:
            self.__risk_score = risk_score_result_body['riskScore']

        if 'riskScoreDetails' in risk_score_result_body:
            self.__risk_score_details = []
            for entry in risk_score_result_body['riskScoreDetails']:
                risk_score_detail = RiskScoreDetail()
                risk_score_detail.parse_rsp_body(entry)
                self.__risk_score_details.append(risk_score_detail)
