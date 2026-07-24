import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.shipping import Shipping
from com.alipay.ams.api.model.item import Item
from com.alipay.ams.api.model.payment import Payment
from com.alipay.ams.api.model.invoice_note import InvoiceNote
from com.alipay.ams.api.model.discount import Discount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoice_id = None  # type: str
        self.__invoice_request_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__invoice_number = None  # type: str
        self.__customer_first_name = None  # type: str
        self.__customer_last_name = None  # type: str
        self.__customer_email = None  # type: str
        self.__reason = None  # type: str
        self.__phase_no = None  # type: str
        self.__status = None  # type: str
        self.__currency = None  # type: str
        self.__subtotal = None  # type: Amount
        self.__discount_amount = None  # type: Amount
        self.__total_amount = None  # type: Amount
        self.__paid_amount = None  # type: Amount
        self.__remaining_amount = None  # type: Amount
        self.__tax_amount = None  # type: Amount
        self.__payment_deducted_amount = None  # type: Amount
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__shipping = None  # type: Shipping
        self.__hosted_invoice_url = None  # type: str
        self.__period_start = None  # type: str
        self.__period_end = None  # type: str
        self.__due_date = None  # type: str
        self.__paid_time = None  # type: str
        self.__description = None  # type: str
        self.__items = None  # type: [Item]
        self.__payments = None  # type: [Payment]
        self.__invoice_notes = None  # type: [InvoiceNote]
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        self.__discounts = None  # type: [Discount]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def invoice_request_id(self):
        """
        The invoice request id. Maximum length: 64 characters.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value
    @property
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def invoice_number(self):
        """
        The invoice number. Maximum length: 64 characters.
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value
    @property
    def customer_first_name(self):
        """
        The customer first name. Maximum length: 256 characters.
        """
        return self.__customer_first_name

    @customer_first_name.setter
    def customer_first_name(self, value):
        self.__customer_first_name = value
    @property
    def customer_last_name(self):
        """
        The customer last name. Maximum length: 256 characters.
        """
        return self.__customer_last_name

    @customer_last_name.setter
    def customer_last_name(self, value):
        self.__customer_last_name = value
    @property
    def customer_email(self):
        """
        The email address of the customer. Maximum length: 256 characters.
        """
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, value):
        self.__customer_email = value
    @property
    def reason(self):
        """
        The reason for the status change. Maximum length: 32 characters.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def phase_no(self):
        """
        The phase no.
        """
        return self.__phase_no

    @phase_no.setter
    def phase_no(self, value):
        self.__phase_no = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def currency(self):
        """
        The 3-letter currency code that follows the ISO 4217 standard. Maximum length: 3 characters.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def subtotal(self):
        """Gets the subtotal of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
    @property
    def discount_amount(self):
        """Gets the discount_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value
    @property
    def total_amount(self):
        """Gets the total_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def paid_amount(self):
        """Gets the paid_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self.__paid_amount = value
    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, value):
        self.__remaining_amount = value
    @property
    def tax_amount(self):
        """Gets the tax_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def payment_deducted_amount(self):
        """Gets the payment_deducted_amount of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__payment_deducted_amount

    @payment_deducted_amount.setter
    def payment_deducted_amount(self, value):
        self.__payment_deducted_amount = value
    @property
    def collection_method(self):
        """
        The collection method. Maximum length: 32 characters.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def shipping(self):
        """Gets the shipping of this AlipayInvoiceInquireDetailsResponse.
        
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value
    @property
    def hosted_invoice_url(self):
        """
        The hosted invoice url. Maximum length: 2048 characters.
        """
        return self.__hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, value):
        self.__hosted_invoice_url = value
    @property
    def period_start(self):
        """
        The period start. Maximum length: 24 characters.
        """
        return self.__period_start

    @period_start.setter
    def period_start(self, value):
        self.__period_start = value
    @property
    def period_end(self):
        """
        The period end. Maximum length: 24 characters.
        """
        return self.__period_end

    @period_end.setter
    def period_end(self, value):
        self.__period_end = value
    @property
    def due_date(self):
        """
        The due date. Maximum length: 24 characters.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def paid_time(self):
        """
        The paid time. Maximum length: 24 characters.
        """
        return self.__paid_time

    @paid_time.setter
    def paid_time(self, value):
        self.__paid_time = value
    @property
    def description(self):
        """
        The description. Maximum length: 512 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def items(self):
        """
        The items.
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def payments(self):
        """
        The payments.
        """
        return self.__payments

    @payments.setter
    def payments(self, value):
        self.__payments = value
    @property
    def invoice_notes(self):
        """
        The invoice notes.
        """
        return self.__invoice_notes

    @invoice_notes.setter
    def invoice_notes(self, value):
        self.__invoice_notes = value
    @property
    def gmt_create(self):
        """
        The creation time. Maximum length: 24 characters.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        The gmt update. Maximum length: 24 characters.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value
    @property
    def discounts(self):
        """
        The discounts applied.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "invoice_number") and self.invoice_number is not None:
            params['invoiceNumber'] = self.invoice_number
        if hasattr(self, "customer_first_name") and self.customer_first_name is not None:
            params['customerFirstName'] = self.customer_first_name
        if hasattr(self, "customer_last_name") and self.customer_last_name is not None:
            params['customerLastName'] = self.customer_last_name
        if hasattr(self, "customer_email") and self.customer_email is not None:
            params['customerEmail'] = self.customer_email
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "phase_no") and self.phase_no is not None:
            params['phaseNo'] = self.phase_no
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "subtotal") and self.subtotal is not None:
            params['subtotal'] = self.subtotal
        if hasattr(self, "discount_amount") and self.discount_amount is not None:
            params['discountAmount'] = self.discount_amount
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "paid_amount") and self.paid_amount is not None:
            params['paidAmount'] = self.paid_amount
        if hasattr(self, "remaining_amount") and self.remaining_amount is not None:
            params['remainingAmount'] = self.remaining_amount
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "payment_deducted_amount") and self.payment_deducted_amount is not None:
            params['paymentDeductedAmount'] = self.payment_deducted_amount
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "shipping") and self.shipping is not None:
            params['shipping'] = self.shipping
        if hasattr(self, "hosted_invoice_url") and self.hosted_invoice_url is not None:
            params['hostedInvoiceUrl'] = self.hosted_invoice_url
        if hasattr(self, "period_start") and self.period_start is not None:
            params['periodStart'] = self.period_start
        if hasattr(self, "period_end") and self.period_end is not None:
            params['periodEnd'] = self.period_end
        if hasattr(self, "due_date") and self.due_date is not None:
            params['dueDate'] = self.due_date
        if hasattr(self, "paid_time") and self.paid_time is not None:
            params['paidTime'] = self.paid_time
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "items") and self.items is not None:
            params['items'] = self.items
        if hasattr(self, "payments") and self.payments is not None:
            params['payments'] = self.payments
        if hasattr(self, "invoice_notes") and self.invoice_notes is not None:
            params['invoiceNotes'] = self.invoice_notes
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'invoiceNumber' in response_body:
            self.__invoice_number = response_body['invoiceNumber']
        if 'customerFirstName' in response_body:
            self.__customer_first_name = response_body['customerFirstName']
        if 'customerLastName' in response_body:
            self.__customer_last_name = response_body['customerLastName']
        if 'customerEmail' in response_body:
            self.__customer_email = response_body['customerEmail']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'phaseNo' in response_body:
            self.__phase_no = response_body['phaseNo']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'subtotal' in response_body:
            self.__subtotal = Amount()
            self.__subtotal.parse_rsp_body(response_body['subtotal'])
        if 'discountAmount' in response_body:
            self.__discount_amount = Amount()
            self.__discount_amount.parse_rsp_body(response_body['discountAmount'])
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'paidAmount' in response_body:
            self.__paid_amount = Amount()
            self.__paid_amount.parse_rsp_body(response_body['paidAmount'])
        if 'remainingAmount' in response_body:
            self.__remaining_amount = Amount()
            self.__remaining_amount.parse_rsp_body(response_body['remainingAmount'])
        if 'taxAmount' in response_body:
            self.__tax_amount = Amount()
            self.__tax_amount.parse_rsp_body(response_body['taxAmount'])
        if 'paymentDeductedAmount' in response_body:
            self.__payment_deducted_amount = Amount()
            self.__payment_deducted_amount.parse_rsp_body(response_body['paymentDeductedAmount'])
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'shipping' in response_body:
            self.__shipping = Shipping()
            self.__shipping.parse_rsp_body(response_body['shipping'])
        if 'hostedInvoiceUrl' in response_body:
            self.__hosted_invoice_url = response_body['hostedInvoiceUrl']
        if 'periodStart' in response_body:
            self.__period_start = response_body['periodStart']
        if 'periodEnd' in response_body:
            self.__period_end = response_body['periodEnd']
        if 'dueDate' in response_body:
            self.__due_date = response_body['dueDate']
        if 'paidTime' in response_body:
            self.__paid_time = response_body['paidTime']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'items' in response_body:
            self.__items = []
            for item in response_body['items']:
                obj = Item()
                obj.parse_rsp_body(item)
                self.__items.append(obj)
        if 'payments' in response_body:
            self.__payments = []
            for item in response_body['payments']:
                obj = Payment()
                obj.parse_rsp_body(item)
                self.__payments.append(obj)
        if 'invoiceNotes' in response_body:
            self.__invoice_notes = []
            for item in response_body['invoiceNotes']:
                obj = InvoiceNote()
                obj.parse_rsp_body(item)
                self.__invoice_notes.append(obj)
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = Discount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
