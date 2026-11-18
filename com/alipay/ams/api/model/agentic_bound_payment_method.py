import json
from com.alipay.ams.api.model.agentic_bound_payment_method_detail import AgenticBoundPaymentMethodDetail




class AgenticBoundPaymentMethod:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_id = None  # type: str
        self.__payment_method_detail = None  # type: AgenticBoundPaymentMethodDetail
        

    @property
    def payment_method_type(self):
        """
        Payment method type. The closed, case-sensitive values are CARD, AlipayCN, AlipayHK and MPay. Internal wallet names with underscores are not public values; unsupported values return PARAM_ILLEGAL/F. Supported values (case-sensitive): CARD, AlipayCN, AlipayHK, MPay.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_id(self):
        """
        An opaque payment method reference returned by Antom for subsequent Agentic Payment calls. Do not parse it or depend on its format, lifetime or reuse count. This is not a payment credential or channel token.
        """
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value
    @property
    def payment_method_detail(self):
        """Gets the payment_method_detail of this AgenticBoundPaymentMethod.
        
        """
        return self.__payment_method_detail

    @payment_method_detail.setter
    def payment_method_detail(self, value):
        self.__payment_method_detail = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_id") and self.payment_method_id is not None:
            params['paymentMethodId'] = self.payment_method_id
        if hasattr(self, "payment_method_detail") and self.payment_method_detail is not None:
            params['paymentMethodDetail'] = self.payment_method_detail
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodId' in response_body:
            self.__payment_method_id = response_body['paymentMethodId']
        if 'paymentMethodDetail' in response_body:
            self.__payment_method_detail = AgenticBoundPaymentMethodDetail()
            self.__payment_method_detail.parse_rsp_body(response_body['paymentMethodDetail'])
