import json




class AuthorizationConsultPassBackParams:
    def __init__(self):
        
        self.__subscription_id = None  # type: str
        self.__item_id = None  # type: str
        

    @property
    def subscription_id(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. The actual international subscription ID. Do not substitute authState, a payment order ID or a placeholder.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def item_id(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. The actual subscription item ID belonging to subscriptionId.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
