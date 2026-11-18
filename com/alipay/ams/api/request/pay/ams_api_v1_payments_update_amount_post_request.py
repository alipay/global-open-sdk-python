import json
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AmsApiV1PaymentsUpdateAmountPostRequest(AlipayRequest):
    def __init__(self):
        super(AmsApiV1PaymentsUpdateAmountPostRequest, self).__init__("/ams/api/v1/payments/updateAmount") 

        self.__update_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__amount = None  # type: Amount
        

    @property
    def update_request_id(self):
        """
        The unique ID that is assigned by the merchant to identify an updateAmount request. Antom uses this field for idempotence control. More information: Maximum length: 64 characters
        """
        return self.__update_request_id

    @update_request_id.setter
    def update_request_id(self, value):
        self.__update_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment. The value of this parameter is the paymentId returned from the first pre-auth. More information: Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def amount(self):
        """Gets the amount of this AmsApiV1PaymentsUpdateAmountPostRequest.
        
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "update_request_id") and self.update_request_id is not None:
            params['updateRequestId'] = self.update_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'updateRequestId' in response_body:
            self.__update_request_id = response_body['updateRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'amount' in response_body:
            self.__amount = Amount()
            self.__amount.parse_rsp_body(response_body['amount'])
