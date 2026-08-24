import json
from com.alipay.ams.api.model.tax_jurisdiction import TaxJurisdiction



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxRegisterRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxRegisterRequest, self).__init__("/ams/api/v1/tax/register") 

        self.__registration_request_id = None  # type: str
        self.__tax_type = None  # type: str
        self.__jurisdiction = None  # type: TaxJurisdiction
        self.__registration_type = None  # type: str
        self.__tax_id = None  # type: str
        self.__active_from = None  # type: str
        self.__expire_at = None  # type: str
        

    @property
    def registration_request_id(self):
        """
        The unique ID assigned by a merchant to identify a tax registration request. Once accepted, the ID is permanently occupied and any subsequent request using it returns REPEATED_SUBMIT. Maximum length: 64 characters.
        """
        return self.__registration_request_id

    @registration_request_id.setter
    def registration_request_id(self, value):
        self.__registration_request_id = value
    @property
    def tax_type(self):
        """
        The tax type. Supported values include CUIT, GST, VAT, CBS, IBS, HST, PST, RST, QST, JCT, SERVICE_TAX, IGV, SALES_TAX, and PERSONAL_PROPERTY_LEASE_TRANSACTION_TAX.
        """
        return self.__tax_type

    @tax_type.setter
    def tax_type(self, value):
        self.__tax_type = value
    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this AlipayTaxRegisterRequest.
        
        """
        return self.__jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, value):
        self.__jurisdiction = value
    @property
    def registration_type(self):
        """
        The tax registration type. Supported values are OSS_NON_UNION, STANDARD_LOCAL_TAX, SINGLE_LOCAL_USE_TAX_RATE, SIMPLIFIED_SELLERS_USE_TAX, STANDARD_SALES_AND_USE_TAX, NORMAL_GST_HST, and SIMPLIFIED_GST_HST. Maximum length: 32 characters.
        """
        return self.__registration_type

    @registration_type.setter
    def registration_type(self, value):
        self.__registration_type = value
    @property
    def tax_id(self):
        """
        The tax ID. Maximum length: 64 characters.
        """
        return self.__tax_id

    @tax_id.setter
    def tax_id(self, value):
        self.__tax_id = value
    @property
    def active_from(self):
        """
        The time from which the tax registration is active. Maximum length: 32 characters.
        """
        return self.__active_from

    @active_from.setter
    def active_from(self, value):
        self.__active_from = value
    @property
    def expire_at(self):
        """
        The expiration time. Maximum length: 32 characters.
        """
        return self.__expire_at

    @expire_at.setter
    def expire_at(self, value):
        self.__expire_at = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "registration_request_id") and self.registration_request_id is not None:
            params['registrationRequestId'] = self.registration_request_id
        if hasattr(self, "tax_type") and self.tax_type is not None:
            params['taxType'] = self.tax_type
        if hasattr(self, "jurisdiction") and self.jurisdiction is not None:
            params['jurisdiction'] = self.jurisdiction
        if hasattr(self, "registration_type") and self.registration_type is not None:
            params['registrationType'] = self.registration_type
        if hasattr(self, "tax_id") and self.tax_id is not None:
            params['taxId'] = self.tax_id
        if hasattr(self, "active_from") and self.active_from is not None:
            params['activeFrom'] = self.active_from
        if hasattr(self, "expire_at") and self.expire_at is not None:
            params['expireAt'] = self.expire_at
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'registrationRequestId' in response_body:
            self.__registration_request_id = response_body['registrationRequestId']
        if 'taxType' in response_body:
            self.__tax_type = response_body['taxType']
        if 'jurisdiction' in response_body:
            self.__jurisdiction = TaxJurisdiction()
            self.__jurisdiction.parse_rsp_body(response_body['jurisdiction'])
        if 'registrationType' in response_body:
            self.__registration_type = response_body['registrationType']
        if 'taxId' in response_body:
            self.__tax_id = response_body['taxId']
        if 'activeFrom' in response_body:
            self.__active_from = response_body['activeFrom']
        if 'expireAt' in response_body:
            self.__expire_at = response_body['expireAt']
