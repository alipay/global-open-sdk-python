from com.alipay.ams.api.model.clearing_channel import ClearingChannel
from com.alipay.ams.api.model.identity_check_result import IdentityCheckResult
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCustomsDeclareResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayCustomsDeclareResponse, self).__init__()
        self.__customs_payment_id = None
        self.__customs_order_id = None
        self.__identity_check_result = None  # type: IdentityCheckResult
        self.__clearing_channel = None  # type: ClearingChannel
        self.__clearing_transaction_id = None
        self.__customs_provider_registration_id = None
        self.__parse_rsp_body(rsp_body)

    @property
    def customs_payment_id(self):
        return self.__customs_payment_id

    @property
    def customs_order_id(self):
        return self.__customs_order_id

    @property
    def identity_check_result(self):
        return self.__identity_check_result

    @property
    def clearing_channel(self):
        return self.__clearing_channel

    @property
    def clearing_transaction_id(self):
        return self.__clearing_transaction_id

    @property
    def customs_provider_registration_id(self):
        return self.__customs_provider_registration_id

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayCustomsDeclareResponse, self).parse_rsp_body(rsp_body)
        if response.get("customsPaymentId"):
            self.__customs_payment_id = response.get("customsPaymentId")
        if response.get("customsOrderId"):
            self.__customs_order_id = response.get("customsOrderId")
        if response.get("identityCheckResult"):
            self.__identity_check_result = response.get("identityCheckResult")
        if response.get("clearingChannel"):
            self.__clearing_channel = response.get("clearingChannel")
        if response.get("clearingTransactionId"):
            self.__clearing_transaction_id = response.get("clearingTransactionId")
        if response.get("customsProviderRegistrationId"):
            self.__customs_provider_registration_id = response.get(
                "customsProviderRegistrationId"
            )
