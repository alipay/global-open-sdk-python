import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Plan:
    def __init__(self):
        
        self.__interest_rate = None  # type: str
        self.__min_installment_amount = None  # type: Amount
        self.__max_installment_amount = None  # type: Amount
        self.__installment_num = None  # type: str
        self.__interval = None  # type: str
        self.__enabled = None  # type: bool
        self.__extend_info = None  # type: str
        

    @property
    def interest_rate(self):
        """
        The interest rate the customer is charged on the installments.    More information:  Maximum length: 8 characters
        """
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value
    @property
    def min_installment_amount(self):
        """Gets the min_installment_amount of this Plan.
        
        """
        return self.__min_installment_amount

    @min_installment_amount.setter
    def min_installment_amount(self, value):
        self.__min_installment_amount = value
    @property
    def max_installment_amount(self):
        """Gets the max_installment_amount of this Plan.
        
        """
        return self.__max_installment_amount

    @max_installment_amount.setter
    def max_installment_amount(self, value):
        self.__max_installment_amount = value
    @property
    def installment_num(self):
        """
        The number of installment payments. The valid value is from 2 to 12.    More information:  Maximum length: 8 characters
        """
        return self.__installment_num

    @installment_num.setter
    def installment_num(self, value):
        self.__installment_num = value
    @property
    def interval(self):
        """
        The interval of each installment payment. The valid value is MONTH.   More information:  Maximum length: 16 characters
        """
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value
    @property
    def enabled(self):
        """
        Indicates whether the installment payment is available. 
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value
    @property
    def extend_info(self):
        """
        Extended information field, used to return extended information of the payment installment plan in the payment consultation interface. The extended fields in the installment plan include interest rates and various amount details to meet the merchant&#39;s amount display requirements.  More information:  Maximum length: 4096 characters
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "interest_rate") and self.interest_rate is not None:
            params['interestRate'] = self.interest_rate
        if hasattr(self, "min_installment_amount") and self.min_installment_amount is not None:
            params['minInstallmentAmount'] = self.min_installment_amount
        if hasattr(self, "max_installment_amount") and self.max_installment_amount is not None:
            params['maxInstallmentAmount'] = self.max_installment_amount
        if hasattr(self, "installment_num") and self.installment_num is not None:
            params['installmentNum'] = self.installment_num
        if hasattr(self, "interval") and self.interval is not None:
            params['interval'] = self.interval
        if hasattr(self, "enabled") and self.enabled is not None:
            params['enabled'] = self.enabled
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'interestRate' in response_body:
            self.__interest_rate = response_body['interestRate']
        if 'minInstallmentAmount' in response_body:
            self.__min_installment_amount = Amount()
            self.__min_installment_amount.parse_rsp_body(response_body['minInstallmentAmount'])
        if 'maxInstallmentAmount' in response_body:
            self.__max_installment_amount = Amount()
            self.__max_installment_amount.parse_rsp_body(response_body['maxInstallmentAmount'])
        if 'installmentNum' in response_body:
            self.__installment_num = response_body['installmentNum']
        if 'interval' in response_body:
            self.__interval = response_body['interval']
        if 'enabled' in response_body:
            self.__enabled = response_body['enabled']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
