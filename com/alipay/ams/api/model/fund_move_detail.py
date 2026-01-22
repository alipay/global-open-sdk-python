import json




class FundMoveDetail:
    def __init__(self):
        
        self.__move_type = None  # type: str
        self.__source_account = None  # type: str
        self.__target_account = None  # type: str
        self.__move_time = None  # type: str
        self.__memo = None  # type: str
        self.__reference_transaction_id = None  # type: str
        self.__payer_asset_id = None  # type: str
        self.__beneficiary_asset_id = None  # type: str
        

    @property
    def move_type(self):
        """Gets the move_type of this FundMoveDetail.
        
        """
        return self.__move_type

    @move_type.setter
    def move_type(self, value):
        self.__move_type = value
    @property
    def source_account(self):
        """Gets the source_account of this FundMoveDetail.
        
        """
        return self.__source_account

    @source_account.setter
    def source_account(self, value):
        self.__source_account = value
    @property
    def target_account(self):
        """Gets the target_account of this FundMoveDetail.
        
        """
        return self.__target_account

    @target_account.setter
    def target_account(self, value):
        self.__target_account = value
    @property
    def move_time(self):
        """Gets the move_time of this FundMoveDetail.
        
        """
        return self.__move_time

    @move_time.setter
    def move_time(self, value):
        self.__move_time = value
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
        if hasattr(self, "move_type") and self.move_type is not None:
            params['moveType'] = self.move_type
        if hasattr(self, "source_account") and self.source_account is not None:
            params['sourceAccount'] = self.source_account
        if hasattr(self, "target_account") and self.target_account is not None:
            params['targetAccount'] = self.target_account
        if hasattr(self, "move_time") and self.move_time is not None:
            params['moveTime'] = self.move_time
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
        if 'moveType' in response_body:
            self.__move_type = response_body['moveType']
        if 'sourceAccount' in response_body:
            self.__source_account = response_body['sourceAccount']
        if 'targetAccount' in response_body:
            self.__target_account = response_body['targetAccount']
        if 'moveTime' in response_body:
            self.__move_time = response_body['moveTime']
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'referenceTransactionId' in response_body:
            self.__reference_transaction_id = response_body['referenceTransactionId']
        if 'payerAssetId' in response_body:
            self.__payer_asset_id = response_body['payerAssetId']
        if 'beneficiaryAssetId' in response_body:
            self.__beneficiary_asset_id = response_body['beneficiaryAssetId']
