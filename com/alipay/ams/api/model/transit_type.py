from enum import Enum, unique
@unique
class TransitType(Enum):
    """Type of transit"""

    FLIGHT = "FLIGHT"
    TRAIN = "TRAIN"
    CRUISE = "CRUISE"
    COACH = "COACH"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TransitType.FLIGHT.value == value:
            return TransitType.FLIGHT
        if TransitType.TRAIN.value == value:
            return TransitType.TRAIN
        if TransitType.CRUISE.value == value:
            return TransitType.CRUISE
        if TransitType.COACH.value == value:
            return TransitType.COACH
        return None
