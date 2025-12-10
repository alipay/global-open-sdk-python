import json
from com.alipay.ams.api.model.amount import Amount




class PeriodRule:
    def __init__(self):
        
        self.__period_type = None  # type: str
        self.__period = None  # type: int
        self.__price = None  # type: Amount
        self.__period_count = None  # type: int
        

    @property
    def period_type(self):
        """
        The subscription period type. Valid values are:  YEAR: indicates that the subscription period is measured in years.  MONTH: indicates that the subscription period is measured in months.  WEEK: indicates that the subscription period is measured in weeks.  DAY: indicates that the subscription period is measured in days.   More information:  Maximum length: 20 characters
        """
        return self.__period_type

    @period_type.setter
    def period_type(self, value):
        self.__period_type = value
    @property
    def period(self):
        """
        Number of periods
        """
        return self.__period

    @period.setter
    def period(self, value):
        self.__period = value
    @property
    def price(self):
        """Gets the price of this PeriodRule.
        
        """
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
    @property
    def period_count(self):
        """
        The number of period types within one subscription period. For example, if the value of periodType is MONTH and the value of periodCount is 2, it means that the subscription period is two months.    More information:  Value range: 1 - unlimited
        """
        return self.__period_count

    @period_count.setter
    def period_count(self, value):
        self.__period_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "period_type") and self.period_type is not None:
            params['periodType'] = self.period_type
        if hasattr(self, "period") and self.period is not None:
            params['period'] = self.period
        if hasattr(self, "price") and self.price is not None:
            params['price'] = self.price
        if hasattr(self, "period_count") and self.period_count is not None:
            params['periodCount'] = self.period_count
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'periodType' in response_body:
            self.__period_type = response_body['periodType']
        if 'period' in response_body:
            self.__period = response_body['period']
        if 'price' in response_body:
            self.__price = Amount()
            self.__price.parse_rsp_body(response_body['price'])
        if 'periodCount' in response_body:
            self.__period_count = response_body['periodCount']
