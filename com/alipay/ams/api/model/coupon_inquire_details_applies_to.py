import json
from com.alipay.ams.api.model.coupon_applicable_product import CouponApplicableProduct




class CouponInquireDetailsAppliesTo:
    def __init__(self):
        
        self.__products = None  # type: [CouponApplicableProduct]
        

    @property
    def products(self):
        """
        Products to which the coupon applies. Product details are assembled by the server.
        """
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "products") and self.products is not None:
            params['products'] = self.products
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'products' in response_body:
            self.__products = []
            for item in response_body['products']:
                obj = CouponApplicableProduct()
                obj.parse_rsp_body(item)
                self.__products.append(obj)
