import json
from com.alipay.ams.api.model.settlement_detail import SettlementDetail



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySettleRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySettleRequest, self).__init__("/ams/api/v1/payments/settle") 

        self.__settlement_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__settlement_details = None  # type: [SettlementDetail]
        

    @property
    def settlement_request_id(self):
        """
        The unique ID that is assigned by the marketplace to identify a settlement request. Antom uses this field for idempotence control.   More information:  This field is an API idempotency field.For registration requests that are initiated with the same value of settlementRequestId and reach a final status (resultStatus &#x3D; S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__settlement_request_id

    @settlement_request_id.setter
    def settlement_request_id(self, value):
        self.__settlement_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment. The value of this parameter is returned through the same parameter in the pay (Cashier Payment) API.    More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def settlement_details(self):
        """
        The settlement details for a payment.    More information:  Maximum length: 20 characters
        """
        return self.__settlement_details

    @settlement_details.setter
    def settlement_details(self, value):
        self.__settlement_details = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settlement_request_id") and self.settlement_request_id is not None:
            params['settlementRequestId'] = self.settlement_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "settlement_details") and self.settlement_details is not None:
            params['settlementDetails'] = self.settlement_details
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'settlementRequestId' in response_body:
            self.__settlement_request_id = response_body['settlementRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'settlementDetails' in response_body:
            self.__settlement_details = []
            for item in response_body['settlementDetails']:
                obj = SettlementDetail()
                obj.parse_rsp_body(item)
                self.__settlement_details.append(obj)
