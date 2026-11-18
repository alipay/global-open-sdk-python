import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireCardRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireCardRequest, self).__init__("/ams/api/v1/aba/cards/inquireCard") 

        self.__page_number = None  # type: int
        self.__page_size = None  # type: int
        self.__last_four_digits = None  # type: str
        self.__card_status = None  # type: str
        self.__card_nick_name = None  # type: str
        

    @property
    def page_number(self):
        """
        页码 (Page number)
        """
        return self.__page_number

    @page_number.setter
    def page_number(self, value):
        self.__page_number = value
    @property
    def page_size(self):
        """
        每页包含的条目数 (Number of entries per page). Max pageSize is 50.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def last_four_digits(self):
        """
        卡号后四位数字。(The last four digits of the card number.)
        """
        return self.__last_four_digits

    @last_four_digits.setter
    def last_four_digits(self, value):
        self.__last_four_digits = value
    @property
    def card_status(self):
        """
        卡状态。可取值范围： ACTIVE：可正常使用 FROZEN：已冻结 CANCEL：已注销 (Card Status. Possible values: ACTIVE: The card is active and can be used normally. FROZEN: The card is frozen and temporarily unavailable for use. CANCEL: The card has been canceled and is no longer valid.)
        """
        return self.__card_status

    @card_status.setter
    def card_status(self, value):
        self.__card_status = value
    @property
    def card_nick_name(self):
        """
        由用户定义的卡昵称，可以帮助用户更方便地管理多张卡。(User-defined card nickname, designed to help users manage multiple cards more conveniently.)
        """
        return self.__card_nick_name

    @card_nick_name.setter
    def card_nick_name(self, value):
        self.__card_nick_name = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "page_number") and self.page_number is not None:
            params['pageNumber'] = self.page_number
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "last_four_digits") and self.last_four_digits is not None:
            params['lastFourDigits'] = self.last_four_digits
        if hasattr(self, "card_status") and self.card_status is not None:
            params['cardStatus'] = self.card_status
        if hasattr(self, "card_nick_name") and self.card_nick_name is not None:
            params['cardNickName'] = self.card_nick_name
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'pageNumber' in response_body:
            self.__page_number = response_body['pageNumber']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'lastFourDigits' in response_body:
            self.__last_four_digits = response_body['lastFourDigits']
        if 'cardStatus' in response_body:
            self.__card_status = response_body['cardStatus']
        if 'cardNickName' in response_body:
            self.__card_nick_name = response_body['cardNickName']
