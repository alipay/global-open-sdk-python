import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.contact import Contact




class Individual:
    def __init__(self):
        
        self.__name = None  # type: UserName
        self.__english_name = None  # type: UserName
        self.__date_of_birth = None  # type: str
        self.__place_of_birth = None  # type: Address
        self.__certificates = None  # type: Certificate
        self.__nationality = None  # type: str
        self.__contacts = None  # type: [Contact]
        

    @property
    def name(self):
        """Gets the name of this Individual.
        
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def english_name(self):
        """Gets the english_name of this Individual.
        
        """
        return self.__english_name

    @english_name.setter
    def english_name(self, value):
        self.__english_name = value
    @property
    def date_of_birth(self):
        """
        The individual&#39;s date of birth. The information is used to verify the company&#39;s legal status and ensure the company complies with regulatory requirements.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is BR.    More information:  Maximum length: 32 characters 
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value
    @property
    def place_of_birth(self):
        """Gets the place_of_birth of this Individual.
        
        """
        return self.__place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, value):
        self.__place_of_birth = value
    @property
    def certificates(self):
        """Gets the certificates of this Individual.
        
        """
        return self.__certificates

    @certificates.setter
    def certificates(self, value):
        self.__certificates = value
    @property
    def nationality(self):
        """
        The nationality of the individual. The value of this parameter is a 2-letter country or region code based on the ISO 3166 Country Codes standard.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is EU, GB, MY, US, or BR.    More information:  Maximum length: 2 characters
        """
        return self.__nationality

    @nationality.setter
    def nationality(self, value):
        self.__nationality = value
    @property
    def contacts(self):
        """
        A list of contact information.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is JP and the value of merchantInfo.entityAssociations.associationType is LEGAL_REPRESENTATIVE.    More information:  Maximum size: 10 elements
        """
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "english_name") and self.english_name is not None:
            params['englishName'] = self.english_name
        if hasattr(self, "date_of_birth") and self.date_of_birth is not None:
            params['dateOfBirth'] = self.date_of_birth
        if hasattr(self, "place_of_birth") and self.place_of_birth is not None:
            params['placeOfBirth'] = self.place_of_birth
        if hasattr(self, "certificates") and self.certificates is not None:
            params['certificates'] = self.certificates
        if hasattr(self, "nationality") and self.nationality is not None:
            params['nationality'] = self.nationality
        if hasattr(self, "contacts") and self.contacts is not None:
            params['contacts'] = self.contacts
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'name' in response_body:
            self.__name = UserName()
            self.__name.parse_rsp_body(response_body['name'])
        if 'englishName' in response_body:
            self.__english_name = UserName()
            self.__english_name.parse_rsp_body(response_body['englishName'])
        if 'dateOfBirth' in response_body:
            self.__date_of_birth = response_body['dateOfBirth']
        if 'placeOfBirth' in response_body:
            self.__place_of_birth = Address()
            self.__place_of_birth.parse_rsp_body(response_body['placeOfBirth'])
        if 'certificates' in response_body:
            self.__certificates = Certificate()
            self.__certificates.parse_rsp_body(response_body['certificates'])
        if 'nationality' in response_body:
            self.__nationality = response_body['nationality']
        if 'contacts' in response_body:
            self.__contacts = []
            for item in response_body['contacts']:
                obj = Contact()
                obj.parse_rsp_body(item)
                self.__contacts.append(obj)
