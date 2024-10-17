from com.alipay.ams.api.model.companyType import CompanyType
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.attachment import Attachment
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.company_unit_type import CompanyUnitType
from com.alipay.ams.api.model.contact import Contact
from com.alipay.ams.api.model.stock_info import StockInfo


class Company:
    def __init__(self):
        self.__legal_name = None
        self.__company_type = None #type:CompanyType
        self.__registered_address = None #type:Address
        self.__operating_address = None #type:Address
        self.__incorporation_date = None
        self.__stock_info = None #type:StockInfo
        self.__certificates = None #type:Certificate
        self.__attachments = None #type: list[Attachment]
        self.__company_unit = None #type: CompanyUnitType
        self.__contacts = None #type: list[Contact]
        self.__vatNo = None

    @property
    def legal_name(self):
        return self.__legal_name

    @legal_name.setter
    def legal_name(self, value):
        self.__legal_name = value

    @property
    def company_type(self):
        return self.__company_type

    @company_type.setter
    def company_type(self, value):
        self.__company_type = value

    @property
    def registered_address(self):
        return self.__registered_address

    @registered_address.setter
    def registered_address(self, value):
        self.__registered_address = value

    @property
    def operating_address(self):
        return self.__operating_address

    @operating_address.setter
    def operating_address(self, value):
        self.__operating_address = value

    @property
    def incorporation_date(self):
        return self.__incorporation_date

    @incorporation_date.setter
    def incorporation_date(self, value):
        self.__incorporation_date = value

    @property
    def stock_info(self):
        return self.__stock_info

    @stock_info.setter
    def stock_info(self, value):
        self.__stock_info = value

    @property
    def certificates(self):
        return self.__certificates

    @certificates.setter
    def certificates(self, value):
        self.__certificates = value

    @property
    def attachments(self):
        return self.__attachments

    @attachments.setter
    def attachments(self, value):
        self.__attachments = value

    @property
    def company_unit(self):
        return self.__company_unit

    @company_unit.setter
    def company_unit(self, value):
        self.__company_unit = value

    @property
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value

    @property
    def vatNo(self):
        return self.__vatNo
    @vatNo.setter
    def vatNo(self, value):
        self.__vatNo = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'legal_name') and self.legal_name:
            params['legalName'] = self.legal_name
        if hasattr(self, 'company_type') and self.company_type:
            params['companyType'] = self.company_type.value
        if hasattr(self, 'registered_address') and self.registered_address:
            params['registeredAddress'] = self.registered_address.to_ams_dict()
        if hasattr(self, 'operating_address') and self.operating_address:
            params['operatingAddress'] = self.operating_address.to_ams_dict()
        if hasattr(self, 'incorporation_date') and self.incorporation_date:
            params['incorporationDate'] = self.incorporation_date
        if hasattr(self, 'stock_info') and self.stock_info:
            params['stockInfo'] = self.stock_info.to_ams_dict()
        if hasattr(self, 'certificates') and self.certificates:
            params['certificates'] = self.certificates
        if hasattr(self, 'attachments') and self.attachments:
            params['attachments'] = self.attachments
            for i in range(len(self.attachments)):
                params['attachments'][i] = self.attachments[i].to_ams_dict()
            params['attachments'] = params['attachments']
        if hasattr(self, 'company_unit') and self.company_unit:
            params['companyUnit'] = self.company_unit.value
        if hasattr(self, 'contacts') and self.contacts:
            params['contacts'] = self.contacts
            for i in range(len(self.contacts)):
                params['contacts'][i] = self.contacts[i].to_ams_dict()
            params['contacts'] = params['contacts']
        if hasattr(self, 'vatNo') and self.vatNo:
            params['vatNo'] = self.vatNo
        return params
