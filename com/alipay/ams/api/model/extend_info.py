from com.alipay.ams.api.model.china_extra_trans_info import ChinaExtraTransInfo


class ExtendInfo(object):
    def __init__(self):
        self.__china_extra_trans_info = None  # type:ChinaExtraTransInfo

    @property
    def china_extra_trans_info(self):
        return self.__china_extra_trans_info

    @china_extra_trans_info.setter
    def china_extra_trans_info(self, value):
        self.__china_extra_trans_info = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "china_extra_trans_info") and self.china_extra_trans_info:
            params['chinaExtraTransInfo'] = self.china_extra_trans_info

        return params
