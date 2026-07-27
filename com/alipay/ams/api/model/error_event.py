import json

from com.alipay.ams.api.model.event_payload import EventPayload


class ErrorEvent:
    def __init__(self):

        self.__error_code = None  # type: str
        self.__idempotency_key = None  # type: str
        self.__event_timestamp = None  # type: int
        self.__payload = None  # type: EventPayload


    @property
    def error_code(self):
        """
        The error code.
        """
        return self.__error_code

    @error_code.setter
    def error_code(self, value):
        self.__error_code = value

    @property
    def idempotency_key(self):
        """
        The idempotency key. Maximum length: 128 characters.
        """
        return self.__idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, value):
        self.__idempotency_key = value

    @property
    def event_timestamp(self):
        """
        The original event timestamp, 13-digit millisecond timestamp.
        """
        return self.__event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, value):
        self.__event_timestamp = value

    @property
    def payload(self):
        """Gets the payload of this ErrorEvent.
        """
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "error_code") and self.error_code is not None:
            params['errorCode'] = self.error_code
        if hasattr(self, "idempotency_key") and self.idempotency_key is not None:
            params['idempotencyKey'] = self.idempotency_key
        if hasattr(self, "event_timestamp") and self.event_timestamp is not None:
            params['eventTimestamp'] = self.event_timestamp
        if hasattr(self, "payload") and self.payload is not None:
            params['payload'] = self.payload
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        if 'errorCode' in response_body:
            self.__error_code = response_body['errorCode']
        if 'idempotencyKey' in response_body:
            self.__idempotency_key = response_body['idempotencyKey']
        if 'eventTimestamp' in response_body:
            self.__event_timestamp = response_body['eventTimestamp']
        if 'payload' in response_body:
            self.__payload = EventPayload()
            self.__payload.parse_rsp_body(response_body['payload'])
