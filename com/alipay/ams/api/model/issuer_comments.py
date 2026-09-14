class IssuerComments(object):
    """Issuer and cardholder comments returned in a dispute notification."""

    def __init__(self):
        self.__cardholder_comments = None
        self.__reason_of_invalid_authorization = None
        self.__explanation_of_credit_presented = None
        self.__judge_reason = None

    @property
    def cardholder_comments(self):
        return self.__cardholder_comments

    @cardholder_comments.setter
    def cardholder_comments(self, value):
        self.__cardholder_comments = value

    @property
    def reason_of_invalid_authorization(self):
        return self.__reason_of_invalid_authorization

    @reason_of_invalid_authorization.setter
    def reason_of_invalid_authorization(self, value):
        self.__reason_of_invalid_authorization = value

    @property
    def explanation_of_credit_presented(self):
        return self.__explanation_of_credit_presented

    @explanation_of_credit_presented.setter
    def explanation_of_credit_presented(self, value):
        self.__explanation_of_credit_presented = value

    @property
    def judge_reason(self):
        return self.__judge_reason

    @judge_reason.setter
    def judge_reason(self, value):
        self.__judge_reason = value
