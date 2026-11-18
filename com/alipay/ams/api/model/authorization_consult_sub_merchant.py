import json




class AuthorizationConsultSubMerchant:
    def __init__(self):
        
        self.__sub_merchant_service_name = None  # type: str
        self.__sub_merchant_service_description = None  # type: str
        

    @property
    def sub_merchant_service_name(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. The actual customer-facing service name displayed on the signing page.
        """
        return self.__sub_merchant_service_name

    @sub_merchant_service_name.setter
    def sub_merchant_service_name(self, value):
        self.__sub_merchant_service_name = value
    @property
    def sub_merchant_service_description(self):
        """
        Provide when seat or billing information must be displayed to the user; otherwise omit. Use accurate customer-facing seat/billing information, not unrelated personal information. Null or blank values are invalid.
        """
        return self.__sub_merchant_service_description

    @sub_merchant_service_description.setter
    def sub_merchant_service_description(self, value):
        self.__sub_merchant_service_description = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "sub_merchant_service_name") and self.sub_merchant_service_name is not None:
            params['subMerchantServiceName'] = self.sub_merchant_service_name
        if hasattr(self, "sub_merchant_service_description") and self.sub_merchant_service_description is not None:
            params['subMerchantServiceDescription'] = self.sub_merchant_service_description
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subMerchantServiceName' in response_body:
            self.__sub_merchant_service_name = response_body['subMerchantServiceName']
        if 'subMerchantServiceDescription' in response_body:
            self.__sub_merchant_service_description = response_body['subMerchantServiceDescription']
