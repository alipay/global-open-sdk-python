import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount




class TransferToDetail:
    def __init__(self):
        
        self.__transfer_to_method = None  # type: PaymentMethod
        self.__transfer_to_amount = None  # type: Amount
        self.__transfer_notify_url = None  # type: str
        self.__transfer_remark = None  # type: str
        self.__transfer_memo = None  # type: str
        

    @property
    def transfer_to_method(self):
        """Gets the transfer_to_method of this TransferToDetail.
        
        """
        return self.__transfer_to_method

    @transfer_to_method.setter
    def transfer_to_method(self, value):
        self.__transfer_to_method = value
    @property
    def transfer_to_amount(self):
        """Gets the transfer_to_amount of this TransferToDetail.
        
        """
        return self.__transfer_to_amount

    @transfer_to_amount.setter
    def transfer_to_amount(self, value):
        self.__transfer_to_amount = value
    @property
    def transfer_notify_url(self):
        """
        The URL that is used to receive the transfer result notification.
        """
        return self.__transfer_notify_url

    @transfer_notify_url.setter
    def transfer_notify_url(self, value):
        self.__transfer_notify_url = value
    @property
    def transfer_remark(self):
        """
        Information provided for bank settlements.
        """
        return self.__transfer_remark

    @transfer_remark.setter
    def transfer_remark(self, value):
        self.__transfer_remark = value
    @property
    def transfer_memo(self):
        """
        The transfer memo that the merchant leaves.
        """
        return self.__transfer_memo

    @transfer_memo.setter
    def transfer_memo(self, value):
        self.__transfer_memo = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_to_method") and self.transfer_to_method is not None:
            params['transferToMethod'] = self.transfer_to_method
        if hasattr(self, "transfer_to_amount") and self.transfer_to_amount is not None:
            params['transferToAmount'] = self.transfer_to_amount
        if hasattr(self, "transfer_notify_url") and self.transfer_notify_url is not None:
            params['transferNotifyUrl'] = self.transfer_notify_url
        if hasattr(self, "transfer_remark") and self.transfer_remark is not None:
            params['transferRemark'] = self.transfer_remark
        if hasattr(self, "transfer_memo") and self.transfer_memo is not None:
            params['transferMemo'] = self.transfer_memo
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transferToMethod' in response_body:
            self.__transfer_to_method = PaymentMethod()
            self.__transfer_to_method.parse_rsp_body(response_body['transferToMethod'])
        if 'transferToAmount' in response_body:
            self.__transfer_to_amount = Amount()
            self.__transfer_to_amount.parse_rsp_body(response_body['transferToAmount'])
        if 'transferNotifyUrl' in response_body:
            self.__transfer_notify_url = response_body['transferNotifyUrl']
        if 'transferRemark' in response_body:
            self.__transfer_remark = response_body['transferRemark']
        if 'transferMemo' in response_body:
            self.__transfer_memo = response_body['transferMemo']
