import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.product import Product



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayProductInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__products = None  # type: [Product]
        self.__has_more = None  # type: bool
        self.__total = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayProductInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def products(self):
        """
        The products.
        """
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value
    @property
    def has_more(self):
        """
        The has more.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def total(self):
        """
        The total number of records. Note: See documentation for details.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "products") and self.products is not None:
            params['products'] = self.products
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayProductInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'products' in response_body:
            self.__products = []
            for item in response_body['products']:
                obj = Product()
                obj.parse_rsp_body(item)
                self.__products.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'total' in response_body:
            self.__total = response_body['total']
