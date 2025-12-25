import json
from com.alipay.ams.api.model.card_limit_detail import CardLimitDetail
from com.alipay.ams.api.model.card_limit_info import CardLimitInfo




class AuthorizationControl:
    def __init__(self):
        
        self.__card_active_time = None  # type: str
        self.__card_cancel_time = None  # type: str
        self.__allowed_merchant_category_list = None  # type: [str]
        self.__allowed_auth_times = None  # type: int
        self.__allowed_currencies = None  # type: [str]
        self.__card_limit_detail = None  # type: CardLimitDetail
        self.__card_limit_info = None  # type: CardLimitInfo
        

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
        if hasattr(self, "card_limit_detail") and self.card_limit_detail is not None:
            params['cardLimitDetail'] = self.card_limit_detail
        if hasattr(self, "card_limit_info") and self.card_limit_info is not None:
            params['cardLimitInfo'] = self.card_limit_info
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
        if 'cardLimitDetail' in response_body:
            self.__card_limit_detail = CardLimitDetail()
            self.__card_limit_detail.parse_rsp_body(response_body['cardLimitDetail'])
        if 'cardLimitInfo' in response_body:
            self.__card_limit_info = CardLimitInfo()
            self.__card_limit_info.parse_rsp_body(response_body['cardLimitInfo'])
