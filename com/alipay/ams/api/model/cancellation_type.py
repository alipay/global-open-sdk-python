from enum import Enum, unique


class CancellationType(Enum):
    CANCEL = "CANCEL"
    TERMINATE = "TERMINATE"

    def to_ams_dict(self):
        return self.name
