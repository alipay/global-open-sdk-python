import json




class AlipayVaultingSessionRequestPaymentMethodMetaData:
    def __init__(self):
        
        self.__recurring_type = None  # type: str
        

    @property
    def recurring_type(self):
        """
        The recurring type for the vaulting session. Valid values are SCHEDULED for a fixed billing cycle and UNSCHEDULED for on-demand billing.
        """
        return self.__recurring_type

    @recurring_type.setter
    def recurring_type(self, value):
        self.__recurring_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "recurring_type") and self.recurring_type is not None:
            params['recurringType'] = self.recurring_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'recurringType' in response_body:
            self.__recurring_type = response_body['recurringType']
