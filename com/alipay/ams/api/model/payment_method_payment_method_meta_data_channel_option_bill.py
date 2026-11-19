import json




class PaymentMethodPaymentMethodMetaDataChannelOptionBill:
    def __init__(self):
        
        self.__channel_promotion_code = None  # type: str
        

    @property
    def channel_promotion_code(self):
        """
        The promotion code(s) agreed between the merchant and Sequra, identifying promotional activities such as interest-free installments. When multiple codes exist, concatenate with commas (max 99 codes, each max 20 characters). IPay only passes through and does not validate. Required when the merchant has agreed promotion codes with Sequra. Default: not transmitted, no impact. Nullable: yes.
        """
        return self.__channel_promotion_code

    @channel_promotion_code.setter
    def channel_promotion_code(self, value):
        self.__channel_promotion_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "channel_promotion_code") and self.channel_promotion_code is not None:
            params['channelPromotionCode'] = self.channel_promotion_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'channelPromotionCode' in response_body:
            self.__channel_promotion_code = response_body['channelPromotionCode']
