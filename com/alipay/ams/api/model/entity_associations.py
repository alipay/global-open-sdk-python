from com.alipay.ams.api.model.association_type import AssociationType
from com.alipay.ams.api.model.company import Company
from com.alipay.ams.api.model.individual import Individual
from com.alipay.ams.api.model.legal_entity_type import LegalEntityType


class EntityAssociations:
    def __init__(self):
        self.__association_type = None #type: AssociationType
        self.__legal_entity_type = None #type: LegalEntityType
        self.__company = None #type: Company
        self.__individual = None #type: Individual
        self.__shareholding_ratio = None

    @property
    def association_type(self):
        return self.__association_type

    @association_type.setter
    def association_type(self, value):
        self.__association_type = value

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
    def individual(self):
        return self.__individual

    @individual.setter
    def individual(self, value):
        self.__individual = value

    @property
    def shareholding_ratio(self):
        return self.__shareholding_ratio

    @shareholding_ratio.setter
    def shareholding_ratio(self, value):
        self.__shareholding_ratio = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'association_type') and self.association_type:
            params['associationType'] = self.association_type.value
        if hasattr(self, 'legal_entity_type') and self.legal_entity_type:
            params['legalEntityType'] = self.legal_entity_type.value
        if hasattr(self, 'company') and self.company:
            params['company'] = self.company.to_ams_dict()
        if hasattr(self, 'individual') and self.individual:
            params['individual'] = self.individual.to_ams_dict()
        if hasattr(self, 'shareholding_ratio') and self.shareholding_ratio:
            params['shareholdingRatio'] = self.shareholding_ratio
        return params
