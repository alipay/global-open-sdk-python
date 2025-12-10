import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.delivery_estimate import DeliveryEstimate




class Shipping:
    def __init__(self):
        
        self.__shipping_name = None  # type: UserName
        self.__shipping_address = None  # type: Address
        self.__shipping_carrier = None  # type: str
        self.__shipping_phone_no = None  # type: str
        self.__ship_to_email = None  # type: str
        self.__shipping_fee_id = None  # type: str
        self.__shipping_fee = None  # type: Amount
        self.__shipping_description = None  # type: str
        self.__delivery_estimate = None  # type: DeliveryEstimate
        self.__shipping_number = None  # type: str
        self.__notes = None  # type: str
        

    @property
    def shipping_name(self):
        """Gets the shipping_name of this Shipping.
        
        """
        return self.__shipping_name

    @shipping_name.setter
    def shipping_name(self, value):
        self.__shipping_name = value
    @property
    def shipping_address(self):
        """Gets the shipping_address of this Shipping.
        
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def shipping_carrier(self):
        """
        The delivery service provider for shipping a physical product, such as FedEx, UPS, or USPS.   Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Maximum length: 128 characters
        """
        return self.__shipping_carrier

    @shipping_carrier.setter
    def shipping_carrier(self, value):
        self.__shipping_carrier = value
    @property
    def shipping_phone_no(self):
        """
        The phone number of a recipient (including extension).  Specify this parameter when you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Maximum length: 16 characters
        """
        return self.__shipping_phone_no

    @shipping_phone_no.setter
    def shipping_phone_no(self, value):
        self.__shipping_phone_no = value
    @property
    def ship_to_email(self):
        """
        The email address where virtual goods are sent.  Specify this parameter when one of the following conditions is met:  if you require risk control. if you are a digital and entertainment merchant. Providing this information helps to increase fraud and identity theft detection.    More information:  Maximum length: 64 characters
        """
        return self.__ship_to_email

    @ship_to_email.setter
    def ship_to_email(self, value):
        self.__ship_to_email = value
    @property
    def shipping_fee_id(self):
        """
        The ID of the shipping fee used for identifying the shipping option.  More information:  Maximum length: 64 characters
        """
        return self.__shipping_fee_id

    @shipping_fee_id.setter
    def shipping_fee_id(self, value):
        self.__shipping_fee_id = value
    @property
    def shipping_fee(self):
        """Gets the shipping_fee of this Shipping.
        
        """
        return self.__shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        self.__shipping_fee = value
    @property
    def shipping_description(self):
        """
        Extended information about logistics-related services, including shipping time, logistics companies, etc.  More information:  Maximum length: 64 characters
        """
        return self.__shipping_description

    @shipping_description.setter
    def shipping_description(self, value):
        self.__shipping_description = value
    @property
    def delivery_estimate(self):
        """Gets the delivery_estimate of this Shipping.
        
        """
        return self.__delivery_estimate

    @delivery_estimate.setter
    def delivery_estimate(self, value):
        self.__delivery_estimate = value
    @property
    def shipping_number(self):
        """
        Added field for shipping number
        """
        return self.__shipping_number

    @shipping_number.setter
    def shipping_number(self, value):
        self.__shipping_number = value
    @property
    def notes(self):
        """
        Added field for shipping notes
        """
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "shipping_name") and self.shipping_name is not None:
            params['shippingName'] = self.shipping_name
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "shipping_carrier") and self.shipping_carrier is not None:
            params['shippingCarrier'] = self.shipping_carrier
        if hasattr(self, "shipping_phone_no") and self.shipping_phone_no is not None:
            params['shippingPhoneNo'] = self.shipping_phone_no
        if hasattr(self, "ship_to_email") and self.ship_to_email is not None:
            params['shipToEmail'] = self.ship_to_email
        if hasattr(self, "shipping_fee_id") and self.shipping_fee_id is not None:
            params['shippingFeeId'] = self.shipping_fee_id
        if hasattr(self, "shipping_fee") and self.shipping_fee is not None:
            params['shippingFee'] = self.shipping_fee
        if hasattr(self, "shipping_description") and self.shipping_description is not None:
            params['shippingDescription'] = self.shipping_description
        if hasattr(self, "delivery_estimate") and self.delivery_estimate is not None:
            params['deliveryEstimate'] = self.delivery_estimate
        if hasattr(self, "shipping_number") and self.shipping_number is not None:
            params['shippingNumber'] = self.shipping_number
        if hasattr(self, "notes") and self.notes is not None:
            params['notes'] = self.notes
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'shippingName' in response_body:
            self.__shipping_name = UserName()
            self.__shipping_name.parse_rsp_body(response_body['shippingName'])
        if 'shippingAddress' in response_body:
            self.__shipping_address = Address()
            self.__shipping_address.parse_rsp_body(response_body['shippingAddress'])
        if 'shippingCarrier' in response_body:
            self.__shipping_carrier = response_body['shippingCarrier']
        if 'shippingPhoneNo' in response_body:
            self.__shipping_phone_no = response_body['shippingPhoneNo']
        if 'shipToEmail' in response_body:
            self.__ship_to_email = response_body['shipToEmail']
        if 'shippingFeeId' in response_body:
            self.__shipping_fee_id = response_body['shippingFeeId']
        if 'shippingFee' in response_body:
            self.__shipping_fee = Amount()
            self.__shipping_fee.parse_rsp_body(response_body['shippingFee'])
        if 'shippingDescription' in response_body:
            self.__shipping_description = response_body['shippingDescription']
        if 'deliveryEstimate' in response_body:
            self.__delivery_estimate = DeliveryEstimate()
            self.__delivery_estimate.parse_rsp_body(response_body['deliveryEstimate'])
        if 'shippingNumber' in response_body:
            self.__shipping_number = response_body['shippingNumber']
        if 'notes' in response_body:
            self.__notes = response_body['notes']
