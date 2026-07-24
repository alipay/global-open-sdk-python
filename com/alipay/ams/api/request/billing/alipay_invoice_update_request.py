import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.shipping import Shipping



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceUpdateRequest, self).__init__("/ams/api/v1/billing/invoice/update") 

        self.__invoice_id = None  # type: str
        self.__description = None  # type: str
        self.__due_date = None  # type: str
        self.__collection_method = None  # type: str
        self.__payment_method = None  # type: PaymentMethod
        self.__shipping = None  # type: Shipping
        

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
        The due date. Maximum length: 24 characters.
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
            self.__shipping = Shipping()
            self.__shipping.parse_rsp_body(response_body['shipping'])
