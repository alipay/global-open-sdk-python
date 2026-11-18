import json
from typing import Optional, Any, Dict

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipaySubscriptionCancelNotify(AlipayNotify):
    def __init__(self, notify_body):
        super(AlipaySubscriptionCancelNotify, self).__init__()
        self.__payment_amount = None  # type: Optional[PaymentAmount]
        self.__payment_create_time = None  # type: Optional[str]
        self.__payment_time = None  # type: Optional[str]
        self.__period_end_time = None  # type: Optional[str]
        self.__phase_no = None  # type: Optional[str]
        self.__subscription_id = None  # type: Optional[str]
        self.__subscription_order_id = None  # type: Optional[str]
        self.__subscription_order_status = None  # type: Optional[str]
        self.__subscription_request_id = None  # type: Optional[str]
        self.__subscription_trans_id = None  # type: Optional[str]
        self.__parse_notify_body(notify_body)

    # --- Properties for payment_amount ---
    @property
    def payment_amount(self) -> Optional['PaymentAmount']:
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value: Optional['PaymentAmount']):
        self.__payment_amount = value

    # --- Properties for payment_create_time ---
    @property
    def payment_create_time(self) -> Optional[str]:
        return self.__payment_create_time

    @payment_create_time.setter
    def payment_create_time(self, value: Optional[str]):
        self.__payment_create_time = value

    # --- Properties for payment_time ---
    @property
    def payment_time(self) -> Optional[str]:
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value: Optional[str]):
        self.__payment_time = value

    # --- Properties for period_end_time ---
    @property
    def period_end_time(self) -> Optional[str]:
        return self.__period_end_time

    @period_end_time.setter
    def period_end_time(self, value: Optional[str]):
        self.__period_end_time = value

    # --- Properties for phase_no ---
    @property
    def phase_no(self) -> Optional[str]:
        return self.__phase_no

    @phase_no.setter
    def phase_no(self, value: Optional[str]):
        self.__phase_no = value


    # --- Properties for subscription_id ---
    @property
    def subscription_id(self) -> Optional[str]:
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value: Optional[str]):
        self.__subscription_id = value

    # --- Properties for subscription_order_id ---
    @property
    def subscription_order_id(self) -> Optional[str]:
        return self.__subscription_order_id

    @subscription_order_id.setter
    def subscription_order_id(self, value: Optional[str]):
        self.__subscription_order_id = value

    # --- Properties for subscription_order_status ---
    @property
    def subscription_order_status(self) -> Optional[str]:
        return self.__subscription_order_status

    @subscription_order_status.setter
    def subscription_order_status(self, value: Optional[str]):
        self.__subscription_order_status = value

    # --- Properties for subscription_request_id ---
    @property
    def subscription_request_id(self) -> Optional[str]:
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value: Optional[str]):
        self.__subscription_request_id = value

    # --- Properties for subscription_trans_id ---
    @property
    def subscription_trans_id(self) -> Optional[str]:
        return self.__subscription_trans_id

    @subscription_trans_id.setter
    def subscription_trans_id(self, value: Optional[str]):
        self.__subscription_trans_id = value

    def to_ams_dict(self) -> Dict[str, Any]:
        """Convert object to dictionary with camelCase keys for AMS API."""
        params = {}

        if self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount.to_ams_dict()
        if self.payment_create_time is not None:
            params['paymentCreateTime'] = self.payment_create_time
        if self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if self.period_end_time is not None:
            params['periodEndTime'] = self.period_end_time
        if self.phase_no is not None:
            params['phaseNo'] = self.phase_no
        if self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if self.subscription_order_id is not None:
            params['subscriptionOrderId'] = self.subscription_order_id
        if self.subscription_order_status is not None:
            params['subscriptionOrderStatus'] = self.subscription_order_status
        if self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if self.subscription_trans_id is not None:
            params['subscriptionTransId'] = self.subscription_trans_id

        return params

    def __parse_notify_body(self, notify_body):
        notify = super(AlipaySubscriptionCancelNotify, self).parse_notify_body(notify_body)
        if "paymentAmount" in notify:
            from com.alipay.ams.api.model.amount import Amount
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(notify["paymentAmount"])
        if "paymentCreateTime" in notify:
            self.__payment_create_time = notify["paymentCreateTime"]
        if "paymentTime" in notify:
            self.__payment_time = notify["paymentTime"]
        if "periodEndTime" in notify:
            self.__period_end_time = notify["periodEndTime"]
        if "phaseNo" in notify:
            self.__phase_no = notify["phaseNo"]
        if "subscriptionId" in notify:
            self.__subscription_id = notify["subscriptionId"]
        if "subscriptionOrderId" in notify:
            self.__subscription_order_id = notify["subscriptionOrderId"]
        if "subscriptionOrderStatus" in notify:
            self.__subscription_order_status = notify["subscriptionOrderStatus"]
        if "subscriptionRequestId" in notify:
            self.__subscription_request_id = notify["subscriptionRequestId"]
        if "subscriptionTransId" in notify:
            self.__subscription_trans_id = notify["subscriptionTransId"]