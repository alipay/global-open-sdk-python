import json
from com.alipay.ams.api.model.payment_method_payment_method_meta_data_channel_option_bill import PaymentMethodPaymentMethodMetaDataChannelOptionBill




class PaymentMethodPaymentMethodMetaData:
    def __init__(self):
        
        self.__channel_option_bill = None  # type: PaymentMethodPaymentMethodMetaDataChannelOptionBill
        

    @property
    def channel_option_bill(self):
        """Gets the channel_option_bill of this PaymentMethodPaymentMethodMetaData.
        
        """
        return self.__channel_option_bill

    @channel_option_bill.setter
    def channel_option_bill(self, value):
        self.__channel_option_bill = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "channel_option_bill") and self.channel_option_bill is not None:
            params['channelOptionBill'] = self.channel_option_bill
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'channelOptionBill' in response_body:
            self.__channel_option_bill = PaymentMethodPaymentMethodMetaDataChannelOptionBill()
            self.__channel_option_bill.parse_rsp_body(response_body['channelOptionBill'])
