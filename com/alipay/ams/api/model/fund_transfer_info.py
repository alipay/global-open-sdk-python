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
        The funds transfer transaction type for Mastercard and Visa. Known values: ACCOUNTFUNDINGTRANSACTION means AFT, a top-up only; BACKTOBACKTRANSACTION means B2B, a top-up followed by a purchase. If neither AFT nor B2B is specified, the transaction is processed as a normal purchase. For AFT, transferSender and transferRecipient may be omitted; omitted information is not sent to the card network, and supplied information is forwarded. For B2B, an omitted sellerMcc or sellerName independently falls back to the corresponding merchant onboarding value. Compatible with non-SDWO merchants. Maximum length: 32 characters.
        """
        return self.__fund_transfer_type

    @fund_transfer_type.setter
    def fund_transfer_type(self, value):
        self.__fund_transfer_type = value
    @property
    def seller_mcc(self):
        """
        The final seller&#39;s merchant category code (MCC) for an SDWO wallet merchant in a BACKTOBACKTRANSACTION. Use a four-digit MCC following ISO 18245. If omitted, Antom uses the wallet merchant&#39;s onboarding MCC, independently of sellerName. For non-wallet merchants, the onboarding MCC is used even if this field is supplied. AFT and other non-B2B transactions use the onboarding MCC. Maximum length: 4 characters.
        """
        return self.__seller_mcc

    @seller_mcc.setter
    def seller_mcc(self, value):
        self.__seller_mcc = value
    @property
    def seller_name(self):
        """
        The final seller&#39;s name for an SDWO wallet merchant in a BACKTOBACKTRANSACTION, used on the cardholder statement. Statement name formats are AlipayHK*&lt;sellerName&gt;, TNGD*&lt;sellerName&gt;, and GrabPay*&lt;sellerName&gt; for the corresponding wallet merchants. If omitted, Antom uses the wallet merchant&#39;s onboarding name, independently of sellerMcc. For non-wallet merchants, the onboarding name is used even if this field is supplied. AFT and other non-B2B transactions use the onboarding name. Maximum length: 256 characters.
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
