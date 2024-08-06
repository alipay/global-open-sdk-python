import json

from com.alipay.ams.api.model.discount import Discount
from com.alipay.ams.api.model.interest_free import InterestFree
from com.alipay.ams.api.model.promotion_type import PromotionType


class PromotionInfo(object):
    def __init__(self):
        self.__promotion_type = None  # type:PromotionType
        self.__discount = None  # type:Discount
        self.__interest_free = None  # type:InterestFree

    @property
    def promotion_type(self):
        return self.__promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self.__promotion_type = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value

    @property
    def interest_free(self):
        return self.__interest_free

    @interest_free.setter
    def interest_free(self, value):
        self.__interest_free = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_type") and self.promotion_type:
            params['promotionType'] = self.promotion_type.value

        if hasattr(self, "discount") and self.discount:
            params['discount'] = self.discount.to_ams_dict()

        if hasattr(self, "interest_free") and self.interest_free:
            params['interestFree'] = self.interest_free.to_ams_dict()

        return params

    def parse_rsp_body(self, promotion_info_body):
        if type(promotion_info_body) == str:
            promotion_info_body = json.loads(promotion_info_body)

        if 'promotionType' in promotion_info_body:
            self.promotion_type = PromotionType(promotion_info_body['promotionType'])

        if 'discount' in promotion_info_body:
            discount_result = Discount()
            discount_result.parse_rsp_body(promotion_info_body['discount'])
            self.discount = discount_result

        if 'interestFree' in promotion_info_body:
            interest_free_result = InterestFree()
            interest_free_result.parse_rsp_body(promotion_info_body['interestFree'])
            self.interest_free = interest_free_result
