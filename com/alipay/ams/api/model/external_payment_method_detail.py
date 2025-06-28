import json




class ExternalPaymentMethodDetail:
    def __init__(self):
        
        self.__asset_token = None  # type: str
        self.__account_display_name = None  # type: str
        self.__disable_reason = None  # type: str
        self.__payment_method_detail_metadata = None  # type: str
        

    @property
    def asset_token(self):
        """Gets the asset_token of this ExternalPaymentMethodDetail.
        
        """
        return self.__asset_token

    @asset_token.setter
    def asset_token(self, value):
        self.__asset_token = value
    @property
    def account_display_name(self):
        """Gets the account_display_name of this ExternalPaymentMethodDetail.
        
        """
        return self.__account_display_name

    @account_display_name.setter
    def account_display_name(self, value):
        self.__account_display_name = value
    @property
    def disable_reason(self):
        """Gets the disable_reason of this ExternalPaymentMethodDetail.
        
        """
        return self.__disable_reason

    @disable_reason.setter
    def disable_reason(self, value):
        self.__disable_reason = value
    @property
    def payment_method_detail_metadata(self):
        """Gets the payment_method_detail_metadata of this ExternalPaymentMethodDetail.
        
        """
        return self.__payment_method_detail_metadata

    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "asset_token") and self.asset_token is not None:
            params['assetToken'] = self.asset_token
        if hasattr(self, "account_display_name") and self.account_display_name is not None:
            params['accountDisplayName'] = self.account_display_name
        if hasattr(self, "disable_reason") and self.disable_reason is not None:
            params['disableReason'] = self.disable_reason
        if hasattr(self, "payment_method_detail_metadata") and self.payment_method_detail_metadata is not None:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'assetToken' in response_body:
            self.__asset_token = response_body['assetToken']
        if 'accountDisplayName' in response_body:
            self.__account_display_name = response_body['accountDisplayName']
        if 'disableReason' in response_body:
            self.__disable_reason = response_body['disableReason']
        if 'paymentMethodDetailMetadata' in response_body:
            self.__payment_method_detail_metadata = response_body['paymentMethodDetailMetadata']
