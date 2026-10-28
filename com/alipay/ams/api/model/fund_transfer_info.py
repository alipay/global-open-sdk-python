import json
from com.alipay.ams.api.model.transfer_sender import TransferSender
from com.alipay.ams.api.model.transfer_recipient import TransferRecipient




class FundTransferInfo:
    def __init__(self):
        
        self.__fund_transfer_type = None  # type: str
        self.__seller_mcc = None  # type: str
        self.__seller_name = None  # type: str
        self.__transfer_sender = None  # type: TransferSender
        self.__transfer_recipient = None  # type: TransferRecipient
        

    @property
    def fund_transfer_type(self):
        """
        The fund transfer type. Known values are ACCOUNTFUNDINGTRANSACTION: an account funding transaction (AFT), used only to top up an account; BACKTOBACKTRANSACTION: a back-to-back transaction (B2B), used to top up and then purchase. If neither value is supplied, the payment is processed as a normal purchase. For AFT, transferSender and transferRecipient can be omitted; when supplied, their information is forwarded to the card network. For B2B, an omitted sellerMcc or sellerName independently falls back to the corresponding merchant information registered with Antom. Maximum length: 32 characters.
        """
        return self.__fund_transfer_type

    @fund_transfer_type.setter
    def fund_transfer_type(self, value):
        self.__fund_transfer_type = value
    @property
    def seller_mcc(self):
        """
        The merchant category code (MCC) of the final seller for a B2B payment. Used only for SDWO merchants when fundTransferType is BACKTOBACKTRANSACTION, to distinguish the final seller from the wallet operator. Use a four-digit MCC under ISO 18245. If omitted, the merchant MCC registered with Antom is used, independently of sellerName. For non-wallet merchants or other transaction types, the registered MCC is used even if this field is supplied. Maximum length: 4 characters.
        """
        return self.__seller_mcc

    @seller_mcc.setter
    def seller_mcc(self, value):
        self.__seller_mcc = value
    @property
    def seller_name(self):
        """
        The name of the final seller for a B2B payment. Used only for SDWO merchants when fundTransferType is BACKTOBACKTRANSACTION. The cardholder statement displays AlipayHK*&lt;sellerName&gt;, TNGD*&lt;sellerName&gt;, or GrabPay*&lt;sellerName&gt;, as applicable to the wallet merchant. If omitted, the merchant name registered with Antom is used, independently of sellerMcc. For non-wallet merchants or other transaction types, the registered merchant name is used even if this field is supplied. Maximum length: 256 characters.
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
            self.__transfer_sender = TransferSender()
            self.__transfer_sender.parse_rsp_body(response_body['transferSender'])
        if 'transferRecipient' in response_body:
            self.__transfer_recipient = TransferRecipient()
            self.__transfer_recipient.parse_rsp_body(response_body['transferRecipient'])
