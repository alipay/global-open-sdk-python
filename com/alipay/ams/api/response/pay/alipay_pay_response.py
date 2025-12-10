import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo
from com.alipay.ams.api.model.challenge_action_form import ChallengeActionForm
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.model.order_code_form import OrderCodeForm
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.payment_result_info import PaymentResultInfo
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo
from com.alipay.ams.api.model.promotion_result import PromotionResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPayResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__processing_amount = None  # type: Amount
        self.__payment_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_data = None  # type: str
        self.__actual_payment_amount = None  # type: Amount
        self.__payment_quote = None  # type: Quote
        self.__payment_time = None  # type: str
        self.__payment_create_time = None  # type: str
        self.__auth_expiry_time = None  # type: str
        self.__non_guarantee_coupon_value = None  # type: Amount
        self.__payment_action_form = None  # type: str
        self.__psp_customer_info = None  # type: PspCustomerInfo
        self.__challenge_action_form = None  # type: ChallengeActionForm
        self.__redirect_action_form = None  # type: RedirectActionForm
        self.__order_code_form = None  # type: OrderCodeForm
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__extend_info = None  # type: str
        self.__normal_url = None  # type: str
        self.__scheme_url = None  # type: str
        self.__applink_url = None  # type: str
        self.__app_identifier = None  # type: str
        self.__payment_result_info = None  # type: PaymentResultInfo
        self.__acquirer_info = None  # type: AcquirerInfo
        self.__promotion_result = None  # type: [PromotionResult]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPayResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def processing_amount(self):
        """Gets the processing_amount of this AlipayPayResponse.
        
        """
        return self.__processing_amount

    @processing_amount.setter
    def processing_amount(self, value):
        self.__processing_amount = value
    @property
    def payment_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a payment request.  Note: This field is returned when resultCode is PAYMENT_IN_PROCESS.  More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  Note: This field is returned when resultCode is PAYMENT_IN_PROCESS.  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayPayResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_data(self):
        """
        Used by the Antom client SDK to render the checkout page. This parameter is returned if the merchant app has integrated Antom client SDK. After receiving the parameter, you can call the showPaymentSheet API of the Antom client SDK.  More information:  Maximum length: 20000 characters
        """
        return self.__payment_data

    @payment_data.setter
    def payment_data(self, value):
        self.__payment_data = value
    @property
    def actual_payment_amount(self):
        """Gets the actual_payment_amount of this AlipayPayResponse.
        
        """
        return self.__actual_payment_amount

    @actual_payment_amount.setter
    def actual_payment_amount(self, value):
        self.__actual_payment_amount = value
    @property
    def payment_quote(self):
        """Gets the payment_quote of this AlipayPayResponse.
        
        """
        return self.__payment_quote

    @payment_quote.setter
    def payment_quote(self, value):
        self.__payment_quote = value
    @property
    def payment_time(self):
        """Gets the payment_time of this AlipayPayResponse.
        
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def payment_create_time(self):
        """
        The date and time when the payment is created.  Note: This field is returned when resultCode is PAYMENT_IN_PROCESS.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__payment_create_time

    @payment_create_time.setter
    def payment_create_time(self, value):
        self.__payment_create_time = value
    @property
    def auth_expiry_time(self):
        """Gets the auth_expiry_time of this AlipayPayResponse.
        
        """
        return self.__auth_expiry_time

    @auth_expiry_time.setter
    def auth_expiry_time(self, value):
        self.__auth_expiry_time = value
    @property
    def non_guarantee_coupon_value(self):
        """Gets the non_guarantee_coupon_value of this AlipayPayResponse.
        
        """
        return self.__non_guarantee_coupon_value

    @non_guarantee_coupon_value.setter
    def non_guarantee_coupon_value(self, value):
        self.__non_guarantee_coupon_value = value
    @property
    def payment_action_form(self):
        """Gets the payment_action_form of this AlipayPayResponse.
        
        """
        return self.__payment_action_form

    @payment_action_form.setter
    def payment_action_form(self, value):
        self.__payment_action_form = value
    @property
    def psp_customer_info(self):
        """Gets the psp_customer_info of this AlipayPayResponse.
        
        """
        return self.__psp_customer_info

    @psp_customer_info.setter
    def psp_customer_info(self, value):
        self.__psp_customer_info = value
    @property
    def challenge_action_form(self):
        """Gets the challenge_action_form of this AlipayPayResponse.
        
        """
        return self.__challenge_action_form

    @challenge_action_form.setter
    def challenge_action_form(self, value):
        self.__challenge_action_form = value
    @property
    def redirect_action_form(self):
        """Gets the redirect_action_form of this AlipayPayResponse.
        
        """
        return self.__redirect_action_form

    @redirect_action_form.setter
    def redirect_action_form(self, value):
        self.__redirect_action_form = value
    @property
    def order_code_form(self):
        """Gets the order_code_form of this AlipayPayResponse.
        
        """
        return self.__order_code_form

    @order_code_form.setter
    def order_code_form(self, value):
        self.__order_code_form = value
    @property
    def gross_settlement_amount(self):
        """Gets the gross_settlement_amount of this AlipayPayResponse.
        
        """
        return self.__gross_settlement_amount

    @gross_settlement_amount.setter
    def gross_settlement_amount(self, value):
        self.__gross_settlement_amount = value
    @property
    def settlement_quote(self):
        """Gets the settlement_quote of this AlipayPayResponse.
        
        """
        return self.__settlement_quote

    @settlement_quote.setter
    def settlement_quote(self, value):
        self.__settlement_quote = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayPayResponse.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def normal_url(self):
        """
        The URL that redirects users to a WAP or WEB page in the default browser or the embedded WebView.  Note: When the value of resultCode is ​PAYMENT_IN_PROCESS​, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters 
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def scheme_url(self):
        """
        The URL scheme that redirects users to open an app in an Android or iOS system when the target app is installed.  Note: When the value of resultCode is ​PAYMENT_IN_PROCESS​, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters
        """
        return self.__scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self.__scheme_url = value
    @property
    def applink_url(self):
        """
        The URL that redirects users to open an app when the target app is installed, or to open a WAP page when the target app is not installed. For Android, the URL is a Native App Link. For iOS, the URL is a Universal Link.  Note: When the value of resultCode is ​PAYMENT_IN_PROCESS​, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters
        """
        return self.__applink_url

    @applink_url.setter
    def applink_url(self, value):
        self.__applink_url = value
    @property
    def app_identifier(self):
        """
        Android package name, which is used by Android apps to open a cashier page.  Note: This field is returned when resultCode is ​PAYMENT_IN_PROCESS​ and terminalType is APP or WAP.
        """
        return self.__app_identifier

    @app_identifier.setter
    def app_identifier(self, value):
        self.__app_identifier = value
    @property
    def payment_result_info(self):
        """Gets the payment_result_info of this AlipayPayResponse.
        
        """
        return self.__payment_result_info

    @payment_result_info.setter
    def payment_result_info(self, value):
        self.__payment_result_info = value
    @property
    def acquirer_info(self):
        """Gets the acquirer_info of this AlipayPayResponse.
        
        """
        return self.__acquirer_info

    @acquirer_info.setter
    def acquirer_info(self, value):
        self.__acquirer_info = value
    @property
    def promotion_result(self):
        """
        Promotion result.
        """
        return self.__promotion_result

    @promotion_result.setter
    def promotion_result(self, value):
        self.__promotion_result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "processing_amount") and self.processing_amount is not None:
            params['processingAmount'] = self.processing_amount
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_data") and self.payment_data is not None:
            params['paymentData'] = self.payment_data
        if hasattr(self, "actual_payment_amount") and self.actual_payment_amount is not None:
            params['actualPaymentAmount'] = self.actual_payment_amount
        if hasattr(self, "payment_quote") and self.payment_quote is not None:
            params['paymentQuote'] = self.payment_quote
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "payment_create_time") and self.payment_create_time is not None:
            params['paymentCreateTime'] = self.payment_create_time
        if hasattr(self, "auth_expiry_time") and self.auth_expiry_time is not None:
            params['authExpiryTime'] = self.auth_expiry_time
        if hasattr(self, "non_guarantee_coupon_value") and self.non_guarantee_coupon_value is not None:
            params['nonGuaranteeCouponValue'] = self.non_guarantee_coupon_value
        if hasattr(self, "payment_action_form") and self.payment_action_form is not None:
            params['paymentActionForm'] = self.payment_action_form
        if hasattr(self, "psp_customer_info") and self.psp_customer_info is not None:
            params['pspCustomerInfo'] = self.psp_customer_info
        if hasattr(self, "challenge_action_form") and self.challenge_action_form is not None:
            params['challengeActionForm'] = self.challenge_action_form
        if hasattr(self, "redirect_action_form") and self.redirect_action_form is not None:
            params['redirectActionForm'] = self.redirect_action_form
        if hasattr(self, "order_code_form") and self.order_code_form is not None:
            params['orderCodeForm'] = self.order_code_form
        if hasattr(self, "gross_settlement_amount") and self.gross_settlement_amount is not None:
            params['grossSettlementAmount'] = self.gross_settlement_amount
        if hasattr(self, "settlement_quote") and self.settlement_quote is not None:
            params['settlementQuote'] = self.settlement_quote
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "scheme_url") and self.scheme_url is not None:
            params['schemeUrl'] = self.scheme_url
        if hasattr(self, "applink_url") and self.applink_url is not None:
            params['applinkUrl'] = self.applink_url
        if hasattr(self, "app_identifier") and self.app_identifier is not None:
            params['appIdentifier'] = self.app_identifier
        if hasattr(self, "payment_result_info") and self.payment_result_info is not None:
            params['paymentResultInfo'] = self.payment_result_info
        if hasattr(self, "acquirer_info") and self.acquirer_info is not None:
            params['acquirerInfo'] = self.acquirer_info
        if hasattr(self, "promotion_result") and self.promotion_result is not None:
            params['promotionResult'] = self.promotion_result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPayResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'processingAmount' in response_body:
            self.__processing_amount = Amount()
            self.__processing_amount.parse_rsp_body(response_body['processingAmount'])
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentData' in response_body:
            self.__payment_data = response_body['paymentData']
        if 'actualPaymentAmount' in response_body:
            self.__actual_payment_amount = Amount()
            self.__actual_payment_amount.parse_rsp_body(response_body['actualPaymentAmount'])
        if 'paymentQuote' in response_body:
            self.__payment_quote = Quote()
            self.__payment_quote.parse_rsp_body(response_body['paymentQuote'])
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'paymentCreateTime' in response_body:
            self.__payment_create_time = response_body['paymentCreateTime']
        if 'authExpiryTime' in response_body:
            self.__auth_expiry_time = response_body['authExpiryTime']
        if 'nonGuaranteeCouponValue' in response_body:
            self.__non_guarantee_coupon_value = Amount()
            self.__non_guarantee_coupon_value.parse_rsp_body(response_body['nonGuaranteeCouponValue'])
        if 'paymentActionForm' in response_body:
            self.__payment_action_form = response_body['paymentActionForm']
        if 'pspCustomerInfo' in response_body:
            self.__psp_customer_info = PspCustomerInfo()
            self.__psp_customer_info.parse_rsp_body(response_body['pspCustomerInfo'])
        if 'challengeActionForm' in response_body:
            self.__challenge_action_form = ChallengeActionForm()
            self.__challenge_action_form.parse_rsp_body(response_body['challengeActionForm'])
        if 'redirectActionForm' in response_body:
            self.__redirect_action_form = RedirectActionForm()
            self.__redirect_action_form.parse_rsp_body(response_body['redirectActionForm'])
        if 'orderCodeForm' in response_body:
            self.__order_code_form = OrderCodeForm()
            self.__order_code_form.parse_rsp_body(response_body['orderCodeForm'])
        if 'grossSettlementAmount' in response_body:
            self.__gross_settlement_amount = Amount()
            self.__gross_settlement_amount.parse_rsp_body(response_body['grossSettlementAmount'])
        if 'settlementQuote' in response_body:
            self.__settlement_quote = Quote()
            self.__settlement_quote.parse_rsp_body(response_body['settlementQuote'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'schemeUrl' in response_body:
            self.__scheme_url = response_body['schemeUrl']
        if 'applinkUrl' in response_body:
            self.__applink_url = response_body['applinkUrl']
        if 'appIdentifier' in response_body:
            self.__app_identifier = response_body['appIdentifier']
        if 'paymentResultInfo' in response_body:
            self.__payment_result_info = PaymentResultInfo()
            self.__payment_result_info.parse_rsp_body(response_body['paymentResultInfo'])
        if 'acquirerInfo' in response_body:
            self.__acquirer_info = AcquirerInfo()
            self.__acquirer_info.parse_rsp_body(response_body['acquirerInfo'])
        if 'promotionResult' in response_body:
            self.__promotion_result = []
            for item in response_body['promotionResult']:
                obj = PromotionResult()
                obj.parse_rsp_body(item)
                self.__promotion_result.append(obj)
