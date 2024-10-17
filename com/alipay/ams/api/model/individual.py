from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.contact import Contact
from com.alipay.ams.api.model.user_name import UserName


class Individual:

    def __init__(self):
        self.__name = None #type: UserName
        self.__english_name = None #type: UserName
        self.__date_of_birth = None
        self.__place_of_birth = None #type: Address
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
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def place_of_birth(self):
        return self.__place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, value):
        self.__place_of_birth = value

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
        if hasattr(self, 'date_of_birth') and self.date_of_birth:
            params['dateOfBirth'] = self.date_of_birth
        if hasattr(self, 'place_of_birth') and self.place_of_birth:
            params['placeOfBirth'] = self.place_of_birth.to_ams_dict()
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