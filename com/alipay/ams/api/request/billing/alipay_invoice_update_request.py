import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.invoice_shipping import InvoiceShipping
from com.alipay.ams.api.model.invoice_custom_field import InvoiceCustomField



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceUpdateRequest, self).__init__("/ams/api/v1/billing/invoice/update") 

        self.__invoice_id = None  # type: str
        self.__description = None  # type: str
        self.__due_date = None  # type: str
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__shipping = None  # type: InvoiceShipping
        self.__customer_id = None  # type: str
        self.__footer = None  # type: str
        self.__include_payment_link = None  # type: bool
        self.__memo = None  # type: str
        self.__custom_fields = None  # type: [InvoiceCustomField]
        self.__invoice_notify_url = None  # type: str
        

    @property
    def invoice_id(self):
        """
        Invoice ID to edit. Must be DRAFT status and belong to the merchant. Cannot be null.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def description(self):
        """
        Updated invoice description. When omitted, the existing value is unchanged. Maximum length: 512 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def due_date(self):
        """
        Updated payment due date in &#x60;yyyy-MM-dd&#x60; or ISO 8601 format. The date must be in the future. When omitted, the existing value is unchanged. Maximum length: 24 characters.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def collection_method(self):
        """
        Updated collection method. Allowed values: &#x60;CHARGE_AUTOMATICALLY&#x60; and &#x60;SEND_INVOICE&#x60;. When omitted, the existing value is unchanged. Maximum length: 32 characters.
        """
        return self.__collection_method

    @collection_method.setter
    def collection_method(self, value):
        self.__collection_method = value
    @property
    def payment_method(self):
        """Gets the payment_method of this AlipayInvoiceUpdateRequest.
        
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def shipping(self):
        """Gets the shipping of this AlipayInvoiceUpdateRequest.
        
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value
    @property
    def customer_id(self):
        """
        Customer ID to associate with this invoice. If the customer differs from the invoice&#39;s current customer, the invoice is soft-deleted and recreated with a new ID in the new customer&#39;s shard. The response includes &#x60;previousInvoiceId&#x60; with the old invoice ID. Can be null (unchanged).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def footer(self):
        """
        Footer text for PDF rendering (multi-line). PATCH semantics: null &#x3D; unchanged, empty string &#x3D; cleared.
        """
        return self.__footer

    @footer.setter
    def footer(self, value):
        self.__footer = value
    @property
    def include_payment_link(self):
        """
        Whether to include payment link in email and PDF. Default: true. Stored in invoice metadata.
        """
        return self.__include_payment_link

    @include_payment_link.setter
    def include_payment_link(self, value):
        self.__include_payment_link = value
    @property
    def memo(self):
        """
        Free-text memo for PDF rendering (multi-line, &#x60;\\n&#x60; separated). PATCH semantics: null &#x3D; unchanged, empty string &#x3D; cleared.
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def custom_fields(self):
        """
        Custom fields for PDF rendering. Max 4 items. Each InvoiceCustomField has &#x60;label&#x60; (String, max 256, M) and &#x60;value&#x60; (String, max 512, M).
        """
        return self.__custom_fields

    @custom_fields.setter
    def custom_fields(self, value):
        self.__custom_fields = value
    @property
    def invoice_notify_url(self):
        """
        Updated HTTPS URL that receives invoice payment-status notifications. When omitted, the existing value is unchanged. Maximum length: 2048 characters.
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
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
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
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "footer") and self.footer is not None:
            params['footer'] = self.footer
        if hasattr(self, "include_payment_link") and self.include_payment_link is not None:
            params['includePaymentLink'] = self.include_payment_link
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "custom_fields") and self.custom_fields is not None:
            params['customFields'] = self.custom_fields
        if hasattr(self, "invoice_notify_url") and self.invoice_notify_url is not None:
            params['invoiceNotifyUrl'] = self.invoice_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
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
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'footer' in response_body:
            self.__footer = response_body['footer']
        if 'includePaymentLink' in response_body:
            self.__include_payment_link = response_body['includePaymentLink']
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'customFields' in response_body:
            self.__custom_fields = []
            for item in response_body['customFields']:
                obj = InvoiceCustomField()
                obj.parse_rsp_body(item)
                self.__custom_fields.append(obj)
        if 'invoiceNotifyUrl' in response_body:
            self.__invoice_notify_url = response_body['invoiceNotifyUrl']
