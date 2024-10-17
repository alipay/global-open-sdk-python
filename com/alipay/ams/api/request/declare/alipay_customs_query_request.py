import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCustomsQueryRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomsQueryRequest, self).__init__(AntomPathConstants.INQUIRY_DECLARE_PATH)
        self.__declaration_request_ids = None  # type: list[str]

    @property
    def declaration_request_ids(self):
        return self.__declaration_request_ids

    @declaration_request_ids.setter
    def declaration_request_ids(self, value):
        self.__declaration_request_ids = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__declaration_request_ids is not None:
            params['declarationRequestIds'] = self.__declaration_request_ids
        return params
