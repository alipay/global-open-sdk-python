import json
from com.alipay.ams.api.model.credit_pay_fee_type import CreditPayFeeType




class CreditPayPlan:
    def __init__(self):
        
        self.__installment_num = None  # type: int
        self.__interval = None  # type: str
        self.__credit_pay_fee_type = None  # type: CreditPayFeeType
        self.__fee_percentage = None  # type: int
        

    @property
    def installment_num(self):
        """Gets the installment_num of this CreditPayPlan.
        
        """
        return self.__installment_num

    @installment_num.setter
    def installment_num(self, value):
        self.__installment_num = value
    @property
    def interval(self):
        """Gets the interval of this CreditPayPlan.
        
        """
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value
    @property
    def credit_pay_fee_type(self):
        """Gets the credit_pay_fee_type of this CreditPayPlan.
        
        """
        return self.__credit_pay_fee_type

    @credit_pay_fee_type.setter
    def credit_pay_fee_type(self, value):
        self.__credit_pay_fee_type = value
    @property
    def fee_percentage(self):
        """Gets the fee_percentage of this CreditPayPlan.
        
        """
        return self.__fee_percentage

    @fee_percentage.setter
    def fee_percentage(self, value):
        self.__fee_percentage = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "installment_num") and self.installment_num is not None:
            params['installmentNum'] = self.installment_num
        if hasattr(self, "interval") and self.interval is not None:
            params['interval'] = self.interval
        if hasattr(self, "credit_pay_fee_type") and self.credit_pay_fee_type is not None:
            params['creditPayFeeType'] = self.credit_pay_fee_type
        if hasattr(self, "fee_percentage") and self.fee_percentage is not None:
            params['feePercentage'] = self.fee_percentage
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'installmentNum' in response_body:
            self.__installment_num = response_body['installmentNum']
        if 'interval' in response_body:
            self.__interval = response_body['interval']
        if 'creditPayFeeType' in response_body:
            credit_pay_fee_type_temp = CreditPayFeeType.value_of(response_body['creditPayFeeType'])
            self.__credit_pay_fee_type = credit_pay_fee_type_temp
        if 'feePercentage' in response_body:
            self.__fee_percentage = response_body['feePercentage']
