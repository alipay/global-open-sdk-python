import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.aba_card import AbaCard



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireCardResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__total_count = None  # type: int
        self.__total_page_number = None  # type: int
        self.__current_page_number = None  # type: int
        self.__card_list = None  # type: [AbaCard]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireCardResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def total_count(self):
        """
        Total card elements.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value
    @property
    def total_page_number(self):
        """
        Total number of pages.
        """
        return self.__total_page_number

    @total_page_number.setter
    def total_page_number(self, value):
        self.__total_page_number = value
    @property
    def current_page_number(self):
        """
        当前页码。 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。  Current page number This field will only be returned as needed when &#x60;result.resultStatus &#x3D; S&#x60;.
        """
        return self.__current_page_number

    @current_page_number.setter
    def current_page_number(self, value):
        self.__current_page_number = value
    @property
    def card_list(self):
        """
        卡列表 此字段只有当 result.resultStatus &#x3D; S 时才会按需返回。  Card list This field will only be returned as needed when &#x60;result.resultStatus &#x3D; S&#x60;.
        """
        return self.__card_list

    @card_list.setter
    def card_list(self, value):
        self.__card_list = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        if hasattr(self, "total_page_number") and self.total_page_number is not None:
            params['totalPageNumber'] = self.total_page_number
        if hasattr(self, "current_page_number") and self.current_page_number is not None:
            params['currentPageNumber'] = self.current_page_number
        if hasattr(self, "card_list") and self.card_list is not None:
            params['cardList'] = self.card_list
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireCardResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'totalPageNumber' in response_body:
            self.__total_page_number = response_body['totalPageNumber']
        if 'currentPageNumber' in response_body:
            self.__current_page_number = response_body['currentPageNumber']
        if 'cardList' in response_body:
            self.__card_list = []
            for item in response_body['cardList']:
                obj = AbaCard()
                obj.parse_rsp_body(item)
                self.__card_list.append(obj)
