import json
from com.alipay.ams.api.model.card_limit_info import CardLimitInfo




class AlipayInquireCardSensitiveInfoResponseAuthorizationControl:
    def __init__(self):
        
        self.__card_limit_info = None  # type: CardLimitInfo
        

    @property
    def card_limit_info(self):
        """Gets the card_limit_info of this AlipayInquireCardSensitiveInfoResponseAuthorizationControl.
        
        """
        return self.__card_limit_info

    @card_limit_info.setter
    def card_limit_info(self, value):
        self.__card_limit_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_limit_info") and self.card_limit_info is not None:
            params['cardLimitInfo'] = self.card_limit_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardLimitInfo' in response_body:
            self.__card_limit_info = CardLimitInfo()
            self.__card_limit_info.parse_rsp_body(response_body['cardLimitInfo'])
