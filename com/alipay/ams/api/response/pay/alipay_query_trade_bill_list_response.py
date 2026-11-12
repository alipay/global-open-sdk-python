import json
from com.alipay.ams.api.model.trade_bill_query_info import TradeBillQueryInfo
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.trade_bill_payment_amount import TradeBillPaymentAmount



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
        self.__reference_store_id = None  # type: str
        self.__tid = None  # type: str
        self.__merchant_transaction_id = None  # type: str
        self.__payment_amount = None  # type: TradeBillPaymentAmount
        self.__biz_order_type = None  # type: str
        self.__start_time = None  # type: str
        self.__completed_time = None  # type: str
        self.__biz_order_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def current_page(self):
        """
        The requested page number. The first page is used when the request omits currentPage.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The requested number of records per page. The page size is 20 when the request omits pageSize.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def time_zone(self):
        """
        The time zone passed in the request, or UTC if omitted.
        """
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, value):
        self.__time_zone = value
    @property
    def total(self):
        """
        The total number of trade bills matching the query conditions. Returns 0 if no records match.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def records(self):
        """
        The matching trade bill records, with at most 200 records. Returns an empty list if no records match.
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
    @property
    def reference_store_id(self):
        """
        The external merchant identifier supplied as referenceStoreId in the payment request. Returns null if the stored value is empty.
        """
        return self.__reference_store_id

    @reference_store_id.setter
    def reference_store_id(self, value):
        self.__reference_store_id = value
    @property
    def tid(self):
        """
        The merchant terminal identifier supplied by the Antom SDK when synchronizing the payment result. Returns null if it was not supplied.
        """
        return self.__tid

    @tid.setter
    def tid(self, value):
        self.__tid = value
    @property
    def merchant_transaction_id(self):
        """
        The merchant&#39;s payment request identifier. Always has a value when returned.
        """
        return self.__merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, value):
        self.__merchant_transaction_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayQueryTradeBillListResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def biz_order_type(self):
        """
        The transaction type. This API queries PAY and CANCEL transactions.
        """
        return self.__biz_order_type

    @biz_order_type.setter
    def biz_order_type(self, value):
        self.__biz_order_type = value
    @property
    def start_time(self):
        """
        The order creation time. Always has a value when returned.
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
    @property
    def completed_time(self):
        """
        The order completion time. Expected to have a value because this API only queries orders in SUCCESS status.
        """
        return self.__completed_time

    @completed_time.setter
    def completed_time(self, value):
        self.__completed_time = value
    @property
    def biz_order_status(self):
        """
        The order status. This API only queries orders in SUCCESS status and returns SUCCESS.
        """
        return self.__biz_order_status

    @biz_order_status.setter
    def biz_order_status(self, value):
        self.__biz_order_status = value


    

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
        if hasattr(self, "reference_store_id") and self.reference_store_id is not None:
            params['referenceStoreId'] = self.reference_store_id
        if hasattr(self, "tid") and self.tid is not None:
            params['tid'] = self.tid
        if hasattr(self, "merchant_transaction_id") and self.merchant_transaction_id is not None:
            params['merchantTransactionId'] = self.merchant_transaction_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "biz_order_type") and self.biz_order_type is not None:
            params['bizOrderType'] = self.biz_order_type
        if hasattr(self, "start_time") and self.start_time is not None:
            params['startTime'] = self.start_time
        if hasattr(self, "completed_time") and self.completed_time is not None:
            params['completedTime'] = self.completed_time
        if hasattr(self, "biz_order_status") and self.biz_order_status is not None:
            params['bizOrderStatus'] = self.biz_order_status
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
        if 'referenceStoreId' in response_body:
            self.__reference_store_id = response_body['referenceStoreId']
        if 'tid' in response_body:
            self.__tid = response_body['tid']
        if 'merchantTransactionId' in response_body:
            self.__merchant_transaction_id = response_body['merchantTransactionId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = TradeBillPaymentAmount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'bizOrderType' in response_body:
            self.__biz_order_type = response_body['bizOrderType']
        if 'startTime' in response_body:
            self.__start_time = response_body['startTime']
        if 'completedTime' in response_body:
            self.__completed_time = response_body['completedTime']
        if 'bizOrderStatus' in response_body:
            self.__biz_order_status = response_body['bizOrderStatus']
