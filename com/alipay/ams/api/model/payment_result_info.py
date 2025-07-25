import json
from com.alipay.ams.api.model.three_ds_result import ThreeDSResult
from com.alipay.ams.api.model.credit_pay_plan import CreditPayPlan




class PaymentResultInfo:
    def __init__(self):
        
        self.__card_no = None  # type: str
        self.__card_brand = None  # type: str
        self.__card_token = None  # type: str
        self.__issuing_country = None  # type: str
        self.__funding = None  # type: str
        self.__payment_method_region = None  # type: str
        self.__three_ds_result = None  # type: ThreeDSResult
        self.__avs_result_raw = None  # type: str
        self.__cvv_result_raw = None  # type: str
        self.__network_transaction_id = None  # type: str
        self.__credit_pay_plan = None  # type: CreditPayPlan
        self.__cardholder_name = None  # type: str
        self.__card_bin = None  # type: str
        self.__last_four = None  # type: str
        self.__expiry_month = None  # type: str
        self.__expiry_year = None  # type: str
        

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
        The card brand, which can be used to display to the user
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def card_token(self):
        """
        The token of the card, the value of this parameter is used by paymentMethodId in the pay
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
        The funding type of the card.
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
        """Gets the three_ds_result of this PaymentResultInfo.
        
        """
        return self.__three_ds_result

    @three_ds_result.setter
    def three_ds_result(self, value):
        self.__three_ds_result = value
    @property
    def avs_result_raw(self):
        """
        The raw AVS result. See AVS result codes to check the valid values
        """
        return self.__avs_result_raw

    @avs_result_raw.setter
    def avs_result_raw(self, value):
        self.__avs_result_raw = value
    @property
    def cvv_result_raw(self):
        """
        The raw Card Verification Value (CVV), Card Security Code (CSC), or Card Verification Code (CVC) result
        """
        return self.__cvv_result_raw

    @cvv_result_raw.setter
    def cvv_result_raw(self, value):
        self.__cvv_result_raw = value
    @property
    def network_transaction_id(self):
        """
        The unique ID assigned by the card scheme to identify a transaction. The value of this parameter is used by the same parameter of pay (Cashier Payment) request in subsequent payments
        """
        return self.__network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, value):
        self.__network_transaction_id = value
    @property
    def credit_pay_plan(self):
        """Gets the credit_pay_plan of this PaymentResultInfo.
        
        """
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value
    @property
    def cardholder_name(self):
        """
        The cardholder&#39;s name.  Note: This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD for specific merchants in specific regions.  More information:  Maximum length: 64 characters
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value
    @property
    def card_bin(self):
        """
        The first six digits of the bank card number, used to identify the issuing bank and card type of the bank card.  Note: This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD for specific merchants in specific regions.  More information:  Maximum length: 8 characters
        """
        return self.__card_bin

    @card_bin.setter
    def card_bin(self, value):
        self.__card_bin = value
    @property
    def last_four(self):
        """
        Last 4 digits of the card number.  Note: This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD for specific merchants in specific regions.  More information:  Maximum length: 4 characters 
        """
        return self.__last_four

    @last_four.setter
    def last_four(self, value):
        self.__last_four = value
    @property
    def expiry_month(self):
        """
        The month the card expires. Pass in two digits representing the month. For example, if the expiry month is February, the value of this parameter is 02.  Note: This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD for specific merchants in specific regions.  More information:  Maximum length: 2 characters
        """
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        self.__expiry_month = value
    @property
    def expiry_year(self):
        """
        The year the card expires. Pass in the last two digits of the year number. For example, if the expiry year is 2025, the value of this parameter is 25.  Note: This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD for specific merchants in specific regions.  More information:  Maximum length: 2 characters
        """
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        self.__expiry_year = value


    

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
        if hasattr(self, "avs_result_raw") and self.avs_result_raw is not None:
            params['avsResultRaw'] = self.avs_result_raw
        if hasattr(self, "cvv_result_raw") and self.cvv_result_raw is not None:
            params['cvvResultRaw'] = self.cvv_result_raw
        if hasattr(self, "network_transaction_id") and self.network_transaction_id is not None:
            params['networkTransactionId'] = self.network_transaction_id
        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan is not None:
            params['creditPayPlan'] = self.credit_pay_plan
        if hasattr(self, "cardholder_name") and self.cardholder_name is not None:
            params['cardholderName'] = self.cardholder_name
        if hasattr(self, "card_bin") and self.card_bin is not None:
            params['cardBin'] = self.card_bin
        if hasattr(self, "last_four") and self.last_four is not None:
            params['lastFour'] = self.last_four
        if hasattr(self, "expiry_month") and self.expiry_month is not None:
            params['expiryMonth'] = self.expiry_month
        if hasattr(self, "expiry_year") and self.expiry_year is not None:
            params['expiryYear'] = self.expiry_year
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
        if 'avsResultRaw' in response_body:
            self.__avs_result_raw = response_body['avsResultRaw']
        if 'cvvResultRaw' in response_body:
            self.__cvv_result_raw = response_body['cvvResultRaw']
        if 'networkTransactionId' in response_body:
            self.__network_transaction_id = response_body['networkTransactionId']
        if 'creditPayPlan' in response_body:
            self.__credit_pay_plan = CreditPayPlan()
            self.__credit_pay_plan.parse_rsp_body(response_body['creditPayPlan'])
        if 'cardholderName' in response_body:
            self.__cardholder_name = response_body['cardholderName']
        if 'cardBin' in response_body:
            self.__card_bin = response_body['cardBin']
        if 'lastFour' in response_body:
            self.__last_four = response_body['lastFour']
        if 'expiryMonth' in response_body:
            self.__expiry_month = response_body['expiryMonth']
        if 'expiryYear' in response_body:
            self.__expiry_year = response_body['expiryYear']
