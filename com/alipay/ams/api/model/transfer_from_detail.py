import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount




class TransferFromDetail:
    def __init__(self):
        
        self.__transfer_from_method = None  # type: PaymentMethod
        self.__transfer_from_amount = None  # type: Amount
        

    @property
    def transfer_from_method(self):
        """Gets the transfer_from_method of this TransferFromDetail.
        
        """
        return self.__transfer_from_method

    @transfer_from_method.setter
    def transfer_from_method(self, value):
        self.__transfer_from_method = value
    @property
    def transfer_from_amount(self):
        """Gets the transfer_from_amount of this TransferFromDetail.
        
        """
        return self.__transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        self.__transfer_from_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_from_method") and self.transfer_from_method is not None:
            params['transferFromMethod'] = self.transfer_from_method
        if hasattr(self, "transfer_from_amount") and self.transfer_from_amount is not None:
            params['transferFromAmount'] = self.transfer_from_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transferFromMethod' in response_body:
            self.__transfer_from_method = PaymentMethod()
            self.__transfer_from_method.parse_rsp_body(response_body['transferFromMethod'])
        if 'transferFromAmount' in response_body:
            self.__transfer_from_amount = Amount()
            self.__transfer_from_amount.parse_rsp_body(response_body['transferFromAmount'])
