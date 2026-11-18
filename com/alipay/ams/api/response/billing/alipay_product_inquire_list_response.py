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
        Product list. Always present; empty array &#x60;[]&#x60; when no results. When products array contains items, each Product object&#39;s M fields (productId, name, type, active, createdAt) are mandatory Returned only when result.resultCode is SUCCESS.
        """
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value
    @property
    def has_more(self):
        """
        Whether more results exist beyond the current page. &#x60;true&#x60; if more results exist, &#x60;false&#x60; otherwise. Detection logic: &#x60;hasMore &#x3D; (fetchedRows &#x3D;&#x3D; limit + 1)&#x60; - the server fetches limit+1 rows; if the extra row exists, hasMore&#x3D;true and only &#x60;limit&#x60; rows are returned. Aligned with Stripe cursor-based pagination pattern Returned only when result.resultCode is SUCCESS.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def total(self):
        """
        Total product count matching the query. O - Returned by default (includeTotal defaults to true). Set includeTotal&#x3D;false to omit and avoid COUNT query latency. When present, enables UI page navigation; when absent, use hasMore for \&quot;Load More\&quot; / infinite scroll patterns Returned only when result.resultCode is SUCCESS.
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
