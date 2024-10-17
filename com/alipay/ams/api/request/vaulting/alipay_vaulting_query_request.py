import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayVaultingQueryRequest(AlipayRequest):
    
    def __init__(self):
        super(AlipayVaultingQueryRequest, self).__init__(AntomPathConstants.INQUIRE_VAULTING_PATH)
        self.__vaulting_request_id = None


    @property
    def vaulting_request_id(self):
        return self.__vaulting_request_id
    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__vaulting_request_id is not None:
            params['vaultingRequestId'] = self.__vaulting_request_id
        return params