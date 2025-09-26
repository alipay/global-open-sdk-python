from enum import Enum, unique
@unique
class CompanyType(Enum):
    """CompanyType枚举类"""

    ENTERPRISE = "ENTERPRISE"
    PARTNERSHIP = "PARTNERSHIP"
    SOLE_PROPRIETORSHIP = "SOLE_PROPRIETORSHIP"
    STATE_OWNED_BUSINESS = "STATE_OWNED_BUSINESS"
    PRIVATELY_OWNED_BUSINESS = "PRIVATELY_OWNED_BUSINESS"
    PUBLICLY_LISTED_BUSINESS = "PUBLICLY_LISTED_BUSINESS"
    LTDA = "LTDA"
    SA = "SA"
    EIRELI = "EIRELI"
    BOFC = "BOFC"
    MEI = "MEI"
    EI = "EI"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CompanyType.ENTERPRISE.value == value:
            return CompanyType.ENTERPRISE
        if CompanyType.PARTNERSHIP.value == value:
            return CompanyType.PARTNERSHIP
        if CompanyType.SOLE_PROPRIETORSHIP.value == value:
            return CompanyType.SOLE_PROPRIETORSHIP
        if CompanyType.STATE_OWNED_BUSINESS.value == value:
            return CompanyType.STATE_OWNED_BUSINESS
        if CompanyType.PRIVATELY_OWNED_BUSINESS.value == value:
            return CompanyType.PRIVATELY_OWNED_BUSINESS
        if CompanyType.PUBLICLY_LISTED_BUSINESS.value == value:
            return CompanyType.PUBLICLY_LISTED_BUSINESS
        if CompanyType.LTDA.value == value:
            return CompanyType.LTDA
        if CompanyType.SA.value == value:
            return CompanyType.SA
        if CompanyType.EIRELI.value == value:
            return CompanyType.EIRELI
        if CompanyType.BOFC.value == value:
            return CompanyType.BOFC
        if CompanyType.MEI.value == value:
            return CompanyType.MEI
        if CompanyType.EI.value == value:
            return CompanyType.EI
        return None
