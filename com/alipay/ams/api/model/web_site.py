import json




class WebSite:
    def __init__(self):
        
        self.__name = None  # type: str
        self.__url = None  # type: str
        self.__desc = None  # type: str
        self.__type = None  # type: str
        

    @property
    def name(self):
        """Gets the name of this WebSite.
        
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def url(self):
        """
        The URL of the merchant website.    More information:  Maximum length: 2048 characters
        """
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
    @property
    def desc(self):
        """Gets the desc of this WebSite.
        
        """
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = value
    @property
    def type(self):
        """
        Website type. Valid values are:  COMPANY_INTRODUCE: the website that introduces company information. Specify websites.type as COMPANY_INTRODUCE when the value of paymentMethodType is TRUEMONEY. TRADING: the trading website. The same applies when the value is empty or you do not specify this parameter. More information:  Maximum length: 32 characters
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "url") and self.url is not None:
            params['url'] = self.url
        if hasattr(self, "desc") and self.desc is not None:
            params['desc'] = self.desc
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'url' in response_body:
            self.__url = response_body['url']
        if 'desc' in response_body:
            self.__desc = response_body['desc']
        if 'type' in response_body:
            self.__type = response_body['type']
