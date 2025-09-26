from enum import Enum, unique
@unique
class AttachmentType(Enum):
    """AttachmentType枚举类"""

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

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if AttachmentType.SIGNATURE_AUTHORIZATION_LETTER.value == value:
            return AttachmentType.SIGNATURE_AUTHORIZATION_LETTER
        if AttachmentType.ARTICLES_OF_ASSOCIATION.value == value:
            return AttachmentType.ARTICLES_OF_ASSOCIATION
        if AttachmentType.LOGO.value == value:
            return AttachmentType.LOGO
        if AttachmentType.AUTHORIZER_SIGNATURE_CONFIRMATION_LETTER.value == value:
            return AttachmentType.AUTHORIZER_SIGNATURE_CONFIRMATION_LETTER
        if AttachmentType.ASSOCIATION_ARTICLE.value == value:
            return AttachmentType.ASSOCIATION_ARTICLE
        if AttachmentType.FINANCIAL_REPORT.value == value:
            return AttachmentType.FINANCIAL_REPORT
        if AttachmentType.OWNERSHIP_STRUCTURE_PIC.value == value:
            return AttachmentType.OWNERSHIP_STRUCTURE_PIC
        if AttachmentType.ADDRESS_PROOF.value == value:
            return AttachmentType.ADDRESS_PROOF
        if AttachmentType.UBO_PROVE.value == value:
            return AttachmentType.UBO_PROVE
        if AttachmentType.ENTERPRISE_REGISTRATION.value == value:
            return AttachmentType.ENTERPRISE_REGISTRATION
        if AttachmentType.LICENSE_INFO.value == value:
            return AttachmentType.LICENSE_INFO
        if AttachmentType.ID_CARD.value == value:
            return AttachmentType.ID_CARD
        if AttachmentType.PASSPORT.value == value:
            return AttachmentType.PASSPORT
        if AttachmentType.DRIVING_LICENSE.value == value:
            return AttachmentType.DRIVING_LICENSE
        if AttachmentType.CPF.value == value:
            return AttachmentType.CPF
        if AttachmentType.CNPJ.value == value:
            return AttachmentType.CNPJ
        return None
