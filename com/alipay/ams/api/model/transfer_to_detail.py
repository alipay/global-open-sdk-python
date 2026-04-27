import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class TransferToDetail:
    def __init__(self):
        
        self.__transfer_to_method = None  # type: PaymentMethod
        self.__transfer_to_currency = None  # type: str
        self.__fee_amount = None  # type: Amount
        self.__actual_transfer_to_amount = None  # type: Amount
        self.__purpose_code = None  # type: str
        self.__transfer_notify_url = None  # type: str
        self.__transfer_remark = None  # type: str
        

    @property
    def transfer_to_method(self):
        """Gets the transfer_to_method of this TransferToDetail.
        
        """
        return self.__transfer_to_method

    @transfer_to_method.setter
    def transfer_to_method(self, value):
        self.__transfer_to_method = value
    @property
    def transfer_to_currency(self):
        """
        A 3-character ISO-4217 currency code representing the currency that the beneficiary collects.    More information:  Maximum length: 3 characters
        """
        return self.__transfer_to_currency

    @transfer_to_currency.setter
    def transfer_to_currency(self, value):
        self.__transfer_to_currency = value
    @property
    def fee_amount(self):
        """Gets the fee_amount of this TransferToDetail.
        
        """
        return self.__fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self.__fee_amount = value
    @property
    def actual_transfer_to_amount(self):
        """Gets the actual_transfer_to_amount of this TransferToDetail.
        
        """
        return self.__actual_transfer_to_amount

    @actual_transfer_to_amount.setter
    def actual_transfer_to_amount(self, value):
        self.__actual_transfer_to_amount = value
    @property
    def purpose_code(self):
        """
        Defines the purpose of the transfer. The value of this parameter is fixed to GSD, which means goods bought or sold.    More information:  Maximum length: 3 characters
        """
        return self.__purpose_code

    @purpose_code.setter
    def purpose_code(self, value):
        self.__purpose_code = value
    @property
    def transfer_notify_url(self):
        """
        If you specify this parameter, Antom will send the transfer result notification to this URL. The URL must be either specified in the request or set in Antom Dashboard.  Specify this parameter if you want to receive an asynchronous notification of the transfer result. If this URL is specified in both the request and Antom Dashboard, the value specified in the request takes precedence.    More information:  Maximum length: 2048 characters
        """
        return self.__transfer_notify_url

    @transfer_notify_url.setter
    def transfer_notify_url(self, value):
        self.__transfer_notify_url = value
    @property
    def transfer_remark(self):
        """
        Remark information for the transfer.  Specify this parameter if you want to provide additional remarks or relevant information regarding the payout.  More information:  Maximum length: 1024 characters
        """
        return self.__transfer_remark

    @transfer_remark.setter
    def transfer_remark(self, value):
        self.__transfer_remark = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_to_method") and self.transfer_to_method is not None:
            params['transferToMethod'] = self.transfer_to_method
        if hasattr(self, "transfer_to_currency") and self.transfer_to_currency is not None:
            params['transferToCurrency'] = self.transfer_to_currency
        if hasattr(self, "fee_amount") and self.fee_amount is not None:
            params['feeAmount'] = self.fee_amount
        if hasattr(self, "actual_transfer_to_amount") and self.actual_transfer_to_amount is not None:
            params['actualTransferToAmount'] = self.actual_transfer_to_amount
        if hasattr(self, "purpose_code") and self.purpose_code is not None:
            params['purposeCode'] = self.purpose_code
        if hasattr(self, "transfer_notify_url") and self.transfer_notify_url is not None:
            params['transferNotifyUrl'] = self.transfer_notify_url
        if hasattr(self, "transfer_remark") and self.transfer_remark is not None:
            params['transferRemark'] = self.transfer_remark
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transferToMethod' in response_body:
            self.__transfer_to_method = PaymentMethod()
            self.__transfer_to_method.parse_rsp_body(response_body['transferToMethod'])
        if 'transferToCurrency' in response_body:
            self.__transfer_to_currency = response_body['transferToCurrency']
        if 'feeAmount' in response_body:
            self.__fee_amount = Amount()
            self.__fee_amount.parse_rsp_body(response_body['feeAmount'])
        if 'actualTransferToAmount' in response_body:
            self.__actual_transfer_to_amount = Amount()
            self.__actual_transfer_to_amount.parse_rsp_body(response_body['actualTransferToAmount'])
        if 'purposeCode' in response_body:
            self.__purpose_code = response_body['purposeCode']
        if 'transferNotifyUrl' in response_body:
            self.__transfer_notify_url = response_body['transferNotifyUrl']
        if 'transferRemark' in response_body:
            self.__transfer_remark = response_body['transferRemark']
