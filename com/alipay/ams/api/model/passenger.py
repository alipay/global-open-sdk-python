import json
from com.alipay.ams.api.model.user_name import UserName




class Passenger:
    def __init__(self):
        
        self.__passenger_name = None  # type: UserName
        self.__passenger_email = None  # type: str
        self.__passenger_phone_no = None  # type: str
        

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
        """Gets the passenger_email of this Passenger.
        
        """
        return self.__passenger_email

    @passenger_email.setter
    def passenger_email(self, value):
        self.__passenger_email = value
    @property
    def passenger_phone_no(self):
        """Gets the passenger_phone_no of this Passenger.
        
        """
        return self.__passenger_phone_no

    @passenger_phone_no.setter
    def passenger_phone_no(self, value):
        self.__passenger_phone_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "passenger_name") and self.passenger_name is not None:
            params['passengerName'] = self.passenger_name
        if hasattr(self, "passenger_email") and self.passenger_email is not None:
            params['passengerEmail'] = self.passenger_email
        if hasattr(self, "passenger_phone_no") and self.passenger_phone_no is not None:
            params['passengerPhoneNo'] = self.passenger_phone_no
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
