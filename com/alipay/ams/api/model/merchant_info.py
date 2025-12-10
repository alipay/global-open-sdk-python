import json
from com.alipay.ams.api.model.legal_entity_type import LegalEntityType
from com.alipay.ams.api.model.company import Company
from com.alipay.ams.api.model.business_info import BusinessInfo
from com.alipay.ams.api.model.entity_associations import EntityAssociations




class MerchantInfo:
    def __init__(self):
        
        self.__reference_merchant_id = None  # type: str
        self.__login_id = None  # type: str
        self.__legal_entity_type = None  # type: LegalEntityType
        self.__company = None  # type: Company
        self.__business_info = None  # type: BusinessInfo
        self.__entity_associations = None  # type: [EntityAssociations]
        

    @property
    def reference_merchant_id(self):
        """
        The unique ID that is assigned by the marketplace to identify the sub-merchant. referenceMerchantId that fails to register the sub-merchant can be used again.    More information:  Maximum length: 64 characters 
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value
    @property
    def login_id(self):
        """
        The sub-merchant&#39;s login ID to the marketplace platform. The value of this parameter is an email. The email that is successfully used to register with Alipay cannot be used again.    More information:  Maximum length: 64 characters
        """
        return self.__login_id

    @login_id.setter
    def login_id(self, value):
        self.__login_id = value
    @property
    def legal_entity_type(self):
        """Gets the legal_entity_type of this MerchantInfo.
        
        """
        return self.__legal_entity_type

    @legal_entity_type.setter
    def legal_entity_type(self, value):
        self.__legal_entity_type = value
    @property
    def company(self):
        """Gets the company of this MerchantInfo.
        
        """
        return self.__company

    @company.setter
    def company(self, value):
        self.__company = value
    @property
    def business_info(self):
        """Gets the business_info of this MerchantInfo.
        
        """
        return self.__business_info

    @business_info.setter
    def business_info(self, value):
        self.__business_info = value
    @property
    def entity_associations(self):
        """
        The list of legal entities that are associated with the sub-merchant. The information is used to verify the company&#39;s legal status and ensure the company complies with regulatory requirements.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is BR, AU, SG, HK, GB, MY, US, or belongs to the European Union.    More information:  Maximum size: 100 elements
        """
        return self.__entity_associations

    @entity_associations.setter
    def entity_associations(self, value):
        self.__entity_associations = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        if hasattr(self, "login_id") and self.login_id is not None:
            params['loginId'] = self.login_id
        if hasattr(self, "legal_entity_type") and self.legal_entity_type is not None:
            params['legalEntityType'] = self.legal_entity_type
        if hasattr(self, "company") and self.company is not None:
            params['company'] = self.company
        if hasattr(self, "business_info") and self.business_info is not None:
            params['businessInfo'] = self.business_info
        if hasattr(self, "entity_associations") and self.entity_associations is not None:
            params['entityAssociations'] = self.entity_associations
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
        if 'loginId' in response_body:
            self.__login_id = response_body['loginId']
        if 'legalEntityType' in response_body:
            legal_entity_type_temp = LegalEntityType.value_of(response_body['legalEntityType'])
            self.__legal_entity_type = legal_entity_type_temp
        if 'company' in response_body:
            self.__company = Company()
            self.__company.parse_rsp_body(response_body['company'])
        if 'businessInfo' in response_body:
            self.__business_info = BusinessInfo()
            self.__business_info.parse_rsp_body(response_body['businessInfo'])
        if 'entityAssociations' in response_body:
            self.__entity_associations = []
            for item in response_body['entityAssociations']:
                obj = EntityAssociations()
                obj.parse_rsp_body(item)
                self.__entity_associations.append(obj)
