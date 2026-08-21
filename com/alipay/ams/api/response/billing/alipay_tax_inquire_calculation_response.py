import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.tax_calculated_customer_details import TaxCalculatedCustomerDetails
from com.alipay.ams.api.model.tax_calculated_ship_from_details import TaxCalculatedShipFromDetails
from com.alipay.ams.api.model.tax_calculated_line_item import TaxCalculatedLineItem
from com.alipay.ams.api.model.tax_breakdown import TaxBreakdown
from com.alipay.ams.api.model.tax_calculated_shipping_cost import TaxCalculatedShippingCost



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayTaxInquireCalculationResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__tax_calculation_id = None  # type: str
        self.__currency = None  # type: str
        self.__customer_details = None  # type: TaxCalculatedCustomerDetails
        self.__ship_from_details = None  # type: TaxCalculatedShipFromDetails
        self.__total_amount = None  # type: str
        self.__exclusive_tax_amount = None  # type: str
        self.__inclusive_tax_amount = None  # type: str
        self.__line_items = None  # type: [TaxCalculatedLineItem]
        self.__tax_breakdown = None  # type: [TaxBreakdown]
        self.__expire_at = None  # type: str
        self.__tax_date = None  # type: str
        self.__shipping_cost = None  # type: TaxCalculatedShippingCost
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayTaxInquireCalculationResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def tax_calculation_id(self):
        """
        The unique ID assigned by Antom to identify a tax calculation. Maximum length: 64 characters.
        """
        return self.__tax_calculation_id

    @tax_calculation_id.setter
    def tax_calculation_id(self, value):
        self.__tax_calculation_id = value
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
    def customer_details(self):
        """Gets the customer_details of this AlipayTaxInquireCalculationResponse.
        
        """
        return self.__customer_details

    @customer_details.setter
    def customer_details(self, value):
        self.__customer_details = value
    @property
    def ship_from_details(self):
        """Gets the ship_from_details of this AlipayTaxInquireCalculationResponse.
        
        """
        return self.__ship_from_details

    @ship_from_details.setter
    def ship_from_details(self, value):
        self.__ship_from_details = value
    @property
    def total_amount(self):
        """
        The total amount. Maximum length: 19 characters.
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def exclusive_tax_amount(self):
        """
        The exclusive tax amount. Maximum length: 19 characters. Note: See documentation for details.
        """
        return self.__exclusive_tax_amount

    @exclusive_tax_amount.setter
    def exclusive_tax_amount(self, value):
        self.__exclusive_tax_amount = value
    @property
    def inclusive_tax_amount(self):
        """
        The inclusive tax amount. Maximum length: 19 characters. Note: See documentation for details.
        """
        return self.__inclusive_tax_amount

    @inclusive_tax_amount.setter
    def inclusive_tax_amount(self, value):
        self.__inclusive_tax_amount = value
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
    def tax_breakdown(self):
        """
        The tax breakdown.
        """
        return self.__tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, value):
        self.__tax_breakdown = value
    @property
    def expire_at(self):
        """
        The expiration time. Maximum length: 32 characters.
        """
        return self.__expire_at

    @expire_at.setter
    def expire_at(self, value):
        self.__expire_at = value
    @property
    def tax_date(self):
        """
        The tax date. Maximum length: 32 characters.
        """
        return self.__tax_date

    @tax_date.setter
    def tax_date(self, value):
        self.__tax_date = value
    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this AlipayTaxInquireCalculationResponse.
        
        """
        return self.__shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, value):
        self.__shipping_cost = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "tax_calculation_id") and self.tax_calculation_id is not None:
            params['taxCalculationId'] = self.tax_calculation_id
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "customer_details") and self.customer_details is not None:
            params['customerDetails'] = self.customer_details
        if hasattr(self, "ship_from_details") and self.ship_from_details is not None:
            params['shipFromDetails'] = self.ship_from_details
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "exclusive_tax_amount") and self.exclusive_tax_amount is not None:
            params['exclusiveTaxAmount'] = self.exclusive_tax_amount
        if hasattr(self, "inclusive_tax_amount") and self.inclusive_tax_amount is not None:
            params['inclusiveTaxAmount'] = self.inclusive_tax_amount
        if hasattr(self, "line_items") and self.line_items is not None:
            params['lineItems'] = self.line_items
        if hasattr(self, "tax_breakdown") and self.tax_breakdown is not None:
            params['taxBreakdown'] = self.tax_breakdown
        if hasattr(self, "expire_at") and self.expire_at is not None:
            params['expireAt'] = self.expire_at
        if hasattr(self, "tax_date") and self.tax_date is not None:
            params['taxDate'] = self.tax_date
        if hasattr(self, "shipping_cost") and self.shipping_cost is not None:
            params['shippingCost'] = self.shipping_cost
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayTaxInquireCalculationResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'taxCalculationId' in response_body:
            self.__tax_calculation_id = response_body['taxCalculationId']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'customerDetails' in response_body:
            self.__customer_details = TaxCalculatedCustomerDetails()
            self.__customer_details.parse_rsp_body(response_body['customerDetails'])
        if 'shipFromDetails' in response_body:
            self.__ship_from_details = TaxCalculatedShipFromDetails()
            self.__ship_from_details.parse_rsp_body(response_body['shipFromDetails'])
        if 'totalAmount' in response_body:
            self.__total_amount = response_body['totalAmount']
        if 'exclusiveTaxAmount' in response_body:
            self.__exclusive_tax_amount = response_body['exclusiveTaxAmount']
        if 'inclusiveTaxAmount' in response_body:
            self.__inclusive_tax_amount = response_body['inclusiveTaxAmount']
        if 'lineItems' in response_body:
            self.__line_items = []
            for item in response_body['lineItems']:
                obj = TaxCalculatedLineItem()
                obj.parse_rsp_body(item)
                self.__line_items.append(obj)
        if 'taxBreakdown' in response_body:
            self.__tax_breakdown = []
            for item in response_body['taxBreakdown']:
                obj = TaxBreakdown()
                obj.parse_rsp_body(item)
                self.__tax_breakdown.append(obj)
        if 'expireAt' in response_body:
            self.__expire_at = response_body['expireAt']
        if 'taxDate' in response_body:
            self.__tax_date = response_body['taxDate']
        if 'shippingCost' in response_body:
            self.__shipping_cost = TaxCalculatedShippingCost()
            self.__shipping_cost.parse_rsp_body(response_body['shippingCost'])
