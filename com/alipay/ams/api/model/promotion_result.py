import json
from com.alipay.ams.api.model.promotion_type import PromotionType
from com.alipay.ams.api.model.discount import Discount




class PromotionResult:
    def __init__(self):
        
        self.__promotion_type = None  # type: PromotionType
        self.__discount = None  # type: Discount
        

    @property
    def promotion_type(self):
        """Gets the promotion_type of this PromotionResult.
        
        """
        return self.__promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self.__promotion_type = value
    @property
    def discount(self):
        """Gets the discount of this PromotionResult.
        
        """
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_type") and self.promotion_type is not None:
            params['promotionType'] = self.promotion_type
        if hasattr(self, "discount") and self.discount is not None:
            params['discount'] = self.discount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionType' in response_body:
            promotion_type_temp = PromotionType.value_of(response_body['promotionType'])
            self.__promotion_type = promotion_type_temp
        if 'discount' in response_body:
            self.__discount = Discount()
            self.__discount.parse_rsp_body(response_body['discount'])
