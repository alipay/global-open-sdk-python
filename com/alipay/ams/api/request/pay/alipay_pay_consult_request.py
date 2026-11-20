import json
from com.alipay.ams.api.model.payment_evaluation import PaymentEvaluation
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.buyer import Buyer



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPayConsultRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPayConsultRequest, self).__init__("/ams/api/v1/payments/consult") 

        self.__payment_evaluation = None  # type: PaymentEvaluation
        self.__product_code = None  # type: ProductCodeType
        self.__payment_amount = None  # type: Amount
        self.__merchant_region = None  # type: str
        self.__allowed_payment_method_regions = None  # type: [str]
        self.__allowed_payment_methods = None  # type: [str]
        self.__blocked_payment_methods = None  # type: [str]
        self.__region = None  # type: str
        self.__customer_id = None  # type: str
        self.__reference_user_id = None  # type: str
        self.__env = None  # type: Env
        self.__extend_info = None  # type: str
        self.__user_region = None  # type: str
        self.__payment_factor = None  # type: PaymentFactor
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__merchant = None  # type: Merchant
        self.__allowed_psp_regions = None  # type: [str]
        self.__buyer = None  # type: Buyer
        self.__merchant_account_id = None  # type: str
        

    @property
    def payment_evaluation(self):
        """Gets the payment_evaluation of this AlipayPayConsultRequest.
        
        """
        return self.__payment_evaluation

    @payment_evaluation.setter
    def payment_evaluation(self, value):
        self.__payment_evaluation = value
    @property
    def product_code(self):
        """Gets the product_code of this AlipayPayConsultRequest.
        
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayPayConsultRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def merchant_region(self):
        """
        The country or region where the merchant operates the business. The parameter is a 2-letter country or region code that follows ISO 3166 Country Codes standard.  Some possible values are US, SG, HK, PK, JP, CN, BR, AU, and MY.    Note: This parameter is required when you use the Global Acquirer Gateway (GAGW) product.  More information:  Maximum length: 2 characters
        """
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value
    @property
    def allowed_payment_method_regions(self):
        """
        A list of region codes that represent the countries or regions of payment methods. The value of this parameter is a 2-letter ISO country code or GLOBAL.   Note: Specify this parameter if you want available payment methods from specific regions to be returned. For example, if you pass in GLOBAL, global cards Visa and Mastercard are returned.    More information:  Maximum length: 6 characters
        """
        return self.__allowed_payment_method_regions

    @allowed_payment_method_regions.setter
    def allowed_payment_method_regions(self, value):
        self.__allowed_payment_method_regions = value
    @property
    def allowed_payment_methods(self):
        """Gets the allowed_payment_methods of this AlipayPayConsultRequest.
        
        """
        return self.__allowed_payment_methods

    @allowed_payment_methods.setter
    def allowed_payment_methods(self, value):
        self.__allowed_payment_methods = value
    @property
    def blocked_payment_methods(self):
        """Gets the blocked_payment_methods of this AlipayPayConsultRequest.
        
        """
        return self.__blocked_payment_methods

    @blocked_payment_methods.setter
    def blocked_payment_methods(self, value):
        self.__blocked_payment_methods = value
    @property
    def region(self):
        """Gets the region of this AlipayPayConsultRequest.
        
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def customer_id(self):
        """Gets the customer_id of this AlipayPayConsultRequest.
        
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def reference_user_id(self):
        """Gets the reference_user_id of this AlipayPayConsultRequest.
        
        """
        return self.__reference_user_id

    @reference_user_id.setter
    def reference_user_id(self, value):
        self.__reference_user_id = value
    @property
    def env(self):
        """Gets the env of this AlipayPayConsultRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayPayConsultRequest.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def user_region(self):
        """
        The 2-letter country or region code. For more information, see ISO 3166 Country Codes standard. The payment methods will be sorted based on payment method relevance for the given user&#39;s region.   More information:  Maximum length: 2 characters
        """
        return self.__user_region

    @user_region.setter
    def user_region(self, value):
        self.__user_region = value
    @property
    def payment_factor(self):
        """Gets the payment_factor of this AlipayPayConsultRequest.
        
        """
        return self.__payment_factor

    @payment_factor.setter
    def payment_factor(self, value):
        self.__payment_factor = value
    @property
    def settlement_strategy(self):
        """Gets the settlement_strategy of this AlipayPayConsultRequest.
        
        """
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value
    @property
    def merchant(self):
        """Gets the merchant of this AlipayPayConsultRequest.
        
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value
    @property
    def allowed_psp_regions(self):
        """Gets the allowed_psp_regions of this AlipayPayConsultRequest.
        
        """
        return self.__allowed_psp_regions

    @allowed_psp_regions.setter
    def allowed_psp_regions(self, value):
        self.__allowed_psp_regions = value
    @property
    def buyer(self):
        """Gets the buyer of this AlipayPayConsultRequest.
        
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value
    @property
    def merchant_account_id(self):
        """
        The unique ID to identify a merchant account.  Note: Specify this parameter when you use a single client ID across multiple locations.  More information:  Maximum length: 32 characters
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_evaluation") and self.payment_evaluation is not None:
            params['paymentEvaluation'] = self.payment_evaluation
        if hasattr(self, "product_code") and self.product_code is not None:
            params['productCode'] = self.product_code
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "allowed_payment_method_regions") and self.allowed_payment_method_regions is not None:
            params['allowedPaymentMethodRegions'] = self.allowed_payment_method_regions
        if hasattr(self, "allowed_payment_methods") and self.allowed_payment_methods is not None:
            params['allowedPaymentMethods'] = self.allowed_payment_methods
        if hasattr(self, "blocked_payment_methods") and self.blocked_payment_methods is not None:
            params['blockedPaymentMethods'] = self.blocked_payment_methods
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "reference_user_id") and self.reference_user_id is not None:
            params['referenceUserId'] = self.reference_user_id
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "user_region") and self.user_region is not None:
            params['userRegion'] = self.user_region
        if hasattr(self, "payment_factor") and self.payment_factor is not None:
            params['paymentFactor'] = self.payment_factor
        if hasattr(self, "settlement_strategy") and self.settlement_strategy is not None:
            params['settlementStrategy'] = self.settlement_strategy
        if hasattr(self, "merchant") and self.merchant is not None:
            params['merchant'] = self.merchant
        if hasattr(self, "allowed_psp_regions") and self.allowed_psp_regions is not None:
            params['allowedPspRegions'] = self.allowed_psp_regions
        if hasattr(self, "buyer") and self.buyer is not None:
            params['buyer'] = self.buyer
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentEvaluation' in response_body:
            self.__payment_evaluation = PaymentEvaluation()
            self.__payment_evaluation.parse_rsp_body(response_body['paymentEvaluation'])
        if 'productCode' in response_body:
            product_code_temp = ProductCodeType.value_of(response_body['productCode'])
            self.__product_code = product_code_temp
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
        if 'allowedPaymentMethodRegions' in response_body:
            self.__allowed_payment_method_regions = response_body['allowedPaymentMethodRegions']
        if 'allowedPaymentMethods' in response_body:
            self.__allowed_payment_methods = response_body['allowedPaymentMethods']
        if 'blockedPaymentMethods' in response_body:
            self.__blocked_payment_methods = response_body['blockedPaymentMethods']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'referenceUserId' in response_body:
            self.__reference_user_id = response_body['referenceUserId']
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'userRegion' in response_body:
            self.__user_region = response_body['userRegion']
        if 'paymentFactor' in response_body:
            self.__payment_factor = PaymentFactor()
            self.__payment_factor.parse_rsp_body(response_body['paymentFactor'])
        if 'settlementStrategy' in response_body:
            self.__settlement_strategy = SettlementStrategy()
            self.__settlement_strategy.parse_rsp_body(response_body['settlementStrategy'])
        if 'merchant' in response_body:
            self.__merchant = Merchant()
            self.__merchant.parse_rsp_body(response_body['merchant'])
        if 'allowedPspRegions' in response_body:
            self.__allowed_psp_regions = response_body['allowedPspRegions']
        if 'buyer' in response_body:
            self.__buyer = Buyer()
            self.__buyer.parse_rsp_body(response_body['buyer'])
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
