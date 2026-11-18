import json




class AbaCard:
    def __init__(self):
        
        self.__asset_id = None  # type: str
        self.__card_nick_name = None  # type: str
        self.__masked_card_no = None  # type: str
        self.__card_status = None  # type: str
        self.__card_brand = None  # type: str
        self.__created_time = None  # type: str
        self.__updated_time = None  # type: str
        

    @property
    def asset_id(self):
        """
        卡资产ID。 Card asset Id.
        """
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value):
        self.__asset_id = value
    @property
    def card_nick_name(self):
        """
        由用户定义的卡昵称，可以帮助用户更方便地管理多张卡。 User-defined card nickname, designed to help users manage multiple cards more conveniently.
        """
        return self.__card_nick_name

    @card_nick_name.setter
    def card_nick_name(self, value):
        self.__card_nick_name = value
    @property
    def masked_card_no(self):
        """
        脱敏卡号。 Masked card number.
        """
        return self.__masked_card_no

    @masked_card_no.setter
    def masked_card_no(self, value):
        self.__masked_card_no = value
    @property
    def card_status(self):
        """
        卡状态。可取值范围： ACTIVE：可正常使用 FROZEN：已冻结 CANCEL：已注销  Card Status: Represents the current state of the card. Possible values include:   ACTIVE: The card is active and can be used normally.   FROZEN: The card has been frozen and cannot be used temporarily.   CANCEL: The card has been canceled and is no longer valid.
        """
        return self.__card_status

    @card_status.setter
    def card_status(self, value):
        self.__card_status = value
    @property
    def card_brand(self):
        """
        卡品牌。 可取值范围： MASTERCARD  Card Brand: Indicates the brand or network of the card. Possible value:   MASTERCARD: The card is part of the Mastercard network.
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value):
        self.__card_brand = value
    @property
    def created_time(self):
        """
        Card creation time ISO 8601
        """
        return self.__created_time

    @created_time.setter
    def created_time(self, value):
        self.__created_time = value
    @property
    def updated_time(self):
        """
        Card update time ISO 8601
        """
        return self.__updated_time

    @updated_time.setter
    def updated_time(self, value):
        self.__updated_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "asset_id") and self.asset_id is not None:
            params['assetId'] = self.asset_id
        if hasattr(self, "card_nick_name") and self.card_nick_name is not None:
            params['cardNickName'] = self.card_nick_name
        if hasattr(self, "masked_card_no") and self.masked_card_no is not None:
            params['maskedCardNo'] = self.masked_card_no
        if hasattr(self, "card_status") and self.card_status is not None:
            params['cardStatus'] = self.card_status
        if hasattr(self, "card_brand") and self.card_brand is not None:
            params['cardBrand'] = self.card_brand
        if hasattr(self, "created_time") and self.created_time is not None:
            params['createdTime'] = self.created_time
        if hasattr(self, "updated_time") and self.updated_time is not None:
            params['updatedTime'] = self.updated_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'assetId' in response_body:
            self.__asset_id = response_body['assetId']
        if 'cardNickName' in response_body:
            self.__card_nick_name = response_body['cardNickName']
        if 'maskedCardNo' in response_body:
            self.__masked_card_no = response_body['maskedCardNo']
        if 'cardStatus' in response_body:
            self.__card_status = response_body['cardStatus']
        if 'cardBrand' in response_body:
            self.__card_brand = response_body['cardBrand']
        if 'createdTime' in response_body:
            self.__created_time = response_body['createdTime']
        if 'updatedTime' in response_body:
            self.__updated_time = response_body['updatedTime']
