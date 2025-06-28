import json
from com.alipay.ams.api.model.amount import Amount




class CouponPaymentMethodDetail:
    def __init__(self):
        
        self.__coupon_id = None  # type: str
        self.__available_amount = None  # type: Amount
        self.__coupon_name = None  # type: str
        self.__coupon_description = None  # type: str
        self.__coupon_expire_time = None  # type: str
        self.__payment_method_detail_metadata = None  # type: str
        

    @property
    def coupon_id(self):
        """Gets the coupon_id of this CouponPaymentMethodDetail.
        
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def available_amount(self):
        """Gets the available_amount of this CouponPaymentMethodDetail.
        
        """
        return self.__available_amount

    @available_amount.setter
    def available_amount(self, value):
        self.__available_amount = value
    @property
    def coupon_name(self):
        """Gets the coupon_name of this CouponPaymentMethodDetail.
        
        """
        return self.__coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value
    @property
    def coupon_description(self):
        """Gets the coupon_description of this CouponPaymentMethodDetail.
        
        """
        return self.__coupon_description

    @coupon_description.setter
    def coupon_description(self, value):
        self.__coupon_description = value
    @property
    def coupon_expire_time(self):
        """Gets the coupon_expire_time of this CouponPaymentMethodDetail.
        
        """
        return self.__coupon_expire_time

    @coupon_expire_time.setter
    def coupon_expire_time(self, value):
        self.__coupon_expire_time = value
    @property
    def payment_method_detail_metadata(self):
        """Gets the payment_method_detail_metadata of this CouponPaymentMethodDetail.
        
        """
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "available_amount") and self.available_amount is not None:
            params['availableAmount'] = self.available_amount
        if hasattr(self, "coupon_name") and self.coupon_name is not None:
            params['couponName'] = self.coupon_name
        if hasattr(self, "coupon_description") and self.coupon_description is not None:
            params['couponDescription'] = self.coupon_description
        if hasattr(self, "coupon_expire_time") and self.coupon_expire_time is not None:
            params['couponExpireTime'] = self.coupon_expire_time
        if hasattr(self, "payment_method_detail_metadata") and self.payment_method_detail_metadata is not None:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'availableAmount' in response_body:
            self.__available_amount = Amount()
            self.__available_amount.parse_rsp_body(response_body['availableAmount'])
        if 'couponName' in response_body:
            self.__coupon_name = response_body['couponName']
        if 'couponDescription' in response_body:
            self.__coupon_description = response_body['couponDescription']
        if 'couponExpireTime' in response_body:
            self.__coupon_expire_time = response_body['couponExpireTime']
        if 'paymentMethodDetailMetadata' in response_body:
            self.__payment_method_detail_metadata = response_body['paymentMethodDetailMetadata']
