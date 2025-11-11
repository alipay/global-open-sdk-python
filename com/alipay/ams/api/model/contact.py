import json
from com.alipay.ams.api.model.contact_type import ContactType




class Contact:
    def __init__(self):
        
        self.__type = None  # type: ContactType
        self.__info = None  # type: str
        self.__home = None  # type: str
        self.__work = None  # type: str
        self.__mobile = None  # type: str
        

    @property
    def type(self):
        """Gets the type of this Contact.
        
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def info(self):
        """
        The contact details of a specific contact type.    More information:  Maximum length: 256 characters
        """
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = value
    @property
    def home(self):
        """Gets the home of this Contact.
        
        """
        return self.__home

    @home.setter
    def home(self, value):
        self.__home = value
    @property
    def work(self):
        """Gets the work of this Contact.
        
        """
        return self.__work

    @work.setter
    def work(self, value):
        self.__work = value
    @property
    def mobile(self):
        """Gets the mobile of this Contact.
        
        """
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        self.__mobile = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "info") and self.info is not None:
            params['info'] = self.info
        if hasattr(self, "home") and self.home is not None:
            params['home'] = self.home
        if hasattr(self, "work") and self.work is not None:
            params['work'] = self.work
        if hasattr(self, "mobile") and self.mobile is not None:
            params['mobile'] = self.mobile
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'type' in response_body:
            type_temp = ContactType.value_of(response_body['type'])
            self.__type = type_temp
        if 'info' in response_body:
            self.__info = response_body['info']
        if 'home' in response_body:
            self.__home = response_body['home']
        if 'work' in response_body:
            self.__work = response_body['work']
        if 'mobile' in response_body:
            self.__mobile = response_body['mobile']
