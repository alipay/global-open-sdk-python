from enum import Enum, unique


@unique
class MethodType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    def to_ams_dict(self):
        return self.name
