from com.alipay.ams.api.model.business_info import BusinessInfo
from com.alipay.ams.api.model.company import Company
from com.alipay.ams.api.model.entity_associations import EntityAssociations
from com.alipay.ams.api.model.legal_entity_type import LegalEntityType


class MerchantInfo:
    def __init__(self):
        self.__reference_merchant_id = None
        self.__login_id = None
        self.__legal_entity_type = None # type: LegalEntityType
        self.__company = None # type: Company
        self.__business_info = None # type: BusinessInfo
        self.__entity_associations = None # type: list[EntityAssociations]

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def login_id(self):
        return self.__login_id

    @login_id.setter
    def login_id(self, value):
        self.__login_id = value

    @property
    def legal_entity_type(self):
        return self.__legal_entity_type

    @legal_entity_type.setter
    def legal_entity_type(self, value):
        self.__legal_entity_type = value

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        self.__company = value

    @property
    def business_info(self):
        return self.__business_info

    @business_info.setter
    def business_info(self, value):
        self.__business_info = value

    @property
    def entity_associations(self):
        return self.__entity_associations

    @entity_associations.setter
    def entity_associations(self, value):
        self.__entity_associations = value

    def to_ams_dict(self):
        params = dict()
        if  hasattr(self, 'reference_merchant_id') and self.reference_merchant_id:
            params['referenceMerchantId'] = self.reference_merchant_id
        if  hasattr(self, 'login_id') and self.login_id:
            params['loginId'] = self.login_id
        if  hasattr(self, 'legal_entity_type') and self.legal_entity_type:
            params['legalEntityType'] = self.legal_entity_type.value
        if  hasattr(self, 'company') and self.company:
            params['company'] = self.company.to_ams_dict()
        if  hasattr(self, 'business_info') and self.business_info:
            params['businessInfo'] = self.business_info.to_ams_dict()
        if  hasattr(self, 'entity_associations') and self.entity_associations:
            params['entityAssociations'] = [entity_association.to_ams_dict() for entity_association in self.entity_associations]

        return params