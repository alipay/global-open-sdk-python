import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AmsApiV1PaymentsInquiryRefundPost200Response(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__refund_id = None  # type: str
        self.__refund_request_id = None  # type: str
        self.__refund_amount = None  # type: Amount
        self.__refund_status = None  # type: TransactionStatusType
        self.__refund_time = None  # type: str
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__acquirer_info = None  # type: AcquirerInfo
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def refund_id(self):
        """
        The unique ID assigned by Antom to identify a refund. A one-to-one correspondence between refundId and refundRequestId exists.  Note: This field is null when the refund record cannot be found, or result.resultStatus is F or U. 
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def refund_request_id(self):
        """
        The unique ID assigned by the merchant to identify a refund request.  Note: This field is null when the refund record cannot be found, or result.resultStatus is F or U.   More information:  Maximum length: 64 characters
        """
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
    @property
    def refund_status(self):
        """Gets the refund_status of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__refund_status

    @refund_status.setter
    def refund_status(self, value):
        self.__refund_status = value
    @property
    def refund_time(self):
        """
        The date and time when the refund reaches a final state of success on the Antom side, not the Alipay+ Mobile Payment Provider (Alipay+ payment methods) side.   Note: This field is returned when the value of refundStatus is SUCCESS.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__refund_time

    @refund_time.setter
    def refund_time(self, value):
        self.__refund_time = value
    @property
    def gross_settlement_amount(self):
        """Gets the gross_settlement_amount of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__gross_settlement_amount

    @gross_settlement_amount.setter
    def gross_settlement_amount(self, value):
        self.__gross_settlement_amount = value
    @property
    def settlement_quote(self):
        """Gets the settlement_quote of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__settlement_quote

    @settlement_quote.setter
    def settlement_quote(self, value):
        self.__settlement_quote = value
    @property
    def acquirer_info(self):
        """Gets the acquirer_info of this AmsApiV1PaymentsInquiryRefundPost200Response.
        
        """
        return self.__acquirer_info

    @acquirer_info.setter
    def acquirer_info(self, value):
        self.__acquirer_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "refund_request_id") and self.refund_request_id is not None:
            params['refundRequestId'] = self.refund_request_id
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refund_status") and self.refund_status is not None:
            params['refundStatus'] = self.refund_status
        if hasattr(self, "refund_time") and self.refund_time is not None:
            params['refundTime'] = self.refund_time
        if hasattr(self, "gross_settlement_amount") and self.gross_settlement_amount is not None:
            params['grossSettlementAmount'] = self.gross_settlement_amount
        if hasattr(self, "settlement_quote") and self.settlement_quote is not None:
            params['settlementQuote'] = self.settlement_quote
        if hasattr(self, "acquirer_info") and self.acquirer_info is not None:
            params['acquirerInfo'] = self.acquirer_info
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AmsApiV1PaymentsInquiryRefundPost200Response, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'refundRequestId' in response_body:
            self.__refund_request_id = response_body['refundRequestId']
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundStatus' in response_body:
            refund_status_temp = TransactionStatusType.value_of(response_body['refundStatus'])
            self.__refund_status = refund_status_temp
        if 'refundTime' in response_body:
            self.__refund_time = response_body['refundTime']
        if 'grossSettlementAmount' in response_body:
            self.__gross_settlement_amount = Amount()
            self.__gross_settlement_amount.parse_rsp_body(response_body['grossSettlementAmount'])
        if 'settlementQuote' in response_body:
            self.__settlement_quote = Quote()
            self.__settlement_quote.parse_rsp_body(response_body['settlementQuote'])
        if 'acquirerInfo' in response_body:
            self.__acquirer_info = AcquirerInfo()
            self.__acquirer_info.parse_rsp_body(response_body['acquirerInfo'])
