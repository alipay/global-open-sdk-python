import json




class PaymentMethodDetailPaymentMethodMetaData:
    def __init__(self):
        
        self.__recurring_type = None  # type: str
        

    @property
    def recurring_type(self):
        """
        The recurring type of subsequent deductions on the vaulted card, where SCHEDULED indicates fixed-schedule deductions and UNSCHEDULED indicates on-demand deductions. Only these two values are supported.
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
