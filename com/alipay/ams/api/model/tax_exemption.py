import json
from com.alipay.ams.api.model.tax_exemption_jurisdiction import TaxExemptionJurisdiction




class TaxExemption:
    def __init__(self):
        
        self.__certificate_number = None  # type: str
        self.__exemption_type = None  # type: str
        self.__jurisdiction = None  # type: TaxExemptionJurisdiction
        

    @property
    def certificate_number(self):
        """
        The tax exemption certificate number. Maximum length: 64 characters.
        """
        return self.__certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self.__certificate_number = value
    @property
    def exemption_type(self):
        """
        The tax exemption type. Currently supported value: RESALE. Maximum length: 32 characters.
        """
        return self.__exemption_type

    @exemption_type.setter
    def exemption_type(self, value):
        self.__exemption_type = value
    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this TaxExemption.
        
        """
        return self.__jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, value):
        self.__jurisdiction = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "certificate_number") and self.certificate_number is not None:
            params['certificateNumber'] = self.certificate_number
        if hasattr(self, "exemption_type") and self.exemption_type is not None:
            params['exemptionType'] = self.exemption_type
        if hasattr(self, "jurisdiction") and self.jurisdiction is not None:
            params['jurisdiction'] = self.jurisdiction
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'certificateNumber' in response_body:
            self.__certificate_number = response_body['certificateNumber']
        if 'exemptionType' in response_body:
            self.__exemption_type = response_body['exemptionType']
        if 'jurisdiction' in response_body:
            self.__jurisdiction = TaxExemptionJurisdiction()
            self.__jurisdiction.parse_rsp_body(response_body['jurisdiction'])
