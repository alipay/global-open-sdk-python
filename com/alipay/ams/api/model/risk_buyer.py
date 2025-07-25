import json




class RiskBuyer:
    def __init__(self):
        
        self.__note_to_merchant = None  # type: str
        self.__note_to_shipping = None  # type: str
        self.__order_count_in1_h = None  # type: int
        self.__order_count_in24_h = None  # type: int
        

    @property
    def note_to_merchant(self):
        """
        The buyer&#39;s note to a merchant.
        """
        return self.__note_to_merchant

    @note_to_merchant.setter
    def note_to_merchant(self, value):
        self.__note_to_merchant = value
    @property
    def note_to_shipping(self):
        """
        The buyer&#39;s note to a deliveryman or a take-out rider.
        """
        return self.__note_to_shipping

    @note_to_shipping.setter
    def note_to_shipping(self, value):
        self.__note_to_shipping = value
    @property
    def order_count_in1_h(self):
        """
        The successful orders the buyer made within the last one hour.
        """
        return self.__order_count_in1_h

    @order_count_in1_h.setter
    def order_count_in1_h(self, value):
        self.__order_count_in1_h = value
    @property
    def order_count_in24_h(self):
        """
        The successful orders the buyer made within the last 24 hour.
        """
        return self.__order_count_in24_h

    @order_count_in24_h.setter
    def order_count_in24_h(self, value):
        self.__order_count_in24_h = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "note_to_merchant") and self.note_to_merchant is not None:
            params['noteToMerchant'] = self.note_to_merchant
        if hasattr(self, "note_to_shipping") and self.note_to_shipping is not None:
            params['noteToShipping'] = self.note_to_shipping
        if hasattr(self, "order_count_in1_h") and self.order_count_in1_h is not None:
            params['orderCountIn1H'] = self.order_count_in1_h
        if hasattr(self, "order_count_in24_h") and self.order_count_in24_h is not None:
            params['orderCountIn24H'] = self.order_count_in24_h
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'noteToMerchant' in response_body:
            self.__note_to_merchant = response_body['noteToMerchant']
        if 'noteToShipping' in response_body:
            self.__note_to_shipping = response_body['noteToShipping']
        if 'orderCountIn1H' in response_body:
            self.__order_count_in1_h = response_body['orderCountIn1H']
        if 'orderCountIn24H' in response_body:
            self.__order_count_in24_h = response_body['orderCountIn24H']
