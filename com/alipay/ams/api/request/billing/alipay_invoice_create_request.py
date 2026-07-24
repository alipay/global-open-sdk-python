import json
from com.alipay.ams.api.model.item import Item
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.shipping import Shipping
from com.alipay.ams.api.model.discount import Discount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceCreateRequest, self).__init__("/ams/api/v1/billing/invoice/create") 

        self.__invoice_request_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__currency = None  # type: str
        self.__items = None  # type: [Item]
        self.__status = None  # type: str
        self.__auto_send = None  # type: bool
        self.__cc_emails = None  # type: [str]
        self.__description = None  # type: str
        self.__due_date = None  # type: str
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__shipping = None  # type: Shipping
        self.__discounts = None  # type: [Discount]
        

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
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
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
    def currency(self):
        """
        The 3-letter currency code that follows the ISO 4217 standard. Maximum length: 3 characters.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
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
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def auto_send(self):
        """
        Indicates whether to automatically send the notification. Note: See documentation for details.
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def cc_emails(self):
        """
        The cc emails.
        """
        return self.__cc_emails

    @cc_emails.setter
    def cc_emails(self, value):
        self.__cc_emails = value
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
    def due_date(self):
        """
        The due date. Maximum length: 24 characters. Note: See documentation for details.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
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
        The discounts applied.
        """
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        self.__discounts = value


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
                obj = Item()
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
            self.__shipping = Shipping()
            self.__shipping.parse_rsp_body(response_body['shipping'])
        if 'discounts' in response_body:
            self.__discounts = []
            for item in response_body['discounts']:
                obj = Discount()
                obj.parse_rsp_body(item)
                self.__discounts.append(obj)
