import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Tier:
    def __init__(self):
        
        self.__up_to = None  # type: int
        self.__unit_amount = None  # type: Amount
        self.__flat_amount = None  # type: Amount
        

    @property
    def up_to(self):
        """
        The up to.
        """
        return self.__up_to

    @up_to.setter
    def up_to(self, value):
        self.__up_to = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this Tier.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def flat_amount(self):
        """Gets the flat_amount of this Tier.
        
        """
        return self.__flat_amount

    @flat_amount.setter
    def flat_amount(self, value):
        self.__flat_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "up_to") and self.up_to is not None:
            params['upTo'] = self.up_to
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "flat_amount") and self.flat_amount is not None:
            params['flatAmount'] = self.flat_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'upTo' in response_body:
            self.__up_to = response_body['upTo']
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'flatAmount' in response_body:
            self.__flat_amount = Amount()
            self.__flat_amount.parse_rsp_body(response_body['flatAmount'])
