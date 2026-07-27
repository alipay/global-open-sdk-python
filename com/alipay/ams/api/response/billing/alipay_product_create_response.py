import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayProductCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__product_id = None  # type: str
        self.__product_request_id = None  # type: str
        self.__name = None  # type: str
        self.__type = None  # type: str
        self.__description = None  # type: str
        self.__images = None  # type: [str]
        self.__unit_label = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__active = None  # type: bool
        self.__created_at = None  # type: str
        self.__deactivated_at = None  # type: str
        self.__updated_at = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayProductCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def product_id(self):
        """
        The product ID. Maximum length: 32 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def product_request_id(self):
        """
        The product request id. Maximum length: 64 characters.
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
        The images.
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value
    @property
    def unit_label(self):
        """
        The unit label. Maximum length: 64 characters.
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def active(self):
        """
        The active.
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def created_at(self):
        """
        The created at. Maximum length: 29 characters.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value
    @property
    def deactivated_at(self):
        """
        The deactivated at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__deactivated_at

    @deactivated_at.setter
    def deactivated_at(self, value):
        self.__deactivated_at = value
    @property
    def updated_at(self):
        """
        The updated at. Maximum length: 29 characters. Note: See documentation for details.
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
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
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        if hasattr(self, "created_at") and self.created_at is not None:
            params['createdAt'] = self.created_at
        if hasattr(self, "deactivated_at") and self.deactivated_at is not None:
            params['deactivatedAt'] = self.deactivated_at
        if hasattr(self, "updated_at") and self.updated_at is not None:
            params['updatedAt'] = self.updated_at
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayProductCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
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
        if 'active' in response_body:
            self.__active = response_body['active']
        if 'createdAt' in response_body:
            self.__created_at = response_body['createdAt']
        if 'deactivatedAt' in response_body:
            self.__deactivated_at = response_body['deactivatedAt']
        if 'updatedAt' in response_body:
            self.__updated_at = response_body['updatedAt']
