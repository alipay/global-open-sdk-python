import json




class AgenticAccountInfoAgent:
    def __init__(self):
        
        self.__agent_id = None  # type: str
        

    @property
    def agent_id(self):
        """
        Stable business identifier of the current Agent. Together with the authenticated merchant and userId, it scopes the asset query. Must not be empty.
        """
        return self.__agent_id

    @agent_id.setter
    def agent_id(self, value):
        self.__agent_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "agent_id") and self.agent_id is not None:
            params['agentId'] = self.agent_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'agentId' in response_body:
            self.__agent_id = response_body['agentId']
