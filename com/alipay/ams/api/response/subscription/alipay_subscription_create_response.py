from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySubscriptionCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySubscriptionCreateResponse, self).__init__()
        self.__scheme_url = None
        self.__applink_url = None
        self.__normal_url = None
        self.__app_identifier = None
        self.__parse_rsp_body(rsp_body)

    @property
    def scheme_url(self):
        return self.__scheme_url

    @property
    def applink_url(self):
        return self.__applink_url

    @property
    def normal_url(self):
        return self.__normal_url

    @property
    def app_identifier(self):
        return self.__app_identifier

    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipaySubscriptionCreateResponse, self).parse_rsp_body(rsp_body)
        if rsp_dict.get('schemeUrl'):
            self.__scheme_url = rsp_dict.get('schemeUrl')
        if rsp_dict.get('applinkUrl'):
            self.__applink_url = rsp_dict.get('applinkUrl')
        if rsp_dict.get('normalUrl'):
            self.__normal_url = rsp_dict.get('normalUrl')
        if rsp_dict.get('appIdentifier'):
            self.__app_identifier = rsp_dict.get('appIdentifier')


