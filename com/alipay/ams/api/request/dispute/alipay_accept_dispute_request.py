import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayAcceptDisputeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayAcceptDisputeRequest, self).__init__(AntomPathConstants.ACCEPT_DISPUTE_PATH)
        self.__dispute_id = None

    @property
    def dispute_id(self):
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__dispute_id is not None:
            params['disputeId'] = self.__dispute_id

        return params
