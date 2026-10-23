import json




class NotificationEvent:
    def __init__(self):
        
        self.__event_id = None  # type: str
        self.__notify_type = None  # type: str
        self.__event_create_time = None  # type: str
        self.__delivery_status = None  # type: str
        self.__reference_merchant_id = None  # type: str
        self.__notification_data = None  # type: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        

    @property
    def event_id(self):
        """
        The UUID v4 identifier shared by the webhook event and query result.
        """
        return self.__event_id

    @event_id.setter
    def event_id(self, value):
        self.__event_id = value
    @property
    def notify_type(self):
        """
        The canonical event type, returned when the event exists.
        """
        return self.__notify_type

    @notify_type.setter
    def notify_type(self, value):
        self.__notify_type = value
    @property
    def event_create_time(self):
        """
        The event creation time in ISO 8601 format, returned in UTC with a Z suffix.
        """
        return self.__event_create_time

    @event_create_time.setter
    def event_create_time(self, value):
        self.__event_create_time = value
    @property
    def delivery_status(self):
        """
        The webhook delivery status: DELIVERED, PENDING, or FAILED.
        """
        return self.__delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self.__delivery_status = value
    @property
    def reference_merchant_id(self):
        """
        The ISV sub-merchant reference. Omitted for events belonging to the caller directly. When also present in notificationData, both values match.
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value
    @property
    def notification_data(self):
        """
        The original webhook payload as a JSON object, returned whenever the source payload exists, regardless of delivery status. Fields and the payload-specific event discriminator follow the source webhook contract.
        """
        return self.__notification_data

    @notification_data.setter
    def notification_data(self, value):
        self.__notification_data = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "event_id") and self.event_id is not None:
            params['eventId'] = self.event_id
        if hasattr(self, "notify_type") and self.notify_type is not None:
            params['notifyType'] = self.notify_type
        if hasattr(self, "event_create_time") and self.event_create_time is not None:
            params['eventCreateTime'] = self.event_create_time
        if hasattr(self, "delivery_status") and self.delivery_status is not None:
            params['deliveryStatus'] = self.delivery_status
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        if hasattr(self, "notification_data") and self.notification_data is not None:
            params['notificationData'] = self.notification_data
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'eventId' in response_body:
            self.__event_id = response_body['eventId']
        if 'notifyType' in response_body:
            self.__notify_type = response_body['notifyType']
        if 'eventCreateTime' in response_body:
            self.__event_create_time = response_body['eventCreateTime']
        if 'deliveryStatus' in response_body:
            self.__delivery_status = response_body['deliveryStatus']
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
        if 'notificationData' in response_body:
            self.__notification_data = response_body['notificationData']
