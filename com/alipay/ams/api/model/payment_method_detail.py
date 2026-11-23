import json
from com.alipay.ams.api.model.payment_method_detail_type import PaymentMethodDetailType
from com.alipay.ams.api.model.card_payment_method_detail import CardPaymentMethodDetail
from com.alipay.ams.api.model.external_payment_method_detail import ExternalPaymentMethodDetail
from com.alipay.ams.api.model.discount_payment_method_detail import DiscountPaymentMethodDetail
from com.alipay.ams.api.model.coupon_payment_method_detail import CouponPaymentMethodDetail
from com.alipay.ams.api.model.wallet import Wallet




class PaymentMethodDetail:
    def __init__(self):
        
        self.__payment_method_detail_type = None  # type: PaymentMethodDetailType
        self.__card = None  # type: CardPaymentMethodDetail
        self.__external_account = None  # type: ExternalPaymentMethodDetail
        self.__discount = None  # type: DiscountPaymentMethodDetail
        self.__coupon = None  # type: CouponPaymentMethodDetail
        self.__payment_method_type = None  # type: str
        self.__extend_info = None  # type: str
        self.__wallet = None  # type: Wallet
        self.__interaction_type = None  # type: str
        

    @property
    def payment_method_detail_type(self):
        """Gets the payment_method_detail_type of this PaymentMethodDetail.
        
        """
        return self.__payment_method_detail_type

    @payment_method_detail_type.setter
    def payment_method_detail_type(self, value):
        self.__payment_method_detail_type = value
    @property
    def card(self):
        """Gets the card of this PaymentMethodDetail.
        
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value
    @property
    def external_account(self):
        """Gets the external_account of this PaymentMethodDetail.
        
        """
        return self.__external_account

    @external_account.setter
    def external_account(self, value):
        self.__external_account = value
    @property
    def discount(self):
        """Gets the discount of this PaymentMethodDetail.
        
        """
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value
    @property
    def coupon(self):
        """Gets the coupon of this PaymentMethodDetail.
        
        """
        return self.__coupon

    @coupon.setter
    def coupon(self, value):
        self.__coupon = value
    @property
    def payment_method_type(self):
        """
        The type of payment method to be vaulted. The value of this parameter is fixed to CARD.    More information:  Maximum length: 64 characters 
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def extend_info(self):
        """Gets the extend_info of this PaymentMethodDetail.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def wallet(self):
        """Gets the wallet of this PaymentMethodDetail.
        
        """
        return self.__wallet

    @wallet.setter
    def wallet(self, value):
        self.__wallet = value
    @property
    def interaction_type(self):
        """Gets the interaction_type of this PaymentMethodDetail.
        
        """
        return self.__interaction_type

    @interaction_type.setter
    def interaction_type(self, value):
        self.__interaction_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_detail_type") and self.payment_method_detail_type is not None:
            params['paymentMethodDetailType'] = self.payment_method_detail_type
        if hasattr(self, "card") and self.card is not None:
            params['card'] = self.card
        if hasattr(self, "external_account") and self.external_account is not None:
            params['externalAccount'] = self.external_account
        if hasattr(self, "discount") and self.discount is not None:
            params['discount'] = self.discount
        if hasattr(self, "coupon") and self.coupon is not None:
            params['coupon'] = self.coupon
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "wallet") and self.wallet is not None:
            params['wallet'] = self.wallet
        if hasattr(self, "interaction_type") and self.interaction_type is not None:
            params['interactionType'] = self.interaction_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodDetailType' in response_body:
            payment_method_detail_type_temp = PaymentMethodDetailType.value_of(response_body['paymentMethodDetailType'])
            self.__payment_method_detail_type = payment_method_detail_type_temp
        if 'card' in response_body:
            self.__card = CardPaymentMethodDetail()
            self.__card.parse_rsp_body(response_body['card'])
        if 'externalAccount' in response_body:
            self.__external_account = ExternalPaymentMethodDetail()
            self.__external_account.parse_rsp_body(response_body['externalAccount'])
        if 'discount' in response_body:
            self.__discount = DiscountPaymentMethodDetail()
            self.__discount.parse_rsp_body(response_body['discount'])
        if 'coupon' in response_body:
            self.__coupon = CouponPaymentMethodDetail()
            self.__coupon.parse_rsp_body(response_body['coupon'])
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'wallet' in response_body:
            self.__wallet = Wallet()
            self.__wallet.parse_rsp_body(response_body['wallet'])
        if 'interactionType' in response_body:
            self.__interaction_type = response_body['interactionType']
