import json
from com.alipay.ams.api.model.user_name import UserName




class Buyer:
    def __init__(self):
        
        self.__reference_buyer_id = None  # type: str
        self.__buyer_name = None  # type: UserName
        self.__buyer_phone_no = None  # type: str
        self.__buyer_email = None  # type: str
        self.__buyer_registration_time = None  # type: str
        self.__is_account_verified = None  # type: bool
        self.__successful_order_count = None  # type: int
        

    @property
    def reference_buyer_id(self):
        """
        The unique ID to identify the buyer.  Specify this parameter:  When you require risk control. When the value of paymentMethodType is CARD. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.   More information:  Maximum length: 64 characters 
        """
        return self.__reference_buyer_id

    @reference_buyer_id.setter
    def reference_buyer_id(self, value):
        self.__reference_buyer_id = value
    @property
    def buyer_name(self):
        """Gets the buyer_name of this Buyer.
        
        """
        return self.__buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self.__buyer_name = value
    @property
    def buyer_phone_no(self):
        """
        The mobile phone number of the buyer.  Specify this parameter when one of the following conditions is met:  You require risk control. The value of paymentMethodType is CARD. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.   More information:  Maximum length: 24 characters 
        """
        return self.__buyer_phone_no

    @buyer_phone_no.setter
    def buyer_phone_no(self, value):
        self.__buyer_phone_no = value
    @property
    def buyer_email(self):
        """
        The email of the buyer.  Specify this parameter:  When you require risk control. When the value of paymentMethodType is CARD. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.   More information:  Maximum length: 64 characters
        """
        return self.__buyer_email

    @buyer_email.setter
    def buyer_email(self, value):
        self.__buyer_email = value
    @property
    def buyer_registration_time(self):
        """
        The time when the buyer registered your account. Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Maximum length: 64 characters The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__buyer_registration_time

    @buyer_registration_time.setter
    def buyer_registration_time(self, value):
        self.__buyer_registration_time = value
    @property
    def is_account_verified(self):
        """Gets the is_account_verified of this Buyer.
        
        """
        return self.__is_account_verified

    @is_account_verified.setter
    def is_account_verified(self, value):
        self.__is_account_verified = value
    @property
    def successful_order_count(self):
        """Gets the successful_order_count of this Buyer.
        
        """
        return self.__successful_order_count

    @successful_order_count.setter
    def successful_order_count(self, value):
        self.__successful_order_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_buyer_id") and self.reference_buyer_id is not None:
            params['referenceBuyerId'] = self.reference_buyer_id
        if hasattr(self, "buyer_name") and self.buyer_name is not None:
            params['buyerName'] = self.buyer_name
        if hasattr(self, "buyer_phone_no") and self.buyer_phone_no is not None:
            params['buyerPhoneNo'] = self.buyer_phone_no
        if hasattr(self, "buyer_email") and self.buyer_email is not None:
            params['buyerEmail'] = self.buyer_email
        if hasattr(self, "buyer_registration_time") and self.buyer_registration_time is not None:
            params['buyerRegistrationTime'] = self.buyer_registration_time
        if hasattr(self, "is_account_verified") and self.is_account_verified is not None:
            params['isAccountVerified'] = self.is_account_verified
        if hasattr(self, "successful_order_count") and self.successful_order_count is not None:
            params['successfulOrderCount'] = self.successful_order_count
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceBuyerId' in response_body:
            self.__reference_buyer_id = response_body['referenceBuyerId']
        if 'buyerName' in response_body:
            self.__buyer_name = UserName()
            self.__buyer_name.parse_rsp_body(response_body['buyerName'])
        if 'buyerPhoneNo' in response_body:
            self.__buyer_phone_no = response_body['buyerPhoneNo']
        if 'buyerEmail' in response_body:
            self.__buyer_email = response_body['buyerEmail']
        if 'buyerRegistrationTime' in response_body:
            self.__buyer_registration_time = response_body['buyerRegistrationTime']
        if 'isAccountVerified' in response_body:
            self.__is_account_verified = response_body['isAccountVerified']
        if 'successfulOrderCount' in response_body:
            self.__successful_order_count = response_body['successfulOrderCount']
