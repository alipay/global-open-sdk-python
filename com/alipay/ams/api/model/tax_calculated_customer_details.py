import json
from com.alipay.ams.api.model.tax_calculated_business_details import TaxCalculatedBusinessDetails
from com.alipay.ams.api.model.tax_calculated_address import TaxCalculatedAddress
from com.alipay.ams.api.model.tax_calculated_address import TaxCalculatedAddress
from com.alipay.ams.api.model.tax_calculated_tax_id import TaxCalculatedTaxId
from com.alipay.ams.api.model.tax_calculated_exemption import TaxCalculatedExemption




class TaxCalculatedCustomerDetails:
    def __init__(self):
        
        self.__business_details = None  # type: TaxCalculatedBusinessDetails
        self.__shipping_address = None  # type: TaxCalculatedAddress
        self.__billing_address = None  # type: TaxCalculatedAddress
        self.__tax_ids = None  # type: [TaxCalculatedTaxId]
        self.__tax_exemptions = None  # type: [TaxCalculatedExemption]
        

    @property
    def business_details(self):
        """Gets the business_details of this TaxCalculatedCustomerDetails.
        
        """
        return self.__business_details

    @business_details.setter
    def business_details(self, value):
        self.__business_details = value
    @property
    def shipping_address(self):
        """Gets the shipping_address of this TaxCalculatedCustomerDetails.
        
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def billing_address(self):
        """Gets the billing_address of this TaxCalculatedCustomerDetails.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value
    @property
    def tax_ids(self):
        """
        The effective customer tax ID list. Maximum size: 10.
        """
        return self.__tax_ids

    @tax_ids.setter
    def tax_ids(self, value):
        self.__tax_ids = value
    @property
    def tax_exemptions(self):
        """
        The effective customer tax exemption list. Maximum size: 10.
        """
        return self.__tax_exemptions

    @tax_exemptions.setter
    def tax_exemptions(self, value):
        self.__tax_exemptions = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "business_details") and self.business_details is not None:
            params['businessDetails'] = self.business_details
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "tax_ids") and self.tax_ids is not None:
            params['taxIds'] = self.tax_ids
        if hasattr(self, "tax_exemptions") and self.tax_exemptions is not None:
            params['taxExemptions'] = self.tax_exemptions
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'businessDetails' in response_body:
            self.__business_details = TaxCalculatedBusinessDetails()
            self.__business_details.parse_rsp_body(response_body['businessDetails'])
        if 'shippingAddress' in response_body:
            self.__shipping_address = TaxCalculatedAddress()
            self.__shipping_address.parse_rsp_body(response_body['shippingAddress'])
        if 'billingAddress' in response_body:
            self.__billing_address = TaxCalculatedAddress()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'taxIds' in response_body:
            self.__tax_ids = []
            for item in response_body['taxIds']:
                obj = TaxCalculatedTaxId()
                obj.parse_rsp_body(item)
                self.__tax_ids.append(obj)
        if 'taxExemptions' in response_body:
            self.__tax_exemptions = []
            for item in response_body['taxExemptions']:
                obj = TaxCalculatedExemption()
                obj.parse_rsp_body(item)
                self.__tax_exemptions.append(obj)
