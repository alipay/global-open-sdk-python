import json




class RiskOrder:
    def __init__(self):
        
        self.__order_type = None  # type: str
        self.__referring_site = None  # type: str
        

    @property
    def order_type(self):
        """
        The order type
        """
        return self.__order_type

    @order_type.setter
    def order_type(self, value):
        self.__order_type = value
    @property
    def referring_site(self):
        """
        The webpage where the buyer accessed the merchant.
        """
        return self.__referring_site

    @referring_site.setter
    def referring_site(self, value):
        self.__referring_site = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "order_type") and self.order_type is not None:
            params['orderType'] = self.order_type
        if hasattr(self, "referring_site") and self.referring_site is not None:
            params['referringSite'] = self.referring_site
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'orderType' in response_body:
            self.__order_type = response_body['orderType']
        if 'referringSite' in response_body:
            self.__referring_site = response_body['referringSite']
