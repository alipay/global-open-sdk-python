import string


class ApplePayConfiguration:
    def __init__(self):
        self.__required_billing_contact_fields = None  # type: list[string]
        self.__required_shipping_contact_fields = None  # type: list[string]
        self.__buttons_bundled = None  # type: bool
        self.__apple_pay_token = None  # type: string

    @property
    def required_billing_contact_fields(self):
        return self.__required_billing_contact_fields

    @required_billing_contact_fields.setter
    def required_billing_contact_fields(self, value):
        self.__required_billing_contact_fields = value

    @property
    def required_shipping_contact_fields(self):
        return self.__required_shipping_contact_fields

    @required_shipping_contact_fields.setter
    def required_shipping_contact_fields(self, value):
        self.__required_shipping_contact_fields = value

    @property
    def buttons_bundled(self):
        return self.__buttons_bundled

    @buttons_bundled.setter
    def buttons_bundled(self, value: bool):
        self.__buttons_bundled = value

    @property
    def apple_pay_token(self):
        return self.__apple_pay_token

    @apple_pay_token.setter
    def apple_pay_token(self, value: str):
        self.__apple_pay_token = value

    def to_ams_dict(self):
        params = dict()
        if (
            hasattr(self, "required_billing_contact_fields")
            and self.required_billing_contact_fields
        ):
            params["referenceBuyerId"] = self.required_shipping_contact_fields
        if (
            hasattr(self, "required_shipping_contact_fields")
            and self.required_shipping_contact_fields
        ):
            params["referenceBuyerId"] = self.required_shipping_contact_fields
        if hasattr(self, "buttons_bundled") and self.buttons_bundled:
            params["referenceBuyerId"] = self.buttons_bundled
        if hasattr(self, "apple_pay_token") and self.apple_pay_token:
            params["referenceBuyerId"] = self.apple_pay_token
        return params
