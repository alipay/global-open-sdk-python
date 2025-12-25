class FailReason:
    def __init__(self, fail_reason_dict):
        self.__error_code = None
        self.__error_desc = None
        self.__parse_fail_reason(fail_reason_dict)

    def __parse_fail_reason(self, fr_dict):
        if not isinstance(fr_dict, dict):
            return
        if "errorCode" in fr_dict:
            self.__error_code = fr_dict["errorCode"]
        if "errorDesc" in fr_dict:
            self.__error_desc = fr_dict["errorDesc"]

    @property
    def error_code(self):
        return self.__error_code

    @property
    def error_desc(self):
        return self.__error_desc
