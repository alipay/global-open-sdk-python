import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.receipt_item import ReceiptItem
from com.alipay.ams.api.model.invoice_payment import InvoicePayment



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayReceiptInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__receipt_id = None  # type: str
        self.__original_receipt_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__refund_id = None  # type: str
        self.__receipt_type = None  # type: str
        self.__status = None  # type: str
        self.__reason = None  # type: str
        self.__customer_first_name = None  # type: str
        self.__customer_last_name = None  # type: str
        self.__customer_email = None  # type: str
        self.__collection_method = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__subtotal = None  # type: Amount
        self.__paid_amount = None  # type: Amount
        self.__discount_amount = None  # type: Amount
        self.__tax_amount = None  # type: Amount
        self.__shipping_fee_amount = None  # type: Amount
        self.__payment_deducted_amount = None  # type: Amount
        self.__refund_amount = None  # type: Amount
        self.__refunded_amount = None  # type: Amount
        self.__remaining_amount = None  # type: Amount
        self.__settlement_amount = None  # type: Amount
        self.__fx_rate = None  # type: str
        self.__fx_rate_id = None  # type: str
        self.__payment_method = None  # type: str
        self.__period_start = None  # type: str
        self.__period_end = None  # type: str
        self.__paid_time = None  # type: str
        self.__due_date = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__pay_to_request_id = None  # type: str
        self.__pay_to_id = None  # type: str
        self.__description = None  # type: str
        self.__file_url = None  # type: str
        self.__items = None  # type: [ReceiptItem]
        self.__payments = None  # type: [InvoicePayment]
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        self.__payment_method_type = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def receipt_id(self):
        """
        Receipt ID. Unique identifier for the receipt. Returned only when result.resultCode is SUCCESS.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def original_receipt_id(self):
        """
        Original receipt ID for refund receipts (FK -&gt; ibilling_receipt.receipt_id). Only set when receiptType&#x3D;REFUND. Null for PAYMENT receipts. Returned only when result.resultCode is SUCCESS.
        """
        return self.__original_receipt_id

    @original_receipt_id.setter
    def original_receipt_id(self, value):
        self.__original_receipt_id = value
    @property
    def invoice_id(self):
        """
        Associated Invoice ID. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def subscription_id(self):
        """
        Associated Subscription ID. Null for standalone receipts not tied to a subscription. Returned only when result.resultCode is SUCCESS.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def customer_id(self):
        """
        Customer ID. Returned only when result.resultCode is SUCCESS.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def payment_id(self):
        """
        Associated Payment transaction ID. Null for refund receipts. Returned only when result.resultCode is SUCCESS.
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def refund_id(self):
        """
        Associated Refund transaction ID. Null for payment receipts. Returned only when result.resultCode is SUCCESS.
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def receipt_type(self):
        """
        Receipt type. Allowed values: &#x60;PAYMENT&#x60; - receipt for a payment transaction; &#x60;REFUND&#x60; - receipt for a refund transaction. Merchants should handle unknown enum values gracefully. Returned only when result.resultCode is SUCCESS.
        """
        return self.__receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self.__receipt_type = value
    @property
    def status(self):
        """
        Receipt lifecycle status. Allowed values: &#x60;ACTIVE&#x60; - payment receipt with no refunds applied, receipt is final; &#x60;PARTIALLY_REFUNDED&#x60; - some amount has been refunded, receipt reflects partial refund; &#x60;REFUNDED&#x60; - fully refunded, no remaining balance. Merchants should handle unknown enum values gracefully. Returned only when result.resultCode is SUCCESS.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def reason(self):
        """
        Reason for receipt creation. Allowed values: &#x60;SUBSCRIPTION_CREATION&#x60; - receipt generated when a new subscription is first charged; &#x60;RECURRENCE&#x60; - receipt generated for a recurring billing cycle; &#x60;UPDATE&#x60; - receipt generated when a subscription change (upgrade, downgrade, or quantity change) triggers a proration charge or credit; &#x60;TRIAL_END&#x60; - receipt generated when a free trial ends and the first paid charge occurs; &#x60;REFUND&#x60; - receipt generated for a refund transaction. Merchants should handle unknown enum values gracefully. Returned only when result.resultCode is SUCCESS.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def customer_first_name(self):
        """
        Customer&#39;s first name. Populated from the customer record at receipt creation time. Null if the customer record had no &#x60;firstName&#x60; at receipt creation time. Returned only when result.resultCode is SUCCESS.
        """
        return self.__customer_first_name

    @customer_first_name.setter
    def customer_first_name(self, value):
        self.__customer_first_name = value
    @property
    def customer_last_name(self):
        """
        Customer&#39;s last name. Populated from the customer record at receipt creation time. Null if the customer record had no &#x60;lastName&#x60; at receipt creation time. Returned only when result.resultCode is SUCCESS.
        """
        return self.__customer_last_name

    @customer_last_name.setter
    def customer_last_name(self, value):
        self.__customer_last_name = value
    @property
    def customer_email(self):
        """
        Customer&#39;s email address. Populated from the customer record at receipt creation time. Null if the customer record had no email at receipt creation time. Returned only when result.resultCode is SUCCESS.
        """
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, value):
        self.__customer_email = value
    @property
    def collection_method(self):
        """
        Payment collection method. Allowed values: &#x60;CHARGE_AUTOMATICALLY&#x60; - payment is collected automatically at billing cycle; &#x60;SEND_INVOICE&#x60; - payment is collected via a sent invoice. Null when not applicable (e.g., manual payment confirmation). Returned only when result.resultCode is SUCCESS.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def total_amount(self):
        """Gets the total_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def subtotal(self):
        """Gets the subtotal of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
    @property
    def paid_amount(self):
        """Gets the paid_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self.__paid_amount = value
    @property
    def discount_amount(self):
        """Gets the discount_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value
    @property
    def tax_amount(self):
        """Gets the tax_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def shipping_fee_amount(self):
        """Gets the shipping_fee_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__shipping_fee_amount

    @shipping_fee_amount.setter
    def shipping_fee_amount(self, value):
        self.__shipping_fee_amount = value
    @property
    def payment_deducted_amount(self):
        """Gets the payment_deducted_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__payment_deducted_amount

    @payment_deducted_amount.setter
    def payment_deducted_amount(self, value):
        self.__payment_deducted_amount = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, value):
        self.__refunded_amount = value
    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, value):
        self.__remaining_amount = value
    @property
    def settlement_amount(self):
        """Gets the settlement_amount of this AlipayReceiptInquireDetailsResponse.
        
        """
        return self.__settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self.__settlement_amount = value
    @property
    def fx_rate(self):
        """
        Foreign exchange rate applied when payment currency differs from settlement currency (e.g., &#x60;1.0600&#x60;). Null for same-currency transactions. Returned only when result.resultCode is SUCCESS.
        """
        return self.__fx_rate

    @fx_rate.setter
    def fx_rate(self, value):
        self.__fx_rate = value
    @property
    def fx_rate_id(self):
        """
        FX rate reference ID for audit and reconciliation. Null when no FX rate was applied. Returned only when result.resultCode is SUCCESS.
        """
        return self.__fx_rate_id

    @fx_rate_id.setter
    def fx_rate_id(self, value):
        self.__fx_rate_id = value
    @property
    def payment_method(self):
        """
        Payment method used. Allowed values: &#x60;CARD&#x60;, &#x60;BANK_TRANSFER&#x60;, &#x60;WALLET&#x60;, &#x60;OFFLINE&#x60;. Null for offline payment or when payment method is not available. Returned only when result.resultCode is SUCCESS.
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def period_start(self):
        """
        ISO 8601 timestamp of billing period start. Null if not subscription-based. Returned only when result.resultCode is SUCCESS.
        """
        return self.__period_start

    @period_start.setter
    def period_start(self, value):
        self.__period_start = value
    @property
    def period_end(self):
        """
        ISO 8601 timestamp of billing period end. Null if not subscription-based. Returned only when result.resultCode is SUCCESS.
        """
        return self.__period_end

    @period_end.setter
    def period_end(self, value):
        self.__period_end = value
    @property
    def paid_time(self):
        """
        ISO 8601 timestamp of when payment was completed. Null for REFUND-type receipts or unpaid receipts. Returned only when result.resultCode is SUCCESS.
        """
        return self.__paid_time

    @paid_time.setter
    def paid_time(self, value):
        self.__paid_time = value
    @property
    def due_date(self):
        """
        ISO 8601 timestamp of payment due date. Null for receipts without a due date (e.g., auto-charged subscriptions). Returned only when result.resultCode is SUCCESS.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def payment_request_id(self):
        """
        Outbound payment request ID used as idempotency key for the payment call. Null for offline confirmations or when no payment was initiated. Returned only when result.resultCode is SUCCESS.
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def pay_to_request_id(self):
        """
        Payment order request ID. Null if not applicable. Returned only when result.resultCode is SUCCESS.
        """
        return self.__pay_to_request_id

    @pay_to_request_id.setter
    def pay_to_request_id(self, value):
        self.__pay_to_request_id = value
    @property
    def pay_to_id(self):
        """
        Payment order ID. Null if not applicable. Returned only when result.resultCode is SUCCESS.
        """
        return self.__pay_to_id

    @pay_to_id.setter
    def pay_to_id(self, value):
        self.__pay_to_id = value
    @property
    def description(self):
        """
        Receipt description or narrative set by the merchant. Null if no description was provided. Returned only when result.resultCode is SUCCESS.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def file_url(self):
        """
        URL to the hosted receipt page or downloadable receipt PDF. Null if receipt file has not been generated. Returned only when result.resultCode is SUCCESS.
        """
        return self.__file_url

    @file_url.setter
    def file_url(self, value):
        self.__file_url = value
    @property
    def items(self):
        """
        Line items from the associated invoice. Sorted by &#x60;periodStart&#x60; desc, then &#x60;itemId&#x60; desc. Invoices rarely exceed 100 line items; if truncated, use the Invoice Detail API for the full list. See LineItem Object below. Note: When the associated invoice has more than 100 items, only the 100 most recent items are returned. Check the Invoice Detail API for the complete list. Returned only when result.resultCode is SUCCESS.
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def payments(self):
        """
        Payment attempt history for the associated invoice. Sorted by &#x60;attemptNo&#x60; asc (chronological). Invoices rarely exceed 50 payment attempts; if truncated, contact Antom support. See PaymentInfo Object below. Null if no payment attempts exist. Note: When there are more than 50 payment attempts, only the first 50 are returned. Contact Antom support for the complete list. Returned only when result.resultCode is SUCCESS.
        """
        return self.__payments

    @payments.setter
    def payments(self, value):
        self.__payments = value
    @property
    def gmt_create(self):
        """
        ISO 8601 timestamp of receipt creation. Maximum length: 29 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        ISO 8601 timestamp of last receipt update. Maximum length: 29 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value
    @property
    def payment_method_type(self):
        """
        Payment method type (e.g., &#x60;CARD&#x60;, &#x60;WALLET&#x60;). Null if not set. Returned only when result.resultCode is SUCCESS.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "original_receipt_id") and self.original_receipt_id is not None:
            params['originalReceiptId'] = self.original_receipt_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "receipt_type") and self.receipt_type is not None:
            params['receiptType'] = self.receipt_type
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "customer_first_name") and self.customer_first_name is not None:
            params['customerFirstName'] = self.customer_first_name
        if hasattr(self, "customer_last_name") and self.customer_last_name is not None:
            params['customerLastName'] = self.customer_last_name
        if hasattr(self, "customer_email") and self.customer_email is not None:
            params['customerEmail'] = self.customer_email
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "subtotal") and self.subtotal is not None:
            params['subtotal'] = self.subtotal
        if hasattr(self, "paid_amount") and self.paid_amount is not None:
            params['paidAmount'] = self.paid_amount
        if hasattr(self, "discount_amount") and self.discount_amount is not None:
            params['discountAmount'] = self.discount_amount
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "shipping_fee_amount") and self.shipping_fee_amount is not None:
            params['shippingFeeAmount'] = self.shipping_fee_amount
        if hasattr(self, "payment_deducted_amount") and self.payment_deducted_amount is not None:
            params['paymentDeductedAmount'] = self.payment_deducted_amount
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refunded_amount") and self.refunded_amount is not None:
            params['refundedAmount'] = self.refunded_amount
        if hasattr(self, "remaining_amount") and self.remaining_amount is not None:
            params['remainingAmount'] = self.remaining_amount
        if hasattr(self, "settlement_amount") and self.settlement_amount is not None:
            params['settlementAmount'] = self.settlement_amount
        if hasattr(self, "fx_rate") and self.fx_rate is not None:
            params['fxRate'] = self.fx_rate
        if hasattr(self, "fx_rate_id") and self.fx_rate_id is not None:
            params['fxRateId'] = self.fx_rate_id
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "period_start") and self.period_start is not None:
            params['periodStart'] = self.period_start
        if hasattr(self, "period_end") and self.period_end is not None:
            params['periodEnd'] = self.period_end
        if hasattr(self, "paid_time") and self.paid_time is not None:
            params['paidTime'] = self.paid_time
        if hasattr(self, "due_date") and self.due_date is not None:
            params['dueDate'] = self.due_date
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "pay_to_request_id") and self.pay_to_request_id is not None:
            params['payToRequestId'] = self.pay_to_request_id
        if hasattr(self, "pay_to_id") and self.pay_to_id is not None:
            params['payToId'] = self.pay_to_id
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "file_url") and self.file_url is not None:
            params['fileUrl'] = self.file_url
        if hasattr(self, "items") and self.items is not None:
            params['items'] = self.items
        if hasattr(self, "payments") and self.payments is not None:
            params['payments'] = self.payments
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayReceiptInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'originalReceiptId' in response_body:
            self.__original_receipt_id = response_body['originalReceiptId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'receiptType' in response_body:
            self.__receipt_type = response_body['receiptType']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'customerFirstName' in response_body:
            self.__customer_first_name = response_body['customerFirstName']
        if 'customerLastName' in response_body:
            self.__customer_last_name = response_body['customerLastName']
        if 'customerEmail' in response_body:
            self.__customer_email = response_body['customerEmail']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'subtotal' in response_body:
            self.__subtotal = Amount()
            self.__subtotal.parse_rsp_body(response_body['subtotal'])
        if 'paidAmount' in response_body:
            self.__paid_amount = Amount()
            self.__paid_amount.parse_rsp_body(response_body['paidAmount'])
        if 'discountAmount' in response_body:
            self.__discount_amount = Amount()
            self.__discount_amount.parse_rsp_body(response_body['discountAmount'])
        if 'taxAmount' in response_body:
            self.__tax_amount = Amount()
            self.__tax_amount.parse_rsp_body(response_body['taxAmount'])
        if 'shippingFeeAmount' in response_body:
            self.__shipping_fee_amount = Amount()
            self.__shipping_fee_amount.parse_rsp_body(response_body['shippingFeeAmount'])
        if 'paymentDeductedAmount' in response_body:
            self.__payment_deducted_amount = Amount()
            self.__payment_deducted_amount.parse_rsp_body(response_body['paymentDeductedAmount'])
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundedAmount' in response_body:
            self.__refunded_amount = Amount()
            self.__refunded_amount.parse_rsp_body(response_body['refundedAmount'])
        if 'remainingAmount' in response_body:
            self.__remaining_amount = Amount()
            self.__remaining_amount.parse_rsp_body(response_body['remainingAmount'])
        if 'settlementAmount' in response_body:
            self.__settlement_amount = Amount()
            self.__settlement_amount.parse_rsp_body(response_body['settlementAmount'])
        if 'fxRate' in response_body:
            self.__fx_rate = response_body['fxRate']
        if 'fxRateId' in response_body:
            self.__fx_rate_id = response_body['fxRateId']
        if 'paymentMethod' in response_body:
            self.__payment_method = response_body['paymentMethod']
        if 'periodStart' in response_body:
            self.__period_start = response_body['periodStart']
        if 'periodEnd' in response_body:
            self.__period_end = response_body['periodEnd']
        if 'paidTime' in response_body:
            self.__paid_time = response_body['paidTime']
        if 'dueDate' in response_body:
            self.__due_date = response_body['dueDate']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'payToRequestId' in response_body:
            self.__pay_to_request_id = response_body['payToRequestId']
        if 'payToId' in response_body:
            self.__pay_to_id = response_body['payToId']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'fileUrl' in response_body:
            self.__file_url = response_body['fileUrl']
        if 'items' in response_body:
            self.__items = []
            for item in response_body['items']:
                obj = ReceiptItem()
                obj.parse_rsp_body(item)
                self.__items.append(obj)
        if 'payments' in response_body:
            self.__payments = []
            for item in response_body['payments']:
                obj = InvoicePayment()
                obj.parse_rsp_body(item)
                self.__payments.append(obj)
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
