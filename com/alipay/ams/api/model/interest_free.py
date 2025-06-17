import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class InterestFree:
    def __init__(self):
        
        self.__provider = None  # type: str
        self.__expire_time = None  # type: str
        self.__installment_free_nums = None  # type: [int]
        self.__min_payment_amount = None  # type: Amount
        self.__max_payment_amount = None  # type: Amount
        self.__free_percentage = None  # type: int
        

    @property
    def provider(self):
        """
        Issuing banks or financial institutions that offer interest-free installment plans.  More information:  Maximum length: 128 characters
        """
        return self.__provider

    @provider.setter
    def provider(self, value):
        self.__provider = value
    @property
    def expire_time(self):
        """
        The promotion expiration time.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__expire_time

    @expire_time.setter
    def expire_time(self, value):
        self.__expire_time = value
    @property
    def installment_free_nums(self):
        """
        The number of interest-free installments.  More information:  Value range: 2-unlimited
        """
        return self.__installment_free_nums

    @installment_free_nums.setter
    def installment_free_nums(self, value):
        self.__installment_free_nums = value
    @property
    def min_payment_amount(self):
        """Gets the min_payment_amount of this InterestFree.
        
        """
        return self.__min_payment_amount

    @min_payment_amount.setter
    def min_payment_amount(self, value):
        self.__min_payment_amount = value
    @property
    def max_payment_amount(self):
        """Gets the max_payment_amount of this InterestFree.
        
        """
        return self.__max_payment_amount

    @max_payment_amount.setter
    def max_payment_amount(self, value):
        self.__max_payment_amount = value
    @property
    def free_percentage(self):
        """
        The interest-free percentage. A value of 0 indicates no interest-free, 100% indicates the buyer is completely interest-free, while the value between 0-100% indicates partial interest-free.
        """
        return self.__free_percentage

    @free_percentage.setter
    def free_percentage(self, value):
        self.__free_percentage = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "provider") and self.provider is not None:
            params['provider'] = self.provider
        if hasattr(self, "expire_time") and self.expire_time is not None:
            params['expireTime'] = self.expire_time
        if hasattr(self, "installment_free_nums") and self.installment_free_nums is not None:
            params['installmentFreeNums'] = self.installment_free_nums
        if hasattr(self, "min_payment_amount") and self.min_payment_amount is not None:
            params['minPaymentAmount'] = self.min_payment_amount
        if hasattr(self, "max_payment_amount") and self.max_payment_amount is not None:
            params['maxPaymentAmount'] = self.max_payment_amount
        if hasattr(self, "free_percentage") and self.free_percentage is not None:
            params['freePercentage'] = self.free_percentage
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'provider' in response_body:
            self.__provider = response_body['provider']
        if 'expireTime' in response_body:
            self.__expire_time = response_body['expireTime']
        if 'installmentFreeNums' in response_body:
            self.__installment_free_nums = response_body['installmentFreeNums']
        if 'minPaymentAmount' in response_body:
            self.__min_payment_amount = Amount()
            self.__min_payment_amount.parse_rsp_body(response_body['minPaymentAmount'])
        if 'maxPaymentAmount' in response_body:
            self.__max_payment_amount = Amount()
            self.__max_payment_amount.parse_rsp_body(response_body['maxPaymentAmount'])
        if 'freePercentage' in response_body:
            self.__free_percentage = response_body['freePercentage']
