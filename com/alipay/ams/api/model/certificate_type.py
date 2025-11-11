from enum import Enum, unique
@unique
class CertificateType(Enum):
    """CertificateType枚举类"""

    ENTERPRISE_REGISTRATION = "ENTERPRISE_REGISTRATION"
    LICENSE_INFO = "LICENSE_INFO"
    ID_CARD = "ID_CARD"
    PASSPORT = "PASSPORT"
    DRIVING_LICENSE = "DRIVING_LICENSE"
    CPF = "CPF"
    CNPJ = "CNPJ"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CertificateType.ENTERPRISE_REGISTRATION.value == value:
            return CertificateType.ENTERPRISE_REGISTRATION
        if CertificateType.LICENSE_INFO.value == value:
            return CertificateType.LICENSE_INFO
        if CertificateType.ID_CARD.value == value:
            return CertificateType.ID_CARD
        if CertificateType.PASSPORT.value == value:
            return CertificateType.PASSPORT
        if CertificateType.DRIVING_LICENSE.value == value:
            return CertificateType.DRIVING_LICENSE
        if CertificateType.CPF.value == value:
            return CertificateType.CPF
        if CertificateType.CNPJ.value == value:
            return CertificateType.CNPJ
        return None
