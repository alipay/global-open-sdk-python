from com.alipay.ams.api.model.web_site import WebSite


class BusinessInfo:
    def __init__(self):
        self.__mcc = None
        self.__websites = None #type: list[WebSite]
        self.__englishName = None
        self.__doingBusinessAs = None
        self.__mainSalesCountry = None
        self.__appName = None
        self.__serviceDescription = None

    @property
    def mcc(self):
        return self.__mcc

    @mcc.setter
    def mcc(self, value):
        self.__mcc = value

    @property
    def websites(self):
        return self.__websites

    @websites.setter
    def websites(self, value):
        self.__websites = value

    @property
    def englishName(self):
        return self.__englishName

    @englishName.setter
    def englishName(self, value):
        self.__englishName = value

    @property
    def doingBusinessAs(self):
        return self.__doingBusinessAs

    @doingBusinessAs.setter
    def doingBusinessAs(self, value):
        self.__doingBusinessAs = value

    @property
    def mainSalesCountry(self):
        return self.__mainSalesCountry

    @mainSalesCountry.setter
    def mainSalesCountry(self, value):
        self.__mainSalesCountry = value

    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, value):
        self.__appName = value

    @property
    def serviceDescription(self):
        return self.__serviceDescription

    @serviceDescription.setter
    def serviceDescription(self, value):
        self.__serviceDescription = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'mcc') and self.mcc:
            params['mcc'] = self.mcc
        if hasattr(self, 'websites') and self.websites:
            params['websites'] = []
            for i in self.websites:
                params['websites'].append(i.to_ams_dict())
        if hasattr(self, 'englishName') and self.englishName:
            params['englishName'] = self.englishName
        if hasattr(self, 'doingBusinessAs') and self.doingBusinessAs:
            params['doingBusinessAs'] = self.doingBusinessAs
        if hasattr(self, 'mainSalesCountry') and self.mainSalesCountry:
            params['mainSalesCountry'] = self.mainSalesCountry
        if hasattr(self, 'appName') and self.appName:
            params['appName'] = self.appName
        if hasattr(self, 'serviceDescription') and self.serviceDescription:
            params['serviceDescription'] = self.serviceDescription
        return params

