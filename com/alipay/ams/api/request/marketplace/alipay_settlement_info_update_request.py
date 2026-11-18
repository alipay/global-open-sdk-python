import json
from com.alipay.ams.api.model.settlement_bank_account import SettlementBankAccount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySettlementInfoUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySettlementInfoUpdateRequest, self).__init__("/ams/api/v1/merchants/settlementInfo/update") 

        self.__update_request_id = None  # type: str
        self.__reference_merchant_id = None  # type: str
        self.__settlement_currency = None  # type: str
        self.__settlement_bank_account = None  # type: SettlementBankAccount
        

    @property
    def update_request_id(self):
        """
        The unique ID that is assigned by the marketplace to identify an update request for settlement information. Alipay uses this field for idempotence control.   More information:  This field is an API idempotency field.For registration requests that are initiated with the same value of registrationRequestId and reach a final status (resultStatus &#x3D; S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__update_request_id

    @update_request_id.setter
    def update_request_id(self, value):
        self.__update_request_id = value
    @property
    def reference_merchant_id(self):
        """
        The unique ID that is assigned by the marketplace to identify the seller.    More information:  Maximum length: 64 characters
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value
    @property
    def settlement_currency(self):
        """
        The seller&#39;s settlement currency that is specified in the settlement contract. The value of this parameter is a 3-letter currency code that follows the ISO 4217 standard.    More information:  Maximum length: 3 characters
        """
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value
    @property
    def settlement_bank_account(self):
        """Gets the settlement_bank_account of this AlipaySettlementInfoUpdateRequest.
        
        """
        return self.__settlement_bank_account

    @settlement_bank_account.setter
    def settlement_bank_account(self, value):
        self.__settlement_bank_account = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "update_request_id") and self.update_request_id is not None:
            params['updateRequestId'] = self.update_request_id
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        if hasattr(self, "settlement_currency") and self.settlement_currency is not None:
            params['settlementCurrency'] = self.settlement_currency
        if hasattr(self, "settlement_bank_account") and self.settlement_bank_account is not None:
            params['settlementBankAccount'] = self.settlement_bank_account
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'updateRequestId' in response_body:
            self.__update_request_id = response_body['updateRequestId']
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
        if 'settlementCurrency' in response_body:
            self.__settlement_currency = response_body['settlementCurrency']
        if 'settlementBankAccount' in response_body:
            self.__settlement_bank_account = SettlementBankAccount()
            self.__settlement_bank_account.parse_rsp_body(response_body['settlementBankAccount'])
