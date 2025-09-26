import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.payment_option import PaymentOption
from com.alipay.ams.api.model.payment_method_info import PaymentMethodInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPayConsultResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_options = None  # type: [PaymentOption]
        self.__payment_method_infos = None  # type: [PaymentMethodInfo]
        self.__extend_info = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPayConsultResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_options(self):
        """
        The payment option list.
        """
        return self.__payment_options

    @payment_options.setter
    def payment_options(self, value):
        self.__payment_options = value
    @property
    def payment_method_infos(self):
        """Gets the payment_method_infos of this AlipayPayConsultResponse.
        
        """
        return self.__payment_method_infos

    @payment_method_infos.setter
    def payment_method_infos(self, value):
        self.__payment_method_infos = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayPayConsultResponse.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_options") and self.payment_options is not None:
            params['paymentOptions'] = self.payment_options
        if hasattr(self, "payment_method_infos") and self.payment_method_infos is not None:
            params['paymentMethodInfos'] = self.payment_method_infos
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPayConsultResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentOptions' in response_body:
            self.__payment_options = []
            for item in response_body['paymentOptions']:
                obj = PaymentOption()
                obj.parse_rsp_body(item)
                self.__payment_options.append(obj)
        if 'paymentMethodInfos' in response_body:
            self.__payment_method_infos = []
            for item in response_body['paymentMethodInfos']:
                obj = PaymentMethodInfo()
                obj.parse_rsp_body(item)
                self.__payment_method_infos.append(obj)
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
