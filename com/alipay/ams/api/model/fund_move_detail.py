import json


class FundMoveDetail(object):
    def __init__(self):
        self.__memo = None
        self.__reference_transaction_id = None

    @property
    def memo(self):
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value

    @property
    def reference_transaction_id(self):
        return self.__reference_transaction_id


    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "memo") and self.memo:
            params['memo'] = self.memo
        if hasattr(self, "reference_transaction_id") and self.reference_transaction_id:
            params['referenceTransactionId'] = self.reference_transaction_id
        return params

    def parse_rsp_body(self, fundMoveDetail_body):
        if type(fundMoveDetail_body) == str:
            fundMoveDetail_body = json.loads(fundMoveDetail_body)

        if 'memo' in fundMoveDetail_body:
            self.__memo = fundMoveDetail_body['memo']

        if 'referenceTransactionId' in fundMoveDetail_body:
            self.__reference_transaction_id = fundMoveDetail_body['referenceTransactionId']