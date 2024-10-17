from enum import Enum, unique


@unique
class PeriodType(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"

    def to_ams_dict(self):
        return self.name
