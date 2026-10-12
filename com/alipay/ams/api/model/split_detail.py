import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class SplitDetail:
    def __init__(self):
        
        self.__split_to = None  # type: str
        self.__split_amount = None  # type: Amount
        self.__actual_split_amount = None  # type: Amount
        self.__description = None  # type: str
        

    @property
    def split_to(self):
        """
        The original split recipient from which the funds are reversed for this refund. Valid values are:  SELLER: indicates that the payment funds were split to the seller. MARKETPLACE: indicates that the payment funds were split to the marketplace. PLATFORM: indicates that the payment funds were split to the platform. ISV: indicates that the payment funds were split to the independent software vendor.  Note: The value must exist in the successful split of the original payment or capture. Unknown values are rejected with the existing PARAM_ILLEGAL behavior.  More information:  Maximum length: 32 characters
        """
        return self.__split_to

    @split_to.setter
    def split_to(self, value):
        self.__split_to = value
    @property
    def split_amount(self):
        """Gets the split_amount of this SplitDetail.
        
        """
        return self.__split_amount

    @split_amount.setter
    def split_amount(self, value):
        self.__split_amount = value
    @property
    def actual_split_amount(self):
        """Gets the actual_split_amount of this SplitDetail.
        
        """
        return self.__actual_split_amount

    @actual_split_amount.setter
    def actual_split_amount(self, value):
        self.__actual_split_amount = value
    @property
    def description(self):
        """
        The merchant-supplied remark for billing and reconciliation. If this field is provided, it is reflected in the bill and returned with the corresponding refund split detail. Omission does not affect refund or split-reversal processing.  More information:  Maximum length: 256 characters
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "split_to") and self.split_to is not None:
            params['splitTo'] = self.split_to
        if hasattr(self, "split_amount") and self.split_amount is not None:
            params['splitAmount'] = self.split_amount
        if hasattr(self, "actual_split_amount") and self.actual_split_amount is not None:
            params['actualSplitAmount'] = self.actual_split_amount
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'splitTo' in response_body:
            self.__split_to = response_body['splitTo']
        if 'splitAmount' in response_body:
            self.__split_amount = Amount()
            self.__split_amount.parse_rsp_body(response_body['splitAmount'])
        if 'actualSplitAmount' in response_body:
            self.__actual_split_amount = Amount()
            self.__actual_split_amount.parse_rsp_body(response_body['actualSplitAmount'])
        if 'description' in response_body:
            self.__description = response_body['description']
