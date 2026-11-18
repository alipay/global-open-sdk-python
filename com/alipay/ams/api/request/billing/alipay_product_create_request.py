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
        self.__metadata = None  # type: str
        

    @property
    def product_request_id(self):
        """
        Optional idempotency key for product creation. Maximum length: 64 characters; letters, digits, hyphens, and underscores are allowed. A retry with the same key and request body returns the original result. Reusing the key with a different request body returns &#x60;BIZ_DUPLICATE_PRODUCT_REQUEST&#x60;. Omitting the key allows network retries to create duplicate products.
        """
        return self.__product_request_id

    @product_request_id.setter
    def product_request_id(self, value):
        self.__product_request_id = value
    @property
    def name(self):
        """
        Product name. Required. Maximum length: 128 characters. Characters &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&amp;&#x60;, &#x60;&#39;&#x60;, and &#x60;\&quot;&#x60; are not allowed.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def type(self):
        """
        Product type. O - Default: SERVICE. Enum: SERVICE(intangible digital service or SaaS offering - checkout skips shipping address collection), GOOD(tangible physical product requiring delivery - checkout collects shipping address). Cannot be null when present; if absent, defaults to SERVICE
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def description(self):
        """
        Optional product description. Maximum length: 256 characters. Characters &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&amp;&#x60;, &#x60;&#39;&#x60;, and &#x60;\&quot;&#x60; are not allowed.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def images(self):
        """
        Optional initial product image URLs. Maximum size: 8 elements; maximum length: 2048 characters per URL. Each URL must use HTTP or HTTPS. Characters &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&amp;&#x60;, &#x60;&#39;&#x60;, and &#x60;\&quot;&#x60; are not allowed.
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value
    @property
    def unit_label(self):
        """
        Product-level unit label (e.g., \&quot;seat\&quot;, \&quot;API call\&quot;). C - Optional at creation; required when any linked price uses usageType&#x3D;LICENSED or METERED (if absent at that point, Price-level unitLabel must provide the value). Price-level unitLabel overrides Product-level unitLabel when both are set; if Price-level is absent, Product-level is inherited. Can be null; default null. Characters &amp; &#39; \&quot; are not allowed
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def metadata(self):
        """
        Optional metadata encoded as a JSON object string. The SDK must forward the string unchanged. Maximum size: 20 entries. Keys must use lowerCamelCase alphanumeric text and be at most 40 characters. Values are at most 500 characters and cannot contain &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&amp;&#x60;, &#x60;&#39;&#x60;, or &#x60;\&quot;&#x60;. PII must not be stored. Invalid keys, values, or entry counts return &#x60;INVALID_METADATA_KEY&#x60;, &#x60;INVALID_METADATA_VALUE&#x60;, or &#x60;INVALID_METADATA_SIZE&#x60;.
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
