from enum import Enum, unique
@unique
class CodeValueType(Enum):
    """CodeValueType枚举类"""

    BARCODE = "BARCODE"
    QRCODE = "QRCODE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CodeValueType.BARCODE.value == value:
            return CodeValueType.BARCODE
        if CodeValueType.QRCODE.value == value:
            return CodeValueType.QRCODE
        return None
