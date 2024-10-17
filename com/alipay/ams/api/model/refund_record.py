from com.alipay.ams.api.model.amount import Amount


class RefundRecord:
    def __init__(self):
        self.__reference_order_id = None
        self.__reference_goods_id = None
        self.__amount = None #type: Amount
        self.__refund_reason = None
        self.__refund_time = None

    @property
    def reference_order_id(self):
        return self.__reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, value):
        self.__reference_order_id = value

    @property
    def reference_goods_id(self):
        return self.__reference_goods_id

    @reference_goods_id.setter
    def reference_goods_id(self, value):
        self.__reference_goods_id = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def refund_reason(self):
        return self.__refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self.__refund_reason = value

    @property
    def refund_time(self):
        return self.__refund_time

    @refund_time.setter
    def refund_time(self, value ):
        self.__refund_time = value


    def to_ams_dict(self):
        params = dict()
        if self.__reference_order_id is not None:
            params['referenceOrderId'] = self.__reference_order_id
        if self.__reference_goods_id is not None:
            params['referenceGoodsId'] = self.__reference_goods_id
        if self.__amount is not None:
            params['amount'] = self.__amount.to_ams_dict()
        if self.__refund_reason is not None:
            params['refundReason'] = self.__refund_reason
        if self.__refund_time is not None:
            params['refundTime'] = self.__refund_time

        return params