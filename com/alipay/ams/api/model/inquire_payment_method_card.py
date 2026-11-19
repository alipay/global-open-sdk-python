import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address




class InquirePaymentMethodCard:
    def __init__(self):
        
        self.__card_token = None  # type: str
        self.__card_no = None  # type: str
        self.__mask = None  # type: str
        self.__brand = None  # type: str
        self.__country_issue = None  # type: str
        self.__card_issuer = None  # type: str
        self.__expiry_month = None  # type: str
        self.__expiry_year = None  # type: str
        self.__inst_user_name = None  # type: UserName
        self.__billing_address = None  # type: Address
        

    @property
    def card_token(self):
        """
        The card token, consistent with the request.
        """
        return self.__card_token

    @card_token.setter
    def card_token(self, value):
        self.__card_token = value
    @property
    def card_no(self):
        """
        The full bank card number (PAN). This is the core capability of this API.
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def mask(self):
        """
        The masked card number, for example 411734******7890.
        """
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value
    @property
    def brand(self):
        """
        The card brand, for example VISA or MASTER. Queried in real time from the card BIN.
        """
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value
    @property
    def country_issue(self):
        """
        The issuing country or region as a two-letter country code. Queried in real time from the card BIN.
        """
        return self.__country_issue

    @country_issue.setter
    def country_issue(self, value):
        self.__country_issue = value
    @property
    def card_issuer(self):
        """
        The card issuer name from the stored card binding. Returned only when a value exists; the field is absent when no value is available.
        """
        return self.__card_issuer

    @card_issuer.setter
    def card_issuer(self, value):
        self.__card_issuer = value
    @property
    def expiry_month(self):
        """
        The card expiry month as two digits, from the stored card binding.
        """
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        self.__expiry_month = value
    @property
    def expiry_year(self):
        """
        The card expiry year as two digits, from the stored card binding.
        """
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        self.__expiry_year = value
    @property
    def inst_user_name(self):
        """Gets the inst_user_name of this InquirePaymentMethodCard.
        
        """
        return self.__inst_user_name

    @inst_user_name.setter
    def inst_user_name(self, value):
        self.__inst_user_name = value
    @property
    def billing_address(self):
        """Gets the billing_address of this InquirePaymentMethodCard.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_token") and self.card_token is not None:
            params['cardToken'] = self.card_token
        if hasattr(self, "card_no") and self.card_no is not None:
            params['cardNo'] = self.card_no
        if hasattr(self, "mask") and self.mask is not None:
            params['mask'] = self.mask
        if hasattr(self, "brand") and self.brand is not None:
            params['brand'] = self.brand
        if hasattr(self, "country_issue") and self.country_issue is not None:
            params['countryIssue'] = self.country_issue
        if hasattr(self, "card_issuer") and self.card_issuer is not None:
            params['cardIssuer'] = self.card_issuer
        if hasattr(self, "expiry_month") and self.expiry_month is not None:
            params['expiryMonth'] = self.expiry_month
        if hasattr(self, "expiry_year") and self.expiry_year is not None:
            params['expiryYear'] = self.expiry_year
        if hasattr(self, "inst_user_name") and self.inst_user_name is not None:
            params['instUserName'] = self.inst_user_name
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardToken' in response_body:
            self.__card_token = response_body['cardToken']
        if 'cardNo' in response_body:
            self.__card_no = response_body['cardNo']
        if 'mask' in response_body:
            self.__mask = response_body['mask']
        if 'brand' in response_body:
            self.__brand = response_body['brand']
        if 'countryIssue' in response_body:
            self.__country_issue = response_body['countryIssue']
        if 'cardIssuer' in response_body:
            self.__card_issuer = response_body['cardIssuer']
        if 'expiryMonth' in response_body:
            self.__expiry_month = response_body['expiryMonth']
        if 'expiryYear' in response_body:
            self.__expiry_year = response_body['expiryYear']
        if 'instUserName' in response_body:
            self.__inst_user_name = UserName()
            self.__inst_user_name.parse_rsp_body(response_body['instUserName'])
        if 'billingAddress' in response_body:
            self.__billing_address = Address()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
