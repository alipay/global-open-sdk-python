class ContactInfo(object):
    def __init__(self):
        self.__contact_no = None
        self.__contact_type = None

    @property
    def contact_no(self):
        return self.__contact_no

    @contact_no.setter
    def contact_no(self, value):
        self.__contact_no = value

    @property
    def contact_type(self):
        return self.__contact_type

    @contact_type.setter
    def contact_type(self, value):
        self.__contact_type = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "contact_no") and self.contact_no:
            params["contactNo"] = self.contact_no

        if hasattr(self, "contact_type") and self.contact_type:
            params["contactType"] = self.contact_type

        return params
