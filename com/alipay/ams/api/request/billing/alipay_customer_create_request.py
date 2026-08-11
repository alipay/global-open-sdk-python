import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCustomerCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomerCreateRequest, self).__init__("/ams/api/v1/billing/customer/create") 

        self.__customer_request_id = None  # type: str
        self.__reference_customer_id = None  # type: str
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
        self.__shipping_zipcode = None  # type: str
        self.__description = None  # type: str
        self.__currency = None  # type: str
        self.__preferred_locales = None  # type: [str]
        self.__default_payment_method = None  # type: str
        self.__metadata = None  # type: str
        self.__phone_no = None  # type: str
        self.__country_code = None  # type: str
        self.__billing_email = None  # type: str
        self.__shipping_first_name = None  # type: str
        self.__shipping_last_name = None  # type: str
        self.__shipping_country_code = None  # type: str
        

    @property
    def customer_request_id(self):
        """
        Merchant-supplied idempotency key for this create request. Must be unique per merchant. Cannot be empty. Maximum length: 64 characters.
        """
        return self.__customer_request_id

    @customer_request_id.setter
    def customer_request_id(self, value):
        self.__customer_request_id = value
    @property
    def reference_customer_id(self):
        """
        Merchant&#39;s own customer identifier in their system. Used for cross-system reference. Maximum length: 32 characters.
        """
        return self.__reference_customer_id

    @reference_customer_id.setter
    def reference_customer_id(self, value):
        self.__reference_customer_id = value
    @property
    def alipay_user_id(self):
        """
        Alipay user ID bound to this customer. Used to associate the Antom customer profile with an Alipay account, enabling channel routing to Alipay payment methods and risk identification. Antom-specific field - see Section 4.2.3.3 for competitor comparison. Maximum length: 64 characters.
        """
        return self.__alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self.__alipay_user_id = value
    @property
    def email(self):
        """
        Customer&#39;s email address. Required - a missing or blank value returns &#x60;PARAM_ILLEGAL&#x60;. No email-format validation is applied; any non-blank string is accepted. Maximum length: 256 characters.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def first_name(self):
        """
        Customer&#39;s first name. Maximum length: 256 characters.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @property
    def last_name(self):
        """
        Customer&#39;s last name. Maximum length: 256 characters.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @property
    def country(self):
        """
        Billing address country code. Format: ISO 3166-1 alpha-2 (e.g. &#x60;US&#x60;, &#x60;SG&#x60;). Maximum length: 2 characters.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def state(self):
        """
        Billing address state/province. Maximum length: 128 characters.
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
    @property
    def city(self):
        """
        Billing address city. Maximum length: 256 characters.
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
    @property
    def address(self):
        """
        Billing address street line 1. Maximum length: 1024 characters.
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    @property
    def address_detail(self):
        """
        Billing address street line 2 / additional detail. Maximum length: 2048 characters.
        """
        return self.__address_detail

    @address_detail.setter
    def address_detail(self, value):
        self.__address_detail = value
    @property
    def zipcode(self):
        """
        Billing address postal/zip code. Maximum length: 32 characters.
        """
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, value):
        self.__zipcode = value
    @property
    def shipping_phone(self):
        """
        Recipient phone number for shipping. Maximum length: 32 characters.
        """
        return self.__shipping_phone

    @shipping_phone.setter
    def shipping_phone(self, value):
        self.__shipping_phone = value
    @property
    def shipping_country(self):
        """
        Shipping address country code. Format: ISO 3166-1 alpha-2. Maximum length: 2 characters.
        """
        return self.__shipping_country

    @shipping_country.setter
    def shipping_country(self, value):
        self.__shipping_country = value
    @property
    def shipping_state(self):
        """
        Shipping address state/province. Maximum length: 128 characters.
        """
        return self.__shipping_state

    @shipping_state.setter
    def shipping_state(self, value):
        self.__shipping_state = value
    @property
    def shipping_city(self):
        """
        Shipping address city. Maximum length: 256 characters.
        """
        return self.__shipping_city

    @shipping_city.setter
    def shipping_city(self, value):
        self.__shipping_city = value
    @property
    def shipping_address(self):
        """
        Shipping address street line 1. Maximum length: 1024 characters.
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def shipping_address_detail(self):
        """
        Shipping address street line 2 / additional detail. Maximum length: 2048 characters.
        """
        return self.__shipping_address_detail

    @shipping_address_detail.setter
    def shipping_address_detail(self, value):
        self.__shipping_address_detail = value
    @property
    def shipping_zipcode(self):
        """
        Shipping address postal/zip code. Maximum length: 32 characters.
        """
        return self.__shipping_zipcode

    @shipping_zipcode.setter
    def shipping_zipcode(self, value):
        self.__shipping_zipcode = value
    @property
    def description(self):
        """
        Free-text description for the customer record. Maximum length: 1024 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def currency(self):
        """
        Customer&#39;s default currency. Format: ISO 4217 alphabetic code (e.g. &#x60;USD&#x60;, &#x60;SGD&#x60;). Maximum length: 3 characters.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def preferred_locales(self):
        """
        Customer&#39;s preferred locale(s) for communications (e.g. &#x60;[\&quot;en-US\&quot;, \&quot;fr-FR\&quot;]&#x60;). Maximum size: 5 elements.
        """
        return self.__preferred_locales

    @preferred_locales.setter
    def preferred_locales(self, value):
        self.__preferred_locales = value
    @property
    def default_payment_method(self):
        """
        Default payment method token for recurring charges. Any non-blank value at create time is rejected with &#x60;PARAM_ILLEGAL&#x60; (\&quot;defaultPaymentMethod cannot be set during customer creation; create the customer first and then update its default payment method\&quot;). Set this field via &#x60;customer.update&#x60; after creation. Maximum length: 64 characters.
        """
        return self.__default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, value):
        self.__default_payment_method = value
    @property
    def metadata(self):
        """
        Merchant-defined metadata encoded as a JSON object string. Maximum length: 500 characters. A non-empty value must contain a valid JSON object string.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def phone_no(self):
        """
        Customer&#39;s phone number (digits only). Maximum length: 32 characters. Cross-field constraint: when &#x60;phoneNo&#x60; is provided, &#x60;countryCode&#x60; is required; omitting it returns &#x60;PARAM_ILLEGAL&#x60;.
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with &#x60;phoneNo&#x60; (NOT a numeric dial prefix). Required when &#x60;phoneNo&#x60; is provided. Maximum length: 2 characters.
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
    @property
    def billing_email(self):
        """
        Invoice recipient email address (independent of account &#x60;email&#x60;). Maximum length: 256 characters.
        """
        return self.__billing_email

    @billing_email.setter
    def billing_email(self, value):
        self.__billing_email = value
    @property
    def shipping_first_name(self):
        """
        Shipping recipient first name. Maximum length: 256 characters.
        """
        return self.__shipping_first_name

    @shipping_first_name.setter
    def shipping_first_name(self, value):
        self.__shipping_first_name = value
    @property
    def shipping_last_name(self):
        """
        Shipping recipient last name. Maximum length: 256 characters.
        """
        return self.__shipping_last_name

    @shipping_last_name.setter
    def shipping_last_name(self, value):
        self.__shipping_last_name = value
    @property
    def shipping_country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with &#x60;phoneNo&#x60;. Required when &#x60;shippingPhone&#x60; is provided. Maximum length: 2 characters.
        """
        return self.__shipping_country_code

    @shipping_country_code.setter
    def shipping_country_code(self, value):
        self.__shipping_country_code = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_request_id") and self.customer_request_id is not None:
            params['customerRequestId'] = self.customer_request_id
        if hasattr(self, "reference_customer_id") and self.reference_customer_id is not None:
            params['referenceCustomerId'] = self.reference_customer_id
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
        if hasattr(self, "shipping_zipcode") and self.shipping_zipcode is not None:
            params['shippingZipcode'] = self.shipping_zipcode
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "preferred_locales") and self.preferred_locales is not None:
            params['preferredLocales'] = self.preferred_locales
        if hasattr(self, "default_payment_method") and self.default_payment_method is not None:
            params['defaultPaymentMethod'] = self.default_payment_method
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
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerRequestId' in response_body:
            self.__customer_request_id = response_body['customerRequestId']
        if 'referenceCustomerId' in response_body:
            self.__reference_customer_id = response_body['referenceCustomerId']
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
        if 'shippingZipcode' in response_body:
            self.__shipping_zipcode = response_body['shippingZipcode']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'preferredLocales' in response_body:
            self.__preferred_locales = response_body['preferredLocales']
        if 'defaultPaymentMethod' in response_body:
            self.__default_payment_method = response_body['defaultPaymentMethod']
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
