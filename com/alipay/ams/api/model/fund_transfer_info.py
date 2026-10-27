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
        Fund transfer scenario. Supported values: ACCOUNTFUNDINGTRANSACTION (account funding/AFT top-up) and BACKTOBACKTRANSACTION (wallet top-up followed by purchase/B2B). If neither value is provided, the transaction is processed as a normal purchase. For AFT, transferSender and transferRecipient may be omitted; if supplied, they are passed to the card schemes. Maximum length: 32 characters.
        """
        return self.__fund_transfer_type

    @fund_transfer_type.setter
    def fund_transfer_type(self, value):
        self.__fund_transfer_type = value
    @property
    def seller_mcc(self):
        """
        MCC of the ultimate seller in a back-to-back transaction, for SDWO wallet merchants only. Use a four-digit ISO 18245 MCC. If omitted, the merchant-onboarding MCC is used independently of sellerName; values supplied by non-wallet merchants are ignored. Maximum length: 4 characters.
        """
        return self.__seller_mcc

    @seller_mcc.setter
    def seller_mcc(self, value):
        self.__seller_mcc = value
    @property
    def seller_name(self):
        """
        Name of the ultimate seller in a back-to-back transaction, for SDWO wallet merchants only. The cardholder statement displays AlipayHK*&lt;sellerName&gt;, TNGD*&lt;sellerName&gt;, or GrabPay*&lt;sellerName&gt;, according to the wallet platform. If omitted, the merchant-onboarding name is used independently of sellerMcc; values supplied by non-wallet merchants are ignored. Maximum length: 256 characters.
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
