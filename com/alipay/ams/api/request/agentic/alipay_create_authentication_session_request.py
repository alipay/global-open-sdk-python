import json
from com.alipay.ams.api.model.agentic_authentication_session_agent import AgenticAuthenticationSessionAgent
from com.alipay.ams.api.model.agentic_payment_method import AgenticPaymentMethod
from com.alipay.ams.api.model.agentic_authentication_session_mandate import AgenticAuthenticationSessionMandate
from com.alipay.ams.api.model.agentic_session_env import AgenticSessionEnv



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateAuthenticationSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateAuthenticationSessionRequest, self).__init__("/ams/api/v1/agenticPayment/createAuthenticationSession") 

        self.__authentication_request_id = None  # type: str
        self.__user_login_id = None  # type: str
        self.__agent = None  # type: AgenticAuthenticationSessionAgent
        self.__bind_on_authorize = None  # type: bool
        self.__payment_method = None  # type: AgenticPaymentMethod
        self.__purchase_type = None  # type: str
        self.__mandate = None  # type: AgenticAuthenticationSessionMandate
        self.__country_code = None  # type: str
        self.__redirect_url = None  # type: str
        self.__env = None  # type: AgenticSessionEnv
        

    @property
    def authentication_request_id(self):
        """
        Authentication/authorization correlation identifier. No deduplication or replay guarantee. Use a new authenticationRequestId to create a new session.
        """
        return self.__authentication_request_id

    @authentication_request_id.setter
    def authentication_request_id(self, value):
        self.__authentication_request_id = value
    @property
    def user_login_id(self):
        """
        An opaque user identifier within the merchant scope. Do not include unnecessary personal information.
        """
        return self.__user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self.__user_login_id = value
    @property
    def agent(self):
        """Gets the agent of this AlipayCreateAuthenticationSessionRequest.
        
        """
        return self.__agent

    @agent.setter
    def agent(self, value):
        self.__agent = value
    @property
    def bind_on_authorize(self):
        """
        Whether to bind a payment method during this authorization. true means authorize and bind; false or omission means authorize only (default false). When true, paymentMethod.paymentMethodId may be omitted and the page selects or collects the payment method.
        """
        return self.__bind_on_authorize

    @bind_on_authorize.setter
    def bind_on_authorize(self, value):
        self.__bind_on_authorize = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayCreateAuthenticationSessionRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def purchase_type(self):
        """
        Purchase mode: IMMEDIATE (in-session purchase) or AUTONOMOUS (delegated purchase). RECURRING is reserved and unsupported; it returns PARAM_ILLEGAL/F without creating a session. Supported values (case-sensitive): IMMEDIATE, AUTONOMOUS.
        """
        return self.__purchase_type

    @purchase_type.setter
    def purchase_type(self, value):
        self.__purchase_type = value
    @property
    def mandate(self):
        """Gets the mandate of this AlipayCreateAuthenticationSessionRequest.
        
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value
    @property
    def country_code(self):
        """
        Country or region code. Use an uppercase ISO 3166-1 alpha-2 two-letter code when provided.
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
    @property
    def redirect_url(self):
        """
        URL to which the user is redirected after completing the session.
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value
    @property
    def env(self):
        """Gets the env of this AlipayCreateAuthenticationSessionRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "authentication_request_id") and self.authentication_request_id is not None:
            params['authenticationRequestId'] = self.authentication_request_id
        if hasattr(self, "user_login_id") and self.user_login_id is not None:
            params['userLoginId'] = self.user_login_id
        if hasattr(self, "agent") and self.agent is not None:
            params['agent'] = self.agent
        if hasattr(self, "bind_on_authorize") and self.bind_on_authorize is not None:
            params['bindOnAuthorize'] = self.bind_on_authorize
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "purchase_type") and self.purchase_type is not None:
            params['purchaseType'] = self.purchase_type
        if hasattr(self, "mandate") and self.mandate is not None:
            params['mandate'] = self.mandate
        if hasattr(self, "country_code") and self.country_code is not None:
            params['countryCode'] = self.country_code
        if hasattr(self, "redirect_url") and self.redirect_url is not None:
            params['redirectUrl'] = self.redirect_url
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'authenticationRequestId' in response_body:
            self.__authentication_request_id = response_body['authenticationRequestId']
        if 'userLoginId' in response_body:
            self.__user_login_id = response_body['userLoginId']
        if 'agent' in response_body:
            self.__agent = AgenticAuthenticationSessionAgent()
            self.__agent.parse_rsp_body(response_body['agent'])
        if 'bindOnAuthorize' in response_body:
            self.__bind_on_authorize = response_body['bindOnAuthorize']
        if 'paymentMethod' in response_body:
            self.__payment_method = AgenticPaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'purchaseType' in response_body:
            self.__purchase_type = response_body['purchaseType']
        if 'mandate' in response_body:
            self.__mandate = AgenticAuthenticationSessionMandate()
            self.__mandate.parse_rsp_body(response_body['mandate'])
        if 'countryCode' in response_body:
            self.__country_code = response_body['countryCode']
        if 'redirectUrl' in response_body:
            self.__redirect_url = response_body['redirectUrl']
        if 'env' in response_body:
            self.__env = AgenticSessionEnv()
            self.__env.parse_rsp_body(response_body['env'])
