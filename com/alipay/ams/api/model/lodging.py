import json
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.user_name import UserName




class Lodging:
    def __init__(self):
        
        self.__hotel_name = None  # type: str
        self.__hotel_address = None  # type: Address
        self.__check_in_date = None  # type: str
        self.__check_out_date = None  # type: str
        self.__number_of_nights = None  # type: int
        self.__number_of_rooms = None  # type: int
        self.__guest_names = None  # type: [UserName]
        

    @property
    def hotel_name(self):
        """
        Hotel name.  More information:  Maximum length: 128 characters
        """
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self.__hotel_name = value
    @property
    def hotel_address(self):
        """Gets the hotel_address of this Lodging.
        
        """
        return self.__hotel_address

    @hotel_address.setter
    def hotel_address(self, value):
        self.__hotel_address = value
    @property
    def check_in_date(self):
        """
        Date on which the guest checked in. In the case of a no-show or a reservation, the scheduled arrival date.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value
    @property
    def check_out_date(self):
        """
        Date on which the guest checked out.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value
    @property
    def number_of_nights(self):
        """
        Number of rooms booked by the payer.  More information:  Value range: 1 - unlimited
        """
        return self.__number_of_nights

    @number_of_nights.setter
    def number_of_nights(self, value):
        self.__number_of_nights = value
    @property
    def number_of_rooms(self):
        """
        Number of nights booked by the payer.  More information:  Value range: 1 - unlimited
        """
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self.__number_of_rooms = value
    @property
    def guest_names(self):
        """
        Name of the guest under which the room is reserved.  More information:  Maximum size: 100 elements
        """
        return self.__guest_names

    @guest_names.setter
    def guest_names(self, value):
        self.__guest_names = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "hotel_name") and self.hotel_name is not None:
            params['hotelName'] = self.hotel_name
        if hasattr(self, "hotel_address") and self.hotel_address is not None:
            params['hotelAddress'] = self.hotel_address
        if hasattr(self, "check_in_date") and self.check_in_date is not None:
            params['checkInDate'] = self.check_in_date
        if hasattr(self, "check_out_date") and self.check_out_date is not None:
            params['checkOutDate'] = self.check_out_date
        if hasattr(self, "number_of_nights") and self.number_of_nights is not None:
            params['numberOfNights'] = self.number_of_nights
        if hasattr(self, "number_of_rooms") and self.number_of_rooms is not None:
            params['numberOfRooms'] = self.number_of_rooms
        if hasattr(self, "guest_names") and self.guest_names is not None:
            params['guestNames'] = self.guest_names
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'hotelName' in response_body:
            self.__hotel_name = response_body['hotelName']
        if 'hotelAddress' in response_body:
            self.__hotel_address = Address()
            self.__hotel_address.parse_rsp_body(response_body['hotelAddress'])
        if 'checkInDate' in response_body:
            self.__check_in_date = response_body['checkInDate']
        if 'checkOutDate' in response_body:
            self.__check_out_date = response_body['checkOutDate']
        if 'numberOfNights' in response_body:
            self.__number_of_nights = response_body['numberOfNights']
        if 'numberOfRooms' in response_body:
            self.__number_of_rooms = response_body['numberOfRooms']
        if 'guestNames' in response_body:
            self.__guest_names = []
            for item in response_body['guestNames']:
                obj = UserName()
                obj.parse_rsp_body(item)
                self.__guest_names.append(obj)
