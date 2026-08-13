import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.credit_grant import CreditGrant



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditGrantInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__page_num = None  # type: int
        self.__page_size = None  # type: int
        self.__total_count = None  # type: int
        self.__credit_grants = None  # type: [CreditGrant]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditGrantInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def page_num(self):
        """
        The current page number.
        """
        return self.__page_num

    @page_num.setter
    def page_num(self, value):
        self.__page_num = value
    @property
    def page_size(self):
        """
        The number of records on the current page.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def total_count(self):
        """
        The total number of matching credit grants at query time.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value
    @property
    def credit_grants(self):
        """
        The matching credit grants. Returned only when result.resultCode is SUCCESS.
        """
        return self.__credit_grants

    @credit_grants.setter
    def credit_grants(self, value):
        self.__credit_grants = value


    

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
        if hasattr(self, "credit_grants") and self.credit_grants is not None:
            params['creditGrants'] = self.credit_grants
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditGrantInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'pageNum' in response_body:
            self.__page_num = response_body['pageNum']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'creditGrants' in response_body:
            self.__credit_grants = []
            for item in response_body['creditGrants']:
                obj = CreditGrant()
                obj.parse_rsp_body(item)
                self.__credit_grants.append(obj)
