import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCustomerInquireDetailsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__customer_id = None  # type: str
        self.__customer_request_id = None  # type: str
        self.__alipay_user_id = None  # type: str
        self.__email = None  # type: str
        self.__first_name = None  # type: str
        self.__last_name = None  # type: str
        self.__country = None  # type: str
        self.__state = None  # type: str
        self.__city = None  # type: str
        self.__address = None  # type: str
        self.__address_detail = None  # type: str
        self.__zipcode = None  # type: str
        self.__shipping_phone = None  # type: str
        self.__shipping_country = None  # type: str
        self.__shipping_state = None  # type: str
        self.__shipping_city = None  # type: str
        self.__shipping_address = None  # type: str
        self.__shipping_address_detail = None  # type: str
        self.__description = None  # type: str
        self.__currency = None  # type: str
        self.__preferred_locales = None  # type: [str]
        self.__default_payment_method = None  # type: str
        self.__status = None  # type: str
        self.__reference_customer_id = None  # type: str
        self.__metadata = None  # type: str
        self.__phone_no = None  # type: str
        self.__country_code = None  # type: str
        self.__billing_email = None  # type: str
        self.__shipping_first_name = None  # type: str
        self.__shipping_last_name = None  # type: str
        self.__shipping_country_code = None  # type: str
        self.__shipping_zipcode = None  # type: str
        self.__gmt_create = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCustomerInquireDetailsResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def customer_id(self):
        """
        System-generated customer ID. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_request_id(self):
        """
        Merchant-supplied idempotency key used at creation. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__customer_request_id

    @customer_request_id.setter
    def customer_request_id(self, value):
        self.__customer_request_id = value
    @property
    def alipay_user_id(self):
        """
        Bound Alipay user ID for channel routing and risk control. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set; omitted (not returned as null) if not set.
        """
        return self.__alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self.__alipay_user_id = value
    @property
    def email(self):
        """
        Customer email address. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def first_name(self):
        """
        Customer first name. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        Customer last name. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def country(self):
        """
        Billing address country (ISO 3166-1 alpha-2). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def state(self):
        """
        Billing address state. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """
        Billing address city. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address(self):
        """
        Billing address street line 1. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    @property
    def address_detail(self):
        """
        Billing address street line 2. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__address_detail

    @address_detail.setter
    def address_detail(self, value):
        self.__address_detail = value
    @property
    def zipcode(self):
        """
        Billing address postal code. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, value):
        self.__zipcode = value
    @property
    def shipping_phone(self):
        """
        Shipping phone. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_phone

    @shipping_phone.setter
    def shipping_phone(self, value):
        self.__shipping_phone = value
    @property
    def shipping_country(self):
        """
        Shipping country (ISO 3166-1 alpha-2). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_country

    @shipping_country.setter
    def shipping_country(self, value):
        self.__shipping_country = value
    @property
    def shipping_state(self):
        """
        Shipping state. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_state

    @shipping_state.setter
    def shipping_state(self, value):
        self.__shipping_state = value
    @property
    def shipping_city(self):
        """
        Shipping city. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_city

    @shipping_city.setter
    def shipping_city(self, value):
        self.__shipping_city = value
    @property
    def shipping_address(self):
        """
        Shipping street line 1. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def shipping_address_detail(self):
        """
        Shipping street line 2. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_address_detail

    @shipping_address_detail.setter
    def shipping_address_detail(self, value):
        self.__shipping_address_detail = value
    @property
    def description(self):
        """
        Free-text description. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def currency(self):
        """
        Default currency (ISO 4217). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def preferred_locales(self):
        """
        Preferred locale(s). Maximum size: 5 elements. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__preferred_locales

    @preferred_locales.setter
    def preferred_locales(self, value):
        self.__preferred_locales = value
    @property
    def default_payment_method(self):
        """
        Default payment method token. Sourced from &#x60;defaultCustomerPaymentMethodId&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, value):
        self.__default_payment_method = value
    @property
    def status(self):
        """
        Customer status: &#x60;ACTIVE&#x60; / &#x60;DELETED&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def reference_customer_id(self):
        """
        Merchant&#39;s internal customer ID reference. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__reference_customer_id

    @reference_customer_id.setter
    def reference_customer_id(self, value):
        self.__reference_customer_id = value
    @property
    def metadata(self):
        """
        Merchant-defined metadata encoded as a JSON object string. Maximum length: 500 characters. Returned only when result.resultCode is SUCCESS and the field was set.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def phone_no(self):
        """
        Customer phone number (digits only). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with &#x60;phoneNo&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
    @property
    def billing_email(self):
        """
        Invoice recipient email (independent of account &#x60;email&#x60;). Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__billing_email

    @billing_email.setter
    def billing_email(self, value):
        self.__billing_email = value
    @property
    def shipping_first_name(self):
        """
        Shipping recipient first name. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_first_name

    @shipping_first_name.setter
    def shipping_first_name(self, value):
        self.__shipping_first_name = value
    @property
    def shipping_last_name(self):
        """
        Shipping recipient last name. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_last_name

    @shipping_last_name.setter
    def shipping_last_name(self, value):
        self.__shipping_last_name = value
    @property
    def shipping_country_code(self):
        """
        Shipping address numeric calling code. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_country_code

    @shipping_country_code.setter
    def shipping_country_code(self, value):
        self.__shipping_country_code = value
    @property
    def shipping_zipcode(self):
        """
        Shipping postal code. Wire name: &#x60;shippingZipcode&#x60;. Returned when resultCode is &#x60;SUCCESS&#x60; and the field was set.
        """
        return self.__shipping_zipcode

    @shipping_zipcode.setter
    def shipping_zipcode(self, value):
        self.__shipping_zipcode = value
    @property
    def gmt_create(self):
        """
        Customer creation timestamp. Note: there is NO &#x60;updateTime&#x60; / &#x60;gmtModified&#x60; field on &#x60;CustomerQueryDetailsResult&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_request_id") and self.customer_request_id is not None:
            params['customerRequestId'] = self.customer_request_id
        if hasattr(self, "alipay_user_id") and self.alipay_user_id is not None:
            params['alipayUserId'] = self.alipay_user_id
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "first_name") and self.first_name is not None:
            params['firstName'] = self.first_name
        if hasattr(self, "last_name") and self.last_name is not None:
            params['lastName'] = self.last_name
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "state") and self.state is not None:
            params['state'] = self.state
        if hasattr(self, "city") and self.city is not None:
            params['city'] = self.city
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        if hasattr(self, "address_detail") and self.address_detail is not None:
            params['addressDetail'] = self.address_detail
        if hasattr(self, "zipcode") and self.zipcode is not None:
            params['zipcode'] = self.zipcode
        if hasattr(self, "shipping_phone") and self.shipping_phone is not None:
            params['shippingPhone'] = self.shipping_phone
        if hasattr(self, "shipping_country") and self.shipping_country is not None:
            params['shippingCountry'] = self.shipping_country
        if hasattr(self, "shipping_state") and self.shipping_state is not None:
            params['shippingState'] = self.shipping_state
        if hasattr(self, "shipping_city") and self.shipping_city is not None:
            params['shippingCity'] = self.shipping_city
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "shipping_address_detail") and self.shipping_address_detail is not None:
            params['shippingAddressDetail'] = self.shipping_address_detail
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "preferred_locales") and self.preferred_locales is not None:
            params['preferredLocales'] = self.preferred_locales
        if hasattr(self, "default_payment_method") and self.default_payment_method is not None:
            params['defaultPaymentMethod'] = self.default_payment_method
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "reference_customer_id") and self.reference_customer_id is not None:
            params['referenceCustomerId'] = self.reference_customer_id
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "phone_no") and self.phone_no is not None:
            params['phoneNo'] = self.phone_no
        if hasattr(self, "country_code") and self.country_code is not None:
            params['countryCode'] = self.country_code
        if hasattr(self, "billing_email") and self.billing_email is not None:
            params['billingEmail'] = self.billing_email
        if hasattr(self, "shipping_first_name") and self.shipping_first_name is not None:
            params['shippingFirstName'] = self.shipping_first_name
        if hasattr(self, "shipping_last_name") and self.shipping_last_name is not None:
            params['shippingLastName'] = self.shipping_last_name
        if hasattr(self, "shipping_country_code") and self.shipping_country_code is not None:
            params['shippingCountryCode'] = self.shipping_country_code
        if hasattr(self, "shipping_zipcode") and self.shipping_zipcode is not None:
            params['shippingZipcode'] = self.shipping_zipcode
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCustomerInquireDetailsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerRequestId' in response_body:
            self.__customer_request_id = response_body['customerRequestId']
        if 'alipayUserId' in response_body:
            self.__alipay_user_id = response_body['alipayUserId']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'firstName' in response_body:
            self.__first_name = response_body['firstName']
        if 'lastName' in response_body:
            self.__last_name = response_body['lastName']
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'state' in response_body:
            self.__state = response_body['state']
        if 'city' in response_body:
            self.__city = response_body['city']
        if 'address' in response_body:
            self.__address = response_body['address']
        if 'addressDetail' in response_body:
            self.__address_detail = response_body['addressDetail']
        if 'zipcode' in response_body:
            self.__zipcode = response_body['zipcode']
        if 'shippingPhone' in response_body:
            self.__shipping_phone = response_body['shippingPhone']
        if 'shippingCountry' in response_body:
            self.__shipping_country = response_body['shippingCountry']
        if 'shippingState' in response_body:
            self.__shipping_state = response_body['shippingState']
        if 'shippingCity' in response_body:
            self.__shipping_city = response_body['shippingCity']
        if 'shippingAddress' in response_body:
            self.__shipping_address = response_body['shippingAddress']
        if 'shippingAddressDetail' in response_body:
            self.__shipping_address_detail = response_body['shippingAddressDetail']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'preferredLocales' in response_body:
            self.__preferred_locales = response_body['preferredLocales']
        if 'defaultPaymentMethod' in response_body:
            self.__default_payment_method = response_body['defaultPaymentMethod']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'referenceCustomerId' in response_body:
            self.__reference_customer_id = response_body['referenceCustomerId']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'phoneNo' in response_body:
            self.__phone_no = response_body['phoneNo']
        if 'countryCode' in response_body:
            self.__country_code = response_body['countryCode']
        if 'billingEmail' in response_body:
            self.__billing_email = response_body['billingEmail']
        if 'shippingFirstName' in response_body:
            self.__shipping_first_name = response_body['shippingFirstName']
        if 'shippingLastName' in response_body:
            self.__shipping_last_name = response_body['shippingLastName']
        if 'shippingCountryCode' in response_body:
            self.__shipping_country_code = response_body['shippingCountryCode']
        if 'shippingZipcode' in response_body:
            self.__shipping_zipcode = response_body['shippingZipcode']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
