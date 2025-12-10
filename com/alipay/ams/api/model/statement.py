import json
from com.alipay.ams.api.model.fund_move_detail import FundMoveDetail




class Statement:
    def __init__(self):
        
        self.__statement_id = None  # type: str
        self.__fund_move_detail = None  # type: FundMoveDetail
        

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


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_id") and self.statement_id is not None:
            params['statementId'] = self.statement_id
        if hasattr(self, "fund_move_detail") and self.fund_move_detail is not None:
            params['fundMoveDetail'] = self.fund_move_detail
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'statementId' in response_body:
            self.__statement_id = response_body['statementId']
        if 'fundMoveDetail' in response_body:
            self.__fund_move_detail = FundMoveDetail()
            self.__fund_move_detail.parse_rsp_body(response_body['fundMoveDetail'])
