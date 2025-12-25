import json
from com.alipay.ams.api.model.result_status_type import ResultStatusType




class ResultResult:
    def __init__(self):
        
        self.__result_code = None  # type: str
        self.__result_status = None  # type: ResultStatusType
        self.__result_message = None  # type: str
        

    @property
    def result_code(self):
        """
        The result code.
        """
        return self.__result_code

    @result_code.setter
    def result_code(self, value):
        self.__result_code = value
    @property
    def result_status(self):
        """Gets the result_status of this ResultResult.
        
        """
        return self.__result_status

    @result_status.setter
    def result_status(self, value):
        self.__result_status = value
    @property
    def result_message(self):
        """
        The result message.
        """
        return self.__result_message

    @result_message.setter
    def result_message(self, value):
        self.__result_message = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result_code") and self.result_code is not None:
            params['resultCode'] = self.result_code
        if hasattr(self, "result_status") and self.result_status is not None:
            params['resultStatus'] = self.result_status
        if hasattr(self, "result_message") and self.result_message is not None:
            params['resultMessage'] = self.result_message
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'resultCode' in response_body:
            self.__result_code = response_body['resultCode']
        if 'resultStatus' in response_body:
            result_status_temp = ResultStatusType.value_of(response_body['resultStatus'])
            self.__result_status = result_status_temp
        if 'resultMessage' in response_body:
            self.__result_message = response_body['resultMessage']
