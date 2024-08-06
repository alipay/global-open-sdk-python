from com.alipay.ams.api.model.funding_type import FundingType
from com.alipay.ams.api.model.support_bank import SupportBank
from com.alipay.ams.api.model.support_card_brand import SupportCardBrand


class PaymentOptionDetail(object):

    def __init__(self):
        self.__support_card_brands = None  # type:list[SupportCardBrand]
        self.__funding = None  # type:list[FundingType]
        self.__support_banks = None  # type:list[SupportBank]

    @property
    def support_card_brands(self):
        return self.__support_card_brands

    @support_card_brands.setter
    def support_card_brands(self, value):
        self.__support_card_brands = value

    @property
    def funding(self):
        return self.__funding

    @funding.setter
    def funding(self, value):
        self.__funding = value

    @property
    def support_banks(self):
        return self.__support_banks

    @support_banks.setter
    def support_banks(self, value):
        self.__support_banks = value

    def parse_rsp_body(self, payment_option_detail_body):
        if payment_option_detail_body.has_key("supportCardBrands"):
            self.support_card_brands = payment_option_detail_body["supportCardBrands"]
        if payment_option_detail_body.has_key("funding"):
            self.funding = payment_option_detail_body["funding"]
        if payment_option_detail_body.has_key("supportBanks "):
            self.support_banks = payment_option_detail_body["supportBanks"]
