import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.passenger_id_type import PassengerIdType




class Passenger:
    def __init__(self):
        
        self.__passenger_name = None  # type: UserName
        self.__passenger_email = None  # type: str
        self.__passenger_phone_no = None  # type: str
        self.__passenger_id = None  # type: str
        self.__passenger_id_type = None  # type: PassengerIdType
        self.__passenger_code = None  # type: str
        

    @property
    def passenger_name(self):
        """Gets the passenger_name of this Passenger.
        
        """
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self.__passenger_name = value
    @property
    def passenger_email(self):
        """
        The email of the passenger.  More information:  Maximum length: 64 characters
        """
        return self.__passenger_email

    @passenger_email.setter
    def passenger_email(self, value):
        self.__passenger_email = value
    @property
    def passenger_phone_no(self):
        """
        The mobile phone number of the passenger.  More information:  Maximum length: 32 characters
        """
        return self.__passenger_phone_no

    @passenger_phone_no.setter
    def passenger_phone_no(self, value):
        self.__passenger_phone_no = value
    @property
    def passenger_id(self):
        """
        Passenger identification number
        """
        return self.__passenger_id

    @passenger_id.setter
    def passenger_id(self, value):
        self.__passenger_id = value
    @property
    def passenger_id_type(self):
        """Gets the passenger_id_type of this Passenger.
        
        """
        return self.__passenger_id_type

    @passenger_id_type.setter
    def passenger_id_type(self, value):
        self.__passenger_id_type = value
    @property
    def passenger_code(self):
        """
        Passenger code or reference number
        """
        return self.__passenger_code

    @passenger_code.setter
    def passenger_code(self, value):
        self.__passenger_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "passenger_name") and self.passenger_name is not None:
            params['passengerName'] = self.passenger_name
        if hasattr(self, "passenger_email") and self.passenger_email is not None:
            params['passengerEmail'] = self.passenger_email
        if hasattr(self, "passenger_phone_no") and self.passenger_phone_no is not None:
            params['passengerPhoneNo'] = self.passenger_phone_no
        if hasattr(self, "passenger_id") and self.passenger_id is not None:
            params['passengerId'] = self.passenger_id
        if hasattr(self, "passenger_id_type") and self.passenger_id_type is not None:
            params['passengerIdType'] = self.passenger_id_type
        if hasattr(self, "passenger_code") and self.passenger_code is not None:
            params['passengerCode'] = self.passenger_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'passengerName' in response_body:
            self.__passenger_name = UserName()
            self.__passenger_name.parse_rsp_body(response_body['passengerName'])
        if 'passengerEmail' in response_body:
            self.__passenger_email = response_body['passengerEmail']
        if 'passengerPhoneNo' in response_body:
            self.__passenger_phone_no = response_body['passengerPhoneNo']
        if 'passengerId' in response_body:
            self.__passenger_id = response_body['passengerId']
        if 'passengerIdType' in response_body:
            passenger_id_type_temp = PassengerIdType.value_of(response_body['passengerIdType'])
            self.__passenger_id_type = passenger_id_type_temp
        if 'passengerCode' in response_body:
            self.__passenger_code = response_body['passengerCode']
