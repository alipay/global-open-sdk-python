import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_result_info import PaymentResultInfo
from com.alipay.ams.api.model.batch_payment_transaction import BatchPaymentTransaction




class AmsInquiryPaymentResult:
    def __init__(self):
        
        self.__payment_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_status = None  # type: str
        self.__payment_result_code = None  # type: str
        self.__payment_result_message = None  # type: str
        self.__payment_result_info = None  # type: PaymentResultInfo
        self.__transactions = None  # type: [BatchPaymentTransaction]
        

    @property
    def payment_request_id(self):
        """
        Merchant-assigned sub-order payment request ID (maximum 64 characters).
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def payment_id(self):
        """
        Antom-assigned sub-order payment ID (maximum 64 characters).
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AmsInquiryPaymentResult.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_status(self):
        """
        Payment status (maximum 16 characters), returned on successful inquiry. SUCCESS: succeeded; FAIL: failed; PROCESSING: processing; CANCELLED: canceled; PENDING: payment complete, final result pending. SUCCESS, FAIL and CANCELLED are final; PROCESSING and PENDING are intermediate. Every sub-order in a batch shares the same payment status.
        """
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, value):
        self.__payment_status = value
    @property
    def payment_result_code(self):
        """
        Sub-order result code (maximum 64 characters), returned on successful inquiry. Applicable codes: SUCCESS (Payment succeeded); ACCESS_DENIED (Access denied); CURRENCY_NOT_SUPPORT (Currency not supported); FRAUD_REJECT (Risk control prevents further processing); INVALID_API (API invalid or inactive); INVALID_CARD (Invalid card); ORDER_NOT_EXIST (Order does not exist); INVALID_EXPIRY_DATE_FORMAT (Invalid card expiry year or month format); ISSUER_REJECTS_TRANSACTION (Issuer rejected transaction); INVALID_ACCESS_TOKEN (Access token expired, revoked, or absent); INVALID_MERCHANT_STATUS (Restricted merchant status); KEY_NOT_FOUND (Antom or merchant key not found); MERCHANT_KYB_NOT_QUALIFIED (Merchant KYB status disqualifies payment); NO_INTERFACE_DEF (Interface undefined); NO_PAY_OPTIONS (No payment options available); ORDER_IS_CLOSED (Payment request ID matches a closed transaction); PARAM_ILLEGAL (Missing or invalid parameter); PAYMENT_AMOUNT_EXCEED_LIMIT (Amount exceeds contract or payment method limit); PAYMENT_COUNT_EXCEED_LIMIT (Payment count exceeds payment method limit); PAYMENT_NOT_QUALIFIED (Merchant not eligible for payment); PROCESS_FAIL (General business failure); RISK_REJECT (Risk control prevents further processing); SUSPECTED_CARD (Card suspected of fraud); SUSPECTED_RISK (Suspected security risk prevents further processing); SYSTEM_ERROR (System error); USER_AMOUNT_EXCEED_LIMIT (Amount exceeds user payment limit); USER_BALANCE_NOT_ENOUGH (Insufficient user balance); USER_KYC_NOT_QUALIFIED (User KYC status disqualifies payment); USER_PAYMENT_VERIFICATION_FAILED (User restricted from payment at provider); USER_STATUS_ABNORMAL (User status abnormal at provider); PAYMENT_IN_PROCESS (Payment processing); UNKNOWN_EXCEPTION (API call failed for an unknown reason); CARD_NOT_SUPPORTED (Card not supported for transaction); INVALID_EXPIRATION_DATE (Invalid card expiration date); INVALID_CARD_NUMBER (Invalid card number); DO_NOT_HONOR (Issuer declined payment).
        """
        return self.__payment_result_code

    @payment_result_code.setter
    def payment_result_code(self, value):
        self.__payment_result_code = value
    @property
    def payment_result_message(self):
        """
        Message explaining the sub-order result code (maximum 256 characters); returned on successful inquiry.
        """
        return self.__payment_result_message

    @payment_result_message.setter
    def payment_result_message(self, value):
        self.__payment_result_message = value
    @property
    def payment_result_info(self):
        """Gets the payment_result_info of this AmsInquiryPaymentResult.
        
        """
        return self.__payment_result_info

    @payment_result_info.setter
    def payment_result_info(self, value):
        self.__payment_result_info = value
    @property
    def transactions(self):
        """
        Transaction details returned when a refund or capture exists.
        """
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        self.__transactions = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_status") and self.payment_status is not None:
            params['paymentStatus'] = self.payment_status
        if hasattr(self, "payment_result_code") and self.payment_result_code is not None:
            params['paymentResultCode'] = self.payment_result_code
        if hasattr(self, "payment_result_message") and self.payment_result_message is not None:
            params['paymentResultMessage'] = self.payment_result_message
        if hasattr(self, "payment_result_info") and self.payment_result_info is not None:
            params['paymentResultInfo'] = self.payment_result_info
        if hasattr(self, "transactions") and self.transactions is not None:
            params['transactions'] = self.transactions
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentStatus' in response_body:
            self.__payment_status = response_body['paymentStatus']
        if 'paymentResultCode' in response_body:
            self.__payment_result_code = response_body['paymentResultCode']
        if 'paymentResultMessage' in response_body:
            self.__payment_result_message = response_body['paymentResultMessage']
        if 'paymentResultInfo' in response_body:
            self.__payment_result_info = PaymentResultInfo()
            self.__payment_result_info.parse_rsp_body(response_body['paymentResultInfo'])
        if 'transactions' in response_body:
            self.__transactions = []
            for item in response_body['transactions']:
                obj = BatchPaymentTransaction()
                obj.parse_rsp_body(item)
                self.__transactions.append(obj)
