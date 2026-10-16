import json
from com.alipay.ams.api.model.agentic_payment_token_agent import AgenticPaymentTokenAgent
from com.alipay.ams.api.model.agentic_payment_method import AgenticPaymentMethod
from com.alipay.ams.api.model.agentic_payment_token_order import AgenticPaymentTokenOrder



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquirePaymentTokenRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquirePaymentTokenRequest, self).__init__("/ams/api/v1/agenticPayment/inquirePaymentToken") 

        self.__payment_token_request_id = None  # type: str
        self.__user_login_id = None  # type: str
        self.__agent = None  # type: AgenticPaymentTokenAgent
        self.__payment_method = None  # type: AgenticPaymentMethod
        self.__mandate_id = None  # type: str
        self.__metadata = None  # type: str
        self.__order = None  # type: AgenticPaymentTokenOrder
        

    @property
    def payment_token_request_id(self):
        """
        Authorization-context correlation identifier. Normally reuse createAuthenticationSession.authenticationRequestId. For A+ bind-and-authorize and CARD + MASTERCARD + authorizeOnBind&#x3D;true + IMMEDIATE, reuse createBindingSession.bindingRequestId and do not call createAuthenticationSession again for that authorization. No idempotency guarantee. mandateId continues to identify the Antom authorization context.
        """
        return self.__payment_token_request_id

    @payment_token_request_id.setter
    def payment_token_request_id(self, value):
        self.__payment_token_request_id = value
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
        """Gets the agent of this AlipayInquirePaymentTokenRequest.
        
        """
        return self.__agent

    @agent.setter
    def agent(self, value):
        self.__agent = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayInquirePaymentTokenRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def mandate_id(self):
        """
        Antom mandate handle paired with paymentMethodId. Reuse the mandateId from the preceding authentication or bind-and-authorize request unchanged. Not a channel mandate ID or an idempotency key.
        """
        return self.__mandate_id

    @mandate_id.setter
    def mandate_id(self, value):
        self.__mandate_id = value
    @property
    def metadata(self):
        """
        String metadata. The request parameter table specifies the L2 mandate hash (sdHash) for Mastercard IMMEDIATE and AUTONOMOUS, taken unchanged from the successful authentication session or the matching Mastercard IMMEDIATE binding session. Mastercard AUTONOMOUS also requires the complete Agent-signed L3 mandate (serializedMandate). Keep it associated with the same authorization context; do not parse or rewrite it. The public table does not specify the internal encoding of these contents. No additional top-level sdHash or serializedMandate field is defined.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def order(self):
        """Gets the order of this AlipayInquirePaymentTokenRequest.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_token_request_id") and self.payment_token_request_id is not None:
            params['paymentTokenRequestId'] = self.payment_token_request_id
        if hasattr(self, "user_login_id") and self.user_login_id is not None:
            params['userLoginId'] = self.user_login_id
        if hasattr(self, "agent") and self.agent is not None:
            params['agent'] = self.agent
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "mandate_id") and self.mandate_id is not None:
            params['mandateId'] = self.mandate_id
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "order") and self.order is not None:
            params['order'] = self.order
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentTokenRequestId' in response_body:
            self.__payment_token_request_id = response_body['paymentTokenRequestId']
        if 'userLoginId' in response_body:
            self.__user_login_id = response_body['userLoginId']
        if 'agent' in response_body:
            self.__agent = AgenticPaymentTokenAgent()
            self.__agent.parse_rsp_body(response_body['agent'])
        if 'paymentMethod' in response_body:
            self.__payment_method = AgenticPaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'mandateId' in response_body:
            self.__mandate_id = response_body['mandateId']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'order' in response_body:
            self.__order = AgenticPaymentTokenOrder()
            self.__order.parse_rsp_body(response_body['order'])
