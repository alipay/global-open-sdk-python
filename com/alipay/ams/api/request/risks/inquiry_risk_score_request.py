#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class InquiryRiskScoreRequest(AlipayRequest):

    def __init__(self):
        super(InquiryRiskScoreRequest, self).__init__()
        self.__customer_belongs_to = None
        self.__customer_id_type = None
        self.__customer_id = None
        self.__risk_score_types = None

    @property
    def customer_belongs_to(self):
        return self.__customer_belongs_to

    @customer_belongs_to.setter
    def customer_belongs_to(self, value):
        self.__customer_belongs_to = value

    @property
    def customer_id_type(self):
        return self.__customer_id_type

    @customer_id_type.setter
    def customer_id_type(self, value):
        self.__customer_id_type = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def risk_score_types(self):
        return self.__risk_score_types

    @risk_score_types.setter
    def risk_score_types(self, value):
        self.__risk_score_types = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_belongs_to") and self.customer_belongs_to:
            params["customerBelongsTo"] = self.customer_belongs_to

        if hasattr(self, "customer_id_type") and self.customer_id_type:
            params["customerIdType"] = self.customer_id_type

        if hasattr(self, "customer_id") and self.customer_id:
            params["customer_id"] = self.customer_id

        if hasattr(self, "risk_score_types") and self.risk_score_types:
            params["riskScoreTypes"] = self.risk_score_types

        return params
