import json




class CouponInquireDetailsAppliesTo:
    def __init__(self):
        
        self.__product_ids = None  # type: [str]
        

    @property
    def product_ids(self):
        """
        The product ids. Maximum length: 64 characters.
        """
        return self.__product_ids

    @product_ids.setter
    def product_ids(self, value):
        self.__product_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_ids") and self.product_ids is not None:
            params['productIds'] = self.product_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productIds' in response_body:
            self.__product_ids = response_body['productIds']
