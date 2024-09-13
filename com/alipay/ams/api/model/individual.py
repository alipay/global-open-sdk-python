from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.contact import Contact
from com.alipay.ams.api.model.user_name import UserName


class Individual:
    def __int__(self):
        self.__name = None #type: UserName
        self.__english_name = None #type: UserName
        self.__dateOf_birth = None
        self.__placeOf_birth = None #type: Address
        self.__certificates = None #type: list[Certificate]
        self.__nationality = None
        self.__contacts = None #type: list[Contact]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def english_name(self):
        return self.__english_name

    @english_name.setter
    def english_name(self, value):
        self.__english_name = value

    @property
    def dateOf_birth(self):
        return self.__dateOf_birth

    @dateOf_birth.setter
    def dateOf_birth(self, value):
        self.__dateOf_birth = value

    @property
    def placeOf_birth(self):
        return self.__placeOf_birth

    @placeOf_birth.setter
    def placeOf_birth(self, value):
        self.__placeOf_birth = value

    @property
    def certificates(self):
        return self.__certificates

    @certificates.setter
    def certificates(self, value):
        self.__certificates = value

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, value):
        self.__nationality = value

    @property
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'name') and self.name:
            params['name'] = self.name.to_ams_dict()
        if hasattr(self, 'english_name') and self.english_name:
            params['englishName'] = self.english_name.to_ams_dict()
        if hasattr(self, 'dateOf_birth') and self.dateOf_birth:
            params['dateOfBirth'] = self.dateOf_birth
        if hasattr(self, 'placeOf_birth') and self.placeOf_birth:
            params['placeOfBirth'] = self.placeOf_birth.to_ams_dict()
        if hasattr(self, 'certificates') and self.certificates:
            certificates_list = list()
            for d in self.certificates:
                certificates_list.append(d.to_ams_dict())
            params['certificates'] = certificates_list
        if hasattr(self, 'nationality') and self.nationality:
            params['nationality'] = self.nationality
        if hasattr(self, 'contacts') and self.contacts:
            contacts_list = list()
            for d in self.contacts:
                contacts_list.append(d.to_ams_dict())
                params['contacts'] = contacts_list
        return params