import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.authorization_control import AuthorizationControl
from com.alipay.ams.api.model.cardholder_info import CardholderInfo




class CardDetail:
    def __init__(self):
        
        self.__result = None  # type: Result
        self.__asset_id = None  # type: str
        self.__card_nick_name = None  # type: str
        self.__card_status = None  # type: str
        self.__masked_card_no = None  # type: str
        self.__card_brand = None  # type: str
        self.__created_time = None  # type: str
        self.__updated_time = None  # type: str
        self.__purpose = None  # type: str
        self.__note = None  # type: str
        self.__metadata = None  # type: {str: (str,)}
        self.__authorization_control = None  # type: AuthorizationControl
        self.__cardholderinfo = None  # type: CardholderInfo
        

    @property
    def result(self):
        """Gets the result of this CardDetail.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def asset_id(self):
        """
        The card asset ID.
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def card_nick_name(self):
        """
        The user-defined card nickname.
        """
        return self.__card_nick_name

    @card_nick_name.setter
    def card_nick_name(self, value):
        self.__card_nick_name = value
    @property
    def card_status(self):
        """
        The current card status.
        """
        return self.__card_status

    @card_status.setter
    def card_status(self, value):
        self.__card_status = value
    @property
    def masked_card_no(self):
        """
        The masked card number.
        """
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value
    @property
    def card_brand(self):
        """
        The card network brand.
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def created_time(self):
        """
        The card creation time in ISO 8601 format.
        """
        return self.__created_time

    @created_time.setter
    def created_time(self, value):
        self.__created_time = value
    @property
    def updated_time(self):
        """
        The card update time in ISO 8601 format.
        """
        return self.__updated_time

    @updated_time.setter
    def updated_time(self, value):
        self.__updated_time = value
    @property
    def purpose(self):
        """
        The purpose of the card.
        """
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        self.__purpose = value
    @property
    def note(self):
        """
        The note supplied for the card application.
        """
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
    @property
    def metadata(self):
        """
        Customer metadata in key-value format.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def authorization_control(self):
        """Gets the authorization_control of this CardDetail.
        
        """
        return self.__authorization_control

    @authorization_control.setter
    def authorization_control(self, value):
        self.__authorization_control = value
    @property
    def cardholderinfo(self):
        """Gets the cardholderinfo of this CardDetail.
        
        """
        return self.__cardholderinfo

    @cardholderinfo.setter
    def cardholderinfo(self, value):
        self.__cardholderinfo = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "card_nick_name") and self.card_nick_name is not None:
            params['cardNickName'] = self.card_nick_name
        if hasattr(self, "card_status") and self.card_status is not None:
            params['cardStatus'] = self.card_status
        if hasattr(self, "masked_card_no") and self.masked_card_no is not None:
            params['maskedCardNo'] = self.masked_card_no
        if hasattr(self, "card_brand") and self.card_brand is not None:
            params['cardBrand'] = self.card_brand
        if hasattr(self, "created_time") and self.created_time is not None:
            params['createdTime'] = self.created_time
        if hasattr(self, "updated_time") and self.updated_time is not None:
            params['updatedTime'] = self.updated_time
        if hasattr(self, "purpose") and self.purpose is not None:
            params['purpose'] = self.purpose
        if hasattr(self, "note") and self.note is not None:
            params['note'] = self.note
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "authorization_control") and self.authorization_control is not None:
            params['authorizationControl'] = self.authorization_control
        if hasattr(self, "cardholderinfo") and self.cardholderinfo is not None:
            params['cardholderinfo'] = self.cardholderinfo
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'cardNickName' in response_body:
            self.__card_nick_name = response_body['cardNickName']
        if 'cardStatus' in response_body:
            self.__card_status = response_body['cardStatus']
        if 'maskedCardNo' in response_body:
            self.__masked_card_no = response_body['maskedCardNo']
        if 'cardBrand' in response_body:
            self.__card_brand = response_body['cardBrand']
        if 'createdTime' in response_body:
            self.__created_time = response_body['createdTime']
        if 'updatedTime' in response_body:
            self.__updated_time = response_body['updatedTime']
        if 'purpose' in response_body:
            self.__purpose = response_body['purpose']
        if 'note' in response_body:
            self.__note = response_body['note']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'authorizationControl' in response_body:
            self.__authorization_control = AuthorizationControl()
            self.__authorization_control.parse_rsp_body(response_body['authorizationControl'])
        if 'cardholderinfo' in response_body:
            self.__cardholderinfo = CardholderInfo()
            self.__cardholderinfo.parse_rsp_body(response_body['cardholderinfo'])
