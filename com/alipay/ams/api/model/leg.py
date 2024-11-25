class Leg(object):

    def __init__(self):
        self.__departure_time = None
        self.__arrival_time = None
        self.__departure_address = None
        self.__arrival_address = None
        self.__carrier_name = None
        self.__carrier_no = None
        self.__class_type = None
        self.__departure_airport_code = None
        self.__arrival_airport_code = None

    @property
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property
    def arrival_time(self):
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value

    @property
    def departure_address(self):
        return self.__departure_address

    @departure_address.setter
    def departure_address(self, value):
        self.__departure_address = value

    @property
    def arrival_address(self):
        return self.__arrival_address

    @arrival_address.setter
    def arrival_address(self, value):
        self.__arrival_address = value

    @property
    def carrier_name(self):
        return self.__carrier_name

    @carrier_name.setter
    def carrier_name(self, value):
        self.__carrier_name = value

    @property
    def carrier_no(self):
        return self.__carrier_no

    @carrier_no.setter
    def carrier_no(self, value):
        self.__carrier_no = value

    @property
    def classs_type(self):
        return self.__classs_type

    @classs_type.setter
    def classs_type(self, value):
        self.__classs_type = value

    @property
    def departure_airport_code(self):
        return self.__departure_airport_code

    @departure_airport_code.setter
    def departure_airport_code(self, value):
        self.__departure_airport_code = value

    @property
    def arrival_airport_code(self):
        return self.__arrival_airport_code

    @arrival_airport_code.setter
    def arrival_airport_code(self, value):
        self.__arrival_airport_code = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "departure_time") and self.departure_time:
            params['departureTime'] = self.departure_time

        if hasattr(self, "arrival_time") and self.arrival_time:
            params['arrivalTime'] = self.arrival_time

        if hasattr(self, "departure_address") and self.departure_address:
            params['departureAddress'] = self.departure_address.to_ams_dict()

        if hasattr(self, "arrival_address") and self.arrival_address:
            params['arrivalAddress'] = self.arrival_address.to_ams_dict()

        if hasattr(self, "carrier_name") and self.carrier_name:
            params['carrierName'] = self.carrier_name

        if hasattr(self, "carrier_no") and self.carrier_no:
            params['carrierNo'] = self.carrier_no

        if hasattr(self, "classs_type") and self.classs_type:
            params['classType'] = self.classs_type

        if hasattr(self, "departure_airport_code") and self.departure_airport_code:
            params['departureAirportCode'] = self.departure_airport_code

        if hasattr(self, "arrival_airport_code") and self.arrival_airport_code:
            params['arrivalAirportCode'] = self.arrival_airport_code

        return params
