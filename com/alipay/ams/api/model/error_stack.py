import json




class ErrorStack:
    def __init__(self):
        
        self.__error_stack = None  # type: str
        

    @property
    def error_stack(self):
        """
        The error stack information.
        """
        return self.__error_stack

    @error_stack.setter
    def error_stack(self, value):
        self.__error_stack = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "error_stack") and self.error_stack is not None:
            params['errorStack'] = self.error_stack
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'errorStack' in response_body:
            self.__error_stack = response_body['errorStack']
