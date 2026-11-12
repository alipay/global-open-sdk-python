import json
from com.alipay.ams.api.model.trade_bill_query_info import TradeBillQueryInfo
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayQueryTradeBillListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        self.__time_zone = None  # type: str
        self.__total = None  # type: int
        self.__records = None  # type: [TradeBillQueryInfo]
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def current_page(self):
        """
        The page number supplied by the merchant, or 1 if omitted.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The page size supplied by the merchant, or 20 if omitted.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def time_zone(self):
        """
        The time zone supplied by the merchant, or UTC if omitted.
        """
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, value):
        self.__time_zone = value
    @property
    def total(self):
        """
        The total number of trade bills matching the query, returned by Antom. Returns 0 when no records match.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def records(self):
        """
        The matching trade bill records returned by Antom. Returns an empty list when no records match.
        """
        return self.__records

    @records.setter
    def records(self, value):
        self.__records = value
    @property
    def result(self):
        """Gets the result of this AlipayQueryTradeBillListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "time_zone") and self.time_zone is not None:
            params['timeZone'] = self.time_zone
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        if hasattr(self, "records") and self.records is not None:
            params['records'] = self.records
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayQueryTradeBillListResponse, self).parse_rsp_body(response_body)
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'timeZone' in response_body:
            self.__time_zone = response_body['timeZone']
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'records' in response_body:
            self.__records = []
            for item in response_body['records']:
                obj = TradeBillQueryInfo()
                obj.parse_rsp_body(item)
                self.__records.append(obj)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
