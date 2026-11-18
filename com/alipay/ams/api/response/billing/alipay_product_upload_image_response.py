import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayProductUploadImageResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__image_url = None  # type: str
        self.__image_name = None  # type: str
        self.__product_id = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayProductUploadImageResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def image_url(self):
        """
        The image url. Maximum length: 2048 characters.
        """
        return self.__image_url

    @image_url.setter
    def image_url(self, value):
        self.__image_url = value
    @property
    def image_name(self):
        """
        The image name. Maximum length: 128 characters.
        """
        return self.__image_name

    @image_name.setter
    def image_name(self, value):
        self.__image_name = value

    @property
    def product_id(self):
        """The product ID echoed from the request."""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "image_url") and self.image_url is not None:
            params['imageUrl'] = self.image_url
        if hasattr(self, "image_name") and self.image_name is not None:
            params['imageName'] = self.image_name
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayProductUploadImageResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'imageUrl' in response_body:
            self.__image_url = response_body['imageUrl']
        if 'imageName' in response_body:
            self.__image_name = response_body['imageName']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
