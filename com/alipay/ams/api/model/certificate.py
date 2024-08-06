from com.alipay.ams.api.model.certificate_type import CertificateType
from com.alipay.ams.api.model.user_name import UserName


class Certificate(object):
    def __init__(self):
        self.__certificate_type = None  # type: CertificateType
        self.__certificate_no = None
        self.__holder_name = None  # type: UserName
        self.__file_keys = None
        self.__certificate_authority = None

    @property
    def certificate_type(self):
        return self.__certificate_type

    @property
    def certificate_no(self):
        return self.__certificate_no

    @property
    def holder_name(self):
        return self.__holder_name

    @property
    def file_keys(self):
        return self.__file_keys

    @property
    def certificate_authority(self):
        return self.__certificate_authority

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        self.__certificate_type = certificate_type

    @certificate_no.setter
    def certificate_no(self, certificate_no):
        self.__certificate_no = certificate_no

    @holder_name.setter
    def holder_name(self, holder_name):
        self.__holder_name = holder_name

    @file_keys.setter
    def file_keys(self, file_keys):
        self.__file_keys = file_keys

    @certificate_authority.setter
    def certificate_authority(self, certificate_authority):
        self.__certificate_authority = certificate_authority

    def to_ams_dict(self):
        params = dict()
        if self.certificate_type is not None:
            params['certificateType'] = self.certificate_type
        if self.certificate_no is not None:
            params['certificateNo'] = self.certificate_no
        if self.holder_name is not None:
            params['holderName'] = self.holder_name.to_ams_dict()
        if self.file_keys is not None:
            params['fileKeys'] = self.file_keys
        if self.certificate_authority is not None:
            params['certificateAuthority'] = self.certificate_authority
        return params
