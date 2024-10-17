
class Contact:
    def __init__(self):
        self.__type = None
        self.__info = None

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_info(self, info):
        self.__info = info

    def get_info(self):
        return self.__info

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'type') and self.__type:
            params['type'] = self.__type

        if hasattr(self, 'info') and self.__info:
            params['info'] = self.__info

        return params