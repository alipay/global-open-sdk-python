import json
from com.alipay.ams.api.model.three_ds_result import ThreeDSResult




class CardInfo:
    def __init__(self):
        
        self.__card_no = None  # type: str
        self.__card_brand = None  # type: str
        self.__card_token = None  # type: str
        self.__issuing_country = None  # type: str
        self.__funding = None  # type: str
        self.__payment_method_region = None  # type: str
        self.__three_ds_result = None  # type: ThreeDSResult
        

    @property
    def card_no(self):
        """
        The masked card number, which just shows part of the card number and can be used to display to the user
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def card_brand(self):
        """
        The card brand
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def card_token(self):
        """
        The token of the card
        """
        return self.__card_token

    @card_token.setter
    def card_token(self, value):
        self.__card_token = value
    @property
    def issuing_country(self):
        """
        The issuing country of the card
        """
        return self.__issuing_country

    @issuing_country.setter
    def issuing_country(self, value):
        self.__issuing_country = value
    @property
    def funding(self):
        """
        The funding type of the card
        """
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value
    @property
    def payment_method_region(self):
        """
        The region code that represents the country or region of the payment method
        """
        return self.__payment_method_region

    @payment_method_region.setter
    def payment_method_region(self, value):
        self.__payment_method_region = value
    @property
    def three_ds_result(self):
        """Gets the three_ds_result of this CardInfo.
        
        """
        return self.__three_ds_result

    @three_ds_result.setter
    def three_ds_result(self, value):
        self.__three_ds_result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_no") and self.card_no is not None:
            params['cardNo'] = self.card_no
        if hasattr(self, "card_brand") and self.card_brand is not None:
            params['cardBrand'] = self.card_brand
        if hasattr(self, "card_token") and self.card_token is not None:
            params['cardToken'] = self.card_token
        if hasattr(self, "issuing_country") and self.issuing_country is not None:
            params['issuingCountry'] = self.issuing_country
        if hasattr(self, "funding") and self.funding is not None:
            params['funding'] = self.funding
        if hasattr(self, "payment_method_region") and self.payment_method_region is not None:
            params['paymentMethodRegion'] = self.payment_method_region
        if hasattr(self, "three_ds_result") and self.three_ds_result is not None:
            params['threeDSResult'] = self.three_ds_result
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardNo' in response_body:
            self.__card_no = response_body['cardNo']
        if 'cardBrand' in response_body:
            self.__card_brand = response_body['cardBrand']
        if 'cardToken' in response_body:
            self.__card_token = response_body['cardToken']
        if 'issuingCountry' in response_body:
            self.__issuing_country = response_body['issuingCountry']
        if 'funding' in response_body:
            self.__funding = response_body['funding']
        if 'paymentMethodRegion' in response_body:
            self.__payment_method_region = response_body['paymentMethodRegion']
        if 'threeDSResult' in response_body:
            self.__three_ds_result = ThreeDSResult()
            self.__three_ds_result.parse_rsp_body(response_body['threeDSResult'])
