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
        self.__card_limit_detail = None  # type: CardLimitDetail
        self.__card_limit_info = None  # type: CardLimitInfo
        self.__refund_preference = None  # type: RefundPreference
        

    @property
    def card_active_time(self):
        """
        The card activation time in ISO 8601 format.
        """
        return self.__card_active_time

    @card_active_time.setter
    def card_active_time(self, value):
        self.__card_active_time = value
    @property
    def card_cancel_time(self):
        """
        The card cancellation time in ISO 8601 format.
        """
        return self.__card_cancel_time

    @card_cancel_time.setter
    def card_cancel_time(self, value):
        self.__card_cancel_time = value
    @property
    def allowed_merchant_category_list(self):
        """
        The allowed merchant category code list.
        """
        return self.__allowed_merchant_category_list

    @allowed_merchant_category_list.setter
    def allowed_merchant_category_list(self, value):
        self.__allowed_merchant_category_list = value
    @property
    def allowed_auth_times(self):
        """
        The number of allowed authorization attempts.
        """
        return self.__allowed_auth_times

    @allowed_auth_times.setter
    def allowed_auth_times(self, value):
        self.__allowed_auth_times = value
    @property
    def allowed_currencies(self):
        """
        The allowed transaction currencies as ISO 4217 codes.
        """
        return self.__allowed_currencies

    @allowed_currencies.setter
    def allowed_currencies(self, value):
        self.__allowed_currencies = value
    @property
    def payment_preference_currencies(self):
        """
        An ordered list of ISO 4217 currency codes that defines the card-level balance-consumption priority. Only applyCard accepts this field in a request; do not send it to updateCard. For applyCard, the list must not contain duplicates and every currency must be supported by Antom. Omission, null, or an empty list configures no card-level preference. The field participates in requestId idempotency, and invalid values, more than 9 entries, duplicates, or capability-disabled use return PARAM_ILLEGAL. For inquireCardDetail, a configured list is returned in stored order; an enabled merchant without a card-level preference receives null, and a disabled merchant does not receive the field. For inquireCardSensitiveInfo, a whitelisted merchant receives the configured list, the child field is omitted when no card-level preference exists, and a non-whitelisted merchant does not receive the parent cardDetail object. The initially supported currencies are USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD; the supported set is configuration-driven and can change without an API contract change.
        """
        return self.__payment_preference_currencies

    @payment_preference_currencies.setter
    def payment_preference_currencies(self, value):
        self.__payment_preference_currencies = value
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
        if 'cardLimitDetail' in response_body:
            self.__card_limit_detail = CardLimitDetail()
            self.__card_limit_detail.parse_rsp_body(response_body['cardLimitDetail'])
        if 'cardLimitInfo' in response_body:
            self.__card_limit_info = CardLimitInfo()
            self.__card_limit_info.parse_rsp_body(response_body['cardLimitInfo'])
        if 'refundPreference' in response_body:
            self.__refund_preference = RefundPreference()
            self.__refund_preference.parse_rsp_body(response_body['refundPreference'])
