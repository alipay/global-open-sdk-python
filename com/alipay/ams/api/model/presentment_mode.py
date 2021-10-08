from enum import Enum, unique

@unique
class PresentmentMode(Enum):
    BUNDLE = "BUNDLE"

    def to_ams_dict(self):
        return self.name