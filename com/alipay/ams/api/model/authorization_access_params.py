import json




class AuthorizationAccessParams:
    def __init__(self):
        
        self.__channel = None  # type: str
        

    @property
    def channel(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. Maximum length: 100 characters. Allowed values: ALIPAYAPP, QRCODE, QRCODEORSMS. The Alipay app, QR-code, or QR-code/SMS signing entry.
        """
        return self.__channel

    @channel.setter
    def channel(self, value):
        self.__channel = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "channel") and self.channel is not None:
            params['channel'] = self.channel
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'channel' in response_body:
            self.__channel = response_body['channel']
