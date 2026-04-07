import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount




class SubscriptionTransaction:
    def __init__(self):
        
        self.__payment_id = None  # type: str
        self.__status = None  # type: str
        self.__phase_no = None  # type: int
        self.__payment_method = None  # type: PaymentMethod
        self.__payment_amount = None  # type: Amount
        self.__payment_time = None  # type: str
        self.__dispute_id = None  # type: str
        

    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def status(self):
        """
        Indicates the payment status. Valid values are: - SUCCESS: Indicates that the payment succeeds. - FAIL: Indicates that the payment fails.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def phase_no(self):
        """
        The phase number that the payment applies to.
        """
        return self.__phase_no

    @phase_no.setter
    def phase_no(self, value):
        self.__phase_no = value
    @property
    def payment_method(self):
        """Gets the payment_method of this SubscriptionTransaction.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this SubscriptionTransaction.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_time(self):
        """
        The successful execution time of this payment by Antom, that is, the date and time when the payment reaches a final state of success.
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def dispute_id(self):
        """
        The unique ID that is assigned by Antom to identify a dispute. Indicates whether a dispute exists for the transaction. If no dispute is present, the value is NULL.
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "phase_no") and self.phase_no is not None:
            params['phaseNo'] = self.phase_no
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'phaseNo' in response_body:
            self.__phase_no = response_body['phaseNo']
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
