from enum import Enum, unique


@unique
class CertificateType(Enum):
    ID_CARD = "ID_CARD"
    PASSPORT = "PASSPORT"
    ENTERPRISE_REGISTRATION = "ENTERPRISE_REGISTRATION"
    LICENSE_INFO = "LICENSE_INFO"
    DRIVING_LICENSE = "DRIVING_LICENSE"
    CPF = "CPF"
    CNPJ = "CNPJ"

    def to_ams_dict(self):
        return self.name
