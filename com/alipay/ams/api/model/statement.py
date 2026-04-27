import json
from com.alipay.ams.api.model.fund_move_detail import FundMoveDetail
from com.alipay.ams.api.model.foreign_exchange_quote import ForeignExchangeQuote
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Statement:
    def __init__(self):
        
        self.__fund_move_detail = None  # type: FundMoveDetail
        self.__foreign_exchange_quote = None  # type: ForeignExchangeQuote
        self.__statement_id = None  # type: str
        self.__transaction_time = None  # type: str
        self.__transaction_type = None  # type: str
        self.__original_transaction_amount = None  # type: Amount
        self.__transaction_amount = None  # type: Amount
        self.__fee_amount = None  # type: Amount
        self.__net_amount = None  # type: Amount
        self.__account_balance = None  # type: Amount
        self.__transaction_id = None  # type: str
        self.__ext_transaction_id = None  # type: str
        self.__transaction_status = None  # type: str
        self.__beneficiary_asset_id = None  # type: str
        

    @property
    def fund_move_detail(self):
        """Gets the fund_move_detail of this Statement.
        
        """
        return self.__fund_move_detail

    @fund_move_detail.setter
    def fund_move_detail(self, value):
        self.__fund_move_detail = value
    @property
    def foreign_exchange_quote(self):
        """Gets the foreign_exchange_quote of this Statement.
        
        """
        return self.__foreign_exchange_quote

    @foreign_exchange_quote.setter
    def foreign_exchange_quote(self, value):
        self.__foreign_exchange_quote = value
    @property
    def statement_id(self):
        """Gets the statement_id of this Statement.
        
        """
        return self.__statement_id

    @statement_id.setter
    def statement_id(self, value):
        self.__statement_id = value
    @property
    def transaction_time(self):
        """Gets the transaction_time of this Statement.
        
        """
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value
    @property
    def transaction_type(self):
        """Gets the transaction_type of this Statement.
        
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value
    @property
    def original_transaction_amount(self):
        """Gets the original_transaction_amount of this Statement.
        
        """
        return self.__original_transaction_amount

    @original_transaction_amount.setter
    def original_transaction_amount(self, value):
        self.__original_transaction_amount = value
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this Statement.
        
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value
    @property
    def fee_amount(self):
        """Gets the fee_amount of this Statement.
        
        """
        return self.__fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self.__fee_amount = value
    @property
    def net_amount(self):
        """Gets the net_amount of this Statement.
        
        """
        return self.__net_amount

    @net_amount.setter
    def net_amount(self, value):
        self.__net_amount = value
    @property
    def account_balance(self):
        """Gets the account_balance of this Statement.
        
        """
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, value):
        self.__account_balance = value
    @property
    def transaction_id(self):
        """Gets the transaction_id of this Statement.
        
        """
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.__transaction_id = value
    @property
    def ext_transaction_id(self):
        """Gets the ext_transaction_id of this Statement.
        
        """
        return self.__ext_transaction_id

    @ext_transaction_id.setter
    def ext_transaction_id(self, value):
        self.__ext_transaction_id = value
    @property
    def transaction_status(self):
        """Gets the transaction_status of this Statement.
        
        """
        return self.__transaction_status

    @transaction_status.setter
    def transaction_status(self, value):
        self.__transaction_status = value
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
        if hasattr(self, "fund_move_detail") and self.fund_move_detail is not None:
            params['fundMoveDetail'] = self.fund_move_detail
        if hasattr(self, "foreign_exchange_quote") and self.foreign_exchange_quote is not None:
            params['foreignExchangeQuote'] = self.foreign_exchange_quote
        if hasattr(self, "statement_id") and self.statement_id is not None:
            params['statementId'] = self.statement_id
        if hasattr(self, "transaction_time") and self.transaction_time is not None:
            params['transactionTime'] = self.transaction_time
        if hasattr(self, "transaction_type") and self.transaction_type is not None:
            params['transactionType'] = self.transaction_type
        if hasattr(self, "original_transaction_amount") and self.original_transaction_amount is not None:
            params['originalTransactionAmount'] = self.original_transaction_amount
        if hasattr(self, "transaction_amount") and self.transaction_amount is not None:
            params['transactionAmount'] = self.transaction_amount
        if hasattr(self, "fee_amount") and self.fee_amount is not None:
            params['feeAmount'] = self.fee_amount
        if hasattr(self, "net_amount") and self.net_amount is not None:
            params['netAmount'] = self.net_amount
        if hasattr(self, "account_balance") and self.account_balance is not None:
            params['accountBalance'] = self.account_balance
        if hasattr(self, "transaction_id") and self.transaction_id is not None:
            params['transactionId'] = self.transaction_id
        if hasattr(self, "ext_transaction_id") and self.ext_transaction_id is not None:
            params['extTransactionId'] = self.ext_transaction_id
        if hasattr(self, "transaction_status") and self.transaction_status is not None:
            params['transactionStatus'] = self.transaction_status
        if hasattr(self, "beneficiary_asset_id") and self.beneficiary_asset_id is not None:
            params['beneficiaryAssetId'] = self.beneficiary_asset_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'fundMoveDetail' in response_body:
            self.__fund_move_detail = FundMoveDetail()
            self.__fund_move_detail.parse_rsp_body(response_body['fundMoveDetail'])
        if 'foreignExchangeQuote' in response_body:
            self.__foreign_exchange_quote = ForeignExchangeQuote()
            self.__foreign_exchange_quote.parse_rsp_body(response_body['foreignExchangeQuote'])
        if 'statementId' in response_body:
            self.__statement_id = response_body['statementId']
        if 'transactionTime' in response_body:
            self.__transaction_time = response_body['transactionTime']
        if 'transactionType' in response_body:
            self.__transaction_type = response_body['transactionType']
        if 'originalTransactionAmount' in response_body:
            self.__original_transaction_amount = Amount()
            self.__original_transaction_amount.parse_rsp_body(response_body['originalTransactionAmount'])
        if 'transactionAmount' in response_body:
            self.__transaction_amount = Amount()
            self.__transaction_amount.parse_rsp_body(response_body['transactionAmount'])
        if 'feeAmount' in response_body:
            self.__fee_amount = Amount()
            self.__fee_amount.parse_rsp_body(response_body['feeAmount'])
        if 'netAmount' in response_body:
            self.__net_amount = Amount()
            self.__net_amount.parse_rsp_body(response_body['netAmount'])
        if 'accountBalance' in response_body:
            self.__account_balance = Amount()
            self.__account_balance.parse_rsp_body(response_body['accountBalance'])
        if 'transactionId' in response_body:
            self.__transaction_id = response_body['transactionId']
        if 'extTransactionId' in response_body:
            self.__ext_transaction_id = response_body['extTransactionId']
        if 'transactionStatus' in response_body:
            self.__transaction_status = response_body['transactionStatus']
        if 'beneficiaryAssetId' in response_body:
            self.__beneficiary_asset_id = response_body['beneficiaryAssetId']
