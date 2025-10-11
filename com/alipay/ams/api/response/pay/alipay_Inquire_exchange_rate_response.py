from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayInquireExchangeRateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayInquireExchangeRateResponse, self).__init__()
        self.__quotes = None #type: list[Quote]
        self.__parse_rsp_body(rsp_body)

    @property
    def quotes(self):
        return self.__quotes

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayInquireExchangeRateResponse, self).parse_rsp_body(rsp_body)
        if 'quotes' in response:
            self.__quotes = response['quotes']
