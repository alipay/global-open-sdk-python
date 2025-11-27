import json

from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayVaultingPaymentMethodResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayVaultingPaymentMethodResponse, self).__init__()
        self.__vaulting_request_id = None
        self.__payment_method_detail = None  # type: PaymentMethodDetail
        self.__normal_url = None
        self.__scheme_url = None
        self.__applink_url = None
        self.__parse_rsp_body(rsp_body)

    @property
    def vaulting_request_id(self):
        return self.__vaulting_request_id

    @property
    def payment_method_detail(self):
        return self.__payment_method_detail

    @property
    def normal_url(self):
        return self.__normal_url

    @property
    def scheme_url(self):
        return self.__scheme_url

    @property
    def applink_url(self):
        return self.__applink_url

    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipayVaultingPaymentMethodResponse, self).parse_rsp_body(
            rsp_body
        )
        if "vaultingRequestId" in rsp_dict:
            self.__vaulting_request_id = rsp_dict["vaultingRequestId"]
        if "paymentMethodDetail" in rsp_dict:
            payment_method_detail = PaymentMethodDetail()
            self.__payment_method_detail = payment_method_detail.parse_rsp_body(
                rsp_dict["paymentMethodDetail"]
            )
        if "normalUrl" in rsp_dict:
            self.__normal_url = rsp_dict["normalUrl"]
        if "schemeUrl" in rsp_dict:
            self.__scheme_url = rsp_dict["schemeUrl"]
        if "applinkUrl" in rsp_dict:
            self.__applink_url = rsp_dict["applinkUrl"]
