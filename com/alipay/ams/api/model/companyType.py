from enum import Enum, unique


@unique
class CompanyType(Enum):
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

    def to_ams_dict(self):
        return self.name
