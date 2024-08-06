import json


class PaymentResultInfo(object):

    def __init__(self):
        self.__avs_result_raw = None
        self.__cvv_result_raw = None
        self.__network_transaction_id = None
        self.__card_no = None
        self.__card_brand = None
        self.__card_token = None
        self.__issuing_country = None
        self.__funding = None
        self.__payment_method_region = None
        self.__three_dS_result = None  # type: ThreeDSResult
        self.__credit_pay_plan = None

    @property
    def avs_result_raw(self):
        return self.__avs_result_raw

    @avs_result_raw.setter
    def avs_result_raw(self, value):
        self.__avs_result_raw = value

    @property
    def cvv_result_raw(self):
        return self.__cvv_result_raw

    @cvv_result_raw.setter
    def cvv_result_raw(self, value):
        self.__cvv_result_raw = value

    @property
    def network_transaction_id(self):
        return self.__network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, value):
        self.__network_transaction_id = value

    @property
    def card_no(self):
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value

    @property
    def card_brand(self):
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value

    @property
    def card_token(self):
        return self.__card_token

    @card_token.setter
    def card_token(self, value):
        self.__card_token = value

    @property
    def issuing_country(self):
        return self.__issuing_country

    @issuing_country.setter
    def issuing_country(self, value):
        self.__issuing_country = value

    @property
    def funding(self):
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value

    @property
    def payment_method_region(self):
        return self.__payment_method_region

    @payment_method_region.setter
    def payment_method_region(self, value):
        self.__payment_method_region = value

    @property
    def three_dS_result(self):
        return self.__three_dS_result

    @three_dS_result.setter
    def three_dS_result(self, value):
        self.__three_dS_result = value

    @property
    def credit_pay_plan(self):
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value

    def to_ams_dict(self):
        param = dict()
        if hasattr(self, 'avs_result_raw') and self.avs_result_raw:
            param['avsResultRaw'] = self.avs_result_raw
        if hasattr(self, 'cvv_result_raw') and self.cvv_result_raw:
            param['cvvResultRaw'] = self.cvv_result_raw
        if hasattr(self, 'network_transaction_id') and self.network_transaction_id:
            param['networkTransactionId'] = self.network_transaction_id
        if hasattr(self, 'card_no') and self.card_no:
            param['cardNo'] = self.card_no
        if hasattr(self, 'card_brand') and self.card_brand:
            param['cardBrand'] = self.card_brand
        if hasattr(self, 'card_token') and self.card_token:
            param['cardToken'] = self.card_token
        if hasattr(self, 'issuing_country') and self.issuing_country:
            param['issuingCountry'] = self.issuing_country
        if hasattr(self, 'funding') and self.funding:
            param['funding'] = self.funding
        if hasattr(self, 'payment_method_region') and self.payment_method_region:
            param['paymentMethodRegion'] = self.payment_method_region
        if hasattr(self, 'three_dS_result') and self.three_dS_result:
            param['threeDSResult'] = self.three_dS_result
        if hasattr(self, 'credit_pay_plan') and self.credit_pay_plan:
            param['creditPayPlan'] = self.credit_pay_plan

        return param

    def parse_rsp_body(self, payment_result_info_body):
        if type(payment_result_info_body) == str:
            payment_result_info_body = json.loads(payment_result_info_body)

        if 'avsResultRaw' in payment_result_info_body:
            self.avs_result_raw = payment_result_info_body['avsResultRaw']
        if 'cvvResultRaw' in payment_result_info_body:
            self.cvv_result_raw = payment_result_info_body['cvvResultRaw']
        if 'networkTransactionId' in payment_result_info_body:
            self.network_transaction_id = payment_result_info_body['networkTransactionId']
        if 'cardNo' in payment_result_info_body:
            self.card_no = payment_result_info_body['cardNo']
        if 'cardBrand' in payment_result_info_body:
            self.card_brand = payment_result_info_body['cardBrand']
        if 'cardToken' in payment_result_info_body:
            self.card_token = payment_result_info_body['cardToken']
        if 'issuingCountry' in payment_result_info_body:
            self.issuing_country = payment_result_info_body['issuingCountry']
        if 'funding' in payment_result_info_body:
            self.funding = payment_result_info_body['funding']
        if 'paymentMethodRegion' in payment_result_info_body:
            self.payment_method_region = payment_result_info_body['paymentMethodRegion']
        if 'threeDSResult' in payment_result_info_body:
            self.three_dS_result = payment_result_info_body['threeDSResult']
        if 'creditPayPlan' in payment_result_info_body:
            self.credit_pay_plan = payment_result_info_body['creditPayPlan']
