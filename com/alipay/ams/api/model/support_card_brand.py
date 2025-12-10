import json
from com.alipay.ams.api.model.logo import Logo




class SupportCardBrand:
    def __init__(self):
        
        self.__card_brand = None  # type: str
        self.__logo = None  # type: Logo
        

    @property
    def card_brand(self):
        """
        The name of the card brand. Valid values are:  VISA: indicates Visa.  MASTERCARD: indicates Mastercard.   AMEX: indicates American Express (Amex). HIPERCARD: indicates Hipercard. ELO: indicates Elo.
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def logo(self):
        """Gets the logo of this SupportCardBrand.
        
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_brand") and self.card_brand is not None:
            params['cardBrand'] = self.card_brand
        if hasattr(self, "logo") and self.logo is not None:
            params['logo'] = self.logo
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardBrand' in response_body:
            self.__card_brand = response_body['cardBrand']
        if 'logo' in response_body:
            self.__logo = Logo()
            self.__logo.parse_rsp_body(response_body['logo'])
