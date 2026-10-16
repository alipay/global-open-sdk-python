import json
from com.alipay.ams.api.model.agentic_amount import AgenticAmount
from com.alipay.ams.api.model.agentic_payment_token_order_merchant import AgenticPaymentTokenOrderMerchant
from com.alipay.ams.api.model.agentic_payment_token_order_goods import AgenticPaymentTokenOrderGoods




class AgenticPaymentTokenOrder:
    def __init__(self):
        
        self.__payment_amount = None  # type: AgenticAmount
        self.__merchant = None  # type: AgenticPaymentTokenOrderMerchant
        self.__goods = None  # type: [AgenticPaymentTokenOrderGoods]
        self.__reference_order_id = None  # type: str
        

    @property
    def payment_amount(self):
        """Gets the payment_amount of this AgenticPaymentTokenOrder.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def merchant(self):
        """Gets the merchant of this AgenticPaymentTokenOrder.
        
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value
    @property
    def goods(self):
        """
        Goods line items. No separate item-count limit is specified; the total AMS message-size limit applies.
        """
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods = value
    @property
    def reference_order_id(self):
        """
        Merchant order reference. Required for Visa AUTONOMOUS; Visa IMMEDIATE reuses the authorization context.
        """
        return self.__reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, value):
        self.__reference_order_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "merchant") and self.merchant is not None:
            params['merchant'] = self.merchant
        if hasattr(self, "goods") and self.goods is not None:
            params['goods'] = self.goods
        if hasattr(self, "reference_order_id") and self.reference_order_id is not None:
            params['referenceOrderId'] = self.reference_order_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentAmount' in response_body:
            self.__payment_amount = AgenticAmount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'merchant' in response_body:
            self.__merchant = AgenticPaymentTokenOrderMerchant()
            self.__merchant.parse_rsp_body(response_body['merchant'])
        if 'goods' in response_body:
            self.__goods = []
            for item in response_body['goods']:
                obj = AgenticPaymentTokenOrderGoods()
                obj.parse_rsp_body(item)
                self.__goods.append(obj)
        if 'referenceOrderId' in response_body:
            self.__reference_order_id = response_body['referenceOrderId']
