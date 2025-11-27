from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.authorization_error import AuthorizationError
from com.alipay.ams.api.model.card_verification_result import CardVerificationResult
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class SendPaymentResultRequest(AlipayRequest):

    def __init__(self):
        super(AlipayRequest, self).__init__(
            AntomPathConstants.RISK_SEND_PAYMENT_RESULT_PATH
        )
        self.__reference_transaction_id = None
        self.__payment_status = None
        self.__authorization_error = None  # type: AuthorizationError
        self.__card_verification_result = None  # type: CardVerificationResult
        self.__payment_method_provider = None

    @property
    def reference_transaction_id(self):
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value

    @property
    def payment_status(self):
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, value):
        self.__payment_status = value

    @property
    def authorization_error(self):
        return self.__authorization_error

    @authorization_error.setter
    def authorization_error(self, value):
        self.__authorization_error = value

    @property
    def card_verification_result(self):
        return self.__card_verification_result

    @card_verification_result.setter
    def card_verification_result(self, value):
        self.__card_verification_result = value

    @property
    def payment_method_provider(self):
        return self.__payment_method_provider

    @payment_method_provider.setter
    def payment_method_provider(self, value):
        self.__payment_method_provider = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__reference_transaction_id is not None:
            params["referenceTransactionId"] = self.__reference_transaction_id
        if self.__payment_status is not None:
            params["paymentStatus"] = self.__payment_status
        if self.__authorization_error is not None:
            params["authorizationError"] = self.__authorization_error
        if self.__card_verification_result is not None:
            params["cardVerificationResult"] = self.__card_verification_result
        if self.__payment_method_provider is not None:
            params["paymentMethodProvider"] = self.__payment_method_provider
        return params
