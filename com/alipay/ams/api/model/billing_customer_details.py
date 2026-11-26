import json
from com.alipay.ams.api.model.customer_address import CustomerAddress
from com.alipay.ams.api.model.customer_address import CustomerAddress
from com.alipay.ams.api.model.customer_address import CustomerAddress
from com.alipay.ams.api.model.customer_tax_id import CustomerTaxId




class BillingCustomerDetails:
    def __init__(self):
        
        self.__full_name = None  # type: str
        self.__billing_address = None  # type: CustomerAddress
        self.__shipping_address = None  # type: CustomerAddress
        self.__customer_type = None  # type: str
        self.__business_name = None  # type: str
        self.__business_address = None  # type: CustomerAddress
        self.__tax_ids = None  # type: [CustomerTaxId]
        

    @property
    def full_name(self):
        """
        The customer name for the profile and invoice. Billing saves a trimmed nonblank value. Omitted, null, or blank preserves the saved name.
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
    @property
    def billing_address(self):
        """Gets the billing_address of this BillingCustomerDetails.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value
    @property
    def shipping_address(self):
        """Gets the shipping_address of this BillingCustomerDetails.
        
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def customer_type(self):
        """
        The customer profile type: C is consumer and B is business. New customers start as C. Omitted or null preserves the stored type.
        """
        return self.__customer_type

    @customer_type.setter
    def customer_type(self, value):
        self.__customer_type = value
    @property
    def business_name(self):
        """
        The business name for profile and invoice. Omitted or null preserves it. Type B requires a nonblank name if none is saved. A supplied blank name is invalid for type B.
        """
        return self.__business_name

    @business_name.setter
    def business_name(self, value):
        self.__business_name = value
    @property
    def business_address(self):
        """Gets the business_address of this BillingCustomerDetails.
        
        """
        return self.__business_address

    @business_address.setter
    def business_address(self, value):
        self.__business_address = value
    @property
    def tax_ids(self):
        """
        Billing tax registrations for eligible B2B invoices. A supplied list replaces saved IDs; [] clears them. Omitted or null preserves them.
        """
        return self.__tax_ids

    @tax_ids.setter
    def tax_ids(self, value):
        self.__tax_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "full_name") and self.full_name is not None:
            params['fullName'] = self.full_name
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "customer_type") and self.customer_type is not None:
            params['customerType'] = self.customer_type
        if hasattr(self, "business_name") and self.business_name is not None:
            params['businessName'] = self.business_name
        if hasattr(self, "business_address") and self.business_address is not None:
            params['businessAddress'] = self.business_address
        if hasattr(self, "tax_ids") and self.tax_ids is not None:
            params['taxIds'] = self.tax_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'fullName' in response_body:
            self.__full_name = response_body['fullName']
        if 'billingAddress' in response_body:
            self.__billing_address = CustomerAddress()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'shippingAddress' in response_body:
            self.__shipping_address = CustomerAddress()
            self.__shipping_address.parse_rsp_body(response_body['shippingAddress'])
        if 'customerType' in response_body:
            self.__customer_type = response_body['customerType']
        if 'businessName' in response_body:
            self.__business_name = response_body['businessName']
        if 'businessAddress' in response_body:
            self.__business_address = CustomerAddress()
            self.__business_address.parse_rsp_body(response_body['businessAddress'])
        if 'taxIds' in response_body:
            self.__tax_ids = []
            for item in response_body['taxIds']:
                obj = CustomerTaxId()
                obj.parse_rsp_body(item)
                self.__tax_ids.append(obj)
