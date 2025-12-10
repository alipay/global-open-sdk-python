import json
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.class_type import ClassType




class Leg:
    def __init__(self):
        
        self.__departure_time = None  # type: str
        self.__arrival_time = None  # type: str
        self.__departure_address = None  # type: Address
        self.__arrival_address = None  # type: Address
        self.__carrier_name = None  # type: str
        self.__carrier_no = None  # type: str
        self.__class_type = None  # type: ClassType
        self.__departure_airport_code = None  # type: str
        self.__arrival_airport_code = None  # type: str
        self.__fare_basis = None  # type: str
        self.__coupon_number = None  # type: str
        self.__flight_number = None  # type: str
        

    @property
    def departure_time(self):
        """
        Time of departure for this leg of the trip.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value
    @property
    def arrival_time(self):
        """
        Time of arrival for this leg of the trip.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value
    @property
    def departure_address(self):
        """Gets the departure_address of this Leg.
        
        """
        return self.__departure_address

    @departure_address.setter
    def departure_address(self, value):
        self.__departure_address = value
    @property
    def arrival_address(self):
        """Gets the arrival_address of this Leg.
        
        """
        return self.__arrival_address

    @arrival_address.setter
    def arrival_address(self, value):
        self.__arrival_address = value
    @property
    def carrier_name(self):
        """
        Company name of the transportation service provider for this leg of the trip.  More information:  Maximum length: 128 characters
        """
        return self.__carrier_name

    @carrier_name.setter
    def carrier_name(self, value):
        self.__carrier_name = value
    @property
    def carrier_no(self):
        """
        Code for the carrier for this leg of the trip.  More information:  Maximum length: 64 characters
        """
        return self.__carrier_no

    @carrier_no.setter
    def carrier_no(self, value):
        self.__carrier_no = value
    @property
    def class_type(self):
        """Gets the class_type of this Leg.
        
        """
        return self.__class_type

    @class_type.setter
    def class_type(self, value):
        self.__class_type = value
    @property
    def departure_airport_code(self):
        """
        IATA code for the originating airport for this leg of the trip.  More information:  Maximum length: 8 characters 
        """
        return self.__departure_airport_code

    @departure_airport_code.setter
    def departure_airport_code(self, value):
        self.__departure_airport_code = value
    @property
    def arrival_airport_code(self):
        """
        IATA code for the destination airport for this leg of the trip.  More information:  Maximum length: 8 characters 
        """
        return self.__arrival_airport_code

    @arrival_airport_code.setter
    def arrival_airport_code(self, value):
        self.__arrival_airport_code = value
    @property
    def fare_basis(self):
        """
        Fare basis code for this leg of the trip.
        """
        return self.__fare_basis

    @fare_basis.setter
    def fare_basis(self, value):
        self.__fare_basis = value
    @property
    def coupon_number(self):
        """
        Coupon number associated with this leg of the trip.
        """
        return self.__coupon_number

    @coupon_number.setter
    def coupon_number(self, value):
        self.__coupon_number = value
    @property
    def flight_number(self):
        """
        Flight number for this leg of the trip.
        """
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value):
        self.__flight_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "departure_time") and self.departure_time is not None:
            params['departureTime'] = self.departure_time
        if hasattr(self, "arrival_time") and self.arrival_time is not None:
            params['arrivalTime'] = self.arrival_time
        if hasattr(self, "departure_address") and self.departure_address is not None:
            params['departureAddress'] = self.departure_address
        if hasattr(self, "arrival_address") and self.arrival_address is not None:
            params['arrivalAddress'] = self.arrival_address
        if hasattr(self, "carrier_name") and self.carrier_name is not None:
            params['carrierName'] = self.carrier_name
        if hasattr(self, "carrier_no") and self.carrier_no is not None:
            params['carrierNo'] = self.carrier_no
        if hasattr(self, "class_type") and self.class_type is not None:
            params['classType'] = self.class_type
        if hasattr(self, "departure_airport_code") and self.departure_airport_code is not None:
            params['departureAirportCode'] = self.departure_airport_code
        if hasattr(self, "arrival_airport_code") and self.arrival_airport_code is not None:
            params['arrivalAirportCode'] = self.arrival_airport_code
        if hasattr(self, "fare_basis") and self.fare_basis is not None:
            params['fareBasis'] = self.fare_basis
        if hasattr(self, "coupon_number") and self.coupon_number is not None:
            params['couponNumber'] = self.coupon_number
        if hasattr(self, "flight_number") and self.flight_number is not None:
            params['flightNumber'] = self.flight_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'departureTime' in response_body:
            self.__departure_time = response_body['departureTime']
        if 'arrivalTime' in response_body:
            self.__arrival_time = response_body['arrivalTime']
        if 'departureAddress' in response_body:
            self.__departure_address = Address()
            self.__departure_address.parse_rsp_body(response_body['departureAddress'])
        if 'arrivalAddress' in response_body:
            self.__arrival_address = Address()
            self.__arrival_address.parse_rsp_body(response_body['arrivalAddress'])
        if 'carrierName' in response_body:
            self.__carrier_name = response_body['carrierName']
        if 'carrierNo' in response_body:
            self.__carrier_no = response_body['carrierNo']
        if 'classType' in response_body:
            class_type_temp = ClassType.value_of(response_body['classType'])
            self.__class_type = class_type_temp
        if 'departureAirportCode' in response_body:
            self.__departure_airport_code = response_body['departureAirportCode']
        if 'arrivalAirportCode' in response_body:
            self.__arrival_airport_code = response_body['arrivalAirportCode']
        if 'fareBasis' in response_body:
            self.__fare_basis = response_body['fareBasis']
        if 'couponNumber' in response_body:
            self.__coupon_number = response_body['couponNumber']
        if 'flightNumber' in response_body:
            self.__flight_number = response_body['flightNumber']
