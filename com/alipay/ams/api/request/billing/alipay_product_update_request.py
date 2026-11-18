import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayProductUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayProductUpdateRequest, self).__init__("/ams/api/v1/billing/product/update") 

        self.__product_id = None  # type: str
        self.__name = None  # type: str
        self.__description = None  # type: str
        self.__images = None  # type: [str]
        self.__unit_label = None  # type: str
        self.__metadata = None  # type: str
        self.__active = None  # type: bool
        

    @property
    def product_id(self):
        """
        Product ID to update. Cannot be null. Format: prod_ prefix + alphanumeric suffix. This field serves as the idempotent key for this operation
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def name(self):
        """
        Product name. O - When provided, updates name. When null, rejected with PARAM_ILLEGAL error (name is mandatory and cannot be cleared). When absent, no change. Characters &amp; &#39; \&quot; are not allowed (XSS prevention - see Section 4.1.1 name field)
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def description(self):
        """
        Product description. O - Present with value: update; present with null: clear; absent: no change. Can be null
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def images(self):
        """
        Product image URLs. O - Present with value: full-replacement of entire image list; present with null: clear all images; absent: no change. Each URL must start with http:// or https://, max 2048 characters. Full-replacement: providing images replaces the entire array, not appends. Merchants are responsible for availability of externally-hosted URLs; Antom does not validate external URL accessibility. See Section 6.13 for image management workflow
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value
    @property
    def unit_label(self):
        """
        Product-level unit label. O - Present with value: update; present with null: clear; absent: no change. Can be null
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def metadata(self):
        """
        Custom metadata encoded as a JSON object string. When provided, the value fully replaces the existing metadata; keys are not merged. When omitted, the existing value is unchanged. PII must not be stored.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def active(self):
        """
        Product active status. O - explicit true&#x3D;activate, explicit false&#x3D;deactivate, absent or null&#x3D;no change. There is no \&quot;clear\&quot; semantic for active - it is always either true or false. When deactivated (active&#x3D;false), the product cannot be used for new subscriptions; existing subscriptions continue using the product
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
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
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'name' in response_body:
            self.__name = response_body['name']
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
