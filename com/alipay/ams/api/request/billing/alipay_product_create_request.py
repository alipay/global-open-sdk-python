import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayProductCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayProductCreateRequest, self).__init__("/ams/api/v1/billing/product/create") 

        self.__product_request_id = None  # type: str
        self.__name = None  # type: str
        self.__type = None  # type: str
        self.__description = None  # type: str
        self.__images = None  # type: [str]
        self.__unit_label = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def product_request_id(self):
        """
        The product request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__product_request_id

    @product_request_id.setter
    def product_request_id(self, value):
        self.__product_request_id = value
    @property
    def name(self):
        """
        The name. Maximum length: 100 characters.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def type(self):
        """
        The type. Maximum length: 16 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def description(self):
        """
        The description. Maximum length: 1024 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def images(self):
        """
        The images. Note: See documentation for details.
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value
    @property
    def unit_label(self):
        """
        The unit label. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_request_id") and self.product_request_id is not None:
            params['productRequestId'] = self.product_request_id
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "images") and self.images is not None:
            params['images'] = self.images
        if hasattr(self, "unit_label") and self.unit_label is not None:
            params['unitLabel'] = self.unit_label
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productRequestId' in response_body:
            self.__product_request_id = response_body['productRequestId']
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'images' in response_body:
            self.__images = response_body['images']
        if 'unitLabel' in response_body:
            self.__unit_label = response_body['unitLabel']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
