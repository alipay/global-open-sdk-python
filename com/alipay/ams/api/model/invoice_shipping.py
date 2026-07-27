import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.delivery_estimate import DeliveryEstimate




class InvoiceShipping:
    def __init__(self):
        
        self.__shipping_name = None  # type: UserName
        self.__shipping_address = None  # type: Address
        self.__shipping_carrier = None  # type: str
        self.__shipping_number = None  # type: str
        self.__shipping_phone_no = None  # type: str
        self.__ship_to_email = None  # type: str
        self.__notes = None  # type: str
        self.__shipping_fee_id = None  # type: str
        self.__shipping_fee = None  # type: Amount
        self.__shipping_description = None  # type: str
        self.__delivery_estimate = None  # type: DeliveryEstimate
        self.__tracking_url = None  # type: str
        self.__shipping_method_indicator = None  # type: str
        

    @property
    def shipping_name(self):
        """Gets the shipping_name of this InvoiceShipping.
        
        """
        return self.__shipping_name

    @shipping_name.setter
    def shipping_name(self, value):
        self.__shipping_name = value
    @property
    def shipping_address(self):
        """Gets the shipping_address of this InvoiceShipping.
        
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def shipping_carrier(self):
        """
        The shipping carrier. Maximum length: 128 characters.
        """
        return self.__shipping_carrier

    @shipping_carrier.setter
    def shipping_carrier(self, value):
        self.__shipping_carrier = value
    @property
    def shipping_number(self):
        """
        The shipping number. Maximum length: 128 characters.
        """
        return self.__shipping_number

    @shipping_number.setter
    def shipping_number(self, value):
        self.__shipping_number = value
    @property
    def shipping_phone_no(self):
        """
        The shipping phone no. Maximum length: 16 characters.
        """
        return self.__shipping_phone_no

    @shipping_phone_no.setter
    def shipping_phone_no(self, value):
        self.__shipping_phone_no = value
    @property
    def ship_to_email(self):
        """
        The ship to email. Maximum length: 256 characters.
        """
        return self.__ship_to_email

    @ship_to_email.setter
    def ship_to_email(self, value):
        self.__ship_to_email = value
    @property
    def notes(self):
        """
        The notes. Maximum length: 512 characters.
        """
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value
    @property
    def shipping_fee_id(self):
        """
        The shipping fee id. Maximum length: 64 characters.
        """
        return self.__shipping_fee_id

    @shipping_fee_id.setter
    def shipping_fee_id(self, value):
        self.__shipping_fee_id = value
    @property
    def shipping_fee(self):
        """Gets the shipping_fee of this InvoiceShipping.
        
        """
        return self.__shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        self.__shipping_fee = value
    @property
    def shipping_description(self):
        """
        The shipping description. Maximum length: 256 characters.
        """
        return self.__shipping_description

    @shipping_description.setter
    def shipping_description(self, value):
        self.__shipping_description = value
    @property
    def delivery_estimate(self):
        """Gets the delivery_estimate of this InvoiceShipping.
        
        """
        return self.__delivery_estimate

    @delivery_estimate.setter
    def delivery_estimate(self, value):
        self.__delivery_estimate = value
    @property
    def tracking_url(self):
        """
        The tracking url. Maximum length: 2048 characters.
        """
        return self.__tracking_url

    @tracking_url.setter
    def tracking_url(self, value):
        self.__tracking_url = value
    @property
    def shipping_method_indicator(self):
        """
        The shipping method indicator. Maximum length: 32 characters.
        """
        return self.__shipping_method_indicator

    @shipping_method_indicator.setter
    def shipping_method_indicator(self, value):
        self.__shipping_method_indicator = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "shipping_name") and self.shipping_name is not None:
            params['shippingName'] = self.shipping_name
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "shipping_carrier") and self.shipping_carrier is not None:
            params['shippingCarrier'] = self.shipping_carrier
        if hasattr(self, "shipping_number") and self.shipping_number is not None:
            params['shippingNumber'] = self.shipping_number
        if hasattr(self, "shipping_phone_no") and self.shipping_phone_no is not None:
            params['shippingPhoneNo'] = self.shipping_phone_no
        if hasattr(self, "ship_to_email") and self.ship_to_email is not None:
            params['shipToEmail'] = self.ship_to_email
        if hasattr(self, "notes") and self.notes is not None:
            params['notes'] = self.notes
        if hasattr(self, "shipping_fee_id") and self.shipping_fee_id is not None:
            params['shippingFeeId'] = self.shipping_fee_id
        if hasattr(self, "shipping_fee") and self.shipping_fee is not None:
            params['shippingFee'] = self.shipping_fee
        if hasattr(self, "shipping_description") and self.shipping_description is not None:
            params['shippingDescription'] = self.shipping_description
        if hasattr(self, "delivery_estimate") and self.delivery_estimate is not None:
            params['deliveryEstimate'] = self.delivery_estimate
        if hasattr(self, "tracking_url") and self.tracking_url is not None:
            params['trackingUrl'] = self.tracking_url
        if hasattr(self, "shipping_method_indicator") and self.shipping_method_indicator is not None:
            params['shippingMethodIndicator'] = self.shipping_method_indicator
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
        if 'shippingNumber' in response_body:
            self.__shipping_number = response_body['shippingNumber']
        if 'shippingPhoneNo' in response_body:
            self.__shipping_phone_no = response_body['shippingPhoneNo']
        if 'shipToEmail' in response_body:
            self.__ship_to_email = response_body['shipToEmail']
        if 'notes' in response_body:
            self.__notes = response_body['notes']
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
        if 'trackingUrl' in response_body:
            self.__tracking_url = response_body['trackingUrl']
        if 'shippingMethodIndicator' in response_body:
            self.__shipping_method_indicator = response_body['shippingMethodIndicator']
