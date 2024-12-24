class PaymentMethodTypeItem:

    def __init__(self):
        self.__payment_method_type = None
        self.__payment_method_order = None
        self.__express_checkout = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value

    @property
    def payment_method_order(self):
        return self.__payment_method_order

    @payment_method_order.setter
    def payment_method_order(self, value):
        self.__payment_method_order = value

    @property
    def express_checkout(self):
        return self.__express_checkout

    @express_checkout.setter
    def express_checkout(self, value):
        self.__express_checkout = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_order") and self.payment_method_order:
            params['paymentMethodOrder'] = self.payment_method_order
        if hasattr(self, "express_checkout") and self.express_checkout:
            params['expressCheckout'] = self.express_checkout.to_ams_dict()
        return params