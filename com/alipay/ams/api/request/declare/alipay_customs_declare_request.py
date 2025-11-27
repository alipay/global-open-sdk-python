import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.customs_info import CustomsInfo
from com.alipay.ams.api.model.merchant_customs_info import MerchantCustomsInfo
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCustomsDeclareRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomsDeclareRequest, self).__init__(
            AntomPathConstants.DECLARE_PATH
        )
        self.__declaration_request_id = None
        self.__payment_id = None
        self.__declaration_amount = None  # type:Amount
        self.__customs = None  # type:CustomsInfo
        self.__merchant_customs_info = None  # type:MerchantCustomsInfo
        self.__split_order = None
        self.__suborder_id = None
        self.__buyer_certificate = None  # type:Certificate

    @property
    def declaration_request_id(self):
        return self.__declaration_request_id

    @declaration_request_id.setter
    def declaration_request_id(self, value):
        self.__declaration_request_id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def declaration_amount(self):
        return self.__declaration_amount

    @declaration_amount.setter
    def declaration_amount(self, value):
        self.__declaration_amount = value

    @property
    def customs(self):
        return self.__customs

    @customs.setter
    def customs(self, value):
        self.__customs = value

    @property
    def merchant_customs_info(self):
        return self.__merchant_customs_info

    @merchant_customs_info.setter
    def merchant_customs_info(self, value):
        self.__merchant_customs_info = value

    @property
    def split_order(self):
        return self.__split_order

    @split_order.setter
    def split_order(self, value):
        self.__split_order = value

    @property
    def suborder_id(self):
        return self.__suborder_id

    @suborder_id.setter
    def suborder_id(self, value):
        self.__suborder_id = value

    @property
    def buyer_certificate(self):
        return self.__buyer_certificate

    @buyer_certificate.setter
    def buyer_certificate(self, value):
        self.__buyer_certificate = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "declaration_request_id") and self.declaration_request_id:
            params["declarationRequestId"] = self.declaration_request_id
        if hasattr(self, "payment_id") and self.payment_id:
            params["paymentId"] = self.payment_id
        if hasattr(self, "declaration_amount") and self.declaration_amount:
            params["declarationAmount"] = self.declaration_amount
        if hasattr(self, "customs") and self.customs:
            params["customs"] = self.customs
        if hasattr(self, "merchant_customs_info") and self.merchant_customs_info:
            params["merchantCustomsInfo"] = self.merchant_customs_info
        if hasattr(self, "split_order") and self.split_order:
            params["splitOrder"] = self.split_order
        if hasattr(self, "suborder_id") and self.suborder_id:
            params["suborderId"] = self.suborder_id
        if hasattr(self, "buyer_certificate") and self.buyer_certificate:
            params["buyerCertificate"] = self.buyer_certificate
        return params
