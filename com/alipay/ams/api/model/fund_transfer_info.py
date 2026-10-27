import json
from com.alipay.ams.api.model.fund_transfer_sender import FundTransferSender
from com.alipay.ams.api.model.fund_transfer_recipient import FundTransferRecipient




class FundTransferInfo:
    def __init__(self):
        
        self.__fund_transfer_type = None  # type: str
        self.__seller_mcc = None  # type: str
        self.__seller_name = None  # type: str
        self.__transfer_sender = None  # type: FundTransferSender
        self.__transfer_recipient = None  # type: FundTransferRecipient
        

    @property
    def fund_transfer_type(self):
        """
        The fund transfer scenario. ACCOUNTFUNDINGTRANSACTION: account funding (AFT) without a purchase. BACKTOBACKTRANSACTION: wallet funding followed by a purchase (B2B). If omitted, the transaction is handled as a regular purchase. Maximum length: 32 characters.
        """
        return self.__fund_transfer_type

    @fund_transfer_type.setter
    def fund_transfer_type(self, value):
        self.__fund_transfer_type = value
    @property
    def seller_mcc(self):
        """
        For an SDWO wallet merchant in a BACKTOBACKTRANSACTION, the actual seller&#39;s four-digit ISO 18245 MCC. If omitted, the merchant&#39;s registered MCC is used; a value sent by a non-wallet merchant does not override its registered MCC. This field is independent of sellerName. Maximum length: 4 characters.
        """
        return self.__seller_mcc

    @seller_mcc.setter
    def seller_mcc(self, value):
        self.__seller_mcc = value
    @property
    def seller_name(self):
        """
        For an SDWO wallet merchant in a BACKTOBACKTRANSACTION, the actual seller&#39;s name, displayed on the cardholder statement after the wallet operator name (for example, AlipayHK*, TNGD*, or GrabPay*). If omitted, the merchant&#39;s registered name is used; a value sent by a non-wallet merchant does not override its registered name. This field is independent of sellerMcc. Maximum length: 256 characters.
        """
        return self.__seller_name

    @seller_name.setter
    def seller_name(self, value):
        self.__seller_name = value
    @property
    def transfer_sender(self):
        """Gets the transfer_sender of this FundTransferInfo.
        
        """
        return self.__transfer_sender

    @transfer_sender.setter
    def transfer_sender(self, value):
        self.__transfer_sender = value
    @property
    def transfer_recipient(self):
        """Gets the transfer_recipient of this FundTransferInfo.
        
        """
        return self.__transfer_recipient

    @transfer_recipient.setter
    def transfer_recipient(self, value):
        self.__transfer_recipient = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "fund_transfer_type") and self.fund_transfer_type is not None:
            params['fundTransferType'] = self.fund_transfer_type
        if hasattr(self, "seller_mcc") and self.seller_mcc is not None:
            params['sellerMcc'] = self.seller_mcc
        if hasattr(self, "seller_name") and self.seller_name is not None:
            params['sellerName'] = self.seller_name
        if hasattr(self, "transfer_sender") and self.transfer_sender is not None:
            params['transferSender'] = self.transfer_sender
        if hasattr(self, "transfer_recipient") and self.transfer_recipient is not None:
            params['transferRecipient'] = self.transfer_recipient
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'fundTransferType' in response_body:
            self.__fund_transfer_type = response_body['fundTransferType']
        if 'sellerMcc' in response_body:
            self.__seller_mcc = response_body['sellerMcc']
        if 'sellerName' in response_body:
            self.__seller_name = response_body['sellerName']
        if 'transferSender' in response_body:
            self.__transfer_sender = FundTransferSender()
            self.__transfer_sender.parse_rsp_body(response_body['transferSender'])
        if 'transferRecipient' in response_body:
            self.__transfer_recipient = FundTransferRecipient()
            self.__transfer_recipient.parse_rsp_body(response_body['transferRecipient'])
