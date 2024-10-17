import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayInquireBalanceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireBalanceRequest, self).__init__(AntomPathConstants.MARKETPLACE_INQUIREBALANCE_PATH)
        self.__referenceMerchantId = None

    @property
    def reference_merchant_id(self):
        return self.__referenceMerchantId

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__referenceMerchantId = value


    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__referenceMerchantId is not None:
            params['referenceMerchantId'] = self.__referenceMerchantId
        return params