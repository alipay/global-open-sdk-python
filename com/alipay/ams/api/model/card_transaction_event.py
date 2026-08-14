import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.event_merchant_info import EventMerchantInfo




class CardTransactionEvent:
    def __init__(self):
        
        self.__event_id = None  # type: str
        self.__lifecycle_id = None  # type: str
        self.__event_type = None  # type: str
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
        self.__merchant_info = None  # type: EventMerchantInfo
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def event_id(self):
        """
        The unique event ID. Use this field to deduplicate events.
        """
        return self.__event_id

    @event_id.setter
    def event_id(self, value):
        self.__event_id = value
    @property
    def lifecycle_id(self):
        """
        The spend-group ID that correlates authorization, capture, refund, and chargeback events.
        """
        return self.__lifecycle_id

    @lifecycle_id.setter
    def lifecycle_id(self, value):
        self.__lifecycle_id = value
    @property
    def event_type(self):
        """
        The event type. Current values are AUTH, AUTH_CANCEL, CAPTURE, REFUND, CHARGEBACK, and REPAYMENT. Consumers must preserve unknown future values.
        """
        return self.__event_type

    @event_type.setter
    def event_type(self, value):
        self.__event_type = value
    @property
    def auth_expire_time(self):
        """
        The authorization expiry time in ISO 8601 format. Returned only for an AUTH event when the source supplies the value.
        """
        return self.__auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, value):
        self.__auth_expire_time = value
    @property
    def auth_type(self):
        """
        The authorization type. Current values are AUTH and PRE_AUTH. Returned only for an AUTH event when available; consumers must preserve unknown future values.
        """
        return self.__auth_type

    @auth_type.setter
    def auth_type(self, value):
        self.__auth_type = value
    @property
    def auth_code(self):
        """
        The network approval code. Returned only for an AUTH event when available.
        """
        return self.__auth_code

    @auth_code.setter
    def auth_code(self, value):
        self.__auth_code = value
    @property
    def failure_reason(self):
        """
        The Antom-normalized public failure code. Returned only when status is FAIL.
        """
        return self.__failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self.__failure_reason = value
    @property
    def status(self):
        """
        The event status. Current values are SUCCESS, FAIL, and PROCESSING. Consumers must treat unknown future values as non-terminal.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def balance_type(self):
        """
        The balance bucket. Current values are ANTOM_BIZ_ACCOUNT and ANTOM_FUND_ACCOUNT. Returned when a balance movement applies; consumers must preserve unknown future values.
        """
        return self.__balance_type

    @balance_type.setter
    def balance_type(self, value):
        self.__balance_type = value
    @property
    def transaction_time(self):
        """
        The time associated with the card event in ISO 8601 format with a timezone.
        """
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value
    @property
    def bill_type(self):
        """
        The bill type. Current values are CARD_PAYMENT and CARD_REFUND. Consumers must preserve unknown future values.
        """
        return self.__bill_type

    @bill_type.setter
    def bill_type(self, value):
        self.__bill_type = value
    @property
    def out_amount(self):
        """Gets the out_amount of this CardTransactionEvent.
        
        """
        return self.__out_amount

    @out_amount.setter
    def out_amount(self, value):
        self.__out_amount = value
    @property
    def in_amount(self):
        """Gets the in_amount of this CardTransactionEvent.
        
        """
        return self.__in_amount

    @in_amount.setter
    def in_amount(self, value):
        self.__in_amount = value
    @property
    def exchange_currency_pair(self):
        """
        The ISO 4217 base/quote currency pair, such as USD/CAD. Returned for cross-currency events when both currencies are available.
        """
        return self.__exchange_currency_pair

    @exchange_currency_pair.setter
    def exchange_currency_pair(self, value):
        self.__exchange_currency_pair = value
    @property
    def exchange_rate(self):
        """
        The channel-supplied base/quote exchange rate. Returned for cross-currency events.
        """
        return self.__exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self.__exchange_rate = value
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this CardTransactionEvent.
        
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value
    @property
    def asset_id(self):
        """
        The card asset ID.
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def masked_card_no(self):
        """
        The PCI-compliant masked card number. Returned when masking information is available.
        """
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value
    @property
    def merchant_info(self):
        """Gets the merchant_info of this CardTransactionEvent.
        
        """
        return self.__merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        self.__merchant_info = value
    @property
    def metadata(self):
        """
        Provider extension metadata. The map supports at most 30 entries; each key is at most 32 characters, each value is at most 128 characters, and the complete serialized JSON is at most 3096 characters. Consumers must not depend on an undeclared key or display it directly.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "event_id") and self.event_id is not None:
            params['eventId'] = self.event_id
        if hasattr(self, "lifecycle_id") and self.lifecycle_id is not None:
            params['lifecycleId'] = self.lifecycle_id
        if hasattr(self, "event_type") and self.event_type is not None:
            params['eventType'] = self.event_type
        if hasattr(self, "auth_expire_time") and self.auth_expire_time is not None:
            params['authExpireTime'] = self.auth_expire_time
        if hasattr(self, "auth_type") and self.auth_type is not None:
            params['authType'] = self.auth_type
        if hasattr(self, "auth_code") and self.auth_code is not None:
            params['authCode'] = self.auth_code
        if hasattr(self, "failure_reason") and self.failure_reason is not None:
            params['failureReason'] = self.failure_reason
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "balance_type") and self.balance_type is not None:
            params['balanceType'] = self.balance_type
        if hasattr(self, "transaction_time") and self.transaction_time is not None:
            params['transactionTime'] = self.transaction_time
        if hasattr(self, "bill_type") and self.bill_type is not None:
            params['billType'] = self.bill_type
        if hasattr(self, "out_amount") and self.out_amount is not None:
            params['outAmount'] = self.out_amount
        if hasattr(self, "in_amount") and self.in_amount is not None:
            params['inAmount'] = self.in_amount
        if hasattr(self, "exchange_currency_pair") and self.exchange_currency_pair is not None:
            params['exchangeCurrencyPair'] = self.exchange_currency_pair
        if hasattr(self, "exchange_rate") and self.exchange_rate is not None:
            params['exchangeRate'] = self.exchange_rate
        if hasattr(self, "transaction_amount") and self.transaction_amount is not None:
            params['transactionAmount'] = self.transaction_amount
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "masked_card_no") and self.masked_card_no is not None:
            params['maskedCardNo'] = self.masked_card_no
        if hasattr(self, "merchant_info") and self.merchant_info is not None:
            params['merchantInfo'] = self.merchant_info
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'eventId' in response_body:
            self.__event_id = response_body['eventId']
        if 'lifecycleId' in response_body:
            self.__lifecycle_id = response_body['lifecycleId']
        if 'eventType' in response_body:
            self.__event_type = response_body['eventType']
        if 'authExpireTime' in response_body:
            self.__auth_expire_time = response_body['authExpireTime']
        if 'authType' in response_body:
            self.__auth_type = response_body['authType']
        if 'authCode' in response_body:
            self.__auth_code = response_body['authCode']
        if 'failureReason' in response_body:
            self.__failure_reason = response_body['failureReason']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'balanceType' in response_body:
            self.__balance_type = response_body['balanceType']
        if 'transactionTime' in response_body:
            self.__transaction_time = response_body['transactionTime']
        if 'billType' in response_body:
            self.__bill_type = response_body['billType']
        if 'outAmount' in response_body:
            self.__out_amount = Amount()
            self.__out_amount.parse_rsp_body(response_body['outAmount'])
        if 'inAmount' in response_body:
            self.__in_amount = Amount()
            self.__in_amount.parse_rsp_body(response_body['inAmount'])
        if 'exchangeCurrencyPair' in response_body:
            self.__exchange_currency_pair = response_body['exchangeCurrencyPair']
        if 'exchangeRate' in response_body:
            self.__exchange_rate = response_body['exchangeRate']
        if 'transactionAmount' in response_body:
            self.__transaction_amount = Amount()
            self.__transaction_amount.parse_rsp_body(response_body['transactionAmount'])
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'maskedCardNo' in response_body:
            self.__masked_card_no = response_body['maskedCardNo']
        if 'merchantInfo' in response_body:
            self.__merchant_info = EventMerchantInfo()
            self.__merchant_info.parse_rsp_body(response_body['merchantInfo'])
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
