import json
from com.alipay.ams.api.model.delivery_estimate_info import DeliveryEstimateInfo
from com.alipay.ams.api.model.delivery_estimate_info import DeliveryEstimateInfo




class DeliveryEstimate:
    def __init__(self):
        
        self.__minimum = None  # type: DeliveryEstimateInfo
        self.__maximum = None  # type: DeliveryEstimateInfo
        

    @property
    def minimum(self):
        """Gets the minimum of this DeliveryEstimate.
        
        """
        return self.__minimum

    @minimum.setter
    def minimum(self, value):
        self.__minimum = value
    @property
    def maximum(self):
        """Gets the maximum of this DeliveryEstimate.
        
        """
        return self.__maximum

    @maximum.setter
    def maximum(self, value):
        self.__maximum = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "minimum") and self.minimum is not None:
            params['minimum'] = self.minimum
        if hasattr(self, "maximum") and self.maximum is not None:
            params['maximum'] = self.maximum
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'minimum' in response_body:
            self.__minimum = DeliveryEstimateInfo()
            self.__minimum.parse_rsp_body(response_body['minimum'])
        if 'maximum' in response_body:
            self.__maximum = DeliveryEstimateInfo()
            self.__maximum.parse_rsp_body(response_body['maximum'])
