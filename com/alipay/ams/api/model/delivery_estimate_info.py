import json




class DeliveryEstimateInfo:
    def __init__(self):
        
        self.__unit = None  # type: str
        self.__value = None  # type: int
        

    @property
    def unit(self):
        """
        Units for the longest shipping time of logistics services. The valid values include:  YEAR: Indicates that the shortest shipping time unit for logistics services is in years. MONTH: Indicates that the shortest shipping time unit for logistics services is in months. DAY: Indicates that the shortest shipping time unit for logistics services is in days. HOUR: Indicates that the shortest shipping time unit for logistics services is in hours. MINUTE: Indicates that the shortest shipping time unit for logistics services is in minutes. SECOND: Indicates that the shortest shipping time unit for logistics services is in seconds. More information:  Maximum length: 16 characters 
        """
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value
    @property
    def value(self):
        """
        Estimated value for the longest shipping time of logistics services.  More information:  Value range: [0, +∞)
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "unit") and self.unit is not None:
            params['unit'] = self.unit
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'unit' in response_body:
            self.__unit = response_body['unit']
        if 'value' in response_body:
            self.__value = response_body['value']
