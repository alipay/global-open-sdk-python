from com.alipay.ams.api.model.transit_type import TransitType


class Transit:

    def __init__(self):
        self.__transit_type = None  # type: TransitType
        self.__legs = None
        self.__passengers = None

    @property
    def transit_type(self):
        return self.__transit_type

    @transit_type.setter
    def transit_type(self, value):
        self.__transit_type = value

    @property
    def legs(self):
        return self.__legs

    @legs.setter
    def legs(self, value):
        self.__legs = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transit_type") and self.transit_type:
            params['transitType'] = self.transit_type

        if hasattr(self, "legs") and self.legs:
            params['legs'] = self.legs

        if hasattr(self, "passengers") and self.passengers:
            params['passengers'] = self.passengers

        return params
