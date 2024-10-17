from enum import Enum, unique


@unique
class AuthorizationPhase(Enum):
    PRE_AUTHORIZATION = "PRE_AUTHORIZATION"
    POST_AUTHORIZATION = "POST_AUTHORIZATION"

    def to_ams_dict(self):
        return self.name
