from enum import Enum, unique


@unique
class CaptureMode(Enum):
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"

    def to_ams_dict(self):
        return self.name
