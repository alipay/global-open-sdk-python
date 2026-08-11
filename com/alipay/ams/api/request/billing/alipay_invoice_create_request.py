import json
from com.alipay.ams.api.model.invoice_create_item import InvoiceCreateItem
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.invoice_shipping import InvoiceShipping
from com.alipay.ams.api.model.billing_discount import BillingDiscount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceCreateRequest, self).__init__("/ams/api/v1/billing/invoice/create") 

        self.__invoice_request_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__currency = None  # type: str
        self.__items = None  # type: [InvoiceCreateItem]
        self.__status = None  # type: str
        self.__auto_send = None  # type: bool
        self.__cc_emails = None  # type: [str]
        self.__description = None  # type: str
        self.__due_date = None  # type: str
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__shipping = None  # type: InvoiceShipping
        self.__discounts = None  # type: [BillingDiscount]
        self.__invoice_notify_url = None  # type: str
        

    @property
    def invoice_request_id(self):
        """
        Merchant-supplied idempotency key. Repeating the same &#x60;invoiceRequestId&#x60; returns the originally created invoice (true idempotency - same key, same result). Must be unique per merchant. Backed by a unique constraint &#x60;UK(merchant_id, invoice_request_id)&#x60; on &#x60;ibilling_invoice&#x60;. Accepts alphanumeric characters, and underscores. Cannot be null.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value
    @property
    def customer_id(self):
        """
        Customer ID this invoice belongs to. The customer must exist and belong to the requesting merchant. Cannot be null.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def subscription_id(self):
        """
        The subscription this invoice is linked to. Leave empty for standalone invoices. If provided, the subscription must exist and belong to the requesting merchant. Can be null.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def currency(self):
        """
        Three-letter ISO currency code in uppercase. The currency in which the invoice item will be charged (e.g., &#x60;\&quot;USD\&quot;&#x60;). Must be consistent across all monetary fields in the request. Cannot be null.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def items(self):
        """
        Line items for the invoice. Minimum 1 item. Maximum 100 for standalone invoices, 20 for subscription-linked invoices (subscription invoices use batch price calculation which requires shared recurring settings). Each item supports three pricing models: Model 1 (Fixed Amount via &#x60;itemAmount&#x60;), Model 2 (Unit Amount x Quantity via &#x60;unitAmount&#x60;), Model 3 (Price Object via &#x60;priceId&#x60;). Only one model per item; mixing is rejected. Additionally, all items within the same invoice must use the same pricing model - mixed pricing models across items are rejected. Cannot be null or empty.
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def status(self):
        """
        Invoice status on creation. Allowed values: &#x60;DRAFT&#x60; and &#x60;OPEN&#x60;. Defaults to &#x60;DRAFT&#x60; when omitted. When set to &#x60;OPEN&#x60;, &#x60;dueDate&#x60; is required. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def auto_send(self):
        """
        Whether to email the invoice to the customer when created as &#x60;OPEN&#x60;. When &#x60;true&#x60;, the email is sent idempotently - sending the same invoice twice won&#39;t produce duplicate emails. Can be null (defaults to false).
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def cc_emails(self):
        """
        CC email addresses for invoice notification. When &#x60;autoSend&#x60; is &#x60;true&#x60;, the invoice email is also sent to these addresses. Can be null.
        """
        return self.__cc_emails

    @cc_emails.setter
    def cc_emails(self, value):
        self.__cc_emails = value
    @property
    def description(self):
        """
        Human-readable description of the invoice. Appears on the invoice PDF and hosted page. HTML tags are stripped for XSS prevention. Can be null.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def due_date(self):
        """
        Payment due date. Format: ISO 8601 date (&#x60;yyyy-MM-dd&#x60;, e.g., &#x60;\&quot;2026-06-01\&quot;&#x60;) or full ISO 8601 datetime with timezone offset (e.g., &#x60;\&quot;2026-06-01T23:59:59+00:00\&quot;&#x60;). Date-only values are interpreted as end-of-day in the merchant&#39;s acquiring-region timezone. Required when &#x60;status&#x3D;OPEN&#x60;; optional when &#x60;status&#x3D;DRAFT&#x60;. Past dates are rejected with &#x60;PARAM_ILLEGAL&#x60;. Maximum length: 64 characters.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def collection_method(self):
        """
        Payment collection method. See enum table below. Default: &#x60;CHARGE_AUTOMATICALLY&#x60;. Can be null (defaults to &#x60;CHARGE_AUTOMATICALLY&#x60;).
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayInvoiceCreateRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def shipping(self):
        """Gets the shipping of this AlipayInvoiceCreateRequest.
        
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value
    @property
    def discounts(self):
        """
        Invoice-level discount items. Each item carries either a &#x60;couponId&#x60; or &#x60;promotionCodeId&#x60; (at least one must be provided per element). Multiple discounts are applied sequentially to the invoice subtotal in the order they appear. The system resolves each discount reference to its actual discount value (percentage or fixed amount) at creation time and computes the resulting &#x60;discountAmount&#x60; internally. Can be null. See DiscountItem Object below for field details.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value
    @property
    def invoice_notify_url(self):
        """
        HTTPS URL that receives invoice payment-status notifications. When omitted, invoice notifications are not sent. Maximum length: 2048 characters.
        """
        return self.__invoice_notify_url

    @invoice_notify_url.setter
    def invoice_notify_url(self, value):
        self.__invoice_notify_url = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "items") and self.items is not None:
            params['items'] = self.items
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "auto_send") and self.auto_send is not None:
            params['autoSend'] = self.auto_send
        if hasattr(self, "cc_emails") and self.cc_emails is not None:
            params['ccEmails'] = self.cc_emails
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "due_date") and self.due_date is not None:
            params['dueDate'] = self.due_date
        if hasattr(self, "collection_method") and self.collection_method is not None:
            params['collectionMethod'] = self.collection_method
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "shipping") and self.shipping is not None:
            params['shipping'] = self.shipping
        if hasattr(self, "discounts") and self.discounts is not None:
            params['discounts'] = self.discounts
        if hasattr(self, "invoice_notify_url") and self.invoice_notify_url is not None:
            params['invoiceNotifyUrl'] = self.invoice_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'items' in response_body:
            self.__items = []
            for item in response_body['items']:
                obj = InvoiceCreateItem()
                obj.parse_rsp_body(item)
                self.__items.append(obj)
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'autoSend' in response_body:
            self.__auto_send = response_body['autoSend']
        if 'ccEmails' in response_body:
            self.__cc_emails = response_body['ccEmails']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'dueDate' in response_body:
            self.__due_date = response_body['dueDate']
        if 'collectionMethod' in response_body:
            self.__collection_method = response_body['collectionMethod']
        if 'paymentMethod' in response_body:
            self.__payment_method = PaymentMethod()
            self.__payment_method.parse_rsp_body(response_body['paymentMethod'])
        if 'shipping' in response_body:
            self.__shipping = InvoiceShipping()
            self.__shipping.parse_rsp_body(response_body['shipping'])
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = BillingDiscount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
        if 'invoiceNotifyUrl' in response_body:
            self.__invoice_notify_url = response_body['invoiceNotifyUrl']
