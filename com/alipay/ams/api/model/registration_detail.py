from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.attachment import Attachment
from com.alipay.ams.api.model.contact_info import ContactInfo


class RegistrationDetail(object):
    def __init__(self):
        self.__legal_name = None
        self.__attachments = None  # type: list[Attachment]
        self.__contact_info = None  # type: ContactInfo
        self.__registration_type = None
        self.__registration_no = None
        self.__registration_address = None  # type: Address
        self.__business_type = None
        self.__registration_effective_date = None
        self.__registration_expire_date = None

    @property
    def legal_name(self):
        return self.__legal_name

    @legal_name.setter
    def legal_name(self, value):
        self.__legal_name = value

    @property
    def attachments(self):
        return self.__attachments

    @attachments.setter
    def attachments(self, value):
        self.__attachments = value

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        self.__contact_info = value

    @property
    def registration_type(self):
        return self.__registration_type

    @registration_type.setter
    def registration_type(self, value):
        self.__registration_type = value

    @property
    def registration_no(self):
        return self.__registration_no

    @registration_no.setter
    def registration_no(self, value):
        self.__registration_no = value

    @property
    def registration_address(self):
        return self.__registration_address

    @registration_address.setter
    def registration_address(self, value):
        self.__registration_address = value

    @property
    def business_type(self):
        return self.__business_type

    @business_type.setter
    def business_type(self, value):
        self.__business_type = value

    @property
    def registration_effective_date(self):
        return self.__registration_effective_date

    @registration_effective_date.setter
    def registration_effective_date(self, value):
        self.__registration_effective_date = value

    @property
    def registration_expire_date(self):
        return self.__registration_expire_date

    @registration_expire_date.setter
    def registration_expire_date(self, value):
        self.__registration_expire_date = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "legal_name") and self.legal_name:
            params['legalName'] = self.legal_name

        if hasattr(self, "attachments") and self.attachments:
            params['attachments'] = self.attachments

        if hasattr(self, "contact_info") and self.contact_info:
            params['contactInfo'] = self.contact_info

        if hasattr(self, "registration_type") and self.registration_type:
            params['registrationType'] = self.registration_type

        if hasattr(self, "registration_no") and self.registration_no:
            params['registrationNo'] = self.registration_no

        if hasattr(self, "registration_address") and self.registration_address:
            params['registrationAddress'] = self.registration_address

        if hasattr(self, "business_type") and self.business_type:
            params['businessType'] = self.business_type

        if hasattr(self, "registration_effective_date") and self.registration_effective_date:
            params['registrationEffectiveDate'] = self.registration_effective_date

        if hasattr(self, "registration_expire_date") and self.registration_expire_date:
            params['registrationExpireDate'] = self.registration_expire_date

        return params
