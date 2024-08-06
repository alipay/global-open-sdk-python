import json

from com.alipay.ams.api.model.discount import Discount
from com.alipay.ams.api.model.promotion_type import PromotionType


class PromotionResult(object):

    def __init__(self):
        self.__promotion_type = None  # type:PromotionType
        self.__discount = None  # type:Discount

    @property
    def promotion_type(self):
        return self.__promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        self.__promotion_type = promotion_type

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_type") and self.promotion_type:
            params['promotionType'] = self.promotion_type

        if hasattr(self, "discount") and self.discount:
            params['discount'] = self.discount

        return params

    def parse_rsp_body(self, promotion_result_body):
        if type(promotion_result_body) == str:
            promotion_result_body = json.loads(promotion_result_body)

        if 'promotionType' in promotion_result_body:
            self.promotion_type = promotion_result_body['promotionType']

        if 'discount' in promotion_result_body:
            discount_result = Discount()
            discount_result.parse_rsp_body(promotion_result_body['discount'])
            self.__promotion_result = discount_result
