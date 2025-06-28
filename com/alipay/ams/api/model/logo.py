import json




class Logo:
    def __init__(self):
        
        self.__logo_name = None  # type: str
        self.__logo_url = None  # type: str
        

    @property
    def logo_name(self):
        """
        The logo name of the card brand. See the Card brands to check the valid values.   More information:  Maximum length: 12 characters
        """
        return self.__logo_name

    @logo_name.setter
    def logo_name(self, value):
        self.__logo_name = value
    @property
    def logo_url(self):
        """
        The logo URL of the card brand.    More information:  Maximum length: 2048 characters
        """
        return self.__logo_url

    @logo_url.setter
    def logo_url(self, value):
        self.__logo_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "logo_name") and self.logo_name is not None:
            params['logoName'] = self.logo_name
        if hasattr(self, "logo_url") and self.logo_url is not None:
            params['logoUrl'] = self.logo_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'logoName' in response_body:
            self.__logo_name = response_body['logoName']
        if 'logoUrl' in response_body:
            self.__logo_url = response_body['logoUrl']
