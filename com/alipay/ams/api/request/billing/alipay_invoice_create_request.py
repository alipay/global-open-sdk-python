import json
from com.alipay.ams.api.model.automatic_tax import AutomaticTax
from com.alipay.ams.api.model.invoice_customer_details import InvoiceCustomerDetails
from com.alipay.ams.api.model.invoice_create_item import InvoiceCreateItem
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.invoice_shipping import InvoiceShipping
from com.alipay.ams.api.model.billing_discount import BillingDiscount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceCreateRequest, self).__init__("/ams/api/v1/billing/invoice/create") 

        self.__include_payment_link = None  # type: bool
        self.__automatic_tax = None  # type: AutomaticTax
        self.__customer_details = None  # type: InvoiceCustomerDetails
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
    def include_payment_link(self):
        """
        Whether invoice emails and PDFs display payment links. Defaults to true on the server; false hides links without suppressing email or hostedInvoiceUrl. Saved for later delivery unless overridden.
        """
        return self.__include_payment_link

    @include_payment_link.setter
    def include_payment_link(self, value):
        self.__include_payment_link = value
    @property
    def automatic_tax(self):
        """Gets the automatic_tax of this AlipayInvoiceCreateRequest.
        
        """
        return self.__automatic_tax

    @automatic_tax.setter
    def automatic_tax(self, value):
        self.__automatic_tax = value
    @property
    def customer_details(self):
        """Gets the customer_details of this AlipayInvoiceCreateRequest.
        
        """
        return self.__customer_details

    @customer_details.setter
    def customer_details(self, value):
        self.__customer_details = value
    @property
    def invoice_request_id(self):
        """
        Merchant-scoped idempotency key. A duplicate returns BIZ_REPEATED_SUBMIT (F) with the persisted invoice ID and status before customer resolution, without comparing replay payloads. Reconcile and retry unknown outcomes with the same ID.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value
    @property
    def customer_id(self):
        """
        Existing customer ID belonging to the merchant. Supply exactly one of customerId and customerDetails.
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
        Request invoice email delivery when created as OPEN. Defaults to false on the server. Independent of includePaymentLink; delivery failure does not undo issuance.
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def cc_emails(self):
        """
        Valid CC email addresses. The current invoice auto-send flow does not guarantee CC forwarding.
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
        Invoice-level discount items. Each item carries either a &#x60;couponId&#x60; or &#x60;promotionCodeId&#x60; (at least one must be provided per element). Multiple discounts are applied sequentially to the invoice subtotal in the order they appear. The system resolves each discount reference to its actual discount value (percentage or fixed amount) at creation time and computes the resulting &#x60;discountAmount&#x60; internally. Can be null. See DiscountItem Object below for field details. Invoice-level discounts are not supported when automaticTax.enabled is true.
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
        if hasattr(self, "include_payment_link") and self.include_payment_link is not None:
            params['includePaymentLink'] = self.include_payment_link
        if hasattr(self, "automatic_tax") and self.automatic_tax is not None:
            params['automaticTax'] = self.automatic_tax
        if hasattr(self, "customer_details") and self.customer_details is not None:
            params['customerDetails'] = self.customer_details
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
        if 'includePaymentLink' in response_body:
            self.__include_payment_link = response_body['includePaymentLink']
        if 'automaticTax' in response_body:
            self.__automatic_tax = AutomaticTax()
            self.__automatic_tax.parse_rsp_body(response_body['automaticTax'])
        if 'customerDetails' in response_body:
            self.__customer_details = InvoiceCustomerDetails()
            self.__customer_details.parse_rsp_body(response_body['customerDetails'])
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
