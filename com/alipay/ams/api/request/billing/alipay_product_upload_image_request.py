import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayProductUploadImageRequest(AlipayRequest):
    def __init__(self):
        super(AlipayProductUploadImageRequest, self).__init__("/ams/api/v1/billing/product/uploadImage") 

        self.__product_id = None  # type: str
        self.__image_file = None  # type: str
        

    @property
    def product_id(self):
        """
        The product ID. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def image_file(self):
        """
        The image file.
        """
        return self.__image_file

    @image_file.setter
    def image_file(self, value):
        self.__image_file = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "image_file") and self.image_file is not None:
            params['imageFile'] = self.image_file
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'imageFile' in response_body:
            self.__image_file = response_body['imageFile']
