import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.card_transaction_event import CardTransactionEvent




class CardTransactionLifecycleDetail:
    def __init__(self):
        
        self.__lifecycle_id = None  # type: str
        self.__latest_event_type = None  # type: str
        self.__latest_event_status = None  # type: str
        self.__last_update_time = None  # type: str
        self.__transaction_time = None  # type: str
        self.__total_billing_amount = None  # type: Amount
        self.__total_auth_amount = None  # type: Amount
        self.__total_cancel_amount = None  # type: Amount
        self.__total_refund_amount = None  # type: Amount
        self.__total_chargeback_amount = None  # type: Amount
        self.__asset_id = None  # type: str
        self.__masked_card_no = None  # type: str
        self.__events = None  # type: [CardTransactionEvent]
        

    @property
    def lifecycle_id(self):
        """
        The spend-group ID.
        """
        return self.__lifecycle_id

    @lifecycle_id.setter
    def lifecycle_id(self, value):
        self.__lifecycle_id = value
    @property
    def latest_event_type(self):
        """
        The most recent event type. Current values are AUTH, AUTH_CANCEL, CAPTURE, REFUND, CHARGEBACK, and REPAYMENT. Returned when the lifecycle contains at least one event; consumers must preserve unknown future values.
        """
        return self.__latest_event_type

    @latest_event_type.setter
    def latest_event_type(self, value):
        self.__latest_event_type = value
    @property
    def latest_event_status(self):
        """
        The most recent event status. Current values are SUCCESS, FAIL, and PROCESSING. Returned when the lifecycle contains at least one event; consumers must treat unknown future values as non-terminal.
        """
        return self.__latest_event_status

    @latest_event_status.setter
    def latest_event_status(self, value):
        self.__latest_event_status = value
    @property
    def last_update_time(self):
        """
        The time of the most recent event in the lifecycle, in ISO 8601 format.
        """
        return self.__last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self.__last_update_time = value
    @property
    def transaction_time(self):
        """
        The time of the earliest event in the lifecycle, in ISO 8601 format.
        """
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value
    @property
    def total_billing_amount(self):
        """Gets the total_billing_amount of this CardTransactionLifecycleDetail.
        
        """
        return self.__total_billing_amount

    @total_billing_amount.setter
    def total_billing_amount(self, value):
        self.__total_billing_amount = value
    @property
    def total_auth_amount(self):
        """Gets the total_auth_amount of this CardTransactionLifecycleDetail.
        
        """
        return self.__total_auth_amount

    @total_auth_amount.setter
    def total_auth_amount(self, value):
        self.__total_auth_amount = value
    @property
    def total_cancel_amount(self):
        """Gets the total_cancel_amount of this CardTransactionLifecycleDetail.
        
        """
        return self.__total_cancel_amount

    @total_cancel_amount.setter
    def total_cancel_amount(self, value):
        self.__total_cancel_amount = value
    @property
    def total_refund_amount(self):
        """Gets the total_refund_amount of this CardTransactionLifecycleDetail.
        
        """
        return self.__total_refund_amount

    @total_refund_amount.setter
    def total_refund_amount(self, value):
        self.__total_refund_amount = value
    @property
    def total_chargeback_amount(self):
        """Gets the total_chargeback_amount of this CardTransactionLifecycleDetail.
        
        """
        return self.__total_chargeback_amount

    @total_chargeback_amount.setter
    def total_chargeback_amount(self, value):
        self.__total_chargeback_amount = value
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
    def events(self):
        """
        The complete stored event set for the lifecycle. Returned whenever lifecycle is present; an empty stored set returns an empty array.
        """
        return self.__events

    @events.setter
    def events(self, value):
        self.__events = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "lifecycle_id") and self.lifecycle_id is not None:
            params['lifecycleId'] = self.lifecycle_id
        if hasattr(self, "latest_event_type") and self.latest_event_type is not None:
            params['latestEventType'] = self.latest_event_type
        if hasattr(self, "latest_event_status") and self.latest_event_status is not None:
            params['latestEventStatus'] = self.latest_event_status
        if hasattr(self, "last_update_time") and self.last_update_time is not None:
            params['lastUpdateTime'] = self.last_update_time
        if hasattr(self, "transaction_time") and self.transaction_time is not None:
            params['transactionTime'] = self.transaction_time
        if hasattr(self, "total_billing_amount") and self.total_billing_amount is not None:
            params['totalBillingAmount'] = self.total_billing_amount
        if hasattr(self, "total_auth_amount") and self.total_auth_amount is not None:
            params['totalAuthAmount'] = self.total_auth_amount
        if hasattr(self, "total_cancel_amount") and self.total_cancel_amount is not None:
            params['totalCancelAmount'] = self.total_cancel_amount
        if hasattr(self, "total_refund_amount") and self.total_refund_amount is not None:
            params['totalRefundAmount'] = self.total_refund_amount
        if hasattr(self, "total_chargeback_amount") and self.total_chargeback_amount is not None:
            params['totalChargebackAmount'] = self.total_chargeback_amount
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "masked_card_no") and self.masked_card_no is not None:
            params['maskedCardNo'] = self.masked_card_no
        if hasattr(self, "events") and self.events is not None:
            params['events'] = self.events
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'lifecycleId' in response_body:
            self.__lifecycle_id = response_body['lifecycleId']
        if 'latestEventType' in response_body:
            self.__latest_event_type = response_body['latestEventType']
        if 'latestEventStatus' in response_body:
            self.__latest_event_status = response_body['latestEventStatus']
        if 'lastUpdateTime' in response_body:
            self.__last_update_time = response_body['lastUpdateTime']
        if 'transactionTime' in response_body:
            self.__transaction_time = response_body['transactionTime']
        if 'totalBillingAmount' in response_body:
            self.__total_billing_amount = Amount()
            self.__total_billing_amount.parse_rsp_body(response_body['totalBillingAmount'])
        if 'totalAuthAmount' in response_body:
            self.__total_auth_amount = Amount()
            self.__total_auth_amount.parse_rsp_body(response_body['totalAuthAmount'])
        if 'totalCancelAmount' in response_body:
            self.__total_cancel_amount = Amount()
            self.__total_cancel_amount.parse_rsp_body(response_body['totalCancelAmount'])
        if 'totalRefundAmount' in response_body:
            self.__total_refund_amount = Amount()
            self.__total_refund_amount.parse_rsp_body(response_body['totalRefundAmount'])
        if 'totalChargebackAmount' in response_body:
            self.__total_chargeback_amount = Amount()
            self.__total_chargeback_amount.parse_rsp_body(response_body['totalChargebackAmount'])
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'maskedCardNo' in response_body:
            self.__masked_card_no = response_body['maskedCardNo']
        if 'events' in response_body:
            self.__events = []
            for item in response_body['events']:
                obj = CardTransactionEvent()
                obj.parse_rsp_body(item)
                self.__events.append(obj)
