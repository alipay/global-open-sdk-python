import json
from com.alipay.ams.api.model.agentic_agent_info import AgenticAgentInfo
from com.alipay.ams.api.model.agentic_payment_method import AgenticPaymentMethod
from com.alipay.ams.api.model.agentic_mandate import AgenticMandate
from com.alipay.ams.api.model.env import Env



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateBindingSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateBindingSessionRequest, self).__init__("/ams/api/v1/agenticPayment/createBindingSession") 

        self.__binding_request_id = None  # type: str
        self.__user_login_id = None  # type: str
        self.__agent = None  # type: AgenticAgentInfo
        self.__authorize_on_bind = None  # type: bool
        self.__payment_method = None  # type: AgenticPaymentMethod
        self.__purchase_type = None  # type: str
        self.__mandate = None  # type: AgenticMandate
        self.__country_code = None  # type: str
        self.__redirect_url = None  # type: str
        self.__env = None  # type: Env
        

    @property
    def binding_request_id(self):
        """
        Request correlation identifier. Each call is processed independently, without deduplication or replay guarantees. Use a new bindingRequestId when creating a new session.
        """
        return self.__binding_request_id

    @binding_request_id.setter
    def binding_request_id(self, value):
        self.__binding_request_id = value
    @property
    def user_login_id(self):
        """
        User email address. This SDK field is a string; no email-format validation is imposed.
        """
        return self.__user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self.__user_login_id = value
    @property
    def agent(self):
        """Gets the agent of this AlipayCreateBindingSessionRequest.
        
        """
        return self.__agent

    @agent.setter
    def agent(self, value):
        self.__agent = value
    @property
    def authorize_on_bind(self):
        """
        Whether to authorize while binding the payment method. false means binding only; true currently supports Visa, as stated in this field description. The selectedCardBrand field has its own documented combination restrictions.
        """
        return self.__authorize_on_bind

    @authorize_on_bind.setter
    def authorize_on_bind(self, value):
        self.__authorize_on_bind = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayCreateBindingSessionRequest.
        
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
        """Gets the mandate of this AlipayCreateBindingSessionRequest.
        
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value
    @property
    def country_code(self):
        """
        ISO 3166-1 alpha-2 two-letter country or region code. Required only for Visa CARD binding; omit for other channels.
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
        """Gets the env of this AlipayCreateBindingSessionRequest.
        
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
        if hasattr(self, "binding_request_id") and self.binding_request_id is not None:
            params['bindingRequestId'] = self.binding_request_id
        if hasattr(self, "user_login_id") and self.user_login_id is not None:
            params['userLoginId'] = self.user_login_id
        if hasattr(self, "agent") and self.agent is not None:
            params['agent'] = self.agent
        if hasattr(self, "authorize_on_bind") and self.authorize_on_bind is not None:
            params['authorizeOnBind'] = self.authorize_on_bind
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
        if 'bindingRequestId' in response_body:
            self.__binding_request_id = response_body['bindingRequestId']
        if 'userLoginId' in response_body:
            self.__user_login_id = response_body['userLoginId']
        if 'agent' in response_body:
            self.__agent = AgenticAgentInfo()
            self.__agent.parse_rsp_body(response_body['agent'])
        if 'authorizeOnBind' in response_body:
            self.__authorize_on_bind = response_body['authorizeOnBind']
        if 'paymentMethod' in response_body:
            self.__payment_method = AgenticPaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'purchaseType' in response_body:
            self.__purchase_type = response_body['purchaseType']
        if 'mandate' in response_body:
            self.__mandate = AgenticMandate()
            self.__mandate.parse_rsp_body(response_body['mandate'])
        if 'countryCode' in response_body:
            self.__country_code = response_body['countryCode']
        if 'redirectUrl' in response_body:
            self.__redirect_url = response_body['redirectUrl']
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
