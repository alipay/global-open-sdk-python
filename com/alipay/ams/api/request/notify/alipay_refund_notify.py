from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayRefundNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayRefundNotify, self).__init__()
        self.__refund_status = None
        self.__refund_request_id = None
        self.__refund_id = None
        self.__refund_amount = None # type: Amount
        self.__refund_time = None
        self.__gross_settlement_amount = None # type: Amount
        self.__settlement_quote = None # type: Quote
        self.__parse_notify_body(notify_body)


    @property
    def refund_status(self):
        return self.__refund_status

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
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayRefundNotify, self).parse_notify_body(notify_body)
        if 'refundStatus' in notify:
            self.__refund_status = notify['refundStatus']
        if 'refundRequestId' in notify:
            self.__refund_request_id = notify['refundRequestId']
        if 'refundId' in notify:
            self.__refund_id = notify['refundId']
        if 'refundAmount' in notify:
            self.__refund_amount = Amount(notify['refundAmount'])
        if 'refundTime' in notify:
            self.__refund_time = notify['refundTime']
        if 'grossSettlementAmount' in notify:
            self.__gross_settlement_amount = Amount(notify['grossSettlementAmount'])
        if 'settlementQuote' in notify:
            queue = Quote()
            queue.parse_rsp_body(notify['settlementQuote'])
            self.__settlement_quote = queue

