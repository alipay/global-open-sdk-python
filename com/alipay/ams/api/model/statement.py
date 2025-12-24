import json
from com.alipay.ams.api.model.fund_move_detail import FundMoveDetail




class Statement:
    def __init__(self):
        
        self.__statement_id = None  # type: str
        self.__fund_move_detail = None  # type: FundMoveDetail
        self.__transaction_type = None  # type: str
        self.__beneficiary_asset_id = None  # type: str
        

    @property
    def statement_id(self):
        """Gets the statement_id of this Statement.
        
        """
        return self.__statement_id

    @statement_id.setter
    def statement_id(self, value):
        self.__statement_id = value
    @property
    def fund_move_detail(self):
        """Gets the fund_move_detail of this Statement.
        
        """
        return self.__fund_move_detail

    @fund_move_detail.setter
    def fund_move_detail(self, value):
        self.__fund_move_detail = value
    @property
    def transaction_type(self):
        """Gets the transaction_type of this Statement.
        
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value
    @property
    def beneficiary_asset_id(self):
        """Gets the beneficiary_asset_id of this Statement.
        
        """
        return self.__beneficiary_asset_id

    @beneficiary_asset_id.setter
    def beneficiary_asset_id(self, value):
        self.__beneficiary_asset_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_id") and self.statement_id is not None:
            params['statementId'] = self.statement_id
        if hasattr(self, "fund_move_detail") and self.fund_move_detail is not None:
            params['fundMoveDetail'] = self.fund_move_detail
        if hasattr(self, "transaction_type") and self.transaction_type is not None:
            params['transactionType'] = self.transaction_type
        if hasattr(self, "beneficiary_asset_id") and self.beneficiary_asset_id is not None:
            params['beneficiaryAssetId'] = self.beneficiary_asset_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'statementId' in response_body:
            self.__statement_id = response_body['statementId']
        if 'fundMoveDetail' in response_body:
            self.__fund_move_detail = FundMoveDetail()
            self.__fund_move_detail.parse_rsp_body(response_body['fundMoveDetail'])
        if 'transactionType' in response_body:
            self.__transaction_type = response_body['transactionType']
        if 'beneficiaryAssetId' in response_body:
            self.__beneficiary_asset_id = response_body['beneficiaryAssetId']
