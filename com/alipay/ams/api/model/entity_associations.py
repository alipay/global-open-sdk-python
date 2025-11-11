import json
from com.alipay.ams.api.model.association_type import AssociationType
from com.alipay.ams.api.model.legal_entity_type import LegalEntityType
from com.alipay.ams.api.model.company import Company
from com.alipay.ams.api.model.individual import Individual




class EntityAssociations:
    def __init__(self):
        
        self.__association_type = None  # type: AssociationType
        self.__legal_entity_type = None  # type: LegalEntityType
        self.__company = None  # type: Company
        self.__individual = None  # type: Individual
        self.__shareholding_ratio = None  # type: str
        

    @property
    def association_type(self):
        """Gets the association_type of this EntityAssociations.
        
        """
        return self.__association_type

    @association_type.setter
    def association_type(self, value):
        self.__association_type = value
    @property
    def legal_entity_type(self):
        """Gets the legal_entity_type of this EntityAssociations.
        
        """
        return self.__legal_entity_type

    @legal_entity_type.setter
    def legal_entity_type(self, value):
        self.__legal_entity_type = value
    @property
    def company(self):
        """Gets the company of this EntityAssociations.
        
        """
        return self.__company

    @company.setter
    def company(self, value):
        self.__company = value
    @property
    def individual(self):
        """Gets the individual of this EntityAssociations.
        
        """
        return self.__individual

    @individual.setter
    def individual(self, value):
        self.__individual = value
    @property
    def shareholding_ratio(self):
        """
        The shareholding ratio of the associated legal entity. The value of this parameter is from 0 to 100. For example, 10.5 represents that the shareholding ratio is 10.5%. The information is used to verify the company&#39;s legal status and ensure the company complies with regulatory requirements.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is BR, AU, SG, HK, US, GB, MY, or the company&#39;s registered region belongs to the European Union.    More information:  Maximum length: 16 characters
        """
        return self.__shareholding_ratio

    @shareholding_ratio.setter
    def shareholding_ratio(self, value):
        self.__shareholding_ratio = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "association_type") and self.association_type is not None:
            params['associationType'] = self.association_type
        if hasattr(self, "legal_entity_type") and self.legal_entity_type is not None:
            params['legalEntityType'] = self.legal_entity_type
        if hasattr(self, "company") and self.company is not None:
            params['company'] = self.company
        if hasattr(self, "individual") and self.individual is not None:
            params['individual'] = self.individual
        if hasattr(self, "shareholding_ratio") and self.shareholding_ratio is not None:
            params['shareholdingRatio'] = self.shareholding_ratio
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'associationType' in response_body:
            association_type_temp = AssociationType.value_of(response_body['associationType'])
            self.__association_type = association_type_temp
        if 'legalEntityType' in response_body:
            legal_entity_type_temp = LegalEntityType.value_of(response_body['legalEntityType'])
            self.__legal_entity_type = legal_entity_type_temp
        if 'company' in response_body:
            self.__company = Company()
            self.__company.parse_rsp_body(response_body['company'])
        if 'individual' in response_body:
            self.__individual = Individual()
            self.__individual.parse_rsp_body(response_body['individual'])
        if 'shareholdingRatio' in response_body:
            self.__shareholding_ratio = response_body['shareholdingRatio']
