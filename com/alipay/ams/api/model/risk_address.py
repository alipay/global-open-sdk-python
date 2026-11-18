import json




class RiskAddress:
    def __init__(self):
        
        self.__shipping_phone_type = None  # type: str
        self.__is_bill_ship_state_same = None  # type: bool
        self.__is_previous_state_same = None  # type: bool
        self.__loc_to_ship_distance = None  # type: int
        self.__min_previous_ship_to_bill_distance = None  # type: int
        

    @property
    def shipping_phone_type(self):
        """
        The type of the receiver&#39;s phone number
        """
        return self.__shipping_phone_type

    @shipping_phone_type.setter
    def shipping_phone_type(self, value):
        self.__shipping_phone_type = value
    @property
    def is_bill_ship_state_same(self):
        """
        Indicates whether the billing state is the same as the shipping state
        """
        return self.__is_bill_ship_state_same

    @is_bill_ship_state_same.setter
    def is_bill_ship_state_same(self, value):
        self.__is_bill_ship_state_same = value
    @property
    def is_previous_state_same(self):
        """
        Indicates whether a previous billing state is the same as the shipping state
        """
        return self.__is_previous_state_same

    @is_previous_state_same.setter
    def is_previous_state_same(self, value):
        self.__is_previous_state_same = value
    @property
    def loc_to_ship_distance(self):
        """
        The distance in meters between the buyer&#39;s location and their shipping address.
        """
        return self.__loc_to_ship_distance

    @loc_to_ship_distance.setter
    def loc_to_ship_distance(self, value):
        self.__loc_to_ship_distance = value
    @property
    def min_previous_ship_to_bill_distance(self):
        """
        The minimum distance in meters between the buyer&#39;s previous shipping address and their billing address.
        """
        return self.__min_previous_ship_to_bill_distance

    @min_previous_ship_to_bill_distance.setter
    def min_previous_ship_to_bill_distance(self, value):
        self.__min_previous_ship_to_bill_distance = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "shipping_phone_type") and self.shipping_phone_type is not None:
            params['shippingPhoneType'] = self.shipping_phone_type
        if hasattr(self, "is_bill_ship_state_same") and self.is_bill_ship_state_same is not None:
            params['isBillShipStateSame'] = self.is_bill_ship_state_same
        if hasattr(self, "is_previous_state_same") and self.is_previous_state_same is not None:
            params['isPreviousStateSame'] = self.is_previous_state_same
        if hasattr(self, "loc_to_ship_distance") and self.loc_to_ship_distance is not None:
            params['locToShipDistance'] = self.loc_to_ship_distance
        if hasattr(self, "min_previous_ship_to_bill_distance") and self.min_previous_ship_to_bill_distance is not None:
            params['minPreviousShipToBillDistance'] = self.min_previous_ship_to_bill_distance
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'shippingPhoneType' in response_body:
            self.__shipping_phone_type = response_body['shippingPhoneType']
        if 'isBillShipStateSame' in response_body:
            self.__is_bill_ship_state_same = response_body['isBillShipStateSame']
        if 'isPreviousStateSame' in response_body:
            self.__is_previous_state_same = response_body['isPreviousStateSame']
        if 'locToShipDistance' in response_body:
            self.__loc_to_ship_distance = response_body['locToShipDistance']
        if 'minPreviousShipToBillDistance' in response_body:
            self.__min_previous_ship_to_bill_distance = response_body['minPreviousShipToBillDistance']
