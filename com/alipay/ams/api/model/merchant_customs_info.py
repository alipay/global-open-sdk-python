class MerchantCustomsInfo(object):
    def __init__(self):
        self.merchant_customs_code = None
        self.__merchant_customs_name = None

    @property
    def merchant_customs_code(self):
        return self.__merchant_customs_code

    @merchant_customs_code.setter
    def merchant_customs_code(self, value):
        self.__merchant_customs_code = value

    @property
    def merchant_customs_name(self):
        return self.__merchant_customs_name

    @merchant_customs_name.setter
    def merchant_customs_name(self, value):
        self.__merchant_customs_name = value

    def to_ams_dict(self):
        params = dict()
        if self.merchant_customs_code is not None:
            params['merchantCustomsCode'] = self.merchant_customs_code
        if self.merchant_customs_name is not None:
            params['merchantCustomsName'] = self.merchant_customs_name
        return params
