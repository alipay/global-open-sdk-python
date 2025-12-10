import json
from com.alipay.ams.api.model.customized_info import CustomizedInfo
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.agreement_info import AgreementInfo
from com.alipay.ams.api.model.subscription_info import SubscriptionInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.credit_pay_plan import CreditPayPlan
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.payment_verification_data import PaymentVerificationData



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPayRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPayRequest, self).__init__("/ams/api/v1/payments/pay") 

        self.__metadata = None  # type: str
        self.__customized_info = None  # type: CustomizedInfo
        self.__payment_quote = None  # type: Quote
        self.__agreement_info = None  # type: AgreementInfo
        self.__subscription_info = None  # type: SubscriptionInfo
        self.__processing_amount = None  # type: Amount
        self.__product_code = None  # type: ProductCodeType
        self.__payment_request_id = None  # type: str
        self.__order = None  # type: Order
        self.__payment_amount = None  # type: Amount
        self.__payment_method = None  # type: PaymentMethod
        self.__payment_expiry_time = None  # type: str
        self.__payment_redirect_url = None  # type: str
        self.__payment_notify_url = None  # type: str
        self.__payment_factor = None  # type: PaymentFactor
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__credit_pay_plan = None  # type: CreditPayPlan
        self.__app_id = None  # type: str
        self.__merchant_region = None  # type: str
        self.__user_region = None  # type: str
        self.__env = None  # type: Env
        self.__pay_to_method = None  # type: PaymentMethod
        self.__is_authorization = None  # type: bool
        self.__merchant = None  # type: Merchant
        self.__payment_verification_data = None  # type: PaymentVerificationData
        self.__extend_info = None  # type: str
        self.__merchant_account_id = None  # type: str
        self.__dual_offline_payment = None  # type: bool
        

    @property
    def metadata(self):
        """
        用于商户自定义元数据信息，支持JSON格式
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def customized_info(self):
        """Gets the customized_info of this AlipayPayRequest.
        
        """
        return self.__customized_info

    @customized_info.setter
    def customized_info(self, value):
        self.__customized_info = value
    @property
    def payment_quote(self):
        """Gets the payment_quote of this AlipayPayRequest.
        
        """
        return self.__payment_quote

    @payment_quote.setter
    def payment_quote(self, value):
        self.__payment_quote = value
    @property
    def agreement_info(self):
        """Gets the agreement_info of this AlipayPayRequest.
        
        """
        return self.__agreement_info

    @agreement_info.setter
    def agreement_info(self, value):
        self.__agreement_info = value
    @property
    def subscription_info(self):
        """Gets the subscription_info of this AlipayPayRequest.
        
        """
        return self.__subscription_info

    @subscription_info.setter
    def subscription_info(self, value):
        self.__subscription_info = value
    @property
    def processing_amount(self):
        """Gets the processing_amount of this AlipayPayRequest.
        
        """
        return self.__processing_amount

    @processing_amount.setter
    def processing_amount(self, value):
        self.__processing_amount = value
    @property
    def product_code(self):
        """Gets the product_code of this AlipayPayRequest.
        
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value
    @property
    def payment_request_id(self):
        """
        The unique ID assigned by a merchant to identify a payment request. Antom uses this field for idempotence control.  More information:  This field is an API idempotency field.For payment requests that are initiated with the same value of paymentRequestId and reach a final status of S or F, the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def order(self):
        """Gets the order of this AlipayPayRequest.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayPayRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayPayRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def payment_expiry_time(self):
        """
        The payment expiration time is a specific time after which the payment will expire and the acquirer or merchant must terminate the order processing.   Notes:  For bank transfer payments, the default payment expiration time is 48 hours after the payment request is sent. For other payment categories, the default payment expiration time is usually 14 minutes after the payment request is sent. For example, if the request is sent on 2019-11-27T12:00:01+08:30, the payment expiration time is 2019-11-27T12:14:01+08:30. Specify this field if you want to use a payment expiration time that differs from the default time. For bank transfer payments, the specified payment expiration time must be less than 48 hours after the payment request is sent. For other payment categories, the specified payment expiration time must be less than 10 minutes after the payment request is sent. More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__payment_expiry_time

    @payment_expiry_time.setter
    def payment_expiry_time(self, value):
        self.__payment_expiry_time = value
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
        The URL that is used to receive the payment result notification.  Note: Specify this parameter if you want to receive an asynchronous notification of the payment result. You can also set the URL to receive the result notification in Antom Dashboard. If the URL is specified in both the request and Antom Dashboard, the value specified in the request takes precedence.  More information:  Maximum length: 2048 characters
        """
        return self.__payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self.__payment_notify_url = value
    @property
    def payment_factor(self):
        """Gets the payment_factor of this AlipayPayRequest.
        
        """
        return self.__payment_factor

    @payment_factor.setter
    def payment_factor(self, value):
        self.__payment_factor = value
    @property
    def settlement_strategy(self):
        """Gets the settlement_strategy of this AlipayPayRequest.
        
        """
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value
    @property
    def credit_pay_plan(self):
        """Gets the credit_pay_plan of this AlipayPayRequest.
        
        """
        return self.__credit_pay_plan

    @credit_pay_plan.setter
    def credit_pay_plan(self, value):
        self.__credit_pay_plan = value
    @property
    def app_id(self):
        """
        The unique ID that is assigned by Antom to identify the mini program.  Note: This field is required when terminalType is MINI_APP.  More information:  Maximum length: 32 characters
        """
        return self.__app_id

    @app_id.setter
    def app_id(self, value):
        self.__app_id = value
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
    def user_region(self):
        """
        A 2-letter country or region code based on the standard of ISO 3166 Country Codes. This parameter is used to sort Alipay+ payment methods according to the user&#39;s region. For example, if ALIPAY_CN and KAKAOPAYare both on your payment method list and the user is from South Korea, KAKAOPAY will be listed first on the Alipay+ cashier page.  Note: This parameter is only for the merchant that has integrated the Alipay+ cashier page.    More information:  Maximum length: 2 characters
        """
        return self.__user_region

    @user_region.setter
    def user_region(self, value):
        self.__user_region = value
    @property
    def env(self):
        """Gets the env of this AlipayPayRequest.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def pay_to_method(self):
        """Gets the pay_to_method of this AlipayPayRequest.
        
        """
        return self.__pay_to_method

    @pay_to_method.setter
    def pay_to_method(self, value):
        self.__pay_to_method = value
    @property
    def is_authorization(self):
        """Gets the is_authorization of this AlipayPayRequest.
        
        """
        return self.__is_authorization

    @is_authorization.setter
    def is_authorization(self, value):
        self.__is_authorization = value
    @property
    def merchant(self):
        """Gets the merchant of this AlipayPayRequest.
        
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value
    @property
    def payment_verification_data(self):
        """Gets the payment_verification_data of this AlipayPayRequest.
        
        """
        return self.__payment_verification_data

    @payment_verification_data.setter
    def payment_verification_data(self, value):
        self.__payment_verification_data = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayPayRequest.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def merchant_account_id(self):
        """
        The unique ID to identify a merchant account.  Note: Specify this parameter when you use a single client ID across multiple locations.  More information:  Maximum length: 32 characters
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def dual_offline_payment(self):
        """Gets the dual_offline_payment of this AlipayPayRequest.
        
        """
        return self.__dual_offline_payment

    @dual_offline_payment.setter
    def dual_offline_payment(self, value):
        self.__dual_offline_payment = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "customized_info") and self.customized_info is not None:
            params['customizedInfo'] = self.customized_info
        if hasattr(self, "payment_quote") and self.payment_quote is not None:
            params['paymentQuote'] = self.payment_quote
        if hasattr(self, "agreement_info") and self.agreement_info is not None:
            params['agreementInfo'] = self.agreement_info
        if hasattr(self, "subscription_info") and self.subscription_info is not None:
            params['subscriptionInfo'] = self.subscription_info
        if hasattr(self, "processing_amount") and self.processing_amount is not None:
            params['processingAmount'] = self.processing_amount
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
        if hasattr(self, "payment_expiry_time") and self.payment_expiry_time is not None:
            params['paymentExpiryTime'] = self.payment_expiry_time
        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url is not None:
            params['paymentRedirectUrl'] = self.payment_redirect_url
        if hasattr(self, "payment_notify_url") and self.payment_notify_url is not None:
            params['paymentNotifyUrl'] = self.payment_notify_url
        if hasattr(self, "payment_factor") and self.payment_factor is not None:
            params['paymentFactor'] = self.payment_factor
        if hasattr(self, "settlement_strategy") and self.settlement_strategy is not None:
            params['settlementStrategy'] = self.settlement_strategy
        if hasattr(self, "credit_pay_plan") and self.credit_pay_plan is not None:
            params['creditPayPlan'] = self.credit_pay_plan
        if hasattr(self, "app_id") and self.app_id is not None:
            params['appId'] = self.app_id
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "user_region") and self.user_region is not None:
            params['userRegion'] = self.user_region
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "pay_to_method") and self.pay_to_method is not None:
            params['payToMethod'] = self.pay_to_method
        if hasattr(self, "is_authorization") and self.is_authorization is not None:
            params['isAuthorization'] = self.is_authorization
        if hasattr(self, "merchant") and self.merchant is not None:
            params['merchant'] = self.merchant
        if hasattr(self, "payment_verification_data") and self.payment_verification_data is not None:
            params['paymentVerificationData'] = self.payment_verification_data
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "dual_offline_payment") and self.dual_offline_payment is not None:
            params['dualOfflinePayment'] = self.dual_offline_payment
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'customizedInfo' in response_body:
            self.__customized_info = CustomizedInfo()
            self.__customized_info.parse_rsp_body(response_body['customizedInfo'])
        if 'paymentQuote' in response_body:
            self.__payment_quote = Quote()
            self.__payment_quote.parse_rsp_body(response_body['paymentQuote'])
        if 'agreementInfo' in response_body:
            self.__agreement_info = AgreementInfo()
            self.__agreement_info.parse_rsp_body(response_body['agreementInfo'])
        if 'subscriptionInfo' in response_body:
            self.__subscription_info = SubscriptionInfo()
            self.__subscription_info.parse_rsp_body(response_body['subscriptionInfo'])
        if 'processingAmount' in response_body:
            self.__processing_amount = Amount()
            self.__processing_amount.parse_rsp_body(response_body['processingAmount'])
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
        if 'paymentExpiryTime' in response_body:
            self.__payment_expiry_time = response_body['paymentExpiryTime']
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
        if 'creditPayPlan' in response_body:
            self.__credit_pay_plan = CreditPayPlan()
            self.__credit_pay_plan.parse_rsp_body(response_body['creditPayPlan'])
        if 'appId' in response_body:
            self.__app_id = response_body['appId']
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
        if 'userRegion' in response_body:
            self.__user_region = response_body['userRegion']
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'payToMethod' in response_body:
            self.__pay_to_method = PaymentMethod()
            self.__pay_to_method.parse_rsp_body(response_body['payToMethod'])
        if 'isAuthorization' in response_body:
            self.__is_authorization = response_body['isAuthorization']
        if 'merchant' in response_body:
            self.__merchant = Merchant()
            self.__merchant.parse_rsp_body(response_body['merchant'])
        if 'paymentVerificationData' in response_body:
            self.__payment_verification_data = PaymentVerificationData()
            self.__payment_verification_data.parse_rsp_body(response_body['paymentVerificationData'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'dualOfflinePayment' in response_body:
            self.__dual_offline_payment = response_body['dualOfflinePayment']
