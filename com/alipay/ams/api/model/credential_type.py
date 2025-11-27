from enum import Enum, unique


@unique
class CredentialType(Enum):
    NETWORK_TOKEN = "NETWORK_TOKEN"
    PAN = "PAN"

    def to_ams_dict(self):
        return self.name
