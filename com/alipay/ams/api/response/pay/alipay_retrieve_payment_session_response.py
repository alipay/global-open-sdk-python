from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.promotion_result import PromotionResult
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayRetrievePaymentSessionResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayRetrievePaymentSessionResponse, self).__init__()
        self.__order = None #type: Order
        self.__promotion_results = None #type: List: PromotionResult
        self.__customized_Info = None

        self.__parse_rsp_body(rsp_body)



    @property
    def order(self):
        return self.__order
    @property
    def promotion_results(self):
        return self.__promotion_results
    @property
    def customized_info(self):
        return self.__customized_info

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayRetrievePaymentSessionResponse, self).parse_rsp_body(rsp_body)
        if 'order' in response:
            self.__order = response['order']
        if 'promotionResults' in response:
            self.__promotion_results = response['promotionResults']
        if 'customizedInfo' in response:
            self.__customized_info = response['customizedInfo']

