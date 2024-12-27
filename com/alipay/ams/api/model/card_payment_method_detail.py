#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.card_brand import CardBrand
from com.alipay.ams.api.model.user_name import UserName


class CardPaymentMethodDetail(object):

    def __init__(self):
        self.__card_token = None
        self.__card_no = None
        self.__brand = None # type: CardBrand
        self.__selected_card_brand = None # type: CardBrand
        self.__card_issuer = None
        self.__country_issue = None
        self.__inst_user_name = None  # type: UserName
        self.__expiry_year = None
        self.__expiry_month = None
        self.__billing_address = None  # type: Address
        self.__mask = None
        self.__last4 = None
        self.__payment_method_detail_metadata = None

        self.__masked_card_no = None
        self.__fingerprint = None
        self.__authentication_flow = None
        self.__funding = None
        self.__avs_result_raw = None
        self.__bin = None
        self.__issuer_name = None
        self.__issuing_country = None
        self.__last_four = None
        self.__cardholder_name = None
        self.__cvv = None
        self.__date_of_birth = None
        self.__businessNo = None
        self.__card_password_digest = None
        self.__cpf = None
        self.__payer_email = None
        self.__network_transaction_id = None
        self.__is_3DS_authentication = None

    @property
    def card_token(self):
        return self.__card_token
    @card_token.setter
    def card_token(self, value):
        self.__card_token = value

    @property
    def card_no(self):
        return self.__card_no
    @card_no.setter
    def card_no(self, value):
        self.__card_no = value

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def selected_card_brand(self):
        return self.__selected_card_brand

    @selected_card_brand.setter
    def selected_card_brand(self, value):
        self.__selected_card_brand = value

    @property
    def card_issuer(self):
        return self.__card_issuer

    @card_issuer.setter
    def card_issuer(self, value):
        self.__card_issuer = value

    @property
    def country_issue(self):
        return self.__country_issue
    @country_issue.setter
    def country_issue(self, value):
        self.__country_issue = value

    @property
    def inst_user_name(self):
        return self.__inst_user_name

    @inst_user_name.setter
    def inst_user_name(self, value):
        self.__inst_user_name = value

    @property
    def expiry_year(self):
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        self.__expiry_year = value

    @property
    def expiry_month(self):
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        self.__expiry_month = value

    @property
    def billing_address(self):
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value

    @property
    def mask(self):
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value

    @property
    def last4(self):
        return self.__last4

    @last4.setter
    def last4(self, value):
        self.__last4 = value

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value

    @property
    def masked_card_no(self):
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value

    @property
    def fingerprint(self):
        return self.__fingerprint

    @fingerprint.setter
    def fingerprint(self, value):
        self.__fingerprint = value

    @property
    def authentication_flow(self):
        return self.__authentication_flow

    @authentication_flow.setter
    def authentication_flow(self, value):
        self.__authentication_flow = value

    @property
    def funding(self):
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value

    @property
    def avs_result_raw(self):
        return self.__avs_result_raw

    @avs_result_raw.setter
    def avs_result_raw(self, value):
        self.__avs_result_raw = value

    @property
    def bin(self):
        return self.__bin

    @bin.setter
    def bin(self, value):
        self.__bin = value

    @property
    def issuer_name(self):
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self.__issuer_name = value

    @property
    def issuing_country(self):
        return self.__issuing_country

    @issuing_country.setter
    def issuing_country(self, value):
        self.__issuing_country = value

    @property
    def last_four(self):
        return self.__last_four

    @last_four.setter
    def last_four(self, value):
        self.__last_four = value

    @property
    def cardholder_name(self):
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def cvv(self):
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def businessNo(self):
        return self.__businessNo

    @businessNo.setter
    def businessNo(self, value):
        self.__businessNo = value

    @property
    def card_password_digest(self):
        return self.__card_password_digest

    @card_password_digest.setter
    def card_password_digest(self, value):
        self.__card_password_digest = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def payer_email(self):
        return self.__payer_email

    @payer_email.setter
    def payer_email(self, value):
        self.__payer_email = value

    @property
    def network_transaction_id(self):
        return self.__network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, value):
        self.__network_transaction_id = value

    @property
    def is_3DS_authentication(self):
        return self.__is_3DS_authentication

    @is_3DS_authentication.setter
    def is_3DS_authentication(self, value):
        self.__is_3DS_authentication = value


    def parse_rsp_body(self, card_payment_method_detail_body):
        if type(card_payment_method_detail_body) == str:
            card_payment_method_detail_body = json.loads(card_payment_method_detail_body)

        if 'cardToken' in card_payment_method_detail_body:
            self.__card_token = card_payment_method_detail_body['cardToken']

        if 'cardNo' in card_payment_method_detail_body:
            self.__card_no = card_payment_method_detail_body['cardNo']

        if 'brand' in card_payment_method_detail_body:
            card_no = CardBrand.value_of(card_payment_method_detail_body['brand'])
            self.__card_no = card_no

        if 'selectedCardBrand' in card_payment_method_detail_body:
            card_no = CardBrand.value_of(card_payment_method_detail_body['selectedCardBrand'])
            self.__selected_card_brand = card_no

        if 'cardIssuer' in card_payment_method_detail_body:
            self.__card_issuer = card_payment_method_detail_body['cardIssuer']

        if 'countryIssue' in card_payment_method_detail_body:
            self.__country_issue = card_payment_method_detail_body['countryIssue']

        if 'instUserName' in card_payment_method_detail_body:
            inst_user_name = UserName()
            inst_user_name.parse_rsp_body(card_payment_method_detail_body['instUserName'])
            self.__inst_user_name = inst_user_name

        if 'expiryYear' in card_payment_method_detail_body:
            self.__expiry_year = card_payment_method_detail_body['expiryYear']

        if 'expiryMonth' in card_payment_method_detail_body:
            self.__expiry_month = card_payment_method_detail_body['expiryMonth']

        if 'billingAddress' in card_payment_method_detail_body:
            billing_address = Address()
            billing_address.parse_rsp_body(card_payment_method_detail_body['billingAddress'])
            self.__billing_address = billing_address

        if 'mask' in card_payment_method_detail_body:
            self.__mask = card_payment_method_detail_body['mask']

        if 'last4' in card_payment_method_detail_body:
            self.__last4 = card_payment_method_detail_body['last4']

        if 'paymentMethodDetailMetadata' in card_payment_method_detail_body:
            self.__payment_method_detail_metadata = card_payment_method_detail_body['paymentMethodDetailMetadata']

        if 'maskedCardNo' in card_payment_method_detail_body:
            self.__masked_card_no = card_payment_method_detail_body['maskedCardNo']

        if 'fingerprint' in card_payment_method_detail_body:
            self.__fingerprint = card_payment_method_detail_body['fingerprint']

        if 'authenticationFlow' in card_payment_method_detail_body:
            self.__authentication_flow = card_payment_method_detail_body['authenticationFlow']

        if 'funding' in card_payment_method_detail_body:
            self.__funding = card_payment_method_detail_body['funding']

        if 'avsResultRaw' in card_payment_method_detail_body:
            self.__avs_result_raw = card_payment_method_detail_body['avsResultRaw']

        if 'bin' in card_payment_method_detail_body:
            self.__bin = card_payment_method_detail_body['bin']

        if 'issuerName' in card_payment_method_detail_body:
            self.__issuer_name = card_payment_method_detail_body['issuerName']

        if 'issuingCountry' in card_payment_method_detail_body:
            self.__issuing_country = card_payment_method_detail_body['issuingCountry']

        if 'lastFour' in card_payment_method_detail_body:
            self.__last_four = card_payment_method_detail_body['lastFour']

        if 'cardholderName' in card_payment_method_detail_body:
            self.__cardholder_name = card_payment_method_detail_body['cardholderName']

        if 'cvv' in card_payment_method_detail_body:
            self.__cvv = card_payment_method_detail_body['cvv']

        if 'dateOfBirth' in card_payment_method_detail_body:
            self.__date_of_birth = card_payment_method_detail_body['dateOfBirth']

        if 'businessNo' in card_payment_method_detail_body:
            self.__businessNo = card_payment_method_detail_body['businessNo']

        if 'cardPasswordDigest' in card_payment_method_detail_body:
            self.__card_password_digest = card_payment_method_detail_body['cardPasswordDigest']

        if 'cpf' in card_payment_method_detail_body:
            self.__cpf = card_payment_method_detail_body['cpf']

        if 'payerEmail' in card_payment_method_detail_body:
            self.__payer_email = card_payment_method_detail_body['payerEmail']
        if 'networkTransactionId' in card_payment_method_detail_body:
            self.__network_transaction_id = card_payment_method_detail_body['networkTransactionId']
        if 'is3DSAuthentication' in card_payment_method_detail_body:
            self.__is_3DS_authentication = card_payment_method_detail_body['is3DSAuthentication']

    def to_ams_dict(self):
        params = dict()
        if self.card_token:
            params['cardToken'] = self.card_token
        if self.card_no:
            params['cardNo'] = self.card_no
        if self.brand:
            params['brand'] = self.brand.name
        if self.selected_card_brand:
            params['selectedCardBrand'] = self.selected_card_brand.name
        if self.card_issuer:
            params['cardIssuer'] = self.card_issuer
        if self.country_issue:
            params['countryIssue'] = self.country_issue
        if self.inst_user_name:
            params['instUserName'] = self.inst_user_name.to_ams_dict()
        if self.expiry_year:
            params['expiryYear'] = self.expiry_year
        if self.expiry_month:
            params['expiryMonth'] = self.expiry_month
        if self.billing_address:
            params['billingAddress'] = self.billing_address.to_ams_dict()
        if self.mask:
            params['mask'] = self.mask
        if self.last4:
            params['last4'] = self.last4
        if self.payment_method_detail_metadata:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        if self.masked_card_no:
            params['maskedCardNo'] = self.masked_card_no
        if self.fingerprint:
            params['fingerprint'] = self.fingerprint
        if self.authentication_flow:
            params['authenticationFlow'] = self.authentication_flow
        if self.funding:
            params['funding'] = self.funding
        if self.avs_result_raw:
            params['avsResultRaw'] = self.avs_result_raw
        if self.bin:
            params['bin'] = self.bin
        if self.issuer_name:
            params['issuerName'] = self.issuer_name
        if self.issuing_country:
            params['issuingCountry'] = self.issuing_country
        if self.last_four:
            params['lastFour'] = self.last_four
        if self.cardholder_name:
            params['cardholderName'] = self.cardholder_name
        if self.cvv:
            params['cvv'] = self.cvv
        if self.date_of_birth:
            params['dateOfBirth'] = self.date_of_birth
        if self.businessNo:
            params['businessNo'] = self.businessNo
        if self.card_password_digest:
            params['cardPasswordDigest'] = self.card_password_digest
        if self.cpf:
            params['cpf'] = self.cpf
        if self.payer_email:
            params['payerEmail'] = self.payer_email
        if self.network_transaction_id:
            params['networkTransactionId'] = self.network_transaction_id
        if self.is_3DS_authentication:
            params['is3DSAuthentication'] = self.is_3DS_authentication
        return params