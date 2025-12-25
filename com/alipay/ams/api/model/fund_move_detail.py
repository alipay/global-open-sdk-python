import json




class FundMoveDetail:
    def __init__(self):
        
        self.__memo = None  # type: str
        self.__reference_transaction_id = None  # type: str
        self.__payer_asset_id = None  # type: str
        self.__beneficiary_asset_id = None  # type: str
        

    @property
    def memo(self):
        """Gets the memo of this FundMoveDetail.
        
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def reference_transaction_id(self):
        """Gets the reference_transaction_id of this FundMoveDetail.
        
        """
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value
    @property
    def payer_asset_id(self):
        """Gets the payer_asset_id of this FundMoveDetail.
        
        """
        return self.__payer_asset_id

    @payer_asset_id.setter
    def payer_asset_id(self, value):
        self.__payer_asset_id = value
    @property
    def beneficiary_asset_id(self):
        """Gets the beneficiary_asset_id of this FundMoveDetail.
        
        """
        return self.__beneficiary_asset_id

    @beneficiary_asset_id.setter
    def beneficiary_asset_id(self, value):
        self.__beneficiary_asset_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "reference_transaction_id") and self.reference_transaction_id is not None:
            params['referenceTransactionId'] = self.reference_transaction_id
        if hasattr(self, "payer_asset_id") and self.payer_asset_id is not None:
            params['payerAssetId'] = self.payer_asset_id
        if hasattr(self, "beneficiary_asset_id") and self.beneficiary_asset_id is not None:
            params['beneficiaryAssetId'] = self.beneficiary_asset_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'referenceTransactionId' in response_body:
            self.__reference_transaction_id = response_body['referenceTransactionId']
        if 'payerAssetId' in response_body:
            self.__payer_asset_id = response_body['payerAssetId']
        if 'beneficiaryAssetId' in response_body:
            self.__beneficiary_asset_id = response_body['beneficiaryAssetId']
