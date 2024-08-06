import json

from com.alipay.ams.api.model.plan import Plan
from com.alipay.ams.api.model.support_card_brand import SupportCardBrand


class Installment(object):
    def __init__(self):
        self.__support_card_brands = None  # type: list[SupportCardBrand]
        self.__plans = None  # type: list[Plan]

    @property
    def support_card_brands(self):
        return self.__support_card_brands

    @support_card_brands.setter
    def support_card_brands(self, value):
        self.__support_card_brands = value

    @property
    def plans(self):
        return self.__plans

    @plans.setter
    def plans(self, value):
        self.__plans = value

    def parse_rsp_body(self, installment_body):
        if type(installment_body) == str:
            installment_body = json.loads(installment_body)
        if 'supportCardBrand' in installment_body:
            self.support_card_brands = installment_body.get('supportCardBrand')
            for support_card_brand in self.support_card_brands:
                support_card_brand.parse_rsp_body(support_card_brand)
                self.support_card_brands = support_card_brand

        if 'plans' in installment_body:
            self.plans = installment_body.get('plans')
            for plan in self.plans:
                plan.parse_rsp_body(plan)
                self.plans = plan
