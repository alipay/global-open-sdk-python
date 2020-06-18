#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class RiskScoreDetail(object):

    def __init__(self):
        self.__risk_info_code = None
        self.__risk_info_code_result = None

    @property
    def risk_info_code(self):
        return self.__risk_info_code

    @risk_info_code.setter
    def risk_info_code(self, value):
        self.__risk_info_code = value

    @property
    def risk_info_code_result(self):
        return self.__risk_info_code_result

    @risk_info_code_result.setter
    def risk_info_code_result(self, value):
        self.__risk_info_code_result = value

    def parse_rsp_body(self, risk_score_detail_body):
        if type(risk_score_detail_body) == str:
            risk_score_detail_body = json.loads(risk_score_detail_body)

        if 'riskInfoCode' in risk_score_detail_body:
            self.__risk_info_code = risk_score_detail_body['riskInfoCode']

        if 'riskInfoCodeResult' in risk_score_detail_body:
            self.__risk_info_code_result = risk_score_detail_body['riskInfoCodeResult']
