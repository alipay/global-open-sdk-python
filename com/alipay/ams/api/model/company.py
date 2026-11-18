import json
from com.alipay.ams.api.model.company_type import CompanyType
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.stock_info import StockInfo
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.attachment import Attachment
from com.alipay.ams.api.model.company_unit_type import CompanyUnitType
from com.alipay.ams.api.model.contact import Contact




class Company:
    def __init__(self):
        
        self.__legal_name = None  # type: str
        self.__company_type = None  # type: CompanyType
        self.__registered_address = None  # type: Address
        self.__operating_address = None  # type: Address
        self.__incorporation_date = None  # type: str
        self.__stock_info = None  # type: StockInfo
        self.__certificates = None  # type: Certificate
        self.__attachments = None  # type: [Attachment]
        self.__company_unit = None  # type: CompanyUnitType
        self.__contacts = None  # type: [Contact]
        self.__vat_no = None  # type: str
        

    @property
    def legal_name(self):
        """
        The legal name of the company.    More information:  Maximum size: 256 elements 
        """
        return self.__legal_name

    @legal_name.setter
    def legal_name(self, value):
        self.__legal_name = value
    @property
    def company_type(self):
        """Gets the company_type of this Company.
        
        """
        return self.__company_type

    @company_type.setter
    def company_type(self, value):
        self.__company_type = value
    @property
    def registered_address(self):
        """Gets the registered_address of this Company.
        
        """
        return self.__registered_address

    @registered_address.setter
    def registered_address(self, value):
        self.__registered_address = value
    @property
    def operating_address(self):
        """Gets the operating_address of this Company.
        
        """
        return self.__operating_address

    @operating_address.setter
    def operating_address(self, value):
        self.__operating_address = value
    @property
    def incorporation_date(self):
        """
        The date when the company was officially registered and incorporated with the government. The value of this parameter is in the format of YYYY-MM-DD, such as 2023-06-25.    Specify this parameter when the value of merchantInfo.company.registeredAddress.region is AU, SG, HK, US, GB, MY, or the company&#39;s registered region belongs to the European Union.   More information:  Maximum length: 32 characters
        """
        return self.__incorporation_date

    @incorporation_date.setter
    def incorporation_date(self, value):
        self.__incorporation_date = value
    @property
    def stock_info(self):
        """Gets the stock_info of this Company.
        
        """
        return self.__stock_info

    @stock_info.setter
    def stock_info(self, value):
        self.__stock_info = value
    @property
    def certificates(self):
        """Gets the certificates of this Company.
        
        """
        return self.__certificates

    @certificates.setter
    def certificates(self, value):
        self.__certificates = value
    @property
    def attachments(self):
        """
        The list of attachment information. The information is used to verify the company&#39;s legal status and ensure the company complies with regulatory requirements.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is BR, AU, SG, HK, GB, MY, or belongs to the European Union.    More information:  Maximum size: 10 elements
        """
        return self.__attachments

    @attachments.setter
    def attachments(self, value):
        self.__attachments = value
    @property
    def company_unit(self):
        """Gets the company_unit of this Company.
        
        """
        return self.__company_unit

    @company_unit.setter
    def company_unit(self, value):
        self.__company_unit = value
    @property
    def contacts(self):
        """
        A list of contact information.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is JP. 
        """
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value
    @property
    def vat_no(self):
        """
        The Value Added Tax (VAT) number of the company.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is GB or the company&#39;s registered region belongs to the European Union.    More information:  Maximum length: 64 characters 
        """
        return self.__vat_no

    @vat_no.setter
    def vat_no(self, value):
        self.__vat_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "legal_name") and self.legal_name is not None:
            params['legalName'] = self.legal_name
        if hasattr(self, "company_type") and self.company_type is not None:
            params['companyType'] = self.company_type
        if hasattr(self, "registered_address") and self.registered_address is not None:
            params['registeredAddress'] = self.registered_address
        if hasattr(self, "operating_address") and self.operating_address is not None:
            params['operatingAddress'] = self.operating_address
        if hasattr(self, "incorporation_date") and self.incorporation_date is not None:
            params['incorporationDate'] = self.incorporation_date
        if hasattr(self, "stock_info") and self.stock_info is not None:
            params['stockInfo'] = self.stock_info
        if hasattr(self, "certificates") and self.certificates is not None:
            params['certificates'] = self.certificates
        if hasattr(self, "attachments") and self.attachments is not None:
            params['attachments'] = self.attachments
        if hasattr(self, "company_unit") and self.company_unit is not None:
            params['companyUnit'] = self.company_unit
        if hasattr(self, "contacts") and self.contacts is not None:
            params['contacts'] = self.contacts
        if hasattr(self, "vat_no") and self.vat_no is not None:
            params['vatNo'] = self.vat_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'legalName' in response_body:
            self.__legal_name = response_body['legalName']
        if 'companyType' in response_body:
            company_type_temp = CompanyType.value_of(response_body['companyType'])
            self.__company_type = company_type_temp
        if 'registeredAddress' in response_body:
            self.__registered_address = Address()
            self.__registered_address.parse_rsp_body(response_body['registeredAddress'])
        if 'operatingAddress' in response_body:
            self.__operating_address = Address()
            self.__operating_address.parse_rsp_body(response_body['operatingAddress'])
        if 'incorporationDate' in response_body:
            self.__incorporation_date = response_body['incorporationDate']
        if 'stockInfo' in response_body:
            self.__stock_info = StockInfo()
            self.__stock_info.parse_rsp_body(response_body['stockInfo'])
        if 'certificates' in response_body:
            self.__certificates = Certificate()
            self.__certificates.parse_rsp_body(response_body['certificates'])
        if 'attachments' in response_body:
            self.__attachments = []
            for item in response_body['attachments']:
                obj = Attachment()
                obj.parse_rsp_body(item)
                self.__attachments.append(obj)
        if 'companyUnit' in response_body:
            company_unit_temp = CompanyUnitType.value_of(response_body['companyUnit'])
            self.__company_unit = company_unit_temp
        if 'contacts' in response_body:
            self.__contacts = []
            for item in response_body['contacts']:
                obj = Contact()
                obj.parse_rsp_body(item)
                self.__contacts.append(obj)
        if 'vatNo' in response_body:
            self.__vat_no = response_body['vatNo']
