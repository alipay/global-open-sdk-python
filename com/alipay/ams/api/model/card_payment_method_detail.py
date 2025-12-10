import json
from com.alipay.ams.api.model.card_brand import CardBrand
from com.alipay.ams.api.model.card_brand import CardBrand
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.mpi_data import MpiData




class CardPaymentMethodDetail:
    def __init__(self):
        
        self.__supported_brands = None  # type: str
        self.__card_token = None  # type: str
        self.__card_no = None  # type: str
        self.__brand = None  # type: CardBrand
        self.__selected_card_brand = None  # type: CardBrand
        self.__card_issuer = None  # type: str
        self.__country_issue = None  # type: str
        self.__inst_user_name = None  # type: UserName
        self.__expiry_year = None  # type: str
        self.__expiry_month = None  # type: str
        self.__billing_address = None  # type: Address
        self.__mask = None  # type: str
        self.__last4 = None  # type: str
        self.__payment_method_detail_metadata = None  # type: str
        self.__masked_card_no = None  # type: str
        self.__fingerprint = None  # type: str
        self.__authentication_flow = None  # type: str
        self.__funding = None  # type: str
        self.__avs_result_raw = None  # type: str
        self.__cvv_result_raw = None  # type: str
        self.__bin = None  # type: str
        self.__issuer_name = None  # type: str
        self.__issuing_country = None  # type: str
        self.__last_four = None  # type: str
        self.__cardholder_name = None  # type: UserName
        self.__cvv = None  # type: str
        self.__date_of_birth = None  # type: str
        self.__business_no = None  # type: str
        self.__card_password_digest = None  # type: str
        self.__cpf = None  # type: str
        self.__payer_email = None  # type: str
        self.__network_transaction_id = None  # type: str
        self.__is3_ds_authentication = None  # type: bool
        self.__request3_ds = None  # type: str
        self.__sca_exemption_indicator = None  # type: str
        self.__enable_authentication_upgrade = None  # type: str
        self.__mpi_data = None  # type: MpiData
        

    @property
    def supported_brands(self):
        """
        Supported card brands for this payment method
        """
        return self.__supported_brands

    @supported_brands.setter
    def supported_brands(self, value):
        self.__supported_brands = value
    @property
    def card_token(self):
        """
        The token of the card. The value of this parameter is used by paymentMethodId in the pay (Checkout Payment) API when initiating payments.   More information:  Maximum length: 2048 characters
        """
        return self.__card_token

    @card_token.setter
    def card_token(self, value):
        self.__card_token = value
    @property
    def card_no(self):
        """
        The card number.   More information:  Maximum length: 32 characters
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def brand(self):
        """Gets the brand of this CardPaymentMethodDetail.
        
        """
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value
    @property
    def selected_card_brand(self):
        """Gets the selected_card_brand of this CardPaymentMethodDetail.
        
        """
        return self.__selected_card_brand

    @selected_card_brand.setter
    def selected_card_brand(self, value):
        self.__selected_card_brand = value
    @property
    def card_issuer(self):
        """Gets the card_issuer of this CardPaymentMethodDetail.
        
        """
        return self.__card_issuer

    @card_issuer.setter
    def card_issuer(self, value):
        self.__card_issuer = value
    @property
    def country_issue(self):
        """Gets the country_issue of this CardPaymentMethodDetail.
        
        """
        return self.__country_issue

    @country_issue.setter
    def country_issue(self, value):
        self.__country_issue = value
    @property
    def inst_user_name(self):
        """Gets the inst_user_name of this CardPaymentMethodDetail.
        
        """
        return self.__inst_user_name

    @inst_user_name.setter
    def inst_user_name(self, value):
        self.__inst_user_name = value
    @property
    def expiry_year(self):
        """
        The year the card expires. Pass in the last two digits of the year number. For example, if the expiration year is 2025, the value of this parameter is 25.   More information:  Maximum length: 2 characters
        """
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        self.__expiry_year = value
    @property
    def expiry_month(self):
        """
        The month the card expires. Pass in two digits representing the month. For example, if the expiration month is February, the value of this parameter is 02.   More information:  Maximum length: 2 characters
        """
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        self.__expiry_month = value
    @property
    def billing_address(self):
        """Gets the billing_address of this CardPaymentMethodDetail.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value
    @property
    def mask(self):
        """Gets the mask of this CardPaymentMethodDetail.
        
        """
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value
    @property
    def last4(self):
        """Gets the last4 of this CardPaymentMethodDetail.
        
        """
        return self.__last4

    @last4.setter
    def last4(self, value):
        self.__last4 = value
    @property
    def payment_method_detail_metadata(self):
        """Gets the payment_method_detail_metadata of this CardPaymentMethodDetail.
        
        """
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value
    @property
    def masked_card_no(self):
        """
        The masked card number, showing only a few digits and hiding the rest.   More information:  Maximum length: 64 characters
        """
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value
    @property
    def fingerprint(self):
        """Gets the fingerprint of this CardPaymentMethodDetail.
        
        """
        return self.__fingerprint

    @fingerprint.setter
    def fingerprint(self, value):
        self.__fingerprint = value
    @property
    def authentication_flow(self):
        """Gets the authentication_flow of this CardPaymentMethodDetail.
        
        """
        return self.__authentication_flow

    @authentication_flow.setter
    def authentication_flow(self, value):
        self.__authentication_flow = value
    @property
    def funding(self):
        """Gets the funding of this CardPaymentMethodDetail.
        
        """
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value
    @property
    def avs_result_raw(self):
        """Gets the avs_result_raw of this CardPaymentMethodDetail.
        
        """
        return self.__avs_result_raw

    @avs_result_raw.setter
    def avs_result_raw(self, value):
        self.__avs_result_raw = value
    @property
    def cvv_result_raw(self):
        """Gets the cvv_result_raw of this CardPaymentMethodDetail.
        
        """
        return self.__cvv_result_raw

    @cvv_result_raw.setter
    def cvv_result_raw(self, value):
        self.__cvv_result_raw = value
    @property
    def bin(self):
        """Gets the bin of this CardPaymentMethodDetail.
        
        """
        return self.__bin

    @bin.setter
    def bin(self, value):
        self.__bin = value
    @property
    def issuer_name(self):
        """Gets the issuer_name of this CardPaymentMethodDetail.
        
        """
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self.__issuer_name = value
    @property
    def issuing_country(self):
        """Gets the issuing_country of this CardPaymentMethodDetail.
        
        """
        return self.__issuing_country

    @issuing_country.setter
    def issuing_country(self, value):
        self.__issuing_country = value
    @property
    def last_four(self):
        """Gets the last_four of this CardPaymentMethodDetail.
        
        """
        return self.__last_four

    @last_four.setter
    def last_four(self, value):
        self.__last_four = value
    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this CardPaymentMethodDetail.
        
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value
    @property
    def cvv(self):
        """
        The card verification value (CVV), which is also known as a card security code (CSC) or a card verification code (CVC).   Note: Specify this parameter when the card issuing bank is in Brazil, Chile, Mexico, or Peru, or the card is a global card.  More information:  Maximum length: 3 characters
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value
    @property
    def date_of_birth(self):
        """
        The date of birth of the cardholder. The value of this parameter is an 8-digit date of birth in the format of YYYY-MM-DD that follows the ISO 8601 standard. For example, 1971-06-07 means the cardholder&#39;s birthday is June 7, 1971.  Specify this parameter when all the following conditions are met:  The card issuing bank is in Korea. The card is a personal card. More information:  Maximum length: 10 characters
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value
    @property
    def business_no(self):
        """
        The business number of the company that holds the corporate card. The value of this parameter is a 10-digit business number, such as 97XXXXXX11.  Specify this parameter when all the following conditions are met:  The card issuing bank is in Korea. The card is a corporate card. More information:  Maximum length: 10 characters 
        """
        return self.__business_no

    @business_no.setter
    def business_no(self, value):
        self.__business_no = value
    @property
    def card_password_digest(self):
        """
        The first two digits of the card payment password.  Note: Specify this parameter when the card issuing bank is in Korea.  More information:  Maximum length: 2 characters 
        """
        return self.__card_password_digest

    @card_password_digest.setter
    def card_password_digest(self, value):
        self.__card_password_digest = value
    @property
    def cpf(self):
        """
        The Cadastro Pessoal de Pessoa Física (CPF) is the tax ID of the Brazilian individual taxpayer.  Note: Specify this parameter when the card issuing bank is in Brazil.  More information:  Maximum length: 11 characters
        """
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value
    @property
    def payer_email(self):
        """
        The email address of the payer.   Note: Specify this parameter when the card issuing bank is in Brazil, Chile, Mexico, or Peru.  More information:  Maximum length: 64 characters 
        """
        return self.__payer_email

    @payer_email.setter
    def payer_email(self, value):
        self.__payer_email = value
    @property
    def network_transaction_id(self):
        """
        The unique ID assigned by the card scheme to identify a transaction.  More information:  Maximum length: 256 characters
        """
        return self.__network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, value):
        self.__network_transaction_id = value
    @property
    def is3_ds_authentication(self):
        """
        Indicates whether the transaction authentication type is 3D secure. Specify this parameter when the value of paymentMethodType is CARD.  
        """
        return self.__is3_ds_authentication

    @is3_ds_authentication.setter
    def is3_ds_authentication(self, value):
        self.__is3_ds_authentication = value
    @property
    def request3_ds(self):
        """Gets the request3_ds of this CardPaymentMethodDetail.
        
        """
        return self.__request3_ds

    @request3_ds.setter
    def request3_ds(self, value):
        self.__request3_ds = value
    @property
    def sca_exemption_indicator(self):
        """Gets the sca_exemption_indicator of this CardPaymentMethodDetail.
        
        """
        return self.__sca_exemption_indicator

    @sca_exemption_indicator.setter
    def sca_exemption_indicator(self, value):
        self.__sca_exemption_indicator = value
    @property
    def enable_authentication_upgrade(self):
        """Gets the enable_authentication_upgrade of this CardPaymentMethodDetail.
        
        """
        return self.__enable_authentication_upgrade

    @enable_authentication_upgrade.setter
    def enable_authentication_upgrade(self, value):
        self.__enable_authentication_upgrade = value
    @property
    def mpi_data(self):
        """Gets the mpi_data of this CardPaymentMethodDetail.
        
        """
        return self.__mpi_data

    @mpi_data.setter
    def mpi_data(self, value):
        self.__mpi_data = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "supported_brands") and self.supported_brands is not None:
            params['supportedBrands'] = self.supported_brands
        if hasattr(self, "card_token") and self.card_token is not None:
            params['cardToken'] = self.card_token
        if hasattr(self, "card_no") and self.card_no is not None:
            params['cardNo'] = self.card_no
        if hasattr(self, "brand") and self.brand is not None:
            params['brand'] = self.brand
        if hasattr(self, "selected_card_brand") and self.selected_card_brand is not None:
            params['selectedCardBrand'] = self.selected_card_brand
        if hasattr(self, "card_issuer") and self.card_issuer is not None:
            params['cardIssuer'] = self.card_issuer
        if hasattr(self, "country_issue") and self.country_issue is not None:
            params['countryIssue'] = self.country_issue
        if hasattr(self, "inst_user_name") and self.inst_user_name is not None:
            params['instUserName'] = self.inst_user_name
        if hasattr(self, "expiry_year") and self.expiry_year is not None:
            params['expiryYear'] = self.expiry_year
        if hasattr(self, "expiry_month") and self.expiry_month is not None:
            params['expiryMonth'] = self.expiry_month
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "mask") and self.mask is not None:
            params['mask'] = self.mask
        if hasattr(self, "last4") and self.last4 is not None:
            params['last4'] = self.last4
        if hasattr(self, "payment_method_detail_metadata") and self.payment_method_detail_metadata is not None:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        if hasattr(self, "masked_card_no") and self.masked_card_no is not None:
            params['maskedCardNo'] = self.masked_card_no
        if hasattr(self, "fingerprint") and self.fingerprint is not None:
            params['fingerprint'] = self.fingerprint
        if hasattr(self, "authentication_flow") and self.authentication_flow is not None:
            params['authenticationFlow'] = self.authentication_flow
        if hasattr(self, "funding") and self.funding is not None:
            params['funding'] = self.funding
        if hasattr(self, "avs_result_raw") and self.avs_result_raw is not None:
            params['avsResultRaw'] = self.avs_result_raw
        if hasattr(self, "cvv_result_raw") and self.cvv_result_raw is not None:
            params['cvvResultRaw'] = self.cvv_result_raw
        if hasattr(self, "bin") and self.bin is not None:
            params['bin'] = self.bin
        if hasattr(self, "issuer_name") and self.issuer_name is not None:
            params['issuerName'] = self.issuer_name
        if hasattr(self, "issuing_country") and self.issuing_country is not None:
            params['issuingCountry'] = self.issuing_country
        if hasattr(self, "last_four") and self.last_four is not None:
            params['lastFour'] = self.last_four
        if hasattr(self, "cardholder_name") and self.cardholder_name is not None:
            params['cardholderName'] = self.cardholder_name
        if hasattr(self, "cvv") and self.cvv is not None:
            params['cvv'] = self.cvv
        if hasattr(self, "date_of_birth") and self.date_of_birth is not None:
            params['dateOfBirth'] = self.date_of_birth
        if hasattr(self, "business_no") and self.business_no is not None:
            params['businessNo'] = self.business_no
        if hasattr(self, "card_password_digest") and self.card_password_digest is not None:
            params['cardPasswordDigest'] = self.card_password_digest
        if hasattr(self, "cpf") and self.cpf is not None:
            params['cpf'] = self.cpf
        if hasattr(self, "payer_email") and self.payer_email is not None:
            params['payerEmail'] = self.payer_email
        if hasattr(self, "network_transaction_id") and self.network_transaction_id is not None:
            params['networkTransactionId'] = self.network_transaction_id
        if hasattr(self, "is3_ds_authentication") and self.is3_ds_authentication is not None:
            params['is3DSAuthentication'] = self.is3_ds_authentication
        if hasattr(self, "request3_ds") and self.request3_ds is not None:
            params['request3DS'] = self.request3_ds
        if hasattr(self, "sca_exemption_indicator") and self.sca_exemption_indicator is not None:
            params['scaExemptionIndicator'] = self.sca_exemption_indicator
        if hasattr(self, "enable_authentication_upgrade") and self.enable_authentication_upgrade is not None:
            params['enableAuthenticationUpgrade'] = self.enable_authentication_upgrade
        if hasattr(self, "mpi_data") and self.mpi_data is not None:
            params['mpiData'] = self.mpi_data
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'supportedBrands' in response_body:
            self.__supported_brands = response_body['supportedBrands']
        if 'cardToken' in response_body:
            self.__card_token = response_body['cardToken']
        if 'cardNo' in response_body:
            self.__card_no = response_body['cardNo']
        if 'brand' in response_body:
            brand_temp = CardBrand.value_of(response_body['brand'])
            self.__brand = brand_temp
        if 'selectedCardBrand' in response_body:
            selected_card_brand_temp = CardBrand.value_of(response_body['selectedCardBrand'])
            self.__selected_card_brand = selected_card_brand_temp
        if 'cardIssuer' in response_body:
            self.__card_issuer = response_body['cardIssuer']
        if 'countryIssue' in response_body:
            self.__country_issue = response_body['countryIssue']
        if 'instUserName' in response_body:
            self.__inst_user_name = UserName()
            self.__inst_user_name.parse_rsp_body(response_body['instUserName'])
        if 'expiryYear' in response_body:
            self.__expiry_year = response_body['expiryYear']
        if 'expiryMonth' in response_body:
            self.__expiry_month = response_body['expiryMonth']
        if 'billingAddress' in response_body:
            self.__billing_address = Address()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'mask' in response_body:
            self.__mask = response_body['mask']
        if 'last4' in response_body:
            self.__last4 = response_body['last4']
        if 'paymentMethodDetailMetadata' in response_body:
            self.__payment_method_detail_metadata = response_body['paymentMethodDetailMetadata']
        if 'maskedCardNo' in response_body:
            self.__masked_card_no = response_body['maskedCardNo']
        if 'fingerprint' in response_body:
            self.__fingerprint = response_body['fingerprint']
        if 'authenticationFlow' in response_body:
            self.__authentication_flow = response_body['authenticationFlow']
        if 'funding' in response_body:
            self.__funding = response_body['funding']
        if 'avsResultRaw' in response_body:
            self.__avs_result_raw = response_body['avsResultRaw']
        if 'cvvResultRaw' in response_body:
            self.__cvv_result_raw = response_body['cvvResultRaw']
        if 'bin' in response_body:
            self.__bin = response_body['bin']
        if 'issuerName' in response_body:
            self.__issuer_name = response_body['issuerName']
        if 'issuingCountry' in response_body:
            self.__issuing_country = response_body['issuingCountry']
        if 'lastFour' in response_body:
            self.__last_four = response_body['lastFour']
        if 'cardholderName' in response_body:
            self.__cardholder_name = UserName()
            self.__cardholder_name.parse_rsp_body(response_body['cardholderName'])
        if 'cvv' in response_body:
            self.__cvv = response_body['cvv']
        if 'dateOfBirth' in response_body:
            self.__date_of_birth = response_body['dateOfBirth']
        if 'businessNo' in response_body:
            self.__business_no = response_body['businessNo']
        if 'cardPasswordDigest' in response_body:
            self.__card_password_digest = response_body['cardPasswordDigest']
        if 'cpf' in response_body:
            self.__cpf = response_body['cpf']
        if 'payerEmail' in response_body:
            self.__payer_email = response_body['payerEmail']
        if 'networkTransactionId' in response_body:
            self.__network_transaction_id = response_body['networkTransactionId']
        if 'is3DSAuthentication' in response_body:
            self.__is3_ds_authentication = response_body['is3DSAuthentication']
        if 'request3DS' in response_body:
            self.__request3_ds = response_body['request3DS']
        if 'scaExemptionIndicator' in response_body:
            self.__sca_exemption_indicator = response_body['scaExemptionIndicator']
        if 'enableAuthenticationUpgrade' in response_body:
            self.__enable_authentication_upgrade = response_body['enableAuthenticationUpgrade']
        if 'mpiData' in response_body:
            self.__mpi_data = MpiData()
            self.__mpi_data.parse_rsp_body(response_body['mpiData'])
