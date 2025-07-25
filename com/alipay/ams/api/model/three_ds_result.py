import json




class ThreeDSResult:
    def __init__(self):
        
        self.__three_ds_version = None  # type: str
        self.__eci = None  # type: str
        self.__cavv = None  # type: str
        self.__ds_transaction_id = None  # type: str
        self.__xid = None  # type: str
        

    @property
    def three_ds_version(self):
        """
        The version of 3D Secure protocol
        """
        return self.__three_ds_version

    @three_ds_version.setter
    def three_ds_version(self, value):
        self.__three_ds_version = value
    @property
    def eci(self):
        """
        Electronic Commerce Indicator (ECI) that is returned by the card scheme
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value
    @property
    def cavv(self):
        """
        The cardholder authentication value
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value
    @property
    def ds_transaction_id(self):
        """
        dsTransactionId
        """
        return self.__ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, value):
        self.__ds_transaction_id = value
    @property
    def xid(self):
        """
        The unique transaction identifier assigned by the Directory Server (DS) for 3D Secure authentication
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value


    

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
        if hasattr(self, "xid") and self.xid is not None:
            params['xid'] = self.xid
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
        if 'xid' in response_body:
            self.__xid = response_body['xid']
