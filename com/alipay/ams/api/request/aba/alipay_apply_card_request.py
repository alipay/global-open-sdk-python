import json
from com.alipay.ams.api.model.authorization_control import AuthorizationControl



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayApplyCardRequest(AlipayRequest):
    def __init__(self):
        super(AlipayApplyCardRequest, self).__init__("/ams/api/v1/aba/cards/applyCard") 

        self.__request_id = None  # type: str
        self.__card_nick_name = None  # type: str
        self.__note = None  # type: str
        self.__card_bin_rule = None  # type: str
        self.__purpose = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__authorization_control = None  # type: AuthorizationControl
        

    @property
    def request_id(self):
        """Gets the request_id of this AlipayApplyCardRequest.
        
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
    @property
    def card_nick_name(self):
        """Gets the card_nick_name of this AlipayApplyCardRequest.
        
        """
        return self.__card_nick_name

    @card_nick_name.setter
    def card_nick_name(self, value):
        self.__card_nick_name = value
    @property
    def note(self):
        """Gets the note of this AlipayApplyCardRequest.
        
        """
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
    @property
    def card_bin_rule(self):
        """Gets the card_bin_rule of this AlipayApplyCardRequest.
        
        """
        return self.__card_bin_rule

    @card_bin_rule.setter
    def card_bin_rule(self, value):
        self.__card_bin_rule = value
    @property
    def purpose(self):
        """Gets the purpose of this AlipayApplyCardRequest.
        
        """
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        self.__purpose = value
    @property
    def metadata(self):
        """Gets the metadata of this AlipayApplyCardRequest.
        
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def authorization_control(self):
        """Gets the authorization_control of this AlipayApplyCardRequest.
        
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
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "card_nick_name") and self.card_nick_name is not None:
            params['cardNickName'] = self.card_nick_name
        if hasattr(self, "note") and self.note is not None:
            params['note'] = self.note
        if hasattr(self, "card_bin_rule") and self.card_bin_rule is not None:
            params['cardBinRule'] = self.card_bin_rule
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
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'cardNickName' in response_body:
            self.__card_nick_name = response_body['cardNickName']
        if 'note' in response_body:
            self.__note = response_body['note']
        if 'cardBinRule' in response_body:
            self.__card_bin_rule = response_body['cardBinRule']
        if 'purpose' in response_body:
            self.__purpose = response_body['purpose']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'authorizationControl' in response_body:
            self.__authorization_control = AuthorizationControl()
            self.__authorization_control.parse_rsp_body(response_body['authorizationControl'])
