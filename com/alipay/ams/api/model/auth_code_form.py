import json
from com.alipay.ams.api.model.code_detail import CodeDetail




class AuthCodeForm:
    def __init__(self):
        
        self.__code_details = None  # type: [CodeDetail]
        

    @property
    def code_details(self):
        """
        A list of QR code information.  
        """
        return self.__code_details

    @code_details.setter
    def code_details(self, value):
        self.__code_details = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "code_details") and self.code_details is not None:
            params['codeDetails'] = self.code_details
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'codeDetails' in response_body:
            self.__code_details = []
            for item in response_body['codeDetails']:
                obj = CodeDetail()
                obj.parse_rsp_body(item)
                self.__code_details.append(obj)
