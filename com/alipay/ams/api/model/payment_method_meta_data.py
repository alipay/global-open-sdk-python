import json




class PaymentMethodMetaData:
    def __init__(self):
        
        self.__recurring_type = None  # type: str
        

    @property
    def recurring_type(self):
        """
        The recurring type of subsequent deductions on the vaulted card: SCHEDULED for fixed-schedule deductions or UNSCHEDULED for on-demand deductions. Optional; if omitted, no recurring type is declared, and any other value returns PARAM_ILLEGAL.
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
