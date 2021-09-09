class Logo(object):

    def __init__(self):
        self.__logo_name = None
        self.__logo_url = None

    @property
    def logo_name(self):
        return self.__logo_name

    @logo_name.setter
    def logo_name(self, value):
        self.__logo_name = value

    @property
    def logo_url(self):
        return self.__logo_url

    @logo_url.setter
    def logo_url(self, value):
        self.__logo_url = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "logo_name") and self.logo_name:
            params['logoName'] = self.logo_name

        if hasattr(self, "logo_url") and self.logo_url:
            params['logoUrl'] = self.logo_url

        return params
