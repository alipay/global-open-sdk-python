from enum import Enum, unique


@unique
class TransitType(Enum):
    FLIGHT = "FLIGHT"
    TRAIN = "TRAIN"
    CRUISE = "CRUISE"
    COACH = "COACH"

    def to_ams_dict(self):
        return self.name
