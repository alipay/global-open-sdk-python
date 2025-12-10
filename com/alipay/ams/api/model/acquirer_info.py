import json




class AcquirerInfo:
    def __init__(self):
        
        self.__acquirer_name = None  # type: str
        self.__reference_request_id = None  # type: str
        self.__acquirer_transaction_id = None  # type: str
        self.__acquirer_merchant_id = None  # type: str
        self.__acquirer_result_code = None  # type: str
        self.__acquirer_result_message = None  # type: str
        self.__acquirer_merchant_name = None  # type: str
        self.__acquirer_reason_description = None  # type: str
        

    @property
    def acquirer_name(self):
        """
        The name of the acquirer.   Note: This parameter is returned if you integrate the APO product.    More information:  Maximum length: 64 characters
        """
        return self.__acquirer_name

    @acquirer_name.setter
    def acquirer_name(self, value):
        self.__acquirer_name = value
    @property
    def reference_request_id(self):
        """
        The unique ID that is assigned by APO to identify a payment request sent to the acquirer.  Note: This parameter is returned if you integrate the APO product.    More information:  Maximum length: 64 characters
        """
        return self.__reference_request_id

    @reference_request_id.setter
    def reference_request_id(self, value):
        self.__reference_request_id = value
    @property
    def acquirer_transaction_id(self):
        """
        The unique ID that is assigned by the acquirer to identify a transaction.   Note: This parameter is returned if you integrate the APO product.  More information:  Maximum length: 64 characters
        """
        return self.__acquirer_transaction_id

    @acquirer_transaction_id.setter
    def acquirer_transaction_id(self, value):
        self.__acquirer_transaction_id = value
    @property
    def acquirer_merchant_id(self):
        """
        The unique ID that is assigned by the acquirer to identify a merchant.   Note: This parameter is returned if you integrate the APO product.    More information:  Maximum length: 64 characters 
        """
        return self.__acquirer_merchant_id

    @acquirer_merchant_id.setter
    def acquirer_merchant_id(self, value):
        self.__acquirer_merchant_id = value
    @property
    def acquirer_result_code(self):
        """
        The acquirer&#39;s result code that indicates the transaction process result.    Note: This parameter is returned if you integrate the APO product.  More information:  Maximum length: 64 characters
        """
        return self.__acquirer_result_code

    @acquirer_result_code.setter
    def acquirer_result_code(self, value):
        self.__acquirer_result_code = value
    @property
    def acquirer_result_message(self):
        """
        The result message that describes acquirerResultCode in detail.    Note: This parameter is returned if you integrate the APO product.  More information:  Maximum length: 64 characters
        """
        return self.__acquirer_result_message

    @acquirer_result_message.setter
    def acquirer_result_message(self, value):
        self.__acquirer_result_message = value
    @property
    def acquirer_merchant_name(self):
        """
        The merchant name registered with the acquirer
        """
        return self.__acquirer_merchant_name

    @acquirer_merchant_name.setter
    def acquirer_merchant_name(self, value):
        self.__acquirer_merchant_name = value
    @property
    def acquirer_reason_description(self):
        """
        The reason description provided by the acquirer
        """
        return self.__acquirer_reason_description

    @acquirer_reason_description.setter
    def acquirer_reason_description(self, value):
        self.__acquirer_reason_description = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "acquirer_name") and self.acquirer_name is not None:
            params['acquirerName'] = self.acquirer_name
        if hasattr(self, "reference_request_id") and self.reference_request_id is not None:
            params['referenceRequestId'] = self.reference_request_id
        if hasattr(self, "acquirer_transaction_id") and self.acquirer_transaction_id is not None:
            params['acquirerTransactionId'] = self.acquirer_transaction_id
        if hasattr(self, "acquirer_merchant_id") and self.acquirer_merchant_id is not None:
            params['acquirerMerchantId'] = self.acquirer_merchant_id
        if hasattr(self, "acquirer_result_code") and self.acquirer_result_code is not None:
            params['acquirerResultCode'] = self.acquirer_result_code
        if hasattr(self, "acquirer_result_message") and self.acquirer_result_message is not None:
            params['acquirerResultMessage'] = self.acquirer_result_message
        if hasattr(self, "acquirer_merchant_name") and self.acquirer_merchant_name is not None:
            params['acquirerMerchantName'] = self.acquirer_merchant_name
        if hasattr(self, "acquirer_reason_description") and self.acquirer_reason_description is not None:
            params['acquirerReasonDescription'] = self.acquirer_reason_description
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'acquirerName' in response_body:
            self.__acquirer_name = response_body['acquirerName']
        if 'referenceRequestId' in response_body:
            self.__reference_request_id = response_body['referenceRequestId']
        if 'acquirerTransactionId' in response_body:
            self.__acquirer_transaction_id = response_body['acquirerTransactionId']
        if 'acquirerMerchantId' in response_body:
            self.__acquirer_merchant_id = response_body['acquirerMerchantId']
        if 'acquirerResultCode' in response_body:
            self.__acquirer_result_code = response_body['acquirerResultCode']
        if 'acquirerResultMessage' in response_body:
            self.__acquirer_result_message = response_body['acquirerResultMessage']
        if 'acquirerMerchantName' in response_body:
            self.__acquirer_merchant_name = response_body['acquirerMerchantName']
        if 'acquirerReasonDescription' in response_body:
            self.__acquirer_reason_description = response_body['acquirerReasonDescription']
