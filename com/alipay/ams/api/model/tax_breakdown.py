import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class TaxBreakdown:
    def __init__(self):
        
        self.__tax_type = None  # type: str
        self.__tax_rate = None  # type: str
        self.__tax_amount = None  # type: Amount
        self.__taxable_amount = None  # type: Amount
        self.__taxability_reason = None  # type: str
        self.__inclusive = None  # type: bool
        

    @property
    def tax_type(self):
        """
        The tax type. Supported values are CUIT, GST, VAT, CBS, IBS, HST, PST, RST, QST, JCT, SERVICE_TAX, IGV, SALES_TAX, and PERSONAL_PROPERTY_LEASE_TRANSACTION_TAX. This response field is extensible; accept unknown values without failing deserialization.
        """
        return self.__tax_type

    @tax_type.setter
    def tax_type(self, value):
        self.__tax_type = value
    @property
    def tax_rate(self):
        """
        The tax rate. Maximum length: 16 characters.
        """
        return self.__tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self.__tax_rate = value
    @property
    def tax_amount(self):
        """Gets the tax_amount of this TaxBreakdown.
        
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def taxable_amount(self):
        """Gets the taxable_amount of this TaxBreakdown.
        
        """
        return self.__taxable_amount

    @taxable_amount.setter
    def taxable_amount(self, value):
        self.__taxable_amount = value
    @property
    def taxability_reason(self):
        """
        The taxability reason. Supported values are NOT_COLLECTING, PRODUCT_EXEMPT, REVERSE_CHARGE, CUSTOMER_EXEMPT, NOT_SUPPORTED, NOT_SUBJECT_TO_TAX, PRODUCT_EXEMPT_HOLIDAY, PORTION_PRODUCT_EXEMPT, ZERO_RATED, STANDARD_RATED, and UNKNOWN_ZERO_TAX.
        """
        return self.__taxability_reason

    @taxability_reason.setter
    def taxability_reason(self, value):
        self.__taxability_reason = value
    @property
    def inclusive(self):
        """
        Indicates whether the tax is inclusive.
        """
        return self.__inclusive

    @inclusive.setter
    def inclusive(self, value):
        self.__inclusive = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "tax_type") and self.tax_type is not None:
            params['taxType'] = self.tax_type
        if hasattr(self, "tax_rate") and self.tax_rate is not None:
            params['taxRate'] = self.tax_rate
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "taxable_amount") and self.taxable_amount is not None:
            params['taxableAmount'] = self.taxable_amount
        if hasattr(self, "taxability_reason") and self.taxability_reason is not None:
            params['taxabilityReason'] = self.taxability_reason
        if hasattr(self, "inclusive") and self.inclusive is not None:
            params['inclusive'] = self.inclusive
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'taxType' in response_body:
            self.__tax_type = response_body['taxType']
        if 'taxRate' in response_body:
            self.__tax_rate = response_body['taxRate']
        if 'taxAmount' in response_body:
            self.__tax_amount = Amount()
            self.__tax_amount.parse_rsp_body(response_body['taxAmount'])
        if 'taxableAmount' in response_body:
            self.__taxable_amount = Amount()
            self.__taxable_amount.parse_rsp_body(response_body['taxableAmount'])
        if 'taxabilityReason' in response_body:
            self.__taxability_reason = response_body['taxabilityReason']
        if 'inclusive' in response_body:
            self.__inclusive = response_body['inclusive']
