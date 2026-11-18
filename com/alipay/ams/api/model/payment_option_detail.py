import json
from com.alipay.ams.api.model.support_card_brand import SupportCardBrand
from com.alipay.ams.api.model.support_bank import SupportBank




class PaymentOptionDetail:
    def __init__(self):
        
        self.__support_card_brands = None  # type: [SupportCardBrand]
        self.__funding = None  # type: [str]
        self.__support_banks = None  # type: [SupportBank]
        self.__interaction_types = None  # type: [str]
        

    @property
    def support_card_brands(self):
        """
        The list of supported card brands.    Note: This parameter is returned when the value of paymentMethodType is ​CARD​.
        """
        return self.__support_card_brands

    @support_card_brands.setter
    def support_card_brands(self, value):
        self.__support_card_brands = value
    @property
    def funding(self):
        """
        The funding type of the card. Valid values are:   CREDIT: indicates a credit card.  DEBIT: indicates a debit card.  PREPAID: indicates a prepaid card CHARGE: indicates a charge card DEFERRED_DEBIT: indicates a deferred debit card This parameter is returned when all the following conditions are met:  The value of paymentMethodType is CARD. The value of cardNo is valid. The information is available in the Antom card database.
        """
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value
    @property
    def support_banks(self):
        """
        The list of supported banks.   This parameter is returned when the value of paymentMethodType is ​P24​ or ONLINEBANKING_FPX.  
        """
        return self.__support_banks

    @support_banks.setter
    def support_banks(self, value):
        self.__support_banks = value
    @property
    def interaction_types(self):
        """
        表示支付方式支持的交互类型，有效取值包括QR(扫码支付)和REDIRECT(重定向支付)
        """
        return self.__interaction_types

    @interaction_types.setter
    def interaction_types(self, value):
        self.__interaction_types = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "support_card_brands") and self.support_card_brands is not None:
            params['supportCardBrands'] = self.support_card_brands
        if hasattr(self, "funding") and self.funding is not None:
            params['funding'] = self.funding
        if hasattr(self, "support_banks") and self.support_banks is not None:
            params['supportBanks'] = self.support_banks
        if hasattr(self, "interaction_types") and self.interaction_types is not None:
            params['interactionTypes'] = self.interaction_types
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'supportCardBrands' in response_body:
            self.__support_card_brands = []
            for item in response_body['supportCardBrands']:
                obj = SupportCardBrand()
                obj.parse_rsp_body(item)
                self.__support_card_brands.append(obj)
        if 'funding' in response_body:
            self.__funding = response_body['funding']
        if 'supportBanks' in response_body:
            self.__support_banks = []
            for item in response_body['supportBanks']:
                obj = SupportBank()
                obj.parse_rsp_body(item)
                self.__support_banks.append(obj)
        if 'interactionTypes' in response_body:
            self.__interaction_types = response_body['interactionTypes']
