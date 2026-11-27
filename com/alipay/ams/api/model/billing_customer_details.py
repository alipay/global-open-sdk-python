import json
from com.alipay.ams.api.model.billing_customer_address import BillingCustomerAddress
from com.alipay.ams.api.model.billing_customer_address import BillingCustomerAddress
from com.alipay.ams.api.model.billing_customer_address import BillingCustomerAddress
from com.alipay.ams.api.model.billing_customer_tax_id import BillingCustomerTaxId




class BillingCustomerDetails:
    def __init__(self):
        
        self.__full_name = None  # type: str
        self.__customer_type = None  # type: str
        self.__business_name = None  # type: str
        self.__billing_address = None  # type: BillingCustomerAddress
        self.__shipping_address = None  # type: BillingCustomerAddress
        self.__business_address = None  # type: BillingCustomerAddress
        self.__tax_ids = None  # type: [BillingCustomerTaxId]
        

    @property
    def full_name(self):
        """
        Customer&#39;s name for the profile and invoice. Billing trims it. Omitted, null, or blank keeps the saved name.
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
    @property
    def customer_type(self):
        """
        Profile type. C is consumer and B is business. New customers default to C. Omitted or null keeps the saved type.
        """
        return self.__customer_type

    @customer_type.setter
    def customer_type(self, value):
        self.__customer_type = value
    @property
    def business_name(self):
        """
        Business name for profile and invoice. Omitted or null keeps it. A B profile requires a saved or supplied name; a supplied blank name is invalid for B.
        """
        return self.__business_name

    @business_name.setter
    def business_name(self, value):
        self.__business_name = value
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
        Tax registrations for profile and eligible B2B invoices. Up to 10 entries/2,000 JSON characters. Supplied list replaces saved list; [] clears it; omitted or null keeps it.
        """
        return self.__tax_ids

    @tax_ids.setter
    def tax_ids(self, value):
        self.__tax_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "full_name") and self.full_name is not None:
            params['fullName'] = self.full_name
        if hasattr(self, "customer_type") and self.customer_type is not None:
            params['customerType'] = self.customer_type
        if hasattr(self, "business_name") and self.business_name is not None:
            params['businessName'] = self.business_name
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
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
        if 'customerType' in response_body:
            self.__customer_type = response_body['customerType']
        if 'businessName' in response_body:
            self.__business_name = response_body['businessName']
        if 'billingAddress' in response_body:
            self.__billing_address = BillingCustomerAddress()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'shippingAddress' in response_body:
            self.__shipping_address = BillingCustomerAddress()
            self.__shipping_address.parse_rsp_body(response_body['shippingAddress'])
        if 'businessAddress' in response_body:
            self.__business_address = BillingCustomerAddress()
            self.__business_address.parse_rsp_body(response_body['businessAddress'])
        if 'taxIds' in response_body:
            self.__tax_ids = []
            for item in response_body['taxIds']:
                obj = BillingCustomerTaxId()
                obj.parse_rsp_body(item)
                self.__tax_ids.append(obj)
