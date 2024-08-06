from com.alipay.ams.api.model.code_detail import CodeDetail


class AuthCodeForm(object):
    def __init__(self):
        self.codeDetails = None  # type: list[CodeDetail]

    @property
    def code_details(self):
        return self.codeDetails

    @code_details.setter
    def code_details(self, value):
        self.codeDetails = value

    def to_ams_dict(self):
        params = dict()
        if self.codeDetails is not None:
            params['codeDetails'] = [item.to_ams_dict() for item in self.codeDetails]
        return params
