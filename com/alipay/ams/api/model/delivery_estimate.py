from com.alipay.ams.api.model.delivery_estimate_info import DeliveryEstimateInfo


class DeliveryEstimate(object):
    def __init__(self):
        self.__minimum = None #type: DeliveryEstimateInfo
        self.__maximum = None #type: DeliveryEstimateInfo


    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, value):
        self.__minimum = value


    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, value):
        self.__maximum = value


    def to_ams_dict(self):
        params = dict()
        if self.minimum is not None:
            params['minimum'] = self.minimum.to_ams_dict()
        if self.maximum is not None:
            params['maximum'] = self.maximum.to_ams_dict()