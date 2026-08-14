import json




class EventMerchantInfo:
    def __init__(self):
        
        self.__name = None  # type: str
        self.__region = None  # type: str
        self.__mcc = None  # type: str
        

    @property
    def name(self):
        """
        The merchant name. Returned when available.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def region(self):
        """
        The merchant country as an ISO 3166-1 alpha-2 code. Returned when available.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def mcc(self):
        """
        The Merchant Category Code that follows ISO 18245. Returned when available.
        """
        return self.__mcc

    @mcc.setter
    def mcc(self, value):
        self.__mcc = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "mcc") and self.mcc is not None:
            params['mcc'] = self.mcc
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'mcc' in response_body:
            self.__mcc = response_body['mcc']
