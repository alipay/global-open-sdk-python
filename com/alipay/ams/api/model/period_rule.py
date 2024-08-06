import json


class PeriodRule(object):
    def __int__(self):
        self.__period_type = None
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

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "period_type") and self.period_type:
            params['periodType'] = self.period_type
        if hasattr(self, "period_count") and self.period_count:
            params['periodCount'] = self.period_countarams = dict()

        return params