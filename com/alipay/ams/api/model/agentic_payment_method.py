import json




class AgenticPaymentMethod:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_id = None  # type: str
        self.__selected_card_brand = None  # type: str
        

    @property
    def payment_method_type(self):
        """
        Payment method type. Case-sensitive supported values: CARD, AlipayCN, AlipayHK, MPay. See the enclosing API paymentMethod description for scenario rules.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_id(self):
        """
        Opaque Antom payment method reference. Pass unchanged. Omit for createBindingSession; conditionally required for createAuthenticationSession and required for inquirePaymentToken. See the enclosing API description.
        """
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value
    @property
    def selected_card_brand(self):
        """
        Case-sensitive card brand: VISA or MASTERCARD. Omit for APM. Requiredness and supported combinations depend on the API and scenario; see the enclosing API paymentMethod description.
        """
        return self.__selected_card_brand

    @selected_card_brand.setter
    def selected_card_brand(self, value):
        self.__selected_card_brand = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_id") and self.payment_method_id is not None:
            params['paymentMethodId'] = self.payment_method_id
        if hasattr(self, "selected_card_brand") and self.selected_card_brand is not None:
            params['selectedCardBrand'] = self.selected_card_brand
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodId' in response_body:
            self.__payment_method_id = response_body['paymentMethodId']
        if 'selectedCardBrand' in response_body:
            self.__selected_card_brand = response_body['selectedCardBrand']
