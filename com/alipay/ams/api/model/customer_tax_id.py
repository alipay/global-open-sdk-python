import json




class CustomerTaxId:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__country = None  # type: str
        self.__region = None  # type: str
        self.__type = None  # type: str
        

    @property
    def value(self):
        """
        The business tax registration number for invoices and eligible tax calculation. Each supplied entry needs a non-null, nonblank value.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def country(self):
        """
        The issuing country as an ISO 3166-1 alpha-2 code. Each supplied entry needs a non-null, nonblank value.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def region(self):
        """
        The issuing subdivision as a full ISO 3166-2 code, such as US-CA. Its prefix must match country. Omission or null leaves the subdivision unspecified.
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value
    @property
    def type(self):
        """
        The tax ID display label, such as VAT or TIN. Omission or null leaves the label unspecified. The label is unused in tax calculation.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "region") and self.region is not None:
            params['region'] = self.region
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'value' in response_body:
            self.__value = response_body['value']
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'region' in response_body:
            self.__region = response_body['region']
        if 'type' in response_body:
            self.__type = response_body['type']
