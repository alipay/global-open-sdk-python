import json
from com.alipay.ams.api.model.tax_calculation_line_item import TaxCalculationLineItem
from com.alipay.ams.api.model.tax_customer_details import TaxCustomerDetails
from com.alipay.ams.api.model.tax_ship_from_details import TaxShipFromDetails
from com.alipay.ams.api.model.tax_shipping_cost import TaxShippingCost



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxCalculateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxCalculateRequest, self).__init__("/ams/api/v1/tax/calculate") 

        self.__tax_calculation_request_id = None  # type: str
        self.__currency = None  # type: str
        self.__line_items = None  # type: [TaxCalculationLineItem]
        self.__customer_id = None  # type: str
        self.__customer_details = None  # type: TaxCustomerDetails
        self.__ship_from_details = None  # type: TaxShipFromDetails
        self.__shipping_cost = None  # type: TaxShippingCost
        self.__tax_date = None  # type: str
        

    @property
    def tax_calculation_request_id(self):
        """
        The unique ID assigned by a merchant to identify a tax calculation request. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__tax_calculation_request_id

    @tax_calculation_request_id.setter
    def tax_calculation_request_id(self, value):
        self.__tax_calculation_request_id = value
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
    def line_items(self):
        """
        The line item list.
        """
        return self.__line_items

    @line_items.setter
    def line_items(self, value):
        self.__line_items = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_details(self):
        """Gets the customer_details of this AlipayTaxCalculateRequest.
        
        """
        return self.__customer_details

    @customer_details.setter
    def customer_details(self, value):
        self.__customer_details = value
    @property
    def ship_from_details(self):
        """Gets the ship_from_details of this AlipayTaxCalculateRequest.
        
        """
        return self.__ship_from_details

    @ship_from_details.setter
    def ship_from_details(self, value):
        self.__ship_from_details = value
    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this AlipayTaxCalculateRequest.
        
        """
        return self.__shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, value):
        self.__shipping_cost = value
    @property
    def tax_date(self):
        """
        The tax date. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__tax_date

    @tax_date.setter
    def tax_date(self, value):
        self.__tax_date = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "tax_calculation_request_id") and self.tax_calculation_request_id is not None:
            params['taxCalculationRequestId'] = self.tax_calculation_request_id
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "line_items") and self.line_items is not None:
            params['lineItems'] = self.line_items
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_details") and self.customer_details is not None:
            params['customerDetails'] = self.customer_details
        if hasattr(self, "ship_from_details") and self.ship_from_details is not None:
            params['shipFromDetails'] = self.ship_from_details
        if hasattr(self, "shipping_cost") and self.shipping_cost is not None:
            params['shippingCost'] = self.shipping_cost
        if hasattr(self, "tax_date") and self.tax_date is not None:
            params['taxDate'] = self.tax_date
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'taxCalculationRequestId' in response_body:
            self.__tax_calculation_request_id = response_body['taxCalculationRequestId']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'lineItems' in response_body:
            self.__line_items = []
            for item in response_body['lineItems']:
                obj = TaxCalculationLineItem()
                obj.parse_rsp_body(item)
                self.__line_items.append(obj)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerDetails' in response_body:
            self.__customer_details = TaxCustomerDetails()
            self.__customer_details.parse_rsp_body(response_body['customerDetails'])
        if 'shipFromDetails' in response_body:
            self.__ship_from_details = TaxShipFromDetails()
            self.__ship_from_details.parse_rsp_body(response_body['shipFromDetails'])
        if 'shippingCost' in response_body:
            self.__shipping_cost = TaxShippingCost()
            self.__shipping_cost.parse_rsp_body(response_body['shippingCost'])
        if 'taxDate' in response_body:
            self.__tax_date = response_body['taxDate']
