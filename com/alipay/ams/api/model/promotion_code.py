import json
from com.alipay.ams.api.model.amount import Amount




class PromotionCode:
    def __init__(self):
        
        self.__promotion_code_request_id = None  # type: str
        self.__code = None  # type: str
        self.__max_redemptions = None  # type: int
        self.__expiry_time = None  # type: str
        self.__min_amount = None  # type: Amount
        self.__one_time_only = None  # type: bool
        self.__customer_id = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def promotion_code_request_id(self):
        """
        The promotion code request id. Maximum length: 128 characters.
        """
        return self.__promotion_code_request_id

    @promotion_code_request_id.setter
    def promotion_code_request_id(self, value):
        self.__promotion_code_request_id = value
    @property
    def code(self):
        """
        The code. Maximum length: 128 characters.
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value
    @property
    def max_redemptions(self):
        """
        The max redemptions.
        """
        return self.__max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, value):
        self.__max_redemptions = value
    @property
    def expiry_time(self):
        """
        The expiry time. Maximum length: 24 characters.
        """
        return self.__expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self.__expiry_time = value
    @property
    def min_amount(self):
        """Gets the min_amount of this PromotionCode.
        
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value
    @property
    def one_time_only(self):
        """
        The one time only.
        """
        return self.__one_time_only

    @one_time_only.setter
    def one_time_only(self, value):
        self.__one_time_only = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_code_request_id") and self.promotion_code_request_id is not None:
            params['promotionCodeRequestId'] = self.promotion_code_request_id
        if hasattr(self, "code") and self.code is not None:
            params['code'] = self.code
        if hasattr(self, "max_redemptions") and self.max_redemptions is not None:
            params['maxRedemptions'] = self.max_redemptions
        if hasattr(self, "expiry_time") and self.expiry_time is not None:
            params['expiryTime'] = self.expiry_time
        if hasattr(self, "min_amount") and self.min_amount is not None:
            params['minAmount'] = self.min_amount
        if hasattr(self, "one_time_only") and self.one_time_only is not None:
            params['oneTimeOnly'] = self.one_time_only
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionCodeRequestId' in response_body:
            self.__promotion_code_request_id = response_body['promotionCodeRequestId']
        if 'code' in response_body:
            self.__code = response_body['code']
        if 'maxRedemptions' in response_body:
            self.__max_redemptions = response_body['maxRedemptions']
        if 'expiryTime' in response_body:
            self.__expiry_time = response_body['expiryTime']
        if 'minAmount' in response_body:
            self.__min_amount = Amount()
            self.__min_amount.parse_rsp_body(response_body['minAmount'])
        if 'oneTimeOnly' in response_body:
            self.__one_time_only = response_body['oneTimeOnly']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
