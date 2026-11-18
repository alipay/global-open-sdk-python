import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount




class BatchPaymentTransaction:
    def __init__(self):
        
        self.__transaction_result = None  # type: Result
        self.__transaction_id = None  # type: str
        self.__transaction_type = None  # type: str
        self.__transaction_status = None  # type: str
        self.__transaction_amount = None  # type: Amount
        self.__transaction_request_id = None  # type: str
        

    @property
    def transaction_result(self):
        """Gets the transaction_result of this BatchPaymentTransaction.
        
        """
        return self.__transaction_result

    @transaction_result.setter
    def transaction_result(self, value):
        self.__transaction_result = value
    @property
    def transaction_id(self):
        """
        Antom-assigned transaction ID (maximum 64 characters); equals refundId for REFUND and captureId for CAPTURE.
        """
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.__transaction_id = value
    @property
    def transaction_type(self):
        """
        Transaction type (maximum 16 characters). REFUND: refund; CAPTURE: capture; INCREMENTAL: incremental amount adjustment.
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value
    @property
    def transaction_status(self):
        """
        Transaction status (maximum 16 characters). SUCCESS: succeeded; FAIL: failed; PROCESSING: processing; CANCELLED: canceled.
        """
        return self.__transaction_status

    @transaction_status.setter
    def transaction_status(self, value):
        self.__transaction_status = value
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this BatchPaymentTransaction.
        
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value
    @property
    def transaction_request_id(self):
        """
        Merchant-assigned transaction request ID (maximum 64 characters); equals refundRequestId for REFUND and captureRequestId for CAPTURE.
        """
        return self.__transaction_request_id

    @transaction_request_id.setter
    def transaction_request_id(self, value):
        self.__transaction_request_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transaction_result") and self.transaction_result is not None:
            params['transactionResult'] = self.transaction_result
        if hasattr(self, "transaction_id") and self.transaction_id is not None:
            params['transactionId'] = self.transaction_id
        if hasattr(self, "transaction_type") and self.transaction_type is not None:
            params['transactionType'] = self.transaction_type
        if hasattr(self, "transaction_status") and self.transaction_status is not None:
            params['transactionStatus'] = self.transaction_status
        if hasattr(self, "transaction_amount") and self.transaction_amount is not None:
            params['transactionAmount'] = self.transaction_amount
        if hasattr(self, "transaction_request_id") and self.transaction_request_id is not None:
            params['transactionRequestId'] = self.transaction_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transactionResult' in response_body:
            self.__transaction_result = Result()
            self.__transaction_result.parse_rsp_body(response_body['transactionResult'])
        if 'transactionId' in response_body:
            self.__transaction_id = response_body['transactionId']
        if 'transactionType' in response_body:
            self.__transaction_type = response_body['transactionType']
        if 'transactionStatus' in response_body:
            self.__transaction_status = response_body['transactionStatus']
        if 'transactionAmount' in response_body:
            self.__transaction_amount = Amount()
            self.__transaction_amount.parse_rsp_body(response_body['transactionAmount'])
        if 'transactionRequestId' in response_body:
            self.__transaction_request_id = response_body['transactionRequestId']
