import json
from com.alipay.ams.api.model.certificate_type import CertificateType
from com.alipay.ams.api.model.user_name import UserName




class Certificate:
    def __init__(self):
        
        self.__certificate_type = None  # type: CertificateType
        self.__certificate_no = None  # type: str
        self.__holder_name = None  # type: UserName
        self.__file_keys = None  # type: [str]
        self.__certificate_authority = None  # type: str
        

    @property
    def certificate_type(self):
        """Gets the certificate_type of this Certificate.
        
        """
        return self.__certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self.__certificate_type = value
    @property
    def certificate_no(self):
        """
        The unique identification number of the certificate.    More information:  Maximum length: 64 characters 
        """
        return self.__certificate_no

    @certificate_no.setter
    def certificate_no(self, value):
        self.__certificate_no = value
    @property
    def holder_name(self):
        """Gets the holder_name of this Certificate.
        
        """
        return self.__holder_name

    @holder_name.setter
    def holder_name(self, value):
        self.__holder_name = value
    @property
    def file_keys(self):
        """
        A list of the unique key values of attachment files. Maximum file size: 32MB.  The value of this parameter is obtained from the attachmentKey parameter in the submitAttachment API. Prior attachment submission using the submitAttachment API is required.  Specify this parameter when the value of merchantInfo.company.certificates.certificateType is ENTERPRISE_REGISTRATION and the value of merchantInfo.company.registeredAddress.region is AU, SG, HK, GB, MY, US or the company&#39;s registered region belongs to the European Union.   More information:  Maximum size: 10 elements
        """
        return self.__file_keys

    @file_keys.setter
    def file_keys(self, value):
        self.__file_keys = value
    @property
    def certificate_authority(self):
        """
        The country that authorizes the certificate. The value of this parameter is a 2-letter country or region code based on the ISO 3166 Country Codes standard.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is US.    More information:  Maximum length: 64 characters
        """
        return self.__certificate_authority

    @certificate_authority.setter
    def certificate_authority(self, value):
        self.__certificate_authority = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "certificate_type") and self.certificate_type is not None:
            params['certificateType'] = self.certificate_type
        if hasattr(self, "certificate_no") and self.certificate_no is not None:
            params['certificateNo'] = self.certificate_no
        if hasattr(self, "holder_name") and self.holder_name is not None:
            params['holderName'] = self.holder_name
        if hasattr(self, "file_keys") and self.file_keys is not None:
            params['fileKeys'] = self.file_keys
        if hasattr(self, "certificate_authority") and self.certificate_authority is not None:
            params['certificateAuthority'] = self.certificate_authority
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'certificateType' in response_body:
            certificate_type_temp = CertificateType.value_of(response_body['certificateType'])
            self.__certificate_type = certificate_type_temp
        if 'certificateNo' in response_body:
            self.__certificate_no = response_body['certificateNo']
        if 'holderName' in response_body:
            self.__holder_name = UserName()
            self.__holder_name.parse_rsp_body(response_body['holderName'])
        if 'fileKeys' in response_body:
            self.__file_keys = response_body['fileKeys']
        if 'certificateAuthority' in response_body:
            self.__certificate_authority = response_body['certificateAuthority']
