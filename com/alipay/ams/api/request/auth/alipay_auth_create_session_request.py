import json

from com.alipay.ams.api.model.agreement_info import AgreementInfo
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.scope_type import ScopeType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayAuthCreateSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayAuthCreateSessionRequest, self).__init__(
            AntomPathConstants.CREATE_SESSION_PATH
        )
        self.__product_code = None  # type:ProductCodeType
        self.__agreement_info = None  # type:AgreementInfo
        self.__scopes = None  # type:list[ScopeType]
        self.__payment_method = None  # type:PaymentMethod
        self.__payment_redirect_url = None

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value: ProductCodeType):
        self.__product_code = value

    @property
    def agreement_info(self):
        return self.__agreement_info

    @agreement_info.setter
    def agreement_info(self, value: AgreementInfo):
        self.__agreement_info = value

    @property
    def scopes(self):
        return self.__scopes

    @scopes.setter
    def scopes(self, value: list[ScopeType]):
        self.__scopes = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: PaymentMethod):
        self.__payment_method = value

    @property
    def payment_redirect_url(self):
        return self.__payment_redirect_url

    @payment_redirect_url.setter
    def payment_redirect_url(self, value: str):
        self.__payment_redirect_url = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code:
            params["productCodeType"] = self.product_code

        if hasattr(self, "agreement_info") and self.agreement_info:
            params["agreementInfo"] = self.agreement_info.to_ams_json()

        if hasattr(self, "scopes") and self.scopes:
            scopes_list = []
            for scope in self.scopes:
                scopes_list.append(scope.value)
            params["scopes"] = scopes_list

        if hasattr(self, "payment_method") and self.payment_method:
            params["paymentMethod"] = self.payment_method.to_ams_dict()

        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url:
            params["paymentRedirectUrl"] = self.payment_redirect_url

        return params
