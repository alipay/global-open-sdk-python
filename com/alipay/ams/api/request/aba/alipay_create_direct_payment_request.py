import json
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateDirectPaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateDirectPaymentRequest, self).__init__("/ams/api/v1/aba/funds/createDirectPayment") 

        self.__payment_request_id = None  # type: str
        self.__memo = None  # type: str
        self.__remark = None  # type: str
        self.__order = None  # type: Order
        self.__payment_notify_url = None  # type: str
        self.__pay_to_method = None  # type: PaymentMethod
        self.__pay_to_amount = None  # type: Amount
        self.__pay_from_amount = None  # type: Amount
        

    @property
    def payment_request_id(self):
        """Gets the payment_request_id of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def memo(self):
        """Gets the memo of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def remark(self):
        """Gets the remark of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__remark

    @remark.setter
    def remark(self, value):
        self.__remark = value
    @property
    def order(self):
        """Gets the order of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
    @property
    def payment_notify_url(self):
        """Gets the payment_notify_url of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self.__payment_notify_url = value
    @property
    def pay_to_method(self):
        """Gets the pay_to_method of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__pay_to_method

    @pay_to_method.setter
    def pay_to_method(self, value):
        self.__pay_to_method = value
    @property
    def pay_to_amount(self):
        """Gets the pay_to_amount of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__pay_to_amount

    @pay_to_amount.setter
    def pay_to_amount(self, value):
        self.__pay_to_amount = value
    @property
    def pay_from_amount(self):
        """Gets the pay_from_amount of this AlipayCreateDirectPaymentRequest.
        
        """
        return self.__pay_from_amount

    @pay_from_amount.setter
    def pay_from_amount(self, value):
        self.__pay_from_amount = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "remark") and self.remark is not None:
            params['remark'] = self.remark
        if hasattr(self, "order") and self.order is not None:
            params['order'] = self.order
        if hasattr(self, "payment_notify_url") and self.payment_notify_url is not None:
            params['paymentNotifyUrl'] = self.payment_notify_url
        if hasattr(self, "pay_to_method") and self.pay_to_method is not None:
            params['payToMethod'] = self.pay_to_method
        if hasattr(self, "pay_to_amount") and self.pay_to_amount is not None:
            params['payToAmount'] = self.pay_to_amount
        if hasattr(self, "pay_from_amount") and self.pay_from_amount is not None:
            params['payFromAmount'] = self.pay_from_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'remark' in response_body:
            self.__remark = response_body['remark']
        if 'order' in response_body:
            self.__order = Order()
            self.__order.parse_rsp_body(response_body['order'])
        if 'paymentNotifyUrl' in response_body:
            self.__payment_notify_url = response_body['paymentNotifyUrl']
        if 'payToMethod' in response_body:
            self.__pay_to_method = PaymentMethod()
            self.__pay_to_method.parse_rsp_body(response_body['payToMethod'])
        if 'payToAmount' in response_body:
            self.__pay_to_amount = Amount()
            self.__pay_to_amount.parse_rsp_body(response_body['payToAmount'])
        if 'payFromAmount' in response_body:
            self.__pay_from_amount = Amount()
            self.__pay_from_amount.parse_rsp_body(response_body['payFromAmount'])
