import json




class AgenticAuthenticationSessionAgent:
    def __init__(self):
        
        self.__agent_id = None  # type: str
        self.__agent_name = None  # type: str
        self.__agent_url = None  # type: str
        self.__agent_jwk = None  # type: str
        

    @property
    def agent_id(self):
        """
        Agent identifier.
        """
        return self.__agent_id

    @agent_id.setter
    def agent_id(self, value):
        self.__agent_id = value
    @property
    def agent_name(self):
        """
        Application name. Required for applicable Visa card-binding/application-registration scenarios.
        """
        return self.__agent_name

    @agent_name.setter
    def agent_name(self, value):
        self.__agent_name = value
    @property
    def agent_url(self):
        """
        Agent URL. Required for Mastercard AUTONOMOUS; maps to the L2 mandate Agent audience.
        """
        return self.__agent_url

    @agent_url.setter
    def agent_url(self, value):
        self.__agent_url = value
    @property
    def agent_jwk(self):
        """
        Required only for Mastercard AUTONOMOUS. Base64URL-encoded UTF-8 public JWK JSON. Only EC/P-256 is supported; include kid, kty, crv, x and y. Private key parameter d is forbidden. Must not be empty when required.
        """
        return self.__agent_jwk

    @agent_jwk.setter
    def agent_jwk(self, value):
        self.__agent_jwk = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "agent_id") and self.agent_id is not None:
            params['agentId'] = self.agent_id
        if hasattr(self, "agent_name") and self.agent_name is not None:
            params['agentName'] = self.agent_name
        if hasattr(self, "agent_url") and self.agent_url is not None:
            params['agentUrl'] = self.agent_url
        if hasattr(self, "agent_jwk") and self.agent_jwk is not None:
            params['agentJwk'] = self.agent_jwk
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'agentId' in response_body:
            self.__agent_id = response_body['agentId']
        if 'agentName' in response_body:
            self.__agent_name = response_body['agentName']
        if 'agentUrl' in response_body:
            self.__agent_url = response_body['agentUrl']
        if 'agentJwk' in response_body:
            self.__agent_jwk = response_body['agentJwk']
