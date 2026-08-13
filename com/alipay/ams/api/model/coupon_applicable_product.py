import json




class CouponApplicableProduct:
    def __init__(self):
        
        self.__can_delete = None  # type: bool
        self.__gmt_modified = None  # type: str
        self.__price_count = None  # type: int
        self.__product_id = None  # type: str
        self.__product_name = None  # type: str
        self.__status = None  # type: str
        

    @property
    def can_delete(self):
        """
        Whether the product can be deleted.
        """
        return self.__can_delete

    @can_delete.setter
    def can_delete(self, value):
        self.__can_delete = value
    @property
    def gmt_modified(self):
        """
        ISO 8601 timestamp of the latest product update.
        """
        return self.__gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self.__gmt_modified = value
    @property
    def price_count(self):
        """
        Number of prices associated with the product.
        """
        return self.__price_count

    @price_count.setter
    def price_count(self, value):
        self.__price_count = value
    @property
    def product_id(self):
        """
        System-generated product ID. Maximum length: 64 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def product_name(self):
        """
        Product display name.
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value
    @property
    def status(self):
        """
        Product status.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "can_delete") and self.can_delete is not None:
            params['canDelete'] = self.can_delete
        if hasattr(self, "gmt_modified") and self.gmt_modified is not None:
            params['gmtModified'] = self.gmt_modified
        if hasattr(self, "price_count") and self.price_count is not None:
            params['priceCount'] = self.price_count
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "product_name") and self.product_name is not None:
            params['productName'] = self.product_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'canDelete' in response_body:
            self.__can_delete = response_body['canDelete']
        if 'gmtModified' in response_body:
            self.__gmt_modified = response_body['gmtModified']
        if 'priceCount' in response_body:
            self.__price_count = response_body['priceCount']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'productName' in response_body:
            self.__product_name = response_body['productName']
        if 'status' in response_body:
            self.__status = response_body['status']
