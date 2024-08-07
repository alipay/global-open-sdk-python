from enum import Enum, unique


@unique
class DisableReasonType(Enum):
    PAYMENT_ACCOUNT_NOT_AVAILABLE = "PAYMENT_ACCOUNT_NOT_AVAILABLE"
    EXCEED_CHANNEL_LIMIT_RULE = "EXCEED_CHANNEL_LIMIT_RULE"
    SERVICE_DEGRADE = "SERVICE_DEGRADE"
    CHANNEL_NOT_SUPPORT_CURRENCY = "CHANNEL_NOT_SUPPORT_CURRENCY"
    CHANNEL_DISABLE = "CHANNEL_DISABLE"
    CHANNEL_NOT_IN_SERVICE_TIME = "CHANNEL_NOT_IN_SERVICE_TIME"
    QUERY_IPP_INFO_FAILED = "QUERY_IPP_INFO_FAILED"
    LIMIT_CENTER_ACCESS_FAIL = "LIMIT_CENTER_ACCESS_FAIL"
    CURRENT_CHANNEL_NOT_EXIST = "CURRENT_CHANNEL_NOT_EXIST"

    def to_ams_dict(self):
        return self.name
