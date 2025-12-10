import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.customized_info import CustomizedInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.model.card_info import CardInfo
from com.alipay.ams.api.model.transaction import Transaction
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.payment_result_info import PaymentResultInfo
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo
from com.alipay.ams.api.model.promotion_result import PromotionResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPayQueryResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__metadata = None  # type: str
        self.__result = None  # type: Result
        self.__customized_info = None  # type: CustomizedInfo
        self.__processing_amount = None  # type: Amount
        self.__payment_status = None  # type: TransactionStatusType
        self.__payment_result_code = None  # type: str
        self.__payment_result_message = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__auth_payment_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__actual_payment_amount = None  # type: Amount
        self.__payment_quote = None  # type: Quote
        self.__auth_expiry_time = None  # type: str
        self.__payment_create_time = None  # type: str
        self.__payment_time = None  # type: str
        self.__non_guarantee_coupon_amount = None  # type: Amount
        self.__psp_customer_info = None  # type: PspCustomerInfo
        self.__redirect_action_form = None  # type: RedirectActionForm
        self.__card_info = None  # type: CardInfo
        self.__acquirer_reference_no = None  # type: str
        self.__extend_info = None  # type: str
        self.__transactions = None  # type: [Transaction]
        self.__customs_declaration_amount = None  # type: Amount
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__payment_result_info = None  # type: PaymentResultInfo
        self.__acquirer_info = None  # type: AcquirerInfo
        self.__merchant_account_id = None  # type: str
        self.__promotion_results = None  # type: [PromotionResult]
        self.__earliest_settlement_time = None  # type: str
        self.__payment_method_type = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def metadata(self):
        """
        Additional metadata about the payment
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def result(self):
        """Gets the result of this AlipayPayQueryResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def customized_info(self):
        """Gets the customized_info of this AlipayPayQueryResponse.
        
        """
        return self.__customized_info

    @customized_info.setter
    def customized_info(self, value):
        self.__customized_info = value
    @property
    def processing_amount(self):
        """Gets the processing_amount of this AlipayPayQueryResponse.
        
        """
        return self.__processing_amount

    @processing_amount.setter
    def processing_amount(self, value):
        self.__processing_amount = value
    @property
    def payment_status(self):
        """Gets the payment_status of this AlipayPayQueryResponse.
        
        """
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, value):
        self.__payment_status = value
    @property
    def payment_result_code(self):
        """
        The result code for different payment statuses. Possible payment result codes are listed in the Payment result codes table on this page.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters 
        """
        return self.__payment_result_code

    @payment_result_code.setter
    def payment_result_code(self, value):
        self.__payment_result_code = value
    @property
    def payment_result_message(self):
        """
        The result message that explains the payment result code.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 256 characters 
        """
        return self.__payment_result_message

    @payment_result_message.setter
    def payment_result_message(self, value):
        self.__payment_result_message = value
    @property
    def payment_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a payment request.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def auth_payment_id(self):
        """Gets the auth_payment_id of this AlipayPayQueryResponse.
        
        """
        return self.__auth_payment_id

    @auth_payment_id.setter
    def auth_payment_id(self, value):
        self.__auth_payment_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayPayQueryResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def actual_payment_amount(self):
        """Gets the actual_payment_amount of this AlipayPayQueryResponse.
        
        """
        return self.__actual_payment_amount

    @actual_payment_amount.setter
    def actual_payment_amount(self, value):
        self.__actual_payment_amount = value
    @property
    def payment_quote(self):
        """Gets the payment_quote of this AlipayPayQueryResponse.
        
        """
        return self.__payment_quote

    @payment_quote.setter
    def payment_quote(self, value):
        self.__payment_quote = value
    @property
    def auth_expiry_time(self):
        """
        The expiration date and time of the authorization payment. You cannot capture the payment after this time.  This parameter is returned when the value of paymentMethodType in the pay (Checkout Payment) API is CARD.  More information about this field:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__auth_expiry_time

    @auth_expiry_time.setter
    def auth_expiry_time(self, value):
        self.__auth_expiry_time = value
    @property
    def payment_create_time(self):
        """
        The date and time when the payment is created.   Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__payment_create_time

    @payment_create_time.setter
    def payment_create_time(self, value):
        self.__payment_create_time = value
    @property
    def payment_time(self):
        """
        The date and time when the payment reaches a final state of success.  Note: This field is returned only when the payment reaches a final state of success (the value of paymentStatus is SUCCESS).   More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def non_guarantee_coupon_amount(self):
        """Gets the non_guarantee_coupon_amount of this AlipayPayQueryResponse.
        
        """
        return self.__non_guarantee_coupon_amount

    @non_guarantee_coupon_amount.setter
    def non_guarantee_coupon_amount(self, value):
        self.__non_guarantee_coupon_amount = value
    @property
    def psp_customer_info(self):
        """Gets the psp_customer_info of this AlipayPayQueryResponse.
        
        """
        return self.__psp_customer_info

    @psp_customer_info.setter
    def psp_customer_info(self, value):
        self.__psp_customer_info = value
    @property
    def redirect_action_form(self):
        """Gets the redirect_action_form of this AlipayPayQueryResponse.
        
        """
        return self.__redirect_action_form

    @redirect_action_form.setter
    def redirect_action_form(self, value):
        self.__redirect_action_form = value
    @property
    def card_info(self):
        """Gets the card_info of this AlipayPayQueryResponse.
        
        """
        return self.__card_info

    @card_info.setter
    def card_info(self, value):
        self.__card_info = value
    @property
    def acquirer_reference_no(self):
        """
        The unique ID assigned by the non-Antom acquirer for the transaction.    More information:  Maximum length: 64 characters 
        """
        return self.__acquirer_reference_no

    @acquirer_reference_no.setter
    def acquirer_reference_no(self, value):
        self.__acquirer_reference_no = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayPayQueryResponse.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def transactions(self):
        """
        Information about the subsequent action against a transaction.  Note: This parameter is returned when a refund or a capture against the transaction exists.
        """
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        self.__transactions = value
    @property
    def customs_declaration_amount(self):
        """Gets the customs_declaration_amount of this AlipayPayQueryResponse.
        
        """
        return self.__customs_declaration_amount

    @customs_declaration_amount.setter
    def customs_declaration_amount(self, value):
        self.__customs_declaration_amount = value
    @property
    def gross_settlement_amount(self):
        """Gets the gross_settlement_amount of this AlipayPayQueryResponse.
        
        """
        return self.__gross_settlement_amount

    @gross_settlement_amount.setter
    def gross_settlement_amount(self, value):
        self.__gross_settlement_amount = value
    @property
    def settlement_quote(self):
        """Gets the settlement_quote of this AlipayPayQueryResponse.
        
        """
        return self.__settlement_quote

    @settlement_quote.setter
    def settlement_quote(self, value):
        self.__settlement_quote = value
    @property
    def payment_result_info(self):
        """Gets the payment_result_info of this AlipayPayQueryResponse.
        
        """
        return self.__payment_result_info

    @payment_result_info.setter
    def payment_result_info(self, value):
        self.__payment_result_info = value
    @property
    def acquirer_info(self):
        """Gets the acquirer_info of this AlipayPayQueryResponse.
        
        """
        return self.__acquirer_info

    @acquirer_info.setter
    def acquirer_info(self, value):
        self.__acquirer_info = value
    @property
    def merchant_account_id(self):
        """Gets the merchant_account_id of this AlipayPayQueryResponse.
        
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def promotion_results(self):
        """
        Promotion result.  Note: This parameter is returned when the buyer applied a promotion while placing an order.
        """
        return self.__promotion_results

    @promotion_results.setter
    def promotion_results(self, value):
        self.__promotion_results = value
    @property
    def earliest_settlement_time(self):
        """Gets the earliest_settlement_time of this AlipayPayQueryResponse.
        
        """
        return self.__earliest_settlement_time

    @earliest_settlement_time.setter
    def earliest_settlement_time(self, value):
        self.__earliest_settlement_time = value
    @property
    def payment_method_type(self):
        """
        The payment method type that is included in payment method options. See Payment methods to check the valid values.   Note: This field will be returned when selecting the Antom Chechkout Page integration.  More information:  Maximum length: 64 characters
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "customized_info") and self.customized_info is not None:
            params['customizedInfo'] = self.customized_info
        if hasattr(self, "processing_amount") and self.processing_amount is not None:
            params['processingAmount'] = self.processing_amount
        if hasattr(self, "payment_status") and self.payment_status is not None:
            params['paymentStatus'] = self.payment_status
        if hasattr(self, "payment_result_code") and self.payment_result_code is not None:
            params['paymentResultCode'] = self.payment_result_code
        if hasattr(self, "payment_result_message") and self.payment_result_message is not None:
            params['paymentResultMessage'] = self.payment_result_message
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "auth_payment_id") and self.auth_payment_id is not None:
            params['authPaymentId'] = self.auth_payment_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "actual_payment_amount") and self.actual_payment_amount is not None:
            params['actualPaymentAmount'] = self.actual_payment_amount
        if hasattr(self, "payment_quote") and self.payment_quote is not None:
            params['paymentQuote'] = self.payment_quote
        if hasattr(self, "auth_expiry_time") and self.auth_expiry_time is not None:
            params['authExpiryTime'] = self.auth_expiry_time
        if hasattr(self, "payment_create_time") and self.payment_create_time is not None:
            params['paymentCreateTime'] = self.payment_create_time
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "non_guarantee_coupon_amount") and self.non_guarantee_coupon_amount is not None:
            params['nonGuaranteeCouponAmount'] = self.non_guarantee_coupon_amount
        if hasattr(self, "psp_customer_info") and self.psp_customer_info is not None:
            params['pspCustomerInfo'] = self.psp_customer_info
        if hasattr(self, "redirect_action_form") and self.redirect_action_form is not None:
            params['redirectActionForm'] = self.redirect_action_form
        if hasattr(self, "card_info") and self.card_info is not None:
            params['cardInfo'] = self.card_info
        if hasattr(self, "acquirer_reference_no") and self.acquirer_reference_no is not None:
            params['acquirerReferenceNo'] = self.acquirer_reference_no
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "transactions") and self.transactions is not None:
            params['transactions'] = self.transactions
        if hasattr(self, "customs_declaration_amount") and self.customs_declaration_amount is not None:
            params['customsDeclarationAmount'] = self.customs_declaration_amount
        if hasattr(self, "gross_settlement_amount") and self.gross_settlement_amount is not None:
            params['grossSettlementAmount'] = self.gross_settlement_amount
        if hasattr(self, "settlement_quote") and self.settlement_quote is not None:
            params['settlementQuote'] = self.settlement_quote
        if hasattr(self, "payment_result_info") and self.payment_result_info is not None:
            params['paymentResultInfo'] = self.payment_result_info
        if hasattr(self, "acquirer_info") and self.acquirer_info is not None:
            params['acquirerInfo'] = self.acquirer_info
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "promotion_results") and self.promotion_results is not None:
            params['promotionResults'] = self.promotion_results
        if hasattr(self, "earliest_settlement_time") and self.earliest_settlement_time is not None:
            params['earliestSettlementTime'] = self.earliest_settlement_time
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPayQueryResponse, self).parse_rsp_body(response_body)
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'customizedInfo' in response_body:
            self.__customized_info = CustomizedInfo()
            self.__customized_info.parse_rsp_body(response_body['customizedInfo'])
        if 'processingAmount' in response_body:
            self.__processing_amount = Amount()
            self.__processing_amount.parse_rsp_body(response_body['processingAmount'])
        if 'paymentStatus' in response_body:
            payment_status_temp = TransactionStatusType.value_of(response_body['paymentStatus'])
            self.__payment_status = payment_status_temp
        if 'paymentResultCode' in response_body:
            self.__payment_result_code = response_body['paymentResultCode']
        if 'paymentResultMessage' in response_body:
            self.__payment_result_message = response_body['paymentResultMessage']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'authPaymentId' in response_body:
            self.__auth_payment_id = response_body['authPaymentId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'actualPaymentAmount' in response_body:
            self.__actual_payment_amount = Amount()
            self.__actual_payment_amount.parse_rsp_body(response_body['actualPaymentAmount'])
        if 'paymentQuote' in response_body:
            self.__payment_quote = Quote()
            self.__payment_quote.parse_rsp_body(response_body['paymentQuote'])
        if 'authExpiryTime' in response_body:
            self.__auth_expiry_time = response_body['authExpiryTime']
        if 'paymentCreateTime' in response_body:
            self.__payment_create_time = response_body['paymentCreateTime']
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'nonGuaranteeCouponAmount' in response_body:
            self.__non_guarantee_coupon_amount = Amount()
            self.__non_guarantee_coupon_amount.parse_rsp_body(response_body['nonGuaranteeCouponAmount'])
        if 'pspCustomerInfo' in response_body:
            self.__psp_customer_info = PspCustomerInfo()
            self.__psp_customer_info.parse_rsp_body(response_body['pspCustomerInfo'])
        if 'redirectActionForm' in response_body:
            self.__redirect_action_form = RedirectActionForm()
            self.__redirect_action_form.parse_rsp_body(response_body['redirectActionForm'])
        if 'cardInfo' in response_body:
            self.__card_info = CardInfo()
            self.__card_info.parse_rsp_body(response_body['cardInfo'])
        if 'acquirerReferenceNo' in response_body:
            self.__acquirer_reference_no = response_body['acquirerReferenceNo']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'transactions' in response_body:
            self.__transactions = []
            for item in response_body['transactions']:
                obj = Transaction()
                obj.parse_rsp_body(item)
                self.__transactions.append(obj)
        if 'customsDeclarationAmount' in response_body:
            self.__customs_declaration_amount = Amount()
            self.__customs_declaration_amount.parse_rsp_body(response_body['customsDeclarationAmount'])
        if 'grossSettlementAmount' in response_body:
            self.__gross_settlement_amount = Amount()
            self.__gross_settlement_amount.parse_rsp_body(response_body['grossSettlementAmount'])
        if 'settlementQuote' in response_body:
            self.__settlement_quote = Quote()
            self.__settlement_quote.parse_rsp_body(response_body['settlementQuote'])
        if 'paymentResultInfo' in response_body:
            self.__payment_result_info = PaymentResultInfo()
            self.__payment_result_info.parse_rsp_body(response_body['paymentResultInfo'])
        if 'acquirerInfo' in response_body:
            self.__acquirer_info = AcquirerInfo()
            self.__acquirer_info.parse_rsp_body(response_body['acquirerInfo'])
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'promotionResults' in response_body:
            self.__promotion_results = []
            for item in response_body['promotionResults']:
                obj = PromotionResult()
                obj.parse_rsp_body(item)
                self.__promotion_results.append(obj)
        if 'earliestSettlementTime' in response_body:
            self.__earliest_settlement_time = response_body['earliestSettlementTime']
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
