import json
from com.alipay.ams.api.model.user_name import UserName




class Card:
    def __init__(self):
        
        self.__card_no = None  # type: str
        self.__cvv = None  # type: str
        self.__expiry_year = None  # type: str
        self.__expiry_month = None  # type: str
        self.__cardholder_name = None  # type: UserName
        

    @property
    def card_no(self):
        """Gets the card_no of this Card.
        
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def cvv(self):
        """Gets the cvv of this Card.
        
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value
    @property
    def expiry_year(self):
        """Gets the expiry_year of this Card.
        
        """
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        self.__expiry_year = value
    @property
    def expiry_month(self):
        """Gets the expiry_month of this Card.
        
        """
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        self.__expiry_month = value
    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this Card.
        
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_no") and self.card_no is not None:
            params['cardNo'] = self.card_no
        if hasattr(self, "cvv") and self.cvv is not None:
            params['cvv'] = self.cvv
        if hasattr(self, "expiry_year") and self.expiry_year is not None:
            params['expiryYear'] = self.expiry_year
        if hasattr(self, "expiry_month") and self.expiry_month is not None:
            params['expiryMonth'] = self.expiry_month
        if hasattr(self, "cardholder_name") and self.cardholder_name is not None:
            params['cardholderName'] = self.cardholder_name
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardNo' in response_body:
            self.__card_no = response_body['cardNo']
        if 'cvv' in response_body:
            self.__cvv = response_body['cvv']
        if 'expiryYear' in response_body:
            self.__expiry_year = response_body['expiryYear']
        if 'expiryMonth' in response_body:
            self.__expiry_month = response_body['expiryMonth']
        if 'cardholderName' in response_body:
            self.__cardholder_name = UserName()
            self.__cardholder_name.parse_rsp_body(response_body['cardholderName'])
