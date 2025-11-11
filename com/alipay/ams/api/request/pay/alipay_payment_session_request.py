import json
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.credit_pay_plan import CreditPayPlan
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.agreement_info import AgreementInfo
from com.alipay.ams.api.model.risk_data import RiskData
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.available_payment_method import AvailablePaymentMethod



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPaymentSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPaymentSessionRequest, self).__init__("/ams/api/v1/payments/createPaymentSession") 

        self.__product_code = None  # type: ProductCodeType
        self.__payment_request_id = None  # type: str
        self.__order = None  # type: Order
        self.__payment_amount = None  # type: Amount
        self.__payment_method = None  # type: PaymentMethod
        self.__payment_session_expiry_time = None  # type: str
        self.__payment_redirect_url = None  # type: str
        self.__payment_notify_url = None  # type: str
        self.__payment_factor = None  # type: PaymentFactor
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__enable_installment_collection = None  # type: bool
        self.__credit_pay_plan = None  # type: CreditPayPlan
        self.__merchant_region = None  # type: str
        self.__env = None  # type: Env
        self.__agreement_info = None  # type: AgreementInfo
        self.__risk_data = None  # type: RiskData
        self.__product_scene = None  # type: str
        self.__saved_payment_methods = None  # type: [PaymentMethod]
        self.__locale = None  # type: str
        self.__available_payment_method = None  # type: AvailablePaymentMethod
        self.__test_file = None  # type: str
        

    @property
    def product_code(self):
        """Gets the product_code of this AlipayPaymentSessionRequest.
        
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value
    @property
    def payment_request_id(self):
        """
        The unique ID assigned by a merchant to identify a payment request.   More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def order(self):
        """Gets the order of this AlipayPaymentSessionRequest.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayPaymentSessionRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayPaymentSessionRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def payment_session_expiry_time(self):
        """
        The specific date and time after which the payment session will expire. The default expiration time is 1 hour after the session creation. For example, if the session is created at 2023-7-27T12:00:01+08:30, the session expiration time is 2023-7-27T13:00:01+08:30.  Specify this parameter if you want to use a payment session expiration time that differs from the default time. The specified expiration time must be 0 to 1 hour after session creation.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__payment_session_expiry_time

    @payment_session_expiry_time.setter
    def payment_session_expiry_time(self, value):
        self.__payment_session_expiry_time = value
    @property
    def payment_redirect_url(self):
        """
        The merchant page URL that the user is redirected to after the payment is completed.  More information:  Maximum length: 2048 characters
        """
        return self.__payment_redirect_url

    @payment_redirect_url.setter
    def payment_redirect_url(self, value):
        self.__payment_redirect_url = value
    @property
    def payment_notify_url(self):
        """
        The URL that is used to receive the payment result notification.  Specify this parameter if you want to receive an asynchronous notification of the payment result. You can also set the URL to receive the result notification in Antom Dashboard. If the URL is specified in both the request and Antom Dashboard, the value specified in the request takes precedence.  More information:  Maximum length: 2048 characters
        """
        return self.__payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self.__payment_notify_url = value
    @property
    def payment_factor(self):
        """Gets the payment_factor of this AlipayPaymentSessionRequest.
        
        """
        return self.__payment_factor

    @payment_factor.setter
    def payment_factor(self, value):
        self.__payment_factor = value
    @property
    def settlement_strategy(self):
        """Gets the settlement_strategy of this AlipayPaymentSessionRequest.
        
        """
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value
    @property
    def enable_installment_collection(self):
        """
        Indicates whether Antom collects the installment information for the payment. Specify this parameter if you need Antom to collect the installment information. Valid values are:  true: indicates Antom collects installment information when the user&#39;s card supports installments. Installments are not available when the user&#39;s card does not support installments. false: indicates you do not need Antom to collect the installment information. The same applies when the value is empty or you do not specify this parameter.   
        """
        return self.__enable_installment_collection

    @enable_installment_collection.setter
    def enable_installment_collection(self, value):
        self.__enable_installment_collection = value
    @property
    def credit_pay_plan(self):
        """Gets the credit_pay_plan of this AlipayPaymentSessionRequest.
        
        """
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value
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
    def env(self):
        """Gets the env of this AlipayPaymentSessionRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def agreement_info(self):
        """Gets the agreement_info of this AlipayPaymentSessionRequest.
        
        """
        return self.__agreement_info

    @agreement_info.setter
    def agreement_info(self, value):
        self.__agreement_info = value
    @property
    def risk_data(self):
        """Gets the risk_data of this AlipayPaymentSessionRequest.
        
        """
        return self.__risk_data

    @risk_data.setter
    def risk_data(self, value):
        self.__risk_data = value
    @property
    def product_scene(self):
        """
        Specified product scenarios include valid values:  ​CHECKOUT_PAYMENT​: Indicates that the merchant integrates using the Checkout Page. ​ELEMENT_PAYMENT​: Indicates that the merchant integrates using the Element. More information:  Maximum length: 32 characters
        """
        return self.__product_scene

    @product_scene.setter
    def product_scene(self, value):
        self.__product_scene = value
    @property
    def saved_payment_methods(self):
        """
        Payment information stored by the user in the merchant system.
        """
        return self.__saved_payment_methods

    @saved_payment_methods.setter
    def saved_payment_methods(self, value):
        self.__saved_payment_methods = value
    @property
    def locale(self):
        """
        Language tag specified for the Checkout Page. If this field is empty or set to automatic, the default language setting of the browser will be used, which is usually English.  More information:  Maximum length: 8 characters
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value
    @property
    def available_payment_method(self):
        """Gets the available_payment_method of this AlipayPaymentSessionRequest.
        
        """
        return self.__available_payment_method

    @available_payment_method.setter
    def available_payment_method(self, value):
        self.__available_payment_method = value
    @property
    def test_file(self):
        """Gets the test_file of this AlipayPaymentSessionRequest.
        
        """
        return self.__test_file

    @test_file.setter
    def test_file(self, value):
        self.__test_file = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code is not None:
            params['productCode'] = self.product_code
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "order") and self.order is not None:
            params['order'] = self.order
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "payment_session_expiry_time") and self.payment_session_expiry_time is not None:
            params['paymentSessionExpiryTime'] = self.payment_session_expiry_time
        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url is not None:
            params['paymentRedirectUrl'] = self.payment_redirect_url
        if hasattr(self, "payment_notify_url") and self.payment_notify_url is not None:
            params['paymentNotifyUrl'] = self.payment_notify_url
        if hasattr(self, "payment_factor") and self.payment_factor is not None:
            params['paymentFactor'] = self.payment_factor
        if hasattr(self, "settlement_strategy") and self.settlement_strategy is not None:
            params['settlementStrategy'] = self.settlement_strategy
        if hasattr(self, "enable_installment_collection") and self.enable_installment_collection is not None:
            params['enableInstallmentCollection'] = self.enable_installment_collection
        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan is not None:
            params['creditPayPlan'] = self.credit_pay_plan
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "agreement_info") and self.agreement_info is not None:
            params['agreementInfo'] = self.agreement_info
        if hasattr(self, "risk_data") and self.risk_data is not None:
            params['riskData'] = self.risk_data
        if hasattr(self, "product_scene") and self.product_scene is not None:
            params['productScene'] = self.product_scene
        if hasattr(self, "saved_payment_methods") and self.saved_payment_methods is not None:
            params['savedPaymentMethods'] = self.saved_payment_methods
        if hasattr(self, "locale") and self.locale is not None:
            params['locale'] = self.locale
        if hasattr(self, "available_payment_method") and self.available_payment_method is not None:
            params['availablePaymentMethod'] = self.available_payment_method
        if hasattr(self, "test_file") and self.test_file is not None:
            params['testFile'] = self.test_file
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productCode' in response_body:
            product_code_temp = ProductCodeType.value_of(response_body['productCode'])
            self.__product_code = product_code_temp
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'order' in response_body:
            self.__order = Order()
            self.__order.parse_rsp_body(response_body['order'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'paymentSessionExpiryTime' in response_body:
            self.__payment_session_expiry_time = response_body['paymentSessionExpiryTime']
        if 'paymentRedirectUrl' in response_body:
            self.__payment_redirect_url = response_body['paymentRedirectUrl']
        if 'paymentNotifyUrl' in response_body:
            self.__payment_notify_url = response_body['paymentNotifyUrl']
        if 'paymentFactor' in response_body:
            self.__payment_factor = PaymentFactor()
            self.__payment_factor.parse_rsp_body(response_body['paymentFactor'])
        if 'settlementStrategy' in response_body:
            self.__settlement_strategy = SettlementStrategy()
            self.__settlement_strategy.parse_rsp_body(response_body['settlementStrategy'])
        if 'enableInstallmentCollection' in response_body:
            self.__enable_installment_collection = response_body['enableInstallmentCollection']
        if 'creditPayPlan' in response_body:
            self.__credit_pay_plan = CreditPayPlan()
            self.__credit_pay_plan.parse_rsp_body(response_body['creditPayPlan'])
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'agreementInfo' in response_body:
            self.__agreement_info = AgreementInfo()
            self.__agreement_info.parse_rsp_body(response_body['agreementInfo'])
        if 'riskData' in response_body:
            self.__risk_data = RiskData()
            self.__risk_data.parse_rsp_body(response_body['riskData'])
        if 'productScene' in response_body:
            self.__product_scene = response_body['productScene']
        if 'savedPaymentMethods' in response_body:
            self.__saved_payment_methods = []
            for item in response_body['savedPaymentMethods']:
                obj = PaymentMethod()
                obj.parse_rsp_body(item)
                self.__saved_payment_methods.append(obj)
        if 'locale' in response_body:
            self.__locale = response_body['locale']
        if 'availablePaymentMethod' in response_body:
            self.__available_payment_method = AvailablePaymentMethod()
            self.__available_payment_method.parse_rsp_body(response_body['availablePaymentMethod'])
        if 'testFile' in response_body:
            self.__test_file = response_body['testFile']
