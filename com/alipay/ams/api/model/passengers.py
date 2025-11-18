from com.alipay.ams.api.model.passenger_id_type import PassengerIdType


class Passengers(object):
    def __init__(self):
        self.__passenger_name = None
        self.__passenger_email = None
        self.__passenger_phoneNo = None
        self.__passenger_id = None
        self.__passenger_id_type = None  # type: PassengerIdType
        self.__passenger_code = None

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

    @property
    def passenger_id(self):
        return self.__passenger_id

    @passenger_id.setter
    def passenger_id(self, value):
        self.__passenger_id = value

    @property
    def passenger_id_type(self):
        return self.__passenger_id_type

    @passenger_id_type.setter
    def passenger_id_type(self, value):
        self.__passenger_id_type = value

    @property
    def passenger_code(self):
        return self.__passenger_code

    @passenger_code.setter
    def passenger_code(self, value):
        self.__passenger_code = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "passenger_name") and self.passenger_name:
            params["passengerName"] = self.passenger_name
        if hasattr(self, "passenger_email") and self.passenger_email:
            params["passengerEmail"] = self.passenger_email
        if hasattr(self, "passenger_phoneNo") and self.passenger_phoneNo:
            params["passengerPhoneNo"] = self.passenger_phoneNo
        if hasattr(self, "passenger_id") and self.passenger_id:
            params["passengerId"] = self.passenger_id
        if hasattr(self, "passenger_id_type") and self.passenger_id_type:
            params["passengerIdType"] = self.passenger_id_type.to_ams_dict()
        if hasattr(self, "passenger_code") and self.passenger_code:
            params["passengerCode"] = self.passenger_code
        return params
