import json
from com.alipay.ams.api.model.amount_limit import AmountLimit
from com.alipay.ams.api.model.amount_limit import AmountLimit
from com.alipay.ams.api.model.amount_limit import AmountLimit




class AmountLimitInfo:
    def __init__(self):
        
        self.__single_limit = None  # type: AmountLimit
        self.__day_limit = None  # type: AmountLimit
        self.__month_limit = None  # type: AmountLimit
        

    @property
    def single_limit(self):
        """Gets the single_limit of this AmountLimitInfo.
        
        """
        return self.__single_limit

    @single_limit.setter
    def single_limit(self, value):
        self.__single_limit = value
    @property
    def day_limit(self):
        """Gets the day_limit of this AmountLimitInfo.
        
        """
        return self.__day_limit

    @day_limit.setter
    def day_limit(self, value):
        self.__day_limit = value
    @property
    def month_limit(self):
        """Gets the month_limit of this AmountLimitInfo.
        
        """
        return self.__month_limit

    @month_limit.setter
    def month_limit(self, value):
        self.__month_limit = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "single_limit") and self.single_limit is not None:
            params['singleLimit'] = self.single_limit
        if hasattr(self, "day_limit") and self.day_limit is not None:
            params['dayLimit'] = self.day_limit
        if hasattr(self, "month_limit") and self.month_limit is not None:
            params['monthLimit'] = self.month_limit
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'singleLimit' in response_body:
            self.__single_limit = AmountLimit()
            self.__single_limit.parse_rsp_body(response_body['singleLimit'])
        if 'dayLimit' in response_body:
            self.__day_limit = AmountLimit()
            self.__day_limit.parse_rsp_body(response_body['dayLimit'])
        if 'monthLimit' in response_body:
            self.__month_limit = AmountLimit()
            self.__month_limit.parse_rsp_body(response_body['monthLimit'])
