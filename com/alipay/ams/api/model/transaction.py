import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.transaction_type import TransactionType
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo




class Transaction:
    def __init__(self):
        
        self.__transaction_result = None  # type: Result
        self.__transaction_id = None  # type: str
        self.__transaction_type = None  # type: TransactionType
        self.__transaction_status = None  # type: TransactionStatusType
        self.__transaction_amount = None  # type: Amount
        self.__transaction_request_id = None  # type: str
        self.__transaction_time = None  # type: str
        self.__acquirer_info = None  # type: AcquirerInfo
        

    @property
    def transaction_result(self):
        """Gets the transaction_result of this Transaction.
        
        """
        return self.__transaction_result

    @transaction_result.setter
    def transaction_result(self, value):
        self.__transaction_result = value
    @property
    def transaction_id(self):
        """
        The unique ID that is assigned by Antom to identify a transaction.  When the transaction type is REFUND, the value of this parameter is identical to refundId. When the transaction type is CAPTURE, the value of this parameter is identical to captureId.   More information:  Maximum length: 64 characters
        """
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.__transaction_id = value
    @property
    def transaction_type(self):
        """Gets the transaction_type of this Transaction.
        
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value
    @property
    def transaction_status(self):
        """Gets the transaction_status of this Transaction.
        
        """
        return self.__transaction_status

    @transaction_status.setter
    def transaction_status(self, value):
        self.__transaction_status = value
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this Transaction.
        
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value
    @property
    def transaction_request_id(self):
        """
        The unique ID that is assigned by the merchant to identify the transaction request.  When the transaction type is REFUND, the value of this parameter is identical to refundRequestId. When the transaction type is CAPTURE, the value of this parameter is identical to captureRequestId.  More information:  Maximum length: 64 characters
        """
        return self.__transaction_request_id

    @transaction_request_id.setter
    def transaction_request_id(self, value):
        self.__transaction_request_id = value
    @property
    def transaction_time(self):
        """Gets the transaction_time of this Transaction.
        
        """
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value
    @property
    def acquirer_info(self):
        """Gets the acquirer_info of this Transaction.
        
        """
        return self.__acquirer_info

    @acquirer_info.setter
    def acquirer_info(self, value):
        self.__acquirer_info = value


    

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
        if hasattr(self, "transaction_time") and self.transaction_time is not None:
            params['transactionTime'] = self.transaction_time
        if hasattr(self, "acquirer_info") and self.acquirer_info is not None:
            params['acquirerInfo'] = self.acquirer_info
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
            transaction_type_temp = TransactionType.value_of(response_body['transactionType'])
            self.__transaction_type = transaction_type_temp
        if 'transactionStatus' in response_body:
            transaction_status_temp = TransactionStatusType.value_of(response_body['transactionStatus'])
            self.__transaction_status = transaction_status_temp
        if 'transactionAmount' in response_body:
            self.__transaction_amount = Amount()
            self.__transaction_amount.parse_rsp_body(response_body['transactionAmount'])
        if 'transactionRequestId' in response_body:
            self.__transaction_request_id = response_body['transactionRequestId']
        if 'transactionTime' in response_body:
            self.__transaction_time = response_body['transactionTime']
        if 'acquirerInfo' in response_body:
            self.__acquirer_info = AcquirerInfo()
            self.__acquirer_info.parse_rsp_body(response_body['acquirerInfo'])
