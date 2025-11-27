from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.customized_info import CustomizedInfo
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayRefundQueryResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayRefundQueryResponse, self).__init__()
        self.__refund_request_id = None
        self.__refund_id = None
        self.__refund_amount = None  # type: Amount
        self.__refund_time = None
        self.__refund_status = None  # type:TransactionStatusType
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__customized_info = None  # type: CustomizedInfo
        self.__arn = None
        self.__actual_refund_amount = None  # type: Amount
        self.__parse_rsp_body(rsp_body)

    @property
    def refund_request_id(self):
        return self.__refund_request_id

    @property
    def refund_id(self):
        return self.__refund_id

    @property
    def refund_amount(self):
        return self.__refund_amount

    @property
    def refund_time(self):
        return self.__refund_time

    @property
    def refund_status(self):
        return self.__refund_status

    @property
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    @property
    def customized_info(self):
        return self.__customized_info

    @property
    def arn(self):
        return self.__arn

    @property
    def actual_refund_amount(self):
        return self.__actual_refund_amount

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayRefundQueryResponse, self).parse_rsp_body(rsp_body)
        if "refundRequestId" in response:
            self.__refund_request_id = response["refundRequestId"]
        if "refundId" in response:
            self.__refund_id = response["refundId"]
        if "refundAmount" in response:
            refund_amount = Amount()
            refund_amount.parse_rsp_body(response["refundAmount"])
            self.__refund_amount = refund_amount
        if "refundTime" in response:
            self.__refund_time = response["refundTime"]
        if "refundStatus" in response:
            self.__refund_status = response["refundStatus"]
        if "grossSettlementAmount" in response:
            gross_settlement_amount = Amount()
            gross_settlement_amount.parse_rsp_body(response["grossSettlementAmount"])
            self.__gross_settlement_amount = gross_settlement_amount
        if "settlementQuote" in response:
            settlement_quote = Quote()
            settlement_quote.parse_rsp_body(response["settlementQuote"])
            self.__settlement_quote = settlement_quote
        if "customizedInfo" in response:
            customized_info = CustomizedInfo()
            customized_info.parse_rsp_body(response["customizedInfo"])
            self.__customized_info = customized_info
        if "arn" in response:
            self.__arn = response["arn"]
        if "actualRefundAmount" in response:
            actual_refund_amount = Amount()
            actual_refund_amount.parse_rsp_body(response["actualRefundAmount"])
            self.__actual_refund_amount = actual_refund_amount
