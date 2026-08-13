import json
from com.alipay.ams.api.model.receipt_payment_method import ReceiptPaymentMethod
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




class Receipt:
    def __init__(self):
        
        self.__receipt_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__original_receipt_id = None  # type: str
        self.__receipt_type = None  # type: str
        self.__status = None  # type: str
        self.__reason = None  # type: str
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: ReceiptPaymentMethod
        self.__subtotal = None  # type: Amount
        self.__total_amount = None  # type: Amount
        self.__paid_amount = None  # type: Amount
        self.__remaining_amount = None  # type: Amount
        self.__refund_amount = None  # type: Amount
        self.__refunded_amount = None  # type: Amount
        self.__payment_deducted_amount = None  # type: Amount
        self.__period_start = None  # type: str
        self.__period_end = None  # type: str
        self.__description = None  # type: str
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        self.__payment_method_type = None  # type: str
        self.__discount_amount = None  # type: Amount
        self.__tax_amount = None  # type: Amount
        self.__shipping_fee_amount = None  # type: Amount
        self.__settlement_amount = None  # type: Amount
        self.__fx_rate = None  # type: str
        self.__fx_rate_id = None  # type: str
        self.__due_date = None  # type: str
        self.__paid_time = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__pay_to_request_id = None  # type: str
        self.__pay_to_id = None  # type: str
        self.__footer = None  # type: str
        self.__file_url = None  # type: str
        

    @property
    def receipt_id(self):
        """
        Receipt ID. Unique identifier.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def invoice_id(self):
        """
        Filter by associated invoice ID. Returns receipts linked to this invoice. Can be null (no filter).
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def customer_id(self):
        """
        Filter by customer ID. Returns only receipts belonging to this customer. Can be null (no filter).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def subscription_id(self):
        """
        Filter by associated subscription ID. Returns receipts linked to this subscription. Can be null (no filter).
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def original_receipt_id(self):
        """
        Original receipt ID for refund receipts. Only set when receiptType&#x3D;REFUND. Null for PAYMENT receipts.
        """
        return self.__original_receipt_id

    @original_receipt_id.setter
    def original_receipt_id(self, value):
        self.__original_receipt_id = value
    @property
    def receipt_type(self):
        """
        Filter by receipt type. Allowed values: &#x60;PAYMENT&#x60; (receipt for a payment), &#x60;REFUND&#x60; (receipt for a refund). Unknown type values are silently ignored (treated as no filter for that value). Can be null (no filter).
        """
        return self.__receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self.__receipt_type = value
    @property
    def status(self):
        """
        Filter by receipt status. Allowed values: &#x60;ACTIVE&#x60; (payment receipt with no refunds), &#x60;PARTIALLY_REFUNDED&#x60; (some amount refunded), &#x60;REFUNDED&#x60; (fully refunded). Unknown status values are silently ignored (treated as no filter for that value). Can be null (no filter).
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def reason(self):
        """
        Reason for receipt creation. Allowed values: &#x60;SUBSCRIPTION_CREATION&#x60;, &#x60;RECURRENCE&#x60;, &#x60;UPDATE&#x60;, &#x60;TRIAL_END&#x60;, &#x60;REFUND&#x60;. Merchants should handle unknown enum values gracefully (e.g., log for review); new values may be added without version change.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def collection_method(self):
        """
        Payment collection method: &#x60;CHARGE_AUTOMATICALLY&#x60; or &#x60;SEND_INVOICE&#x60;. Returned when the receipt has an associated collection method; null when not applicable (e.g., manual payment confirmation).
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def payment_method(self):
        """Gets the payment_method of this Receipt.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def subtotal(self):
        """Gets the subtotal of this Receipt.
        
        """
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
    @property
    def total_amount(self):
        """Gets the total_amount of this Receipt.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def paid_amount(self):
        """Gets the paid_amount of this Receipt.
        
        """
        return self.__paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self.__paid_amount = value
    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this Receipt.
        
        """
        return self.__remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, value):
        self.__remaining_amount = value
    @property
    def refund_amount(self):
        """Gets the refund_amount of this Receipt.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this Receipt.
        
        """
        return self.__refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, value):
        self.__refunded_amount = value
    @property
    def payment_deducted_amount(self):
        """Gets the payment_deducted_amount of this Receipt.
        
        """
        return self.__payment_deducted_amount

    @payment_deducted_amount.setter
    def payment_deducted_amount(self, value):
        self.__payment_deducted_amount = value
    @property
    def period_start(self):
        """
        ISO 8601 timestamp of billing period start. Null if not subscription-based.
        """
        return self.__period_start

    @period_start.setter
    def period_start(self, value):
        self.__period_start = value
    @property
    def period_end(self):
        """
        ISO 8601 timestamp of billing period end. Null if not subscription-based.
        """
        return self.__period_end

    @period_end.setter
    def period_end(self, value):
        self.__period_end = value
    @property
    def description(self):
        """
        Receipt narrative. Returned when merchant set a receipt narrative; null if no description was provided.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def gmt_create(self):
        """
        ISO 8601 timestamp of receipt creation.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        ISO 8601 timestamp of last receipt update.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value
    @property
    def payment_method_type(self):
        """
        Payment method type (e.g., &#x60;CARD&#x60;, &#x60;WALLET&#x60;). Can be null.
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def discount_amount(self):
        """Gets the discount_amount of this Receipt.
        
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value
    @property
    def tax_amount(self):
        """Gets the tax_amount of this Receipt.
        
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def shipping_fee_amount(self):
        """Gets the shipping_fee_amount of this Receipt.
        
        """
        return self.__shipping_fee_amount

    @shipping_fee_amount.setter
    def shipping_fee_amount(self, value):
        self.__shipping_fee_amount = value
    @property
    def settlement_amount(self):
        """Gets the settlement_amount of this Receipt.
        
        """
        return self.__settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self.__settlement_amount = value
    @property
    def fx_rate(self):
        """
        Foreign exchange rate applied when payment currency differs from settlement currency. Null for same-currency transactions.
        """
        return self.__fx_rate

    @fx_rate.setter
    def fx_rate(self, value):
        self.__fx_rate = value
    @property
    def fx_rate_id(self):
        """
        FX rate reference ID for audit and reconciliation. Null when no FX rate was applied.
        """
        return self.__fx_rate_id

    @fx_rate_id.setter
    def fx_rate_id(self, value):
        self.__fx_rate_id = value
    @property
    def due_date(self):
        """
        ISO 8601 timestamp of payment due date. Null for receipts without a due date.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def paid_time(self):
        """
        ISO 8601 timestamp of when payment was completed. Null for unpaid receipts.
        """
        return self.__paid_time

    @paid_time.setter
    def paid_time(self, value):
        self.__paid_time = value
    @property
    def payment_request_id(self):
        """
        Outbound payment request ID used as idempotency key. Null for offline confirmations.
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def pay_to_request_id(self):
        """
        Payment order request ID. Null if not applicable.
        """
        return self.__pay_to_request_id

    @pay_to_request_id.setter
    def pay_to_request_id(self, value):
        self.__pay_to_request_id = value
    @property
    def pay_to_id(self):
        """
        Payment order ID. Null if not applicable.
        """
        return self.__pay_to_id

    @pay_to_id.setter
    def pay_to_id(self, value):
        self.__pay_to_id = value
    @property
    def footer(self):
        """
        Receipt footer text. Can be null.
        """
        return self.__footer

    @footer.setter
    def footer(self, value):
        self.__footer = value
    @property
    def file_url(self):
        """
        URL to the receipt PDF file. Can be null (PDF not yet generated).
        """
        return self.__file_url

    @file_url.setter
    def file_url(self, value):
        self.__file_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "original_receipt_id") and self.original_receipt_id is not None:
            params['originalReceiptId'] = self.original_receipt_id
        if hasattr(self, "receipt_type") and self.receipt_type is not None:
            params['receiptType'] = self.receipt_type
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "subtotal") and self.subtotal is not None:
            params['subtotal'] = self.subtotal
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "paid_amount") and self.paid_amount is not None:
            params['paidAmount'] = self.paid_amount
        if hasattr(self, "remaining_amount") and self.remaining_amount is not None:
            params['remainingAmount'] = self.remaining_amount
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refunded_amount") and self.refunded_amount is not None:
            params['refundedAmount'] = self.refunded_amount
        if hasattr(self, "payment_deducted_amount") and self.payment_deducted_amount is not None:
            params['paymentDeductedAmount'] = self.payment_deducted_amount
        if hasattr(self, "period_start") and self.period_start is not None:
            params['periodStart'] = self.period_start
        if hasattr(self, "period_end") and self.period_end is not None:
            params['periodEnd'] = self.period_end
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "discount_amount") and self.discount_amount is not None:
            params['discountAmount'] = self.discount_amount
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "shipping_fee_amount") and self.shipping_fee_amount is not None:
            params['shippingFeeAmount'] = self.shipping_fee_amount
        if hasattr(self, "settlement_amount") and self.settlement_amount is not None:
            params['settlementAmount'] = self.settlement_amount
        if hasattr(self, "fx_rate") and self.fx_rate is not None:
            params['fxRate'] = self.fx_rate
        if hasattr(self, "fx_rate_id") and self.fx_rate_id is not None:
            params['fxRateId'] = self.fx_rate_id
        if hasattr(self, "due_date") and self.due_date is not None:
            params['dueDate'] = self.due_date
        if hasattr(self, "paid_time") and self.paid_time is not None:
            params['paidTime'] = self.paid_time
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "pay_to_request_id") and self.pay_to_request_id is not None:
            params['payToRequestId'] = self.pay_to_request_id
        if hasattr(self, "pay_to_id") and self.pay_to_id is not None:
            params['payToId'] = self.pay_to_id
        if hasattr(self, "footer") and self.footer is not None:
            params['footer'] = self.footer
        if hasattr(self, "file_url") and self.file_url is not None:
            params['fileUrl'] = self.file_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'originalReceiptId' in response_body:
            self.__original_receipt_id = response_body['originalReceiptId']
        if 'receiptType' in response_body:
            self.__receipt_type = response_body['receiptType']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'paymentMethod' in response_body:
            self.__payment_method = ReceiptPaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'subtotal' in response_body:
            self.__subtotal = Amount()
            self.__subtotal.parse_rsp_body(response_body['subtotal'])
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'paidAmount' in response_body:
            self.__paid_amount = Amount()
            self.__paid_amount.parse_rsp_body(response_body['paidAmount'])
        if 'remainingAmount' in response_body:
            self.__remaining_amount = Amount()
            self.__remaining_amount.parse_rsp_body(response_body['remainingAmount'])
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundedAmount' in response_body:
            self.__refunded_amount = Amount()
            self.__refunded_amount.parse_rsp_body(response_body['refundedAmount'])
        if 'paymentDeductedAmount' in response_body:
            self.__payment_deducted_amount = Amount()
            self.__payment_deducted_amount.parse_rsp_body(response_body['paymentDeductedAmount'])
        if 'periodStart' in response_body:
            self.__period_start = response_body['periodStart']
        if 'periodEnd' in response_body:
            self.__period_end = response_body['periodEnd']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'discountAmount' in response_body:
            self.__discount_amount = Amount()
            self.__discount_amount.parse_rsp_body(response_body['discountAmount'])
        if 'taxAmount' in response_body:
            self.__tax_amount = Amount()
            self.__tax_amount.parse_rsp_body(response_body['taxAmount'])
        if 'shippingFeeAmount' in response_body:
            self.__shipping_fee_amount = Amount()
            self.__shipping_fee_amount.parse_rsp_body(response_body['shippingFeeAmount'])
        if 'settlementAmount' in response_body:
            self.__settlement_amount = Amount()
            self.__settlement_amount.parse_rsp_body(response_body['settlementAmount'])
        if 'fxRate' in response_body:
            self.__fx_rate = response_body['fxRate']
        if 'fxRateId' in response_body:
            self.__fx_rate_id = response_body['fxRateId']
        if 'dueDate' in response_body:
            self.__due_date = response_body['dueDate']
        if 'paidTime' in response_body:
            self.__paid_time = response_body['paidTime']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'payToRequestId' in response_body:
            self.__pay_to_request_id = response_body['payToRequestId']
        if 'payToId' in response_body:
            self.__pay_to_id = response_body['payToId']
        if 'footer' in response_body:
            self.__footer = response_body['footer']
        if 'fileUrl' in response_body:
            self.__file_url = response_body['fileUrl']
