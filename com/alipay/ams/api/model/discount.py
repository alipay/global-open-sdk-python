import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Discount:
    def __init__(self):
        
        self.__discount_tag = None  # type: str
        self.__discount_name = None  # type: str
        self.__savings_amount = None  # type: Amount
        self.__estimate_savings_amount = None  # type: Amount
        

    @property
    def discount_tag(self):
        """Gets the discount_tag of this Discount.
        
        """
        return self.__discount_tag

    @discount_tag.setter
    def discount_tag(self, value):
        self.__discount_tag = value
    @property
    def discount_name(self):
        """
        The discount name displayed in the default language.  More information:  Maximum length: 128 characters
        """
        return self.__discount_name

    @discount_name.setter
    def discount_name(self, value):
        self.__discount_name = value
    @property
    def savings_amount(self):
        """Gets the savings_amount of this Discount.
        
        """
        return self.__savings_amount

    @savings_amount.setter
    def savings_amount(self, value):
        self.__savings_amount = value
    @property
    def estimate_savings_amount(self):
        """Gets the estimate_savings_amount of this Discount.
        
        """
        return self.__estimate_savings_amount

    @estimate_savings_amount.setter
    def estimate_savings_amount(self, value):
        self.__estimate_savings_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "discount_tag") and self.discount_tag is not None:
            params['discountTag'] = self.discount_tag
        if hasattr(self, "discount_name") and self.discount_name is not None:
            params['discountName'] = self.discount_name
        if hasattr(self, "savings_amount") and self.savings_amount is not None:
            params['savingsAmount'] = self.savings_amount
        if hasattr(self, "estimate_savings_amount") and self.estimate_savings_amount is not None:
            params['estimateSavingsAmount'] = self.estimate_savings_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'discountTag' in response_body:
            self.__discount_tag = response_body['discountTag']
        if 'discountName' in response_body:
            self.__discount_name = response_body['discountName']
        if 'savingsAmount' in response_body:
            self.__savings_amount = Amount()
            self.__savings_amount.parse_rsp_body(response_body['savingsAmount'])
        if 'estimateSavingsAmount' in response_body:
            self.__estimate_savings_amount = Amount()
            self.__estimate_savings_amount.parse_rsp_body(response_body['estimateSavingsAmount'])
