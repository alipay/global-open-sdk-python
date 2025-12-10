import json




class MpiData:
    def __init__(self):
        
        self.__three_ds_version = None  # type: str
        self.__eci = None  # type: str
        self.__cavv = None  # type: str
        self.__ds_transaction_id = None  # type: str
        self.__credential_type = None  # type: str
        

    @property
    def three_ds_version(self):
        """Gets the three_ds_version of this MpiData.
        
        """
        return self.__three_ds_version

    @three_ds_version.setter
    def three_ds_version(self, value):
        self.__three_ds_version = value
    @property
    def eci(self):
        """Gets the eci of this MpiData.
        
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value
    @property
    def cavv(self):
        """Gets the cavv of this MpiData.
        
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value
    @property
    def ds_transaction_id(self):
        """Gets the ds_transaction_id of this MpiData.
        
        """
        return self.__ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, value):
        self.__ds_transaction_id = value
    @property
    def credential_type(self):
        """Gets the credential_type of this MpiData.
        
        """
        return self.__credential_type

    @credential_type.setter
    def credential_type(self, value):
        self.__credential_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "three_ds_version") and self.three_ds_version is not None:
            params['threeDSVersion'] = self.three_ds_version
        if hasattr(self, "eci") and self.eci is not None:
            params['eci'] = self.eci
        if hasattr(self, "cavv") and self.cavv is not None:
            params['cavv'] = self.cavv
        if hasattr(self, "ds_transaction_id") and self.ds_transaction_id is not None:
            params['dsTransactionId'] = self.ds_transaction_id
        if hasattr(self, "credential_type") and self.credential_type is not None:
            params['credentialType'] = self.credential_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'threeDSVersion' in response_body:
            self.__three_ds_version = response_body['threeDSVersion']
        if 'eci' in response_body:
            self.__eci = response_body['eci']
        if 'cavv' in response_body:
            self.__cavv = response_body['cavv']
        if 'dsTransactionId' in response_body:
            self.__ds_transaction_id = response_body['dsTransactionId']
        if 'credentialType' in response_body:
            self.__credential_type = response_body['credentialType']
