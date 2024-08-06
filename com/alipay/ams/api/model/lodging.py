from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.user_name import UserName


class Lodging(object):
    def __init__(self):
        self.__hotel_name = None
        self.__hotel_address = None  # type: Address
        self.__check_in_date = None
        self.__check_out_date = None
        self.__number_of_nights = None
        self.__number_of_rooms = None
        self.__guest_names = None  # type: list[UserName]

    @property
    def hotel_name(self):
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self.__hotel_name = value

    @property
    def hotel_address(self):
        return self.__hotel_address

    @hotel_address.setter
    def hotel_address(self, value):
        self.__hotel_address = value

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value

    @property
    def number_of_nights(self):
        return self

    @number_of_nights.setter
    def number_of_nights(self, value):
        self.__number_of_nights = value

    @property
    def number_of_rooms(self):
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self.__number_of_rooms = value

    @property
    def guest_names(self):
        return self.__guest_names

    @guest_names.setter
    def guest_names(self, value):
        self.__guest_names = value

    def to_ams_dict(self):
        params = dict()

        if hasattr(self, "hotel_name") and self.hotel_name:
            params['hotelName'] = self.hotel_name

        if hasattr(self, "hotel_address") and self.hotel_address:
            params['hotelAddress'] = self.hotel_address.to_ams_dict()

        if hasattr(self, "check_in_date") and self.check_in_date:
            params['checkInDate'] = self.check_in_date

        if hasattr(self, "check_out_date") and self.check_out_date:
            params['checkOutDate'] = self.check_out_date

        if hasattr(self, "number_of_nights") and self.number_of_nights:
            params['numberOfNights'] = self.number_of_nights

        if hasattr(self, "number_of_rooms") and self.number_of_rooms:
            params['numberOfRooms'] = self.number_of_rooms

        if hasattr(self, "guest_names") and self.guest_names:
            params['guestNames'] = [guest_name.to_ams_dict() for guest_name in self.guest_names]

        return params
