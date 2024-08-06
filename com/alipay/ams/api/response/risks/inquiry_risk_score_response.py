#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.risk_score_result import RiskScoreResult
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class InquiryRiskScoreResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(InquiryRiskScoreResponse, self).__init__()
        self.__result = None
        self.__risk_score_results = None
        self.__parse_rsp_body(rsp_body)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @property
    def risk_score_results(self):
        return self.__risk_score_results

    @risk_score_results.setter
    def risk_score_results(self, value):
        self.__risk_score_results = value

    def __parse_rsp_body(self, rsp_body):
        response = super(InquiryRiskScoreResponse, self).parse_rsp_body(rsp_body)
        if 'result' in response:
            self.__result = response['result']

        if 'risk_score_results' in response:
            self.__risk_score_results = []
            for entry in response['risk_score_results']:
                risk_score_result = RiskScoreResult()
                risk_score_result.parse_rsp_body(entry)
                self.__risk_score_results.append(risk_score_result)
