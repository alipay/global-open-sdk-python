import json
from com.alipay.ams.api.model.authorization_control import AuthorizationControl



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayUpdateCardRequest(AlipayRequest):
    def __init__(self):
        super(AlipayUpdateCardRequest, self).__init__("/ams/api/v1/aba/cards/updateCard") 

        self.__asset_id = None  # type: str
        self.__request_id = None  # type: str
        self.__card_nick_name = None  # type: str
        self.__note = None  # type: str
        self.__purpose = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__authorization_control = None  # type: AuthorizationControl
        

    @property
    def asset_id(self):
        """
        卡资产ID。 Card asset Id
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def request_id(self):
        """
        针对本次申卡请求，由集成商指定的唯一请求号 The unique request number specified by the integrator for this card application request.
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
    @property
    def card_nick_name(self):
        """
        The nickname of the Card. This parameter is useful for managing multiple cards.
        """
        return self.__card_nick_name

    @card_nick_name.setter
    def card_nick_name(self, value):
        self.__card_nick_name = value
    @property
    def note(self):
        """
        Note information of card application
        """
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
    @property
    def purpose(self):
        """
        Purpose of the card.
        """
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        self.__purpose = value
    @property
    def metadata(self):
        """
        Customer metadata in key-value format. - Key max length: 32 - Value max length: 128 - Max number of keys: 30 - Total JSON string max length: 3096 (application-layer validation required)
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def authorization_control(self):
        """Gets the authorization_control of this AlipayUpdateCardRequest.
        
        """
        return self.__authorization_control

    @authorization_control.setter
    def authorization_control(self, value):
        self.__authorization_control = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "card_nick_name") and self.card_nick_name is not None:
            params['cardNickName'] = self.card_nick_name
        if hasattr(self, "note") and self.note is not None:
            params['note'] = self.note
        if hasattr(self, "purpose") and self.purpose is not None:
            params['purpose'] = self.purpose
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "authorization_control") and self.authorization_control is not None:
            params['authorizationControl'] = self.authorization_control
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'cardNickName' in response_body:
            self.__card_nick_name = response_body['cardNickName']
        if 'note' in response_body:
            self.__note = response_body['note']
        if 'purpose' in response_body:
            self.__purpose = response_body['purpose']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'authorizationControl' in response_body:
            self.__authorization_control = AuthorizationControl()
            self.__authorization_control.parse_rsp_body(response_body['authorizationControl'])
