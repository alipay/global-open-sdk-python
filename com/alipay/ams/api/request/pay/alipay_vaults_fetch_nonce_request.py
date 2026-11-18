import json
from com.alipay.ams.api.model.card import Card



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayVaultsFetchNonceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVaultsFetchNonceRequest, self).__init__("/ams/api/v1/vaults/fetchNonce") 

        self.__card = None  # type: Card
        

    @property
    def card(self):
        """Gets the card of this AlipayVaultsFetchNonceRequest.
        
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card") and self.card is not None:
            params['card'] = self.card
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'card' in response_body:
            self.__card = Card()
            self.__card.parse_rsp_body(response_body['card'])
