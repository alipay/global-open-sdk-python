import json
from com.alipay.ams.api.model.payment_method_response import PaymentMethodResponse
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class TransferFromDetailResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__transfer_from_method = None  # type: PaymentMethodResponse
        self.__transfer_from_amount = None  # type: Amount
        self.__fee_amount = None  # type: Amount
        self.parse_rsp_body(rsp_body) 


    @property
    def transfer_from_method(self):
        """Gets the transfer_from_method of this TransferFromDetailResponse.
        
        """
        return self.__transfer_from_method

    @transfer_from_method.setter
    def transfer_from_method(self, value):
        self.__transfer_from_method = value
    @property
    def transfer_from_amount(self):
        """Gets the transfer_from_amount of this TransferFromDetailResponse.
        
        """
        return self.__transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        self.__transfer_from_amount = value
    @property
    def fee_amount(self):
        """Gets the fee_amount of this TransferFromDetailResponse.
        
        """
        return self.__fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self.__fee_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_from_method") and self.transfer_from_method is not None:
            params['transferFromMethod'] = self.transfer_from_method
        if hasattr(self, "transfer_from_amount") and self.transfer_from_amount is not None:
            params['transferFromAmount'] = self.transfer_from_amount
        if hasattr(self, "fee_amount") and self.fee_amount is not None:
            params['feeAmount'] = self.fee_amount
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(TransferFromDetailResponse, self).parse_rsp_body(response_body)
        if 'transferFromMethod' in response_body:
            self.__transfer_from_method = PaymentMethodResponse()
            self.__transfer_from_method.parse_rsp_body(response_body['transferFromMethod'])
        if 'transferFromAmount' in response_body:
            self.__transfer_from_amount = Amount()
            self.__transfer_from_amount.parse_rsp_body(response_body['transferFromAmount'])
        if 'feeAmount' in response_body:
            self.__fee_amount = Amount()
            self.__fee_amount.parse_rsp_body(response_body['feeAmount'])
