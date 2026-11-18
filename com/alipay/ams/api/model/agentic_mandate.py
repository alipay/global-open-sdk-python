import json
from com.alipay.ams.api.model.agentic_mandate_intent import AgenticMandateIntent
from com.alipay.ams.api.model.order import Order




class AgenticMandate:
    def __init__(self):
        
        self.__mandate_id = None  # type: str
        self.__intent = None  # type: AgenticMandateIntent
        self.__order = None  # type: Order
        

    @property
    def mandate_id(self):
        """
        CreateBindingSession: Caller-provided Antom mandate identifier. Required when authorizeOnBind&#x3D;true and reused unchanged by inquirePaymentToken. Forbidden when authorizeOnBind&#x3D;false. Not a channel mandate ID or an idempotency key. CreateAuthenticationSession: Non-empty caller-generated Antom mandate handle, unique within merchant, userId and agent.agentId scope. Reuse unchanged in inquirePaymentToken. Not a channel mandate ID or request idempotency key. Required for createAuthenticationSession; use the createBindingSession parameter table for that session scenario.
        """
        return self.__mandate_id

    @mandate_id.setter
    def mandate_id(self, value):
        self.__mandate_id = value
    @property
    def intent(self):
        """Gets the intent of this AgenticMandate.
        
        """
        return self.__intent

    @intent.setter
    def intent(self, value):
        self.__intent = value
    @property
    def order(self):
        """Gets the order of this AgenticMandate.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "mandate_id") and self.mandate_id is not None:
            params['mandateId'] = self.mandate_id
        if hasattr(self, "intent") and self.intent is not None:
            params['intent'] = self.intent
        if hasattr(self, "order") and self.order is not None:
            params['order'] = self.order
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'mandateId' in response_body:
            self.__mandate_id = response_body['mandateId']
        if 'intent' in response_body:
            self.__intent = AgenticMandateIntent()
            self.__intent.parse_rsp_body(response_body['intent'])
        if 'order' in response_body:
            self.__order = Order()
            self.__order.parse_rsp_body(response_body['order'])
