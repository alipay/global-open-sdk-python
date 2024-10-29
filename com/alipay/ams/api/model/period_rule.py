import json

from com.alipay.ams.api.model.period_type import PeriodType


class PeriodRule(object):
    def __init__(self):
        self.__period_type = None #type: PeriodType
        self.__period_count = None

    @property
    def period_type(self):
        return self.__period_type

    @period_type.setter
    def period_type(self, value):
        self.__period_type = value

    @property
    def period_count(self):
        return self.__period_count

    @period_count.setter
    def period_count(self, value):
        self.__period_count = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "period_type") and self.period_type:
            params['periodType'] = self.period_type
        if hasattr(self, "period_count") and self.period_count:
            params['periodCount'] = self.period_count

        return params

    def parse_rsp_body(self, result_body):
        if type(result_body) == str:
            result_body = json.loads(result_body)

        if 'periodType' in result_body:
            self.__period_type = result_body['periodType']
        if 'periodCount' in result_body:
            self.__period_count = result_body['periodCount']




