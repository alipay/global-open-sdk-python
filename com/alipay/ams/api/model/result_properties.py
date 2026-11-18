import json
from com.alipay.ams.api.model.result_properties_result_code import ResultPropertiesResultCode
from com.alipay.ams.api.model.result_properties_result_status import ResultPropertiesResultStatus
from com.alipay.ams.api.model.result_properties_result_code import ResultPropertiesResultCode




class ResultProperties:
    def __init__(self):
        
        self.__result_code = None  # type: ResultPropertiesResultCode
        self.__result_status = None  # type: ResultPropertiesResultStatus
        self.__result_message = None  # type: ResultPropertiesResultCode
        

    @property
    def result_code(self):
        """Gets the result_code of this ResultProperties.
        
        """
        return self.__result_code

    @result_code.setter
    def result_code(self, value):
        self.__result_code = value
    @property
    def result_status(self):
        """Gets the result_status of this ResultProperties.
        
        """
        return self.__result_status

    @result_status.setter
    def result_status(self, value):
        self.__result_status = value
    @property
    def result_message(self):
        """Gets the result_message of this ResultProperties.
        
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
            self.__result_code = ResultPropertiesResultCode()
            self.__result_code.parse_rsp_body(response_body['resultCode'])
        if 'resultStatus' in response_body:
            self.__result_status = ResultPropertiesResultStatus()
            self.__result_status.parse_rsp_body(response_body['resultStatus'])
        if 'resultMessage' in response_body:
            self.__result_message = ResultPropertiesResultCode()
            self.__result_message.parse_rsp_body(response_body['resultMessage'])
