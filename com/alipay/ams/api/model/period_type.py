from enum import Enum, unique
@unique
class PeriodType(Enum):
    """The subscription period type. Valid values are:  WEEK: indicates that the subscription period is measured in weeks. MONTH: indicates that the subscription period is measured in months. QUARTER: indicates that the subscription period is measured in quarters. HALF_YEAR: indicates that the subscription period is measured in half years. YEAR: indicates that the subscription period is measured in years."""

    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    HALF_YEAR = "HALF_YEAR"
    YEAR = "YEAR"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PeriodType.WEEK.value == value:
            return PeriodType.WEEK
        if PeriodType.MONTH.value == value:
            return PeriodType.MONTH
        if PeriodType.QUARTER.value == value:
            return PeriodType.QUARTER
        if PeriodType.HALF_YEAR.value == value:
            return PeriodType.HALF_YEAR
        if PeriodType.YEAR.value == value:
            return PeriodType.YEAR
        return None
