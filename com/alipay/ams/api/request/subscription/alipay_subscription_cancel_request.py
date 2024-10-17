import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.cancellation_type import CancellationType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySubscriptionCancelRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionCancelRequest, self).__init__(AntomPathConstants.SUBSCRIPTION_CANCEL_PATH)
        self.__subscription_id = None
        self.__subscription_request_id = None
        self.__cancellation_type = None  # type:CancellationType

    @property
    def subscription_id(self):
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value

    @property
    def subscription_request_id(self):
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value

    @property
    def cancellation_type(self):
        return self.__cancellation_type

    @cancellation_type.setter
    def cancellation_type(self, value):
        self.__cancellation_type = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_request_id") and self.subscription_request_id:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "cancellation_type") and self.cancellation_type:
            params['cancellationType'] = self.cancellation_type

        return params
