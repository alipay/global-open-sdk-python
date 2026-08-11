import json




class BillingSubscriptionCancellationDetails:
    def __init__(self):
        
        self.__feedback = None  # type: str
        self.__comment = None  # type: str
        

    @property
    def feedback(self):
        """
        Structured cancellation feedback. Recommended values include TOO_EXPENSIVE, UNUSED, MISSING_FEATURES, TOO_COMPLEX, SWITCHED_SERVICE, LOW_QUALITY, CUSTOMER_SERVICE, and OTHER. Other values are accepted. Maximum length: 64 characters.
        """
        return self.__feedback

    @feedback.setter
    def feedback(self, value):
        self.__feedback = value
    @property
    def comment(self):
        """
        Additional cancellation details. Do not include personally identifiable information. Maximum length: 500 characters.
        """
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "feedback") and self.feedback is not None:
            params['feedback'] = self.feedback
        if hasattr(self, "comment") and self.comment is not None:
            params['comment'] = self.comment
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'feedback' in response_body:
            self.__feedback = response_body['feedback']
        if 'comment' in response_body:
            self.__comment = response_body['comment']
