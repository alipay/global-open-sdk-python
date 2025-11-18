from com.alipay.ams.api.model.Statement import Statement
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayInquiryStatementListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayInquiryStatementListResponse, self).__init__()
        self.__statement_list = None  # type: list:Statement
        self.__parse_rsp_body(rsp_body)

    @property
    def statement_list(self):
        return self.__statement_list

    @statement_list.setter
    def statement_list(self, value):
        self.__statement_list = value

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayInquiryStatementListResponse, self).parse_rsp_body(
            rsp_body
        )
        if "statementList" in response:
            self.__statement_list = response["statementList"]
