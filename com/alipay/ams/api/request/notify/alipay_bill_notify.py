from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.fail_reason import FailReason
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayBillNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayBillNotify, self).__init__()
        self.__asset_id = None
        self.__masked_card_no = None
        self.__order_no = None
        self.__card_nick_name = None
        self.__transaction_time = None
        self.__merchant_name = None
        self.__trade_amount = None
        self.__in_amount = None
        self.__out_amount = None
        self.__exchange_rate = None
        self.__bill_type = None
        self.__trade_country = None
        self.__bill_status = None
        self.__bill_fail_reason = None  # 现在是 FailReason 对象
        self.__last_update = None
        self.__metadata = None
        self.__parse_notify_body(notify_body)

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def masked_card_no(self):
        return self.__masked_card_no

    @property
    def order_no(self):
        return self.__order_no

    @property
    def card_nick_name(self):
        return self.__card_nick_name

    @property
    def transaction_time(self):
        return self.__transaction_time

    @property
    def merchant_name(self):
        return self.__merchant_name

    @property
    def trade_amount(self):
        return self.__trade_amount

    @property
    def in_amount(self):
        return self.__in_amount

    @property
    def out_amount(self):
        return self.__out_amount

    @property
    def exchange_rate(self):
        return self.__exchange_rate

    @property
    def bill_type(self):
        return self.__bill_type

    @property
    def trade_country(self):
        return self.__trade_country

    @property
    def bill_status(self):
        return self.__bill_status

    @property
    def bill_fail_reason(self):
        return self.__bill_fail_reason

    @property
    def last_update(self):
        return self.__last_update

    @property
    def metadata(self):
        return self.__metadata

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayBillNotify, self).parse_notify_body(notify_body)

        if "assetId" in notify:
            self.__asset_id = notify["assetId"]
        if "maskedCardNo" in notify:
            self.__masked_card_no = notify["maskedCardNo"]
        if "orderNo" in notify:
            self.__order_no = notify["orderNo"]
        if "cardNickName" in notify:
            self.__card_nick_name = notify["cardNickName"]
        if "transactionTime" in notify:
            self.__transaction_time = notify["transactionTime"]
        if "merchantName" in notify:
            self.__merchant_name = notify["merchantName"]

        if "tradeAmount" in notify:
            self.__trade_amount = Amount(notify["tradeAmount"])
        if "inAmount" in notify:
            self.__in_amount = Amount(notify["inAmount"])
        if "outAmount" in notify:
            self.__out_amount = Amount(notify["outAmount"])

        if "exchangeRate" in notify:
            self.__exchange_rate = notify["exchangeRate"]
        if "billType" in notify:
            self.__bill_type = notify["billType"]
        if "tradeCountry" in notify:
            self.__trade_country = notify["tradeCountry"]
        if "billStatus" in notify:
            self.__bill_status = notify["billStatus"]

        # 👇 关键修改：解析 billFailReason 为 FailReason 对象
        if "billFailReason" in notify and isinstance(notify["billFailReason"], dict):
            self.__bill_fail_reason = FailReason(notify["billFailReason"])

        if "lastUpdate" in notify:
            self.__last_update = notify["lastUpdate"]
        if "metadata" in notify:
            self.__metadata = notify["metadata"]
