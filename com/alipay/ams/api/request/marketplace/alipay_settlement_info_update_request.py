import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.settlement_bank_account import SettlementBankAccount
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySettlementInfoUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySettlementInfoUpdateRequest, self).__init__(AntomPathConstants.MARKETPLACE_SETTLEMENTINFO_UPDATE_PATH)
        self.__update_request_id = None
        self.__reference_merchant_id = None
        self.__settlement_currency = None
        self.__settlement_bank_account = None #type: SettlementBankAccount

    @property
    def update_request_id(self):
        return self.__update_request_id

    @update_request_id.setter
    def update_request_id(self, value):
        self.__update_request_id = value

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def settlement_currency(self):
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value

    @property
    def settlement_bank_account(self):
        return self.__settlement_bank_account

    @settlement_bank_account.setter
    def settlement_bank_account(self, value):
        self.__settlement_bank_account = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, 'update_request_id') and self.update_request_id:
            params['updateRequestId'] = self.__update_request_id
        if hasattr(self, 'reference_merchant_id') and self.reference_merchant_id:
            params['referenceMerchantId'] = self.__reference_merchant_id
        if hasattr(self, 'settlement_currency') and self.settlement_currency:
            params['settlementCurrency'] = self.__settlement_currency
        if hasattr(self, 'settlement_bank_account') and self.settlement_bank_account:
            params['settlementBankAccount'] = self.__settlement_bank_account
        return params