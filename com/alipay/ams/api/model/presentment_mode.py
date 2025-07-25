from enum import Enum, unique
@unique
class PresentmentMode(Enum):
    """PresentmentMode枚举类"""

    BUNDLE = "BUNDLE"
    TILE = "TILE"
    UNIFIED = "UNIFIED"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PresentmentMode.BUNDLE.value == value:
            return PresentmentMode.BUNDLE
        if PresentmentMode.TILE.value == value:
            return PresentmentMode.TILE
        if PresentmentMode.UNIFIED.value == value:
            return PresentmentMode.UNIFIED
        return None
