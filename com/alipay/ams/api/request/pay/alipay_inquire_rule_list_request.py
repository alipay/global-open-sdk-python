import json
from com.alipay.ams.api.model.funds_type import FundsType
from com.alipay.ams.api.model.take_type import TakeType
from com.alipay.ams.api.model.release_type import ReleaseType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireRuleListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireRuleListRequest, self).__init__("/ams/api/v1/payments/reserve/inquireRuleList") 

        self.__funds_type = None  # type: FundsType
        self.__take_type = None  # type: TakeType
        self.__release_type = None  # type: ReleaseType
        self.__limit = None  # type: int
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        

    @property
    def funds_type(self):
        """Gets the funds_type of this AlipayInquireRuleListRequest.
        
        """
        return self.__funds_type

    @funds_type.setter
    def funds_type(self, value):
        self.__funds_type = value
    @property
    def take_type(self):
        """Gets the take_type of this AlipayInquireRuleListRequest.
        
        """
        return self.__take_type

    @take_type.setter
    def take_type(self, value):
        self.__take_type = value
    @property
    def release_type(self):
        """Gets the release_type of this AlipayInquireRuleListRequest.
        
        """
        return self.__release_type

    @release_type.setter
    def release_type(self, value):
        self.__release_type = value
    @property
    def limit(self):
        """
        The maximum number of rules to return. The default value is 10.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def starting_after(self):
        """
        The forward-pagination cursor. Return rules with a ruleId lower than this value in descending ruleId order. This field is mutually exclusive with endingBefore. Omission, null, empty, or blank means no cursor.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        The backward-pagination cursor. Return the nearest page of rules with a ruleId higher than this value, presented in descending ruleId order. This field is mutually exclusive with startingAfter. Omission, null, empty, or blank means no cursor.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "funds_type") and self.funds_type is not None:
            params['fundsType'] = self.funds_type
        if hasattr(self, "take_type") and self.take_type is not None:
            params['takeType'] = self.take_type
        if hasattr(self, "release_type") and self.release_type is not None:
            params['releaseType'] = self.release_type
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        if hasattr(self, "ending_before") and self.ending_before is not None:
            params['endingBefore'] = self.ending_before
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'fundsType' in response_body:
            funds_type_temp = FundsType.value_of(response_body['fundsType'])
            self.__funds_type = funds_type_temp
        if 'takeType' in response_body:
            take_type_temp = TakeType.value_of(response_body['takeType'])
            self.__take_type = take_type_temp
        if 'releaseType' in response_body:
            release_type_temp = ReleaseType.value_of(response_body['releaseType'])
            self.__release_type = release_type_temp
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
