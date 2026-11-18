import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireNotificationListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireNotificationListRequest, self).__init__("/ams/api/v1/notification/inquireNotificationList") 

        self.__notify_type = None  # type: [str]
        self.__event_create_time_from = None  # type: str
        self.__event_create_time_to = None  # type: str
        self.__limit = None  # type: int
        self.__starting_after = None  # type: str
        

    @property
    def notify_type(self):
        """
        Canonical event types to include: PAYMENT_RESULT, PAYMENT_PENDING, CAPTURE_RESULT, REFUND_RESULT, REGISTRATION_STATUS, PAYMENT_METHOD_ACTIVATION_STATUS, PAYMENT_METHOD_DEACTIVATION_STATUS, MERCHANT_RISK_NOTIFICATION, MERCHANT_INFO_UPDATE_RESULT, MERCHANT_RISK_RFI, MERCHANT_INFO_UPDATED, RISK_POST_REVIEW, DISPUTE_CREATED, DISPUTE_CANCELLED, DISPUTE_JUDGED, DISPUTE_ACCEPTED, RDR_RESOLVED, DEFENSE_SUPPLIED, DEFENSE_DUE_ALERT, TRANSFER_RESULT, TRANSFER_REVERSE_RESULT, BALANCE_TRANSACTION_RESULT, PAYOUT_RESULT. If omitted, null, or empty, all supported types are included.
        """
        return self.__notify_type

    @notify_type.setter
    def notify_type(self, value):
        self.__notify_type = value
    @property
    def event_create_time_from(self):
        """
        Inclusive start time in ISO 8601 format. If omitted, null, or empty, defaults to seven days before eventCreateTimeTo. Earlier values are clamped to the 30-day retention boundary.
        """
        return self.__event_create_time_from

    @event_create_time_from.setter
    def event_create_time_from(self, value):
        self.__event_create_time_from = value
    @property
    def event_create_time_to(self):
        """
        Inclusive end time in ISO 8601 format, not earlier than eventCreateTimeFrom. If omitted, null, or empty, defaults to the first request receive time. Reuse the same value and filters for subsequent pages.
        """
        return self.__event_create_time_to

    @event_create_time_to.setter
    def event_create_time_to(self, value):
        self.__event_create_time_to = value
    @property
    def limit(self):
        """
        Maximum events per page. The server defaults to 10 when omitted or null.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def starting_after(self):
        """
        The UUID v4 event ID returned by an earlier page, used as the forward cursor. If omitted, null, or empty, no cursor is applied.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "notify_type") and self.notify_type is not None:
            params['notifyType'] = self.notify_type
        if hasattr(self, "event_create_time_from") and self.event_create_time_from is not None:
            params['eventCreateTimeFrom'] = self.event_create_time_from
        if hasattr(self, "event_create_time_to") and self.event_create_time_to is not None:
            params['eventCreateTimeTo'] = self.event_create_time_to
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'notifyType' in response_body:
            self.__notify_type = response_body['notifyType']
        if 'eventCreateTimeFrom' in response_body:
            self.__event_create_time_from = response_body['eventCreateTimeFrom']
        if 'eventCreateTimeTo' in response_body:
            self.__event_create_time_to = response_body['eventCreateTimeTo']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
