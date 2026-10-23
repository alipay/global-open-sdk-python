class DisputeDefenseFile(object):
    """Metadata of a generated defense material, without its body."""

    def __init__(self):
        self.__file_name = None
        self.__file_format = None
        self.__file_md5 = None

    @property
    def file_name(self):
        """Name of the generated defense material."""
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def file_format(self):
        """Material format: PDF or WORD."""
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = value

    @property
    def file_md5(self):
        """MD5 of the material body as 32 lowercase hexadecimal characters."""
        return self.__file_md5

    @file_md5.setter
    def file_md5(self, value):
        self.__file_md5 = value
