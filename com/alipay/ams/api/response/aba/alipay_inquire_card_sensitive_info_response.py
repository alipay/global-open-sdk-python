import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireCardSensitiveInfoResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__asset_id = None  # type: str
        self.__cvv = None  # type: str
        self.__card_no = None  # type: str
        self.__expired_month = None  # type: str
        self.__expired_year = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireCardSensitiveInfoResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def asset_id(self):
        """
        卡资产ID。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。 Card Asset ID. This field will only be returned on demand when result.resultStatus &#x3D; S.
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def cvv(self):
        """
        加密cvv号。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。 CVV number. This field will only be returned on demand when result.resultStatus &#x3D; S.
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value
    @property
    def card_no(self):
        """
        加密卡号。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。 card number. This field will only be returned on demand when result.resultStatus &#x3D; S.
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def expired_month(self):
        """
        卡片过期月份，格式为“MM“，如：”07“。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。 Card expiration month, formatted as \&quot;MM,\&quot; e.g., \&quot;07.\&quot; This field will only be returned on demand when result.resultStatus &#x3D; S.
        """
        return self.__expired_month

    @expired_month.setter
    def expired_month(self, value):
        self.__expired_month = value
    @property
    def expired_year(self):
        """
        卡片过期年份，格式为“YY“，取年份后两位数字，如：”29“。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。 Card expiration year, formatted as \&quot;YY,\&quot; using the last two digits of the year, e.g., \&quot;29.\&quot; This field will only be returned on demand when result.resultStatus &#x3D; S.
        """
        return self.__expired_year

    @expired_year.setter
    def expired_year(self, value):
        self.__expired_year = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "cvv") and self.cvv is not None:
            params['cvv'] = self.cvv
        if hasattr(self, "card_no") and self.card_no is not None:
            params['cardNo'] = self.card_no
        if hasattr(self, "expired_month") and self.expired_month is not None:
            params['expiredMonth'] = self.expired_month
        if hasattr(self, "expired_year") and self.expired_year is not None:
            params['expiredYear'] = self.expired_year
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireCardSensitiveInfoResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'cvv' in response_body:
            self.__cvv = response_body['cvv']
        if 'cardNo' in response_body:
            self.__card_no = response_body['cardNo']
        if 'expiredMonth' in response_body:
            self.__expired_month = response_body['expiredMonth']
        if 'expiredYear' in response_body:
            self.__expired_year = response_body['expiredYear']
