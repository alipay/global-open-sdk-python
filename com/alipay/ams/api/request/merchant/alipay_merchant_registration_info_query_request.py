import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayMerchantRegistrationInfoQueryRequest(AlipayRequest):

    def __init__(self):
        super(AlipayMerchantRegistrationInfoQueryRequest, self).__init__(AntomPathConstants.MERCHANTS_INQUIRY_REGISTRATION_PATH)
        self.__reference_merchant_id = None

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id:
            params['referenceMerchantId'] = self.reference_merchant_id

        return params
