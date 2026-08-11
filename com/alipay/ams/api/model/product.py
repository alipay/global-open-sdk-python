import json




class Product:
    def __init__(self):
        
        self.__product_id = None  # type: str
        self.__product_request_id = None  # type: str
        self.__name = None  # type: str
        self.__type = None  # type: str
        self.__description = None  # type: str
        self.__images = None  # type: [str]
        self.__unit_label = None  # type: str
        self.__metadata = None  # type: str
        self.__active = None  # type: bool
        self.__created_at = None  # type: str
        self.__deactivated_at = None  # type: str
        self.__updated_at = None  # type: str
        

    @property
    def product_id(self):
        """
        System-generated product ID
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def product_request_id(self):
        """
        The idempotency key supplied when the product was created. Returned only when result.resultCode is SUCCESS.
        """
        return self.__product_request_id

    @product_request_id.setter
    def product_request_id(self, value):
        self.__product_request_id = value
    @property
    def name(self):
        """
        Product name
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def type(self):
        """
        Filter by product type. O - When provided, returns only products of the specified type; when absent, returns all types. Enum: SERVICE, GOOD. Can be null; default null. Invalid values return PARAM_ILLEGAL error
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def description(self):
        """
        Product description. O - May be null in the response when the value is not set
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def images(self):
        """
        Product image URLs
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value
    @property
    def unit_label(self):
        """
        Product-level unit label. O - May be null in the response when the value is not set
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def metadata(self):
        """
        Custom key-value metadata stored as JSON string The value must be a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def active(self):
        """
        Filter by active status. O - true&#x3D;return only active products, false&#x3D;return only deactivated products, absent or null&#x3D;return all products. No default value
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def created_at(self):
        """
        ISO 8601 creation timestamp
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value
    @property
    def deactivated_at(self):
        """
        ISO 8601 deactivation timestamp. O - Returned when product has been deactivated (active&#x3D;false); absent when product is active
        """
        return self.__deactivated_at

    @deactivated_at.setter
    def deactivated_at(self, value):
        self.__deactivated_at = value
    @property
    def updated_at(self):
        """
        ISO 8601 last update timestamp. O - Returned when non-null; absent from response if never updated after creation
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value


    

    def to_ams_dict(self):
        params = dict()
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
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
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
