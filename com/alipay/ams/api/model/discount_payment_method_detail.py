import json
from com.alipay.ams.api.model.amount import Amount




class DiscountPaymentMethodDetail:
    def __init__(self):
        
        self.__discount_id = None  # type: str
        self.__available_amount = None  # type: Amount
        self.__discount_name = None  # type: str
        self.__discount_description = None  # type: str
        self.__payment_method_detail_metadata = None  # type: str
        

    @property
    def discount_id(self):
        """Gets the discount_id of this DiscountPaymentMethodDetail.
        
        """
        return self.__discount_id

    @discount_id.setter
    def discount_id(self, value):
        self.__discount_id = value
    @property
    def available_amount(self):
        """Gets the available_amount of this DiscountPaymentMethodDetail.
        
        """
        return self.__available_amount

    @available_amount.setter
    def available_amount(self, value):
        self.__available_amount = value
    @property
    def discount_name(self):
        """Gets the discount_name of this DiscountPaymentMethodDetail.
        
        """
        return self.__discount_name

    @discount_name.setter
    def discount_name(self, value):
        self.__discount_name = value
    @property
    def discount_description(self):
        """Gets the discount_description of this DiscountPaymentMethodDetail.
        
        """
        return self.__discount_description

    @discount_description.setter
    def discount_description(self, value):
        self.__discount_description = value
    @property
    def payment_method_detail_metadata(self):
        """Gets the payment_method_detail_metadata of this DiscountPaymentMethodDetail.
        
        """
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "discount_id") and self.discount_id is not None:
            params['discountId'] = self.discount_id
        if hasattr(self, "available_amount") and self.available_amount is not None:
            params['availableAmount'] = self.available_amount
        if hasattr(self, "discount_name") and self.discount_name is not None:
            params['discountName'] = self.discount_name
        if hasattr(self, "discount_description") and self.discount_description is not None:
            params['discountDescription'] = self.discount_description
        if hasattr(self, "payment_method_detail_metadata") and self.payment_method_detail_metadata is not None:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'discountId' in response_body:
            self.__discount_id = response_body['discountId']
        if 'availableAmount' in response_body:
            self.__available_amount = Amount()
            self.__available_amount.parse_rsp_body(response_body['availableAmount'])
        if 'discountName' in response_body:
            self.__discount_name = response_body['discountName']
        if 'discountDescription' in response_body:
            self.__discount_description = response_body['discountDescription']
        if 'paymentMethodDetailMetadata' in response_body:
            self.__payment_method_detail_metadata = response_body['paymentMethodDetailMetadata']
