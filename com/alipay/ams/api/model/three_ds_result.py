import json


class ThreeDSResult(object):
    def __init__(self):
        self.__three_ds_version = None
        self.__eci = None
        self.__cavv = None
        self.__ds_transaction_id = None
        self.__xid = None

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
    def xid(self):
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value

    def to_ams_dict(self):
        param = dict()
        if hasattr(self, 'three_ds_version') and self.three_ds_version:
            param['threeDSVersion'] = self.three_ds_version
        if hasattr(self, 'eci') and self.eci:
            param['eci'] = self.eci
        if hasattr(self, 'cavv') and self.cavv:
            param['cavv'] = self.cavv
        if hasattr(self, 'ds_transaction_id') and self.ds_transaction_id:
            param['dsTransactionId'] = self.ds_transaction_id
        if hasattr(self, 'xid') and self.xid:
            param['xid'] = self.xid
        return param

    def parse_rsp_body(self, three_dS_result_body):
        if type(three_dS_result_body) == str:
            three_dS_result_body = json.loads(three_dS_result_body)
        if 'threeDSVersion' in three_dS_result_body:
            self.three_ds_version = three_dS_result_body['threeDSVersion']
        if 'eci' in three_dS_result_body:
            self.eci = three_dS_result_body['eci']
        if 'cavv' in three_dS_result_body:
            self.cavv = three_dS_result_body['cavv']
        if 'dsTransactionId' in three_dS_result_body:
            self.ds_transaction_id = three_dS_result_body['dsTransactionId']
        if 'xid' in three_dS_result_body:
            self.xid = three_dS_result_body['xid']
