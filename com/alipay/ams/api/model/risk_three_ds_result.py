import json




class RiskThreeDSResult:
    def __init__(self):
        
        self.__three_ds_version = None  # type: str
        self.__three_ds_interaction_mode = None  # type: str
        self.__eci = None  # type: str
        self.__cavv = None  # type: str
        

    @property
    def three_ds_version(self):
        """
        The version of 3D Secure protocol
        """
        return self.__three_ds_version

    @three_ds_version.setter
    def three_ds_version(self, value):
        self.__three_ds_version = value
    @property
    def three_ds_interaction_mode(self):
        """
        Indicates the type of user interactions during 3DS 2.0 authentication
        """
        return self.__three_ds_interaction_mode

    @three_ds_interaction_mode.setter
    def three_ds_interaction_mode(self, value):
        self.__three_ds_interaction_mode = value
    @property
    def eci(self):
        """
        Electronic Commerce Indicator (ECI) that is returned by the card scheme
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value
    @property
    def cavv(self):
        """
        The cardholder authentication value
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "three_ds_version") and self.three_ds_version is not None:
            params['threeDSVersion'] = self.three_ds_version
        if hasattr(self, "three_ds_interaction_mode") and self.three_ds_interaction_mode is not None:
            params['threeDSInteractionMode'] = self.three_ds_interaction_mode
        if hasattr(self, "eci") and self.eci is not None:
            params['eci'] = self.eci
        if hasattr(self, "cavv") and self.cavv is not None:
            params['cavv'] = self.cavv
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'threeDSVersion' in response_body:
            self.__three_ds_version = response_body['threeDSVersion']
        if 'threeDSInteractionMode' in response_body:
            self.__three_ds_interaction_mode = response_body['threeDSInteractionMode']
        if 'eci' in response_body:
            self.__eci = response_body['eci']
        if 'cavv' in response_body:
            self.__cavv = response_body['cavv']
