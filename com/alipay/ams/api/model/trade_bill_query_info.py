import json
from com.alipay.ams.api.model.trade_bill_payment_amount import TradeBillPaymentAmount




class TradeBillQueryInfo:
    def __init__(self):
        
        self.__merchant_id = None  # type: str
        self.__reference_store_id = None  # type: str
        self.__tid = None  # type: str
        self.__merchant_transaction_id = None  # type: str
        self.__payment_amount = None  # type: TradeBillPaymentAmount
        self.__biz_order_type = None  # type: str
        self.__biz_order_status = None  # type: str
        self.__start_time = None  # type: str
        self.__completed_time = None  # type: str
        

    @property
    def merchant_id(self):
        """
        The merchant identifier returned by Antom.
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self.__merchant_id = value
    @property
    def reference_store_id(self):
        """
        The external merchant identifier for the store, supplied by the merchant. Returned when referenceStoreId was provided in the payment request; null when no value is available.
        """
        return self.__reference_store_id

    @reference_store_id.setter
    def reference_store_id(self, value):
        self.__reference_store_id = value
    @property
    def tid(self):
        """
        The merchant terminal identifier passed through by Antom SDK during payment result synchronization. Returns null if it was not supplied.
        """
        return self.__tid

    @tid.setter
    def tid(self, value):
        self.__tid = value
    @property
    def merchant_transaction_id(self):
        """
        The merchant payment request identifier. This value is always available.
        """
        return self.__merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, value):
        self.__merchant_transaction_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this TradeBillQueryInfo.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def biz_order_type(self):
        """
        The transaction type returned by Antom. PAY represents a SALE payment; CANCEL represents a VOID cancellation that releases the user&#39;s frozen funds. This API returns only PAY and CANCEL transactions.
        """
        return self.__biz_order_type

    @biz_order_type.setter
    def biz_order_type(self, value):
        self.__biz_order_type = value
    @property
    def biz_order_status(self):
        """
        The transaction status returned by Antom. This API queries only successful transactions and returns SUCCESS.
        """
        return self.__biz_order_status

    @biz_order_status.setter
    def biz_order_status(self, value):
        self.__biz_order_status = value
    @property
    def start_time(self):
        """
        The transaction creation time returned by Antom. This value is always available.
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
    @property
    def completed_time(self):
        """
        The transaction completion time returned by Antom. This value is expected to be nonempty because only successful transactions are queried.
        """
        return self.__completed_time

    @completed_time.setter
    def completed_time(self, value):
        self.__completed_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_id") and self.merchant_id is not None:
            params['merchantId'] = self.merchant_id
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
        if hasattr(self, "biz_order_status") and self.biz_order_status is not None:
            params['bizOrderStatus'] = self.biz_order_status
        if hasattr(self, "start_time") and self.start_time is not None:
            params['startTime'] = self.start_time
        if hasattr(self, "completed_time") and self.completed_time is not None:
            params['completedTime'] = self.completed_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantId' in response_body:
            self.__merchant_id = response_body['merchantId']
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
        if 'bizOrderStatus' in response_body:
            self.__biz_order_status = response_body['bizOrderStatus']
        if 'startTime' in response_body:
            self.__start_time = response_body['startTime']
        if 'completedTime' in response_body:
            self.__completed_time = response_body['completedTime']
