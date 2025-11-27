from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayMerchantRegistrationInfoQueryResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayMerchantRegistrationInfoQueryResponse, self).__init__()
        self.__merchant_info = None
        self.__product_codes = None
        self.__parse_rsp_body(rsp_body)

    @property
    def merchant_info(self):
        return self.__merchant_info

    @property
    def product_codes(self):
        return self.__product_codes

    def __parse_rsp_body(self, rsp_body):
        response = super(
            AlipayMerchantRegistrationInfoQueryResponse, self
        ).parse_rsp_body(rsp_body)
        if "merchantInfo" in response:
            self.__merchant_info = response["merchantInfo"]
        if "productCodes" in response:
            self.__product_codes = response["productCodes"]
