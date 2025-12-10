from enum import Enum, unique
@unique
class DeclarationBizSceneType(Enum):
    """申报时对应的行业分类。非OTA结汇场景不传，OTA场景必传，且与declarationBeneficiaryId需同时存在。"""

    AIRLINE = "AIRLINE"
    HOTEL = "HOTEL"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DeclarationBizSceneType.AIRLINE.value == value:
            return DeclarationBizSceneType.AIRLINE
        if DeclarationBizSceneType.HOTEL.value == value:
            return DeclarationBizSceneType.HOTEL
        return None
