from com.alipay.ams.api.model.card_brand_type import CardBrandType
from com.alipay.ams.api.model.logo import Logo


class SupportCardBrand(object):
    def __init__(self):
        self.__card_brand = None  # type: CardBrandType
        self.__logo = None  # type: Logo

    @property
    def card_brand(self):
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value

    @property
    def logo(self):
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_brand") and self.card_brand:
            params['cardBrandType'] = self.card_brand.value
        if hasattr(self, "logo") and self.logo:
            params['logo'] = self.logo.to_ams_dict()
        return params

    def parse_rsp_body(self, support_card_brand_body):
        if support_card_brand_body.get('cardBrandType'):
            self.card_brand = CardBrandType(support_card_brand_body.get('cardBrandType'))
        if support_card_brand_body.get('logo'):
            self.logo = Logo()
            self.logo.to_ams_dict()
