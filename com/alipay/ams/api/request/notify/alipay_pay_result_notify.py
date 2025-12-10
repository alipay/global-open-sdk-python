from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayPayResultNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayPayResultNotify, self).__init__()
        self.__payment_request_id = None
        self.__payment_id = None
        self.__payment_amount = None
        self.__payment_create_time = None
        self.__payment_time = None
        self.__customs_declaration_amount = None
        self.__gross_settlement_amount = None
        self.__settlement_quote = None
        self.__psp_customer_info = None
        self.__acquirer_reference_no = None
        self.__payment_result_info = None
        self.__acquirer_info = None
        self.__promotion_result = None
        self.__payment_method_type = None
        self.__metadata = None  # type: str
        self.__parse_notify_body(notify_body)

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def payment_amount(self):
        return self.__payment_amount

    @property
    def payment_create_time(self):
        return self.__payment_create_time

    @property
    def payment_time(self):
        return self.__payment_time

    @property
    def customs_declaration_amount(self):
        return self.__customs_declaration_amount

    @property
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    @property
    def psp_customer_info(self):
        return self.__psp_customer_info

    @property
    def acquirer_reference_no(self):
        return self.__acquirer_reference_no

    @property
    def payment_result_info(self):
        return self.__payment_result_info

    @property
    def acquirer_info(self):
        return self.__acquirer_info

    @property
    def promotion_result(self):
        return self.__promotion_result

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @property
    def metadata(self):
        return self.__metadata

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayPayResultNotify, self).parse_notify_body(notify_body)
        if "paymentRequestId" in notify:
            self.__payment_request_id = notify["paymentRequestId"]
        if "paymentId" in notify:
            self.__payment_id = notify["paymentId"]
        if "paymentAmount" in notify:
            self.__payment_amount = notify["paymentAmount"]
        if "paymentCreateTime" in notify:
            self.__payment_create_time = notify["paymentCreateTime"]
        if "paymentTime" in notify:
            self.__payment_time = notify["paymentTime"]
        if "customsDeclarationAmount" in notify:
            self.__customs_declaration_amount = notify["customsDeclarationAmount"]
        if "grossSettlementAmount" in notify:
            self.__gross_settlement_amount = notify["grossSettlementAmount"]
        if "settlementQuote" in notify:
            self.__settlement_quote = notify["settlementQuote"]
        if "pspCustomerInfo" in notify:
            self.__psp_customer_info = notify["pspCustomerInfo"]
        if "acquirerReferenceNo" in notify:
            self.__acquirer_reference_no = notify["acquirerReferenceNo"]
        if "paymentResultInfo" in notify:
            self.__payment_result_info = notify["paymentResultInfo"]
        if "acquirerInfo" in notify:
            self.__acquirer_info = notify["acquirerInfo"]
        if "promotionResult" in notify:
            self.__promotion_result = notify["promotionResult"]

        if "paymentMethodType" in notify:
            self.__payment_method_type = notify["paymentMethodType"]
        if "metadata" in notify:
            self.__metadata = notify["metadata"]