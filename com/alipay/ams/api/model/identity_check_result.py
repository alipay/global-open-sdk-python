from enum import Enum


class IdentityCheckResult(Enum):
    CHECK_PASSED = "CHECK_PASSED"
    CHECK_NOT_PASSED = "CHECK_NOT_PASSED"

    def to_ams_dict(self):
        return self.name
