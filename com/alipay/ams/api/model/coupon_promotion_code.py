import json




class CouponPromotionCode:
    def __init__(self):
        
        self.__promotion_code_id = None  # type: str
        self.__code = None  # type: str
        self.__status = None  # type: str
        

    @property
    def promotion_code_id(self):
        """
        The system-generated promotion code ID.
        """
        return self.__promotion_code_id

    @promotion_code_id.setter
    def promotion_code_id(self, value):
        self.__promotion_code_id = value
    @property
    def code(self):
        """
        The merchant-supplied or system-generated promotion code string.
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value
    @property
    def status(self):
        """
        The promotion code status. The value is ACTIVE on creation.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "promotion_code_id") and self.promotion_code_id is not None:
            params['promotionCodeId'] = self.promotion_code_id
        if hasattr(self, "code") and self.code is not None:
            params['code'] = self.code
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'promotionCodeId' in response_body:
            self.__promotion_code_id = response_body['promotionCodeId']
        if 'code' in response_body:
            self.__code = response_body['code']
        if 'status' in response_body:
            self.__status = response_body['status']
