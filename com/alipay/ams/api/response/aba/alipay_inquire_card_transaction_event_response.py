import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.card_transaction_event import CardTransactionEvent



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireCardTransactionEventResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__events = None  # type: [CardTransactionEvent]
        self.__total_count = None  # type: int
        self.__total_page_number = None  # type: int
        self.__current_page_number = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireCardTransactionEventResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def events(self):
        """
        The card transaction events. Returned when resultStatus is S; an empty match returns an empty array.
        """
        return self.__events

    @events.setter
    def events(self, value):
        self.__events = value
    @property
    def total_count(self):
        """
        The total number of matching records. Returned when resultStatus is S.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value
    @property
    def total_page_number(self):
        """
        The total number of pages. Returned when resultStatus is S; an empty match returns zero.
        """
        return self.__total_page_number

    @total_page_number.setter
    def total_page_number(self, value):
        self.__total_page_number = value
    @property
    def current_page_number(self):
        """
        The current one-based page number. Returned when resultStatus is S.
        """
        return self.__current_page_number

    @current_page_number.setter
    def current_page_number(self, value):
        self.__current_page_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "events") and self.events is not None:
            params['events'] = self.events
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        if hasattr(self, "total_page_number") and self.total_page_number is not None:
            params['totalPageNumber'] = self.total_page_number
        if hasattr(self, "current_page_number") and self.current_page_number is not None:
            params['currentPageNumber'] = self.current_page_number
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireCardTransactionEventResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'events' in response_body:
            self.__events = []
            for item in response_body['events']:
                obj = CardTransactionEvent()
                obj.parse_rsp_body(item)
                self.__events.append(obj)
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'totalPageNumber' in response_body:
            self.__total_page_number = response_body['totalPageNumber']
        if 'currentPageNumber' in response_body:
            self.__current_page_number = response_body['currentPageNumber']
