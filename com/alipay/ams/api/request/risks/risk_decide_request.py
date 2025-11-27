import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.authorization_phase import AuthorizationPhase
from com.alipay.ams.api.model.buyer import Buyer
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_detail import PaymentDetail
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class RiskDecideRequest(AlipayRequest):
    def __init__(self):
        super(RiskDecideRequest, self).__init__(AntomPathConstants.RISK_DECIDE_PATH)
        self.__reference_transaction_id = None
        self.__authorization_phase = None  # type: AuthorizationPhase
        self.__orders = None  # type: list:Order
        self.__buyer = None  # type: Buyer
        self.__actual_payment_amount = None  # type: Amount
        self.__payment_details = None  # type: PaymentDetail
        self.__discount_amount = None  # type: Amount
        self.__env = None  # type: Env

    @property
    def reference_transaction_id(self):
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value

    @property
    def authorization_phase(self):
        return self.__authorization_phase

    @authorization_phase.setter
    def authorization_phase(self, value):
        self.__authorization_phase = value

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        self.__orders = value

    @property
    def buyer(self):
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value

    @property
    def actual_payment_amount(self):
        return self.__actual_payment_amount

    @actual_payment_amount.setter
    def actual_payment_amount(self, value):
        self.__actual_payment_amount = value

    @property
    def payment_details(self):
        return self.__payment_details

    @payment_details.setter
    def payment_details(self, value):
        self.__payment_details = value

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()

        if hasattr(self, "reference_transaction_id") and self.reference_transaction_id:
            params["referenceTransactionId"] = self.reference_transaction_id

        if hasattr(self, "authorization_phase") and self.authorization_phase:
            params["authorizationPhase"] = self.authorization_phase

        if hasattr(self, "orders") and self.orders:
            params["orders"] = self.orders

        if hasattr(self, "buyer") and self.buyer:
            params["buyer"] = self.buyer

        if hasattr(self, "actual_payment_amount") and self.actual_payment_amount:
            params["actualPaymentAmount"] = self.actual_payment_amount

        if hasattr(self, "payment_details") and self.payment_details:
            params["paymentDetails"] = self.payment_details

        if hasattr(self, "discount_amount") and self.discount_amount:
            params["discountAmount"] = self.discount_amount

        if hasattr(self, "env") and self.env:
            params["env"] = self.env

        return params
