import json




class AutomaticTax:
    def __init__(self):
        
        self.__enabled = None  # type: bool
        

    @property
    def enabled(self):
        """
        Whether automatic tax is enabled. createPaymentSession requires an explicit value when automaticTax is supplied. For invoice/create, omission defaults to false; tax is calculated at OPEN issuance or DRAFT finalization, not DRAFT creation.
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "enabled") and self.enabled is not None:
            params['enabled'] = self.enabled
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'enabled' in response_body:
            self.__enabled = response_body['enabled']
