from enum import Enum, unique


@unique
class DeliveryMethodType(Enum):
    PHYSICAL = "PHYSICAL"
    DIGITAL = "DIGITAL"

    def to_ams_dict(self):
        return self.name
