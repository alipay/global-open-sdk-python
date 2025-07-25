import json




class RedirectActionForm:
    def __init__(self):
        
        self.__method = None  # type: str
        self.__parameters = None  # type: str
        self.__redirect_url = None  # type: str
        self.__action_form_type = None  # type: str
        

    @property
    def method(self):
        """
        The HTTP method to be used when the merchant initiates a redirection to the redirection URL. Valid values are:  POST: Indicates that the request that is sent to the redirection address needs to be a POST request. GET: Indicates that the request that is sent to the redirection address needs to be a GET request. 
        """
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value
    @property
    def parameters(self):
        """
        Parameters required for the HTTP method in the key-value pair.  Note: This field is returned only when the method is POST.  More information:  Maximum length: 2048 characters
        """
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        self.__parameters = value
    @property
    def redirect_url(self):
        """
        The URL where the user is redirected to.   More information:  Maximum length: 2048 characters 
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value
    @property
    def action_form_type(self):
        """
        The value is fixed as RedirectActionForm.  More information:  Maximum length: 32 characters
        """
        return self.__action_form_type

    @action_form_type.setter
    def action_form_type(self, value):
        self.__action_form_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "method") and self.method is not None:
            params['method'] = self.method
        if hasattr(self, "parameters") and self.parameters is not None:
            params['parameters'] = self.parameters
        if hasattr(self, "redirect_url") and self.redirect_url is not None:
            params['redirectUrl'] = self.redirect_url
        if hasattr(self, "action_form_type") and self.action_form_type is not None:
            params['actionFormType'] = self.action_form_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'method' in response_body:
            self.__method = response_body['method']
        if 'parameters' in response_body:
            self.__parameters = response_body['parameters']
        if 'redirectUrl' in response_body:
            self.__redirect_url = response_body['redirectUrl']
        if 'actionFormType' in response_body:
            self.__action_form_type = response_body['actionFormType']
