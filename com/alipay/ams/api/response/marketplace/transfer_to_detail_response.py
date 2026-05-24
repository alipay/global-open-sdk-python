import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class TransferToDetailResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__transfer_to_method = None  # type: PaymentMethod
        self.__transfer_to_amount = None  # type: Amount
        self.__fee_amount = None  # type: Amount
        self.parse_rsp_body(rsp_body) 


    @property
    def transfer_to_method(self):
        """Gets the transfer_to_method of this TransferToDetailResponse.
        
        """
        return self.__transfer_to_method

    @transfer_to_method.setter
    def transfer_to_method(self, value):
        self.__transfer_to_method = value
    @property
    def transfer_to_amount(self):
        """Gets the transfer_to_amount of this TransferToDetailResponse.
        
        """
        return self.__transfer_to_amount

    @transfer_to_amount.setter
    def transfer_to_amount(self, value):
        self.__transfer_to_amount = value
    @property
    def fee_amount(self):
        """Gets the fee_amount of this TransferToDetailResponse.
        
        """
        return self.__fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self.__fee_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_to_method") and self.transfer_to_method is not None:
            params['transferToMethod'] = self.transfer_to_method
        if hasattr(self, "transfer_to_amount") and self.transfer_to_amount is not None:
            params['transferToAmount'] = self.transfer_to_amount
        if hasattr(self, "fee_amount") and self.fee_amount is not None:
            params['feeAmount'] = self.fee_amount
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(TransferToDetailResponse, self).parse_rsp_body(response_body)
        if 'transferToMethod' in response_body:
            self.__transfer_to_method = PaymentMethod()
            self.__transfer_to_method.parse_rsp_body(response_body['transferToMethod'])
        if 'transferToAmount' in response_body:
            self.__transfer_to_amount = Amount()
            self.__transfer_to_amount.parse_rsp_body(response_body['transferToAmount'])
        if 'feeAmount' in response_body:
            self.__fee_amount = Amount()
            self.__fee_amount.parse_rsp_body(response_body['feeAmount'])
