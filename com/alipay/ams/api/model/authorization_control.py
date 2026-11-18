import json
from com.alipay.ams.api.model.card_limit_detail import CardLimitDetail
from com.alipay.ams.api.model.card_limit_info import CardLimitInfo
from com.alipay.ams.api.model.refund_preference import RefundPreference




class AuthorizationControl:
    def __init__(self):
        
        self.__card_active_time = None  # type: str
        self.__card_cancel_time = None  # type: str
        self.__allowed_merchant_category_list = None  # type: [str]
        self.__allowed_auth_times = None  # type: int
        self.__allowed_currencies = None  # type: [str]
        self.__payment_preference_currencies = None  # type: [str]
        self.__same_currency_preference = None  # type: bool
        self.__three_ds_mode = None  # type: str
        self.__phone_no = None  # type: str
        self.__email = None  # type: str
        self.__card_limit_detail = None  # type: CardLimitDetail
        self.__card_limit_info = None  # type: CardLimitInfo
        self.__refund_preference = None  # type: RefundPreference
        

    @property
    def card_active_time(self):
        """
        If not present, It will be activated when the card is created. Datetime UTC time: 2018-10-31T00:00:00+0800 ISO 8601
        """
        return self.__card_active_time

    @card_active_time.setter
    def card_active_time(self, value):
        self.__card_active_time = value
    @property
    def card_cancel_time(self):
        """
        Datetime UTC time: 2018-10-31T00:00:00+0800 ISO 8601
        """
        return self.__card_cancel_time

    @card_cancel_time.setter
    def card_cancel_time(self, value):
        self.__card_cancel_time = value
    @property
    def allowed_merchant_category_list(self):
        """
        Allowed MCC (Merchant Category Code) list. If not set or left empty, all transactions are allowed.
        """
        return self.__allowed_merchant_category_list

    @allowed_merchant_category_list.setter
    def allowed_merchant_category_list(self, value):
        self.__allowed_merchant_category_list = value
    @property
    def allowed_auth_times(self):
        """
        Indicates the number of allowed authorization times. If not set or left empty, all transactions are allowed.
        """
        return self.__allowed_auth_times

    @allowed_auth_times.setter
    def allowed_auth_times(self, value):
        self.__allowed_auth_times = value
    @property
    def allowed_currencies(self):
        """
        Allowed transaction currencies (ISO 4217 three-letter codes). If not set, no currency restriction applies.
        """
        return self.__allowed_currencies

    @allowed_currencies.setter
    def allowed_currencies(self, value):
        self.__allowed_currencies = value
    @property
    def payment_preference_currencies(self):
        """
        An ordered list of ISO 4217 currency codes that defines the card-level balance-consumption priority. Only applyCard accepts this field in a request; do not send it to updateCard. For applyCard, the list must not contain duplicates and every currency must be supported by Antom. Omission, null, or an empty list configures no card-level preference. The field participates in requestId idempotency, and invalid values, more than 9 entries, duplicates, or capability-disabled use return PARAM_ILLEGAL. For inquireCardDetail, a configured list is returned in stored order; an enabled merchant without a card-level preference receives null, and a disabled merchant does not receive the field. For inquireCardSensitiveInfo, the current contract exposes authorizationControl at the response top level for whitelisted merchants. The legacy cardDetail property remains in the SDK for compatibility, without automatic copying between the two locations. The order field is subject to its existing capability and visibility rules; an absent order field must not be interpreted as proof that no stored order exists. The initially supported currencies are USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD; the supported set is configuration-driven and can change without an API contract change.
        """
        return self.__payment_preference_currencies

    @payment_preference_currencies.setter
    def payment_preference_currencies(self, value):
        self.__payment_preference_currencies = value
    @property
    def same_currency_preference(self):
        """
        Whether to prioritize the transaction currency balance. Accepted only by applyCard and immutable after creation; do not send to updateCard. True enables same-currency-first deduction; false skips it and follows paymentPreferenceCurrencies when configured, otherwise the account-level setting. Omission preserves the server default behavior (same-currency-first); SDKs must not supply a default and must preserve explicit false. An omitted, null, or empty currency order is accepted. Returned by inquireCardDetail and the top-level authorizationControl of inquireCardSensitiveInfo when a standing is stored; otherwise omitted. Sensitive-info enrichment requires the existing merchant whitelist. Availability is controlled by WorldFirst; an ignored preference is not stored. Applicable to eligible Z18 merchants in CN/HK. Each payment is funded in full from one currency; balances are never split across currencies. A configured card-level currency order is exclusive: the account-level order is not consulted, and the payment fails if no eligible currency can fund it in full. On inquiry, an absent paymentPreferenceCurrencies field can mean the order is hidden or unavailable; it must not be interpreted as proof that no order is configured. Retain endpoint and capability context when interpreting returned fields.
        """
        return self.__same_currency_preference

    @same_currency_preference.setter
    def same_currency_preference(self, value):
        self.__same_currency_preference = value
    @property
    def three_ds_mode(self):
        """
        Card-level 3DS mode. Accepted only by applyCard and immutable after creation; do not send to updateCard. Current values are STANDARD and FRICTIONLESS. For card-level configuration, omission or null uses the server default STANDARD; FRICTIONLESS requires merchant enablement and remains subject to issuer risk decisions. MID-level configuration takes precedence where applicable. Returned by inquireCardDetail and the top-level authorizationControl of inquireCardSensitiveInfo for the card-level cohort; omitted for MID-level-only or Antom-hidden merchants. A null response means no stored card-level mode. SDKs must not insert defaults and must tolerate future response values.
        """
        return self.__three_ds_mode

    @three_ds_mode.setter
    def three_ds_mode(self, value):
        self.__three_ds_mode = value
    @property
    def phone_no(self):
        """
        Cardholder phone number for STANDARD-mode 3DS OTP authentication. Accepted by updateCard only; do not send to applyCard. Supply a complete E.164 number including the leading plus sign to update this card-specific value. Omission leaves the existing value unchanged and updating this field does not change email or merchant security settings. Initially populated from security settings. In inquireCardDetail and the top-level authorizationControl of inquireCardSensitiveInfo, returned masked when stored and visible to the card-level cohort, for both STANDARD and FRICTIONLESS; omitted for the hidden cohort. Never send a masked response value back to updateCard. Contains personal data; avoid logging complete values. This contract does not define null or empty-string clearing semantics.
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def email(self):
        """
        Cardholder email address for STANDARD-mode 3DS OTP authentication. Accepted by updateCard only; do not send to applyCard. Supply a complete email address to update this card-specific value. Omission leaves the existing value unchanged and updating this field does not change phoneNo or merchant security settings. Initially populated from security settings. In inquireCardDetail and the top-level authorizationControl of inquireCardSensitiveInfo, returned masked when stored and visible to the card-level cohort, for both STANDARD and FRICTIONLESS; omitted for the hidden cohort. Never send a masked response value back to updateCard. Contains personal data; avoid logging complete values. This contract does not define null or empty-string clearing semantics.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def card_limit_detail(self):
        """Gets the card_limit_detail of this AuthorizationControl.
        
        """
        return self.__card_limit_detail

    @card_limit_detail.setter
    def card_limit_detail(self, value):
        self.__card_limit_detail = value
    @property
    def card_limit_info(self):
        """Gets the card_limit_info of this AuthorizationControl.
        
        """
        return self.__card_limit_info

    @card_limit_info.setter
    def card_limit_info(self, value):
        self.__card_limit_info = value
    @property
    def refund_preference(self):
        """Gets the refund_preference of this AuthorizationControl.
        
        """
        return self.__refund_preference

    @refund_preference.setter
    def refund_preference(self, value):
        self.__refund_preference = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_active_time") and self.card_active_time is not None:
            params['cardActiveTime'] = self.card_active_time
        if hasattr(self, "card_cancel_time") and self.card_cancel_time is not None:
            params['cardCancelTime'] = self.card_cancel_time
        if hasattr(self, "allowed_merchant_category_list") and self.allowed_merchant_category_list is not None:
            params['allowedMerchantCategoryList'] = self.allowed_merchant_category_list
        if hasattr(self, "allowed_auth_times") and self.allowed_auth_times is not None:
            params['allowedAuthTimes'] = self.allowed_auth_times
        if hasattr(self, "allowed_currencies") and self.allowed_currencies is not None:
            params['allowedCurrencies'] = self.allowed_currencies
        if hasattr(self, "payment_preference_currencies") and self.payment_preference_currencies is not None:
            params['paymentPreferenceCurrencies'] = self.payment_preference_currencies
        if hasattr(self, "same_currency_preference") and self.same_currency_preference is not None:
            params['sameCurrencyPreference'] = self.same_currency_preference
        if hasattr(self, "three_ds_mode") and self.three_ds_mode is not None:
            params['threeDSMode'] = self.three_ds_mode
        if hasattr(self, "phone_no") and self.phone_no is not None:
            params['phoneNo'] = self.phone_no
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "card_limit_detail") and self.card_limit_detail is not None:
            params['cardLimitDetail'] = self.card_limit_detail
        if hasattr(self, "card_limit_info") and self.card_limit_info is not None:
            params['cardLimitInfo'] = self.card_limit_info
        if hasattr(self, "refund_preference") and self.refund_preference is not None:
            params['refundPreference'] = self.refund_preference
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardActiveTime' in response_body:
            self.__card_active_time = response_body['cardActiveTime']
        if 'cardCancelTime' in response_body:
            self.__card_cancel_time = response_body['cardCancelTime']
        if 'allowedMerchantCategoryList' in response_body:
            self.__allowed_merchant_category_list = response_body['allowedMerchantCategoryList']
        if 'allowedAuthTimes' in response_body:
            self.__allowed_auth_times = response_body['allowedAuthTimes']
        if 'allowedCurrencies' in response_body:
            self.__allowed_currencies = response_body['allowedCurrencies']
        if 'paymentPreferenceCurrencies' in response_body:
            self.__payment_preference_currencies = response_body['paymentPreferenceCurrencies']
        if 'sameCurrencyPreference' in response_body:
            self.__same_currency_preference = response_body['sameCurrencyPreference']
        if 'threeDSMode' in response_body:
            self.__three_ds_mode = response_body['threeDSMode']
        if 'phoneNo' in response_body:
            self.__phone_no = response_body['phoneNo']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'cardLimitDetail' in response_body:
            self.__card_limit_detail = CardLimitDetail()
            self.__card_limit_detail.parse_rsp_body(response_body['cardLimitDetail'])
        if 'cardLimitInfo' in response_body:
            self.__card_limit_info = CardLimitInfo()
            self.__card_limit_info.parse_rsp_body(response_body['cardLimitInfo'])
        if 'refundPreference' in response_body:
            self.__refund_preference = RefundPreference()
            self.__refund_preference.parse_rsp_body(response_body['refundPreference'])
