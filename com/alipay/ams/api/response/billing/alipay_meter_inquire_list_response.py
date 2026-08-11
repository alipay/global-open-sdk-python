import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.meter import Meter



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayMeterInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__page_num = None  # type: int
        self.__page_size = None  # type: int
        self.__total_count = None  # type: int
        self.__meters = None  # type: [Meter]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayMeterInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def page_num(self):
        """
        The current page number. Returned only when result.resultCode is SUCCESS.
        """
        return self.__page_num

    @page_num.setter
    def page_num(self, value):
        self.__page_num = value
    @property
    def page_size(self):
        """
        The number of records on the current page. Returned only when result.resultCode is SUCCESS.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def total_count(self):
        """
        The total number of matching meters at query time. Returned only when result.resultCode is SUCCESS.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value
    @property
    def meters(self):
        """
        The matching meters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__meters

    @meters.setter
    def meters(self, value):
        self.__meters = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "page_num") and self.page_num is not None:
            params['pageNum'] = self.page_num
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        if hasattr(self, "meters") and self.meters is not None:
            params['meters'] = self.meters
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayMeterInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'pageNum' in response_body:
            self.__page_num = response_body['pageNum']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'meters' in response_body:
            self.__meters = []
            for item in response_body['meters']:
                obj = Meter()
                obj.parse_rsp_body(item)
                self.__meters.append(obj)
