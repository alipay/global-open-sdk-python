import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayApplyCardResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__request_id = None  # type: str
        self.__status = None  # type: str
        self.__asset_id = None  # type: str
        self.__cvv = None  # type: str
        self.__card_no = None  # type: str
        self.__expired_month = None  # type: str
        self.__expired_year = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayApplyCardResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def request_id(self):
        """Gets the request_id of this AlipayApplyCardResponse.
        
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
    @property
    def status(self):
        """Gets the status of this AlipayApplyCardResponse.
        
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def asset_id(self):
        """Gets the asset_id of this AlipayApplyCardResponse.
        
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def cvv(self):
        """Gets the cvv of this AlipayApplyCardResponse.
        
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value
    @property
    def card_no(self):
        """Gets the card_no of this AlipayApplyCardResponse.
        
        """
        return self.__card_no

    @card_no.setter
    def card_no(self, value):
        self.__card_no = value
    @property
    def expired_month(self):
        """Gets the expired_month of this AlipayApplyCardResponse.
        
        """
        return self.__expired_month

    @expired_month.setter
    def expired_month(self, value):
        self.__expired_month = value
    @property
    def expired_year(self):
        """Gets the expired_year of this AlipayApplyCardResponse.
        
        """
        return self.__expired_year

    @expired_year.setter
    def expired_year(self, value):
        self.__expired_year = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
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
        response_body = super(AlipayApplyCardResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'status' in response_body:
            self.__status = response_body['status']
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
