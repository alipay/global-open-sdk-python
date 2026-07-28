import json
from com.alipay.ams.api.model.tax_business_details import TaxBusinessDetails
from com.alipay.ams.api.model.tax_address import TaxAddress
from com.alipay.ams.api.model.tax_address import TaxAddress
from com.alipay.ams.api.model.tax_id import TaxId




class TaxCustomerDetails:
    def __init__(self):
        
        self.__name = None  # type: str
        self.__business_details = None  # type: TaxBusinessDetails
        self.__shipping_address = None  # type: TaxAddress
        self.__billing_address = None  # type: TaxAddress
        self.__tax_ids = None  # type: [TaxId]
        

    @property
    def name(self):
        """
        The name. Maximum length: 128 characters. Note: See documentation for details.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def business_details(self):
        """Gets the business_details of this TaxCustomerDetails.
        
        """
        return self.__business_details

    @business_details.setter
    def business_details(self, value):
        self.__business_details = value
    @property
    def shipping_address(self):
        """Gets the shipping_address of this TaxCustomerDetails.
        
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def billing_address(self):
        """Gets the billing_address of this TaxCustomerDetails.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value
    @property
    def tax_ids(self):
        """
        The tax ID list. Note: See documentation for details.
        """
        return self.__tax_ids

    @tax_ids.setter
    def tax_ids(self, value):
        self.__tax_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "business_details") and self.business_details is not None:
            params['businessDetails'] = self.business_details
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "tax_ids") and self.tax_ids is not None:
            params['taxIds'] = self.tax_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'businessDetails' in response_body:
            self.__business_details = TaxBusinessDetails()
            self.__business_details.parse_rsp_body(response_body['businessDetails'])
        if 'shippingAddress' in response_body:
            self.__shipping_address = TaxAddress()
            self.__shipping_address.parse_rsp_body(response_body['shippingAddress'])
        if 'billingAddress' in response_body:
            self.__billing_address = TaxAddress()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'taxIds' in response_body:
            self.__tax_ids = []
            for item in response_body['taxIds']:
                obj = TaxId()
                obj.parse_rsp_body(item)
                self.__tax_ids.append(obj)
