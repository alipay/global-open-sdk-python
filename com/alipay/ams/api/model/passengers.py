class Passengers(object):
    def __init__(self):
        self.__passenger_name = None
        self.__passenger_email = None
        self.__passenger_phoneNo = None

    @property
    def passenger_name(self):
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self.__passenger_name = value

    @property
    def passenger_email(self):
        return self.__passenger_email

    @passenger_email.setter
    def passenger_email(self, value):
        self.__passenger_email = value

    @property
    def passenger_phoneNo(self):
        return self.__passenger_phoneNo

    @passenger_phoneNo.setter
    def passenger_phoneNo(self, value):
        self.__passenger_phoneNo = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "passenger_name") and self.passenger_name:
            params['passengerName'] = self.passenger_name
        if hasattr(self, "passenger_email") and self.passenger_email:
            params['passengerEmail'] = self.passenger_email
        if hasattr(self, "passenger_phoneNo") and self.passenger_phoneNo:
            params['passengerPhoneNo'] = self.passenger_phoneNo
        return params
