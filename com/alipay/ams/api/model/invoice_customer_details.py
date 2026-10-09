import json
from com.alipay.ams.api.model.customer_business_address import CustomerBusinessAddress
from com.alipay.ams.api.model.buyer_tax_id import BuyerTaxId




class InvoiceCustomerDetails:
    def __init__(self):
        
        self.__email = None  # type: str
        self.__customer_type = None  # type: str
        self.__business_name = None  # type: str
        self.__first_name = None  # type: str
        self.__last_name = None  # type: str
        self.__business_address = None  # type: CustomerBusinessAddress
        self.__preferred_locales = None  # type: str
        self.__tax_ids = None  # type: [BuyerTaxId]
        

    @property
    def email(self):
        """
        Customer email for merchant/email lookup and invoice contact. Delivery uses the current billing email, otherwise account email.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def customer_type(self):
        """
        B (business) or C (consumer). If omitted, uses the matched customer type, otherwise C.
        """
        return self.__customer_type

    @customer_type.setter
    def customer_type(self, value):
        self.__customer_type = value
    @property
    def business_name(self):
        """
        Effective business name required for type B. Omitted values may come from the matched customer; its profile is not overwritten.
        """
        return self.__business_name

    @business_name.setter
    def business_name(self, value):
        self.__business_name = value
    @property
    def first_name(self):
        """
        Effective first name required for type C; may use the matched customer value when omitted. Optional contact name for type B.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        Effective last name required for type C; may use the matched customer value when omitted. Optional contact name for type B.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def business_address(self):
        """Gets the business_address of this InvoiceCustomerDetails.
        
        """
        return self.__business_address

    @business_address.setter
    def business_address(self, value):
        self.__business_address = value
    @property
    def preferred_locales(self):
        """
        Comma-separated invoice and offline receipt PDF locales, such as ja-JP,en-US. First supported locale wins, with English fallback. Does not select email language.
        """
        return self.__preferred_locales

    @preferred_locales.setter
    def preferred_locales(self, value):
        self.__preferred_locales = value
    @property
    def tax_ids(self):
        """
        Tax IDs saved for invoice and offline receipt PDF display. Omit to use stored customer IDs; an empty array suppresses display. Does not change tax calculation.
        """
        return self.__tax_ids

    @tax_ids.setter
    def tax_ids(self, value):
        self.__tax_ids = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "customer_type") and self.customer_type is not None:
            params['customerType'] = self.customer_type
        if hasattr(self, "business_name") and self.business_name is not None:
            params['businessName'] = self.business_name
        if hasattr(self, "first_name") and self.first_name is not None:
            params['firstName'] = self.first_name
        if hasattr(self, "last_name") and self.last_name is not None:
            params['lastName'] = self.last_name
        if hasattr(self, "business_address") and self.business_address is not None:
            params['businessAddress'] = self.business_address
        if hasattr(self, "preferred_locales") and self.preferred_locales is not None:
            params['preferredLocales'] = self.preferred_locales
        if hasattr(self, "tax_ids") and self.tax_ids is not None:
            params['taxIds'] = self.tax_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'customerType' in response_body:
            self.__customer_type = response_body['customerType']
        if 'businessName' in response_body:
            self.__business_name = response_body['businessName']
        if 'firstName' in response_body:
            self.__first_name = response_body['firstName']
        if 'lastName' in response_body:
            self.__last_name = response_body['lastName']
        if 'businessAddress' in response_body:
            self.__business_address = CustomerBusinessAddress()
            self.__business_address.parse_rsp_body(response_body['businessAddress'])
        if 'preferredLocales' in response_body:
            self.__preferred_locales = response_body['preferredLocales']
        if 'taxIds' in response_body:
            self.__tax_ids = []
            for item in response_body['taxIds']:
                obj = BuyerTaxId()
                obj.parse_rsp_body(item)
                self.__tax_ids.append(obj)
