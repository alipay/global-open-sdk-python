import json
from typing import List

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayInquiryStatementListRequest(AlipayRequest):

    def __init__(self):
        super(AlipayInquiryStatementListRequest, self).__init__(
            AntomPathConstants.ABA_INQUERY_STATEMENT_LIST_PATH
        )
        self.__customer_id = None
        self.__access_token = None
        self.__start_time = None
        self.__end_time = None
        self.__transaction_type_list = None  # type: List[str]
        self.__currency_list = None  # type: List[str]
        self.__page_number = None
        self.__page_size = None

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    @property
    def transaction_type_list(self):
        return self.__transaction_type_list

    @transaction_type_list.setter
    def transaction_type_list(self, value):
        if isinstance(value, list):
            self.__transaction_type_list = value
        else:
            self.__transaction_type_list = [value]

    @property
    def currency_list(self):
        return self.__currency_list

    @currency_list.setter
    def currency_list(self, value):
        if isinstance(value, list):
            self.__currency_list = value
        else:
            self.__currency_list = [value]

    @property
    def page_number(self):
        return self.__page_number

    @page_number.setter
    def page_number(self, value):
        self.__page_number = value

    @property
    def page_size(self):
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id:
            params["customerId"] = self.customer_id
        if hasattr(self, "access_token") and self.access_token:
            params["accessToken"] = self.access_token
        if hasattr(self, "start_time") and self.start_time:
            params["startTime"] = self.start_time
        if hasattr(self, "end_time") and self.end_time:
            params["endTime"] = self.end_time
        if hasattr(self, "transaction_type_list") and self.transaction_type_list:
            params["transactionTypeList"] = self.transaction_type_list
        if hasattr(self, "currency_list") and self.currency_list:
            params["currencyList"] = self.currency_list
        if hasattr(self, "page_number") and self.page_number:
            params["pageNumber"] = self.page_number
        if hasattr(self, "page_size") and self.page_size:
            params["pageSize"] = self.page_size
        return params
