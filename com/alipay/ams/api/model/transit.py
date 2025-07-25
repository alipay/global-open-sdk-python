import json
from com.alipay.ams.api.model.transit_type import TransitType
from com.alipay.ams.api.model.leg import Leg
from com.alipay.ams.api.model.passenger import Passenger




class Transit:
    def __init__(self):
        
        self.__transit_type = None  # type: TransitType
        self.__legs = None  # type: [Leg]
        self.__passengers = None  # type: [Passenger]
        

    @property
    def transit_type(self):
        """Gets the transit_type of this Transit.
        
        """
        return self.__transit_type

    @transit_type.setter
    def transit_type(self, value):
        self.__transit_type = value
    @property
    def legs(self):
        """
        Information about sections of the trip, including departure time, arrival time, departure address, arrival address, transportation company name, carrier code and service type.  More information:  Maximum size: 10 elements
        """
        return self.__legs

    @legs.setter
    def legs(self, value):
        self.__legs = value
    @property
    def passengers(self):
        """
        Information about the passenger of the trip, including the passenger names, passenger email and phone number.  More information:  Maximum size: 100 elements
        """
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transit_type") and self.transit_type is not None:
            params['transitType'] = self.transit_type
        if hasattr(self, "legs") and self.legs is not None:
            params['legs'] = self.legs
        if hasattr(self, "passengers") and self.passengers is not None:
            params['passengers'] = self.passengers
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transitType' in response_body:
            transit_type_temp = TransitType.value_of(response_body['transitType'])
            self.__transit_type = transit_type_temp
        if 'legs' in response_body:
            self.__legs = []
            for item in response_body['legs']:
                obj = Leg()
                obj.parse_rsp_body(item)
                self.__legs.append(obj)
        if 'passengers' in response_body:
            self.__passengers = []
            for item in response_body['passengers']:
                obj = Passenger()
                obj.parse_rsp_body(item)
                self.__passengers.append(obj)
