import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.refund_from_type import RefundFromType


class RefundDetail(object):
    def __init__(self):
        self.__refund_amount = None  # type:Amount
        self.__refund_from = None  # type:RefundFromType

    @property
    def refund_amount(self):
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value

    @property
    def refund_from(self):
        return self.__refund_from

    @refund_from.setter
    def refund_from(self, value):
        self.__refund_from = value

    def parse_rsp_body(self, quote_body):
        if type(quote_body) == str:
            quote_body = json.loads(quote_body)
        if 'refundAmount' in quote_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(quote_body['refundAmount'])
        if 'refundFrom' in quote_body:
            self.__refund_from = quote_body['refundFrom']
