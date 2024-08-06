class CreditPayPlan(object):
    def __init__(self):
        self.__installment_num = None
        self.__credit_pay_fee_type = None
        self.__fee_percentage = None

    @property
    def installment_num(self):
        return self.__installment_num

    @property
    def credit_pay_fee_type(self):
        return self.__credit_pay_fee_type

    @property
    def fee_percentage(self):
        return self.__fee_percentage

    @installment_num.setter
    def installment_num(self, value):
        self.__installment_num = value

    @credit_pay_fee_type.setter
    def credit_pay_fee_type(self, value):
        self.__credit_pay_fee_type = value

    @fee_percentage.setter
    def fee_percentage(self, value):
        self.__fee_percentage = value

    def to_ams_dict(self):
        params = dict()

        if hasattr(self, "installment_num") and self.installment_num:
            params['installmentNum'] = self.installment_num
        if hasattr(self, "credit_pay_fee_type") and self.credit_pay_fee_type:
            params['creditPayFeeType'] = self.credit_pay_fee_type
        if hasattr(self, "fee_percentage") and self.fee_percentage:
            params['feePercentage'] = self.fee_percentage

        return params
