import json
from com.alipay.ams.api.model.amount import Amount




class ProrationSettings:
    def __init__(self):
        
        self.__proration_mode = None  # type: str
        self.__custom_amount = None  # type: Amount
        

    @property
    def proration_mode(self):
        """
        用于标识\&quot;扣差价\&quot;或者\&quot;退差价\&quot;场景。有差价处理需求场景必传。  取值范围： - IMMEDIATE_PAY_CUSTOM_AMOUNT：商户指定金额扣款模式，在这个模式下商户可以用customAmount的指定金额扣差价，差价需要商户提前算好 - IMMEDIATE_REFUND_CUSTOM_AMOUNT：商户指定金额退款模式，在这个模式下商户可以用customAmount的指定金额来退差价，差价需要商户提前算好
        """
        return self.__proration_mode

    @proration_mode.setter
    def proration_mode(self, value):
        self.__proration_mode = value
    @property
    def custom_amount(self):
        """Gets the custom_amount of this ProrationSettings.
        
        """
        return self.__custom_amount

    @custom_amount.setter
    def custom_amount(self, value):
        self.__custom_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "proration_mode") and self.proration_mode is not None:
            params['prorationMode'] = self.proration_mode
        if hasattr(self, "custom_amount") and self.custom_amount is not None:
            params['customAmount'] = self.custom_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'prorationMode' in response_body:
            self.__proration_mode = response_body['prorationMode']
        if 'customAmount' in response_body:
            self.__custom_amount = Amount()
            self.__custom_amount.parse_rsp_body(response_body['customAmount'])
