import json




class BillingSubscriptionStatusChange:
    def __init__(self):
        
        self.__action = None  # type: str
        

    @property
    def action(self):
        """
        The subscription status change action. The currently supported value is PAUSE, which pauses payment collection and changes the subscription status from ACTIVE to PAUSED. To reactivate a paused subscription, call the resume subscription API. Maximum length: 10 characters.
        """
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "action") and self.action is not None:
            params['action'] = self.action
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'action' in response_body:
            self.__action = response_body['action']
