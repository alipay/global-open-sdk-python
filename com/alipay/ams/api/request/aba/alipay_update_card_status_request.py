import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayUpdateCardStatusRequest(AlipayRequest):
    def __init__(self):
        super(AlipayUpdateCardStatusRequest, self).__init__("/ams/api/v1/aba/cards/updateCardStatus") 

        self.__asset_id = None  # type: str
        self.__request_id = None  # type: str
        self.__operate_type = None  # type: str
        self.__notify_url = None  # type: str
        

    @property
    def asset_id(self):
        """
        卡资产ID。 Card asset Id
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def request_id(self):
        """
        针对本次申卡请求，由集成商指定的唯一请求号 The unique request number specified by the integrator for this card application request.
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
    @property
    def operate_type(self):
        """
        操作类型。可取值范围： FREEZE：冻结卡 UNFREEZE：解冻卡 CANCEL：删除卡  Enumeration of Operation Type. Possible values:   FREEZE: Freeze the card   UNFREEZE: Unfreeze the card   CANCEL: Delete the card
        """
        return self.__operate_type

    @operate_type.setter
    def operate_type(self, value):
        self.__operate_type = value
    @property
    def notify_url(self):
        """
        Notification priority -&gt; request.notifyUrl. If not provided, the notify URL configured by the user in the portal will be used.
        """
        return self.__notify_url

    @notify_url.setter
    def notify_url(self, value):
        self.__notify_url = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "operate_type") and self.operate_type is not None:
            params['operateType'] = self.operate_type
        if hasattr(self, "notify_url") and self.notify_url is not None:
            params['notifyUrl'] = self.notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'operateType' in response_body:
            self.__operate_type = response_body['operateType']
        if 'notifyUrl' in response_body:
            self.__notify_url = response_body['notifyUrl']
