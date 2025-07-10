


class DeliveryEstimateInfo(object):
    def __init__(self):
        self.__unit = None
        self.__value = None

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    def to_ams_dict(self):
        params = dict()
        if self.unit is not None:
            params['unit'] = self.unit
        if self.value is not None:
            params['value'] = self.value
        return params