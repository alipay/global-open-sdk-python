

from enum import Enum, unique


@unique
class AttachmentType(Enum):
    SIGNATURE_AUTHORIZATION_LETTER = "SIGNATURE_AUTHORIZATION_LETTER"
    ARTICLES_OF_ASSOCIATION = "ARTICLES_OF_ASSOCIATION"
    LOGO = "LOGO"
    AUTHORIZER_SIGNATURE_CONFIRMATION_LETTER = "AUTHORIZER_SIGNATURE_CONFIRMATION_LETTER"
    ASSOCIATION_ARTICLE = "ASSOCIATION_ARTICLE"
    FINANCIAL_REPORT = "FINANCIAL_REPORT"
    OWNERSHIP_STRUCTURE_PIC = "OWNERSHIP_STRUCTURE_PIC"
    ADDRESS_PROOF = "ADDRESS_PROOF"
    UBO_PROVE = "UBO_PROVE"
    ENTERPRISE_REGISTRATION = "ENTERPRISE_REGISTRATION"
    LICENSE_INFO = "LICENSE_INFO"
    ID_CARD = "ID_CARD"
    PASSPORT = "PASSPORT"
    DRIVING_LICENSE = "DRIVING_LICENSE"
    CPF = "CPF"
    CNPJ = "CNPJ"

    def to_ams_dict(self):
        return self.name