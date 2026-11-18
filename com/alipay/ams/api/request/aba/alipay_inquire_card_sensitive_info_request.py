import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireCardSensitiveInfoRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireCardSensitiveInfoRequest, self).__init__("/ams/api/v1/aba/cards/inquireCardSensitiveInfo") 

        self.__asset_id = None  # type: str
        

    @property
    def asset_id(self):
        """
        卡资产ID。
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
