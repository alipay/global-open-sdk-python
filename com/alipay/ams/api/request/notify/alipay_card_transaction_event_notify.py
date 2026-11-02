import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.event_merchant_info import EventMerchantInfo


class AlipayCardTransactionEventNotify:
    """One flat ABA VCC card transaction event callback (notification profile v2.1, document v2.13).

    Verify the raw-body signature before constructing this object. The merchant handles
    durable acceptance, eventId deduplication and ACK. Amount values remain quoted
    minor-unit strings of up to 20 digits. Parsing does not enforce business validation.
    """

    def __init__(self, notify_body):
        self.__event_id = None  # type: str
        self.__lifecycle_id = None  # type: str
        self.__event_type = None  # type: str
        self.__auth_time = None  # type: str
        self.__auth_expire_time = None  # type: str
        self.__auth_type = None  # type: str
        self.__auth_code = None  # type: str
        self.__failure_reason = None  # type: str
        self.__status = None  # type: str
        self.__balance_type = None  # type: str
        self.__transaction_time = None  # type: str
        self.__bill_type = None  # type: str
        self.__out_amount = None  # type: Amount
        self.__in_amount = None  # type: Amount
        self.__exchange_currency_pair = None  # type: str
        self.__exchange_rate = None  # type: str
        self.__transaction_amount = None  # type: Amount
        self.__asset_id = None  # type: str
        self.__masked_card_no = None  # type: str
        self.__card_product = None  # type: str
        self.__merchant_info = None  # type: EventMerchantInfo
        self.__metadata = None  # type: dict
        self.__parse_notify_body(notify_body)

    @property
    def event_id(self):
        """Stable event ID and the only callback idempotency key. Required; maximum 64 characters."""
        return self.__event_id

    @event_id.setter
    def event_id(self, value):
        self.__event_id = value

    @property
    def lifecycle_id(self):
        """Spend-group ID shared with inquiry. Required; maximum 64 characters."""
        return self.__lifecycle_id

    @lifecycle_id.setter
    def lifecycle_id(self, value):
        self.__lifecycle_id = value

    @property
    def event_type(self):
        """Required event type: AUTH, AUTH_CANCEL, CAPTURE, REFUND, CHARGEBACK or REPAYMENT. Preserve unknown future values."""
        return self.__event_type

    @event_type.setter
    def event_type(self, value):
        self.__event_type = value

    @property
    def auth_time(self):
        """Optional ISO 8601 time of the channel-correlated authorization, maximum 32 characters. Omitted for AUTH or when unavailable; never inferred from transactionTime or authExpireTime."""
        return self.__auth_time

    @auth_time.setter
    def auth_time(self, value):
        self.__auth_time = value

    @property
    def auth_expire_time(self):
        """Optional ISO 8601 authorization expiry time, maximum 32 characters. Sent only for AUTH when available."""
        return self.__auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, value):
        self.__auth_expire_time = value

    @property
    def auth_type(self):
        """Optional AUTH or PRE_AUTH, maximum 32 characters. Sent only for AUTH when available."""
        return self.__auth_type

    @auth_type.setter
    def auth_type(self, value):
        self.__auth_type = value

    @property
    def auth_code(self):
        """Optional network approval code, maximum 64 characters. Sent only for AUTH when available."""
        return self.__auth_code

    @auth_code.setter
    def auth_code(self, value):
        self.__auth_code = value

    @property
    def failure_reason(self):
        """Optional Antom-normalized failure code, maximum 64 characters. Sent only for FAIL when a mapped code exists."""
        return self.__failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self.__failure_reason = value

    @property
    def status(self):
        """Required terminal status: SUCCESS or FAIL. CAPTURE is SUCCESS-only. The accepted status never changes."""
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def balance_type(self):
        """ANTOM_BIZ_ACCOUNT or ANTOM_FUND_ACCOUNT, maximum 32 characters. Required with a directional amount; CAPTURE sends ANTOM_BIZ_ACCOUNT."""
        return self.__balance_type

    @balance_type.setter
    def balance_type(self, value):
        self.__balance_type = value

    @property
    def transaction_time(self):
        """Required business-event time in ISO 8601 format with timezone; maximum 32 characters."""
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value

    @property
    def bill_type(self):
        """Required CARD_PAYMENT for AUTH, CAPTURE and REPAYMENT, or CARD_REFUND for AUTH_CANCEL, REFUND and CHARGEBACK."""
        return self.__bill_type

    @bill_type.setter
    def bill_type(self, value):
        self.__bill_type = value

    @property
    def out_amount(self):
        """Required for successful AUTH, CAPTURE and REPAYMENT. CAPTURE carries value "0" and billing currency, not another debit; omitted otherwise."""
        return self.__out_amount

    @out_amount.setter
    def out_amount(self, value):
        self.__out_amount = value

    @property
    def in_amount(self):
        """Optional billing-currency inflow for successful AUTH_CANCEL, REFUND or CHARGEBACK when available. Omitted for CAPTURE."""
        return self.__in_amount

    @in_amount.setter
    def in_amount(self, value):
        self.__in_amount = value

    @property
    def exchange_currency_pair(self):
        """Optional BASE/QUOTE currency pair, maximum 8 characters. Sent with exchangeRate for a cross-currency transaction when both are available."""
        return self.__exchange_currency_pair

    @exchange_currency_pair.setter
    def exchange_currency_pair(self, value):
        self.__exchange_currency_pair = value

    @property
    def exchange_rate(self):
        """Optional positive quoted decimal string, maximum 32 characters. One major BASE unit equals this many QUOTE units; paired with exchangeCurrencyPair."""
        return self.__exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self.__exchange_rate = value

    @property
    def transaction_amount(self):
        """Required current-event amount in original transaction currency. For CAPTURE this is the captured amount, not the zero additional outflow."""
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value

    @property
    def asset_id(self):
        """Required merchant-owned card asset ID; maximum 32 characters."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value

    @property
    def masked_card_no(self):
        """Optional PCI-safe card mask exposing at most the last four digits; maximum 32 characters."""
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value

    @property
    def card_product(self):
        """Optional original-transaction program code matching ^[A-Z0-9]{3}$. Extensible string, not a fixed enum or rebate rate; later card-profile changes do not rewrite it."""
        return self.__card_product

    @card_product.setter
    def card_product(self, value):
        self.__card_product = value

    @property
    def merchant_info(self):
        """Optional approved merchant context. Name maximum 256 characters, region exactly 2 and mcc exactly 4; parent omitted when no child is available."""
        return self.__merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        self.__merchant_info = value

    @property
    def metadata(self):
        """Optional approved context: at most 30 entries, keys at most 32 characters, values at most 128 and serialized JSON at most 3096. No key is approved in notification profile v2.1, so it is omitted."""
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    def __parse_notify_body(self, notify_body):
        notify = json.loads(notify_body)
        if "eventId" in notify:
            self.__event_id = notify["eventId"]
        if "lifecycleId" in notify:
            self.__lifecycle_id = notify["lifecycleId"]
        if "eventType" in notify:
            self.__event_type = notify["eventType"]
        if "authTime" in notify:
            self.__auth_time = notify["authTime"]
        if "authExpireTime" in notify:
            self.__auth_expire_time = notify["authExpireTime"]
        if "authType" in notify:
            self.__auth_type = notify["authType"]
        if "authCode" in notify:
            self.__auth_code = notify["authCode"]
        if "failureReason" in notify:
            self.__failure_reason = notify["failureReason"]
        if "status" in notify:
            self.__status = notify["status"]
        if "balanceType" in notify:
            self.__balance_type = notify["balanceType"]
        if "transactionTime" in notify:
            self.__transaction_time = notify["transactionTime"]
        if "billType" in notify:
            self.__bill_type = notify["billType"]
        if notify.get("outAmount") is not None:
            self.__out_amount = Amount()
            self.__out_amount.parse_rsp_body(notify["outAmount"])
        if notify.get("inAmount") is not None:
            self.__in_amount = Amount()
            self.__in_amount.parse_rsp_body(notify["inAmount"])
        if "exchangeCurrencyPair" in notify:
            self.__exchange_currency_pair = notify["exchangeCurrencyPair"]
        if "exchangeRate" in notify:
            self.__exchange_rate = notify["exchangeRate"]
        if notify.get("transactionAmount") is not None:
            self.__transaction_amount = Amount()
            self.__transaction_amount.parse_rsp_body(notify["transactionAmount"])
        if "assetId" in notify:
            self.__asset_id = notify["assetId"]
        if "maskedCardNo" in notify:
            self.__masked_card_no = notify["maskedCardNo"]
        if "cardProduct" in notify:
            self.__card_product = notify["cardProduct"]
        if notify.get("merchantInfo") is not None:
            self.__merchant_info = EventMerchantInfo()
            self.__merchant_info.parse_rsp_body(notify["merchantInfo"])
        if "metadata" in notify:
            self.__metadata = notify["metadata"]
