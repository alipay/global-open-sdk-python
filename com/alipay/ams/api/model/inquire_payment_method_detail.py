import json
from com.alipay.ams.api.model.inquire_payment_method_card import InquirePaymentMethodCard




class InquirePaymentMethodDetail:
    def __init__(self):
        
        self.__payment_method_detail_type = None  # type: str
        self.__card = None  # type: InquirePaymentMethodCard
        

    @property
    def payment_method_detail_type(self):
        """
        The payment method detail type. The value is CARD; only credit card assets are supported.
        """
        return self.__payment_method_detail_type

    @payment_method_detail_type.setter
    def payment_method_detail_type(self, value):
        self.__payment_method_detail_type = value
    @property
    def card(self):
        """Gets the card of this InquirePaymentMethodDetail.
        
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_detail_type") and self.payment_method_detail_type is not None:
            params['paymentMethodDetailType'] = self.payment_method_detail_type
        if hasattr(self, "card") and self.card is not None:
            params['card'] = self.card
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodDetailType' in response_body:
            self.__payment_method_detail_type = response_body['paymentMethodDetailType']
        if 'card' in response_body:
            self.__card = InquirePaymentMethodCard()
            self.__card.parse_rsp_body(response_body['card'])
