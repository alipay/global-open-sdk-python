import json
from com.alipay.ams.api.model.agentic_account_info_agent import AgenticAccountInfoAgent
from com.alipay.ams.api.model.agentic_account_info_env import AgenticAccountInfoEnv



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireAccountInfoRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireAccountInfoRequest, self).__init__("/ams/api/v1/agenticPayment/inquireAccountInfo") 

        self.__request_id = None  # type: str
        self.__user_login_id = None  # type: str
        self.__agent = None  # type: AgenticAccountInfoAgent
        self.__env = None  # type: AgenticAccountInfoEnv
        

    @property
    def request_id(self):
        """
        Unique identifier for each call, used for correlation, tracing and internal context mapping. Not an idempotency key or a mandate ID for subsequent Agentic Payment calls. Use a new requestId on retry.
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
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
        """Gets the agent of this AlipayInquireAccountInfoRequest.
        
        """
        return self.__agent

    @agent.setter
    def agent(self, value):
        self.__agent = value
    @property
    def env(self):
        """Gets the env of this AlipayInquireAccountInfoRequest.
        
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
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "user_login_id") and self.user_login_id is not None:
            params['userLoginId'] = self.user_login_id
        if hasattr(self, "agent") and self.agent is not None:
            params['agent'] = self.agent
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'userLoginId' in response_body:
            self.__user_login_id = response_body['userLoginId']
        if 'agent' in response_body:
            self.__agent = AgenticAccountInfoAgent()
            self.__agent.parse_rsp_body(response_body['agent'])
        if 'env' in response_body:
            self.__env = AgenticAccountInfoEnv()
            self.__env.parse_rsp_body(response_body['env'])
