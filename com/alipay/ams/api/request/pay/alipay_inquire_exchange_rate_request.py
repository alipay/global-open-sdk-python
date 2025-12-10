import json
from com.alipay.ams.api.model.currency_pair import CurrencyPair
from com.alipay.ams.api.model.product_code_type import ProductCodeType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireExchangeRateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireExchangeRateRequest, self).__init__("/ams/api/v1/payments/inquireExchangeRate") 

        self.__merchant_account_id = None  # type: str
        self.__payment_currency = None  # type: str
        self.__currency_pairs = None  # type: [CurrencyPair]
        self.__sell_currency = None  # type: str
        self.__buy_currency = None  # type: str
        self.__product_code = None  # type: ProductCodeType
        

    @property
    def merchant_account_id(self):
        """Gets the merchant_account_id of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def payment_currency(self):
        """Gets the payment_currency of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self.__payment_currency = value
    @property
    def currency_pairs(self):
        """Gets the currency_pairs of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__currency_pairs

    @currency_pairs.setter
    def currency_pairs(self, value):
        self.__currency_pairs = value
    @property
    def sell_currency(self):
        """Gets the sell_currency of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value
    @property
    def buy_currency(self):
        """Gets the buy_currency of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value
    @property
    def product_code(self):
        """Gets the product_code of this AlipayInquireExchangeRateRequest.
        
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "payment_currency") and self.payment_currency is not None:
            params['paymentCurrency'] = self.payment_currency
        if hasattr(self, "currency_pairs") and self.currency_pairs is not None:
            params['currencyPairs'] = self.currency_pairs
        if hasattr(self, "sell_currency") and self.sell_currency is not None:
            params['sellCurrency'] = self.sell_currency
        if hasattr(self, "buy_currency") and self.buy_currency is not None:
            params['buyCurrency'] = self.buy_currency
        if hasattr(self, "product_code") and self.product_code is not None:
            params['productCode'] = self.product_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'paymentCurrency' in response_body:
            self.__payment_currency = response_body['paymentCurrency']
        if 'currencyPairs' in response_body:
            self.__currency_pairs = []
            for item in response_body['currencyPairs']:
                obj = CurrencyPair()
                obj.parse_rsp_body(item)
                self.__currency_pairs.append(obj)
        if 'sellCurrency' in response_body:
            self.__sell_currency = response_body['sellCurrency']
        if 'buyCurrency' in response_body:
            self.__buy_currency = response_body['buyCurrency']
        if 'productCode' in response_body:
            product_code_temp = ProductCodeType.value_of(response_body['productCode'])
            self.__product_code = product_code_temp
