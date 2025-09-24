import json


class MpiData(object):

    def __init__(self):
        self.__three_ds_version = None
        self.eci = None
        self.cavv = None
        self.ds_transaction_id = None
        self.credential_type = None

    @property
    def three_ds_version(self):
        return self.__three_ds_version

    @three_ds_version.setter
    def three_ds_version(self, value):
        self.__three_ds_version = value


    @property
    def eci(self):
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value


    @property
    def cavv(self):
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value


    @property
    def ds_transaction_id(self):
        return self.__ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, value):
        self.__ds_transaction_id = value

    @property
    def credential_type(self):
        return self.__credential_type

    @credential_type.setter
    def credential_type(self, value):
        self.__credential_type = value


    def to_ams_dict(self):
        ams_dict = {}
        if self.three_ds_version:
            ams_dict['threeDSVersion'] = self.three_ds_version
        if self.eci:
            ams_dict['eci'] = self.eci
        if self.cavv:
            ams_dict['cavv'] = self.cavv
        if self.ds_transaction_id:
            ams_dict['dsTransactionId'] = self.ds_transaction_id
        if self.credential_type:
            ams_dict['credentialType'] = self.credential_type
        return ams_dict


    def parse_rsp_body(self, response_body):
        if type(response_body) == str:
            response_body = json.loads(response_body)
            if 'threeDSVersion' in response_body:
                self.three_ds_version = response_body['threeDSVersion']
            if 'eci' in response_body:
                self.eci = response_body['eci']
            if 'cavv' in response_body:
                self.cavv = response_body['cavv']
            if 'dsTransactionId' in response_body:
                self.ds_transaction_id = response_body['dsTransactionId']
            if 'credentialType' in response_body:
                self.credential_type = response_body['credentialType']

