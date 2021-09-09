class WebSite(object):
    def __init__(self):
        self.__name = None
        self.__url = None
        self.__desc = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "name") and self.name:
            params['name'] = self.name

        if hasattr(self, "url") and self.url:
            params['url'] = self.url

        if hasattr(self, "desc") and self.desc:
            params['desc'] = self.desc

        return params
