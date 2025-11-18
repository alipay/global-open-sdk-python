import json

from com.alipay.ams.api.model.fund_move_detail import FundMoveDetail


class Statement(object):
    def __init__(self):
        self.__statement_id = None
        self.__fund_move_detail = None #type: FundMoveDetail


    @property
    def StatementId(self):
        return self.__statement_id

    @StatementId.setter
    def StatementId(self, value):
        self.__statement_id = value


    @property
    def FundMoveDetail(self):
        return self.__fund_move_detail

    @FundMoveDetail.setter
    def FundMoveDetail(self, value):
        self.__fund_move_detail = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_id") and self.statement_id:
            params['statementId'] = self.statement_id
        if hasattr(self, "fund_move_detail") and self.fund_move_detail:
            params['fundMoveDetail'] = self.fund_move_detail.to_ams_dict()
        return params

    def parse_rsp_body(self, statement_body):
        if type(statement_body) == str:
            statement_body = json.loads(statement_body)

        if 'fundMoveDetail' in statement_body:
            self.__fund_move_detail = FundMoveDetail()
            self.__fund_move_detail.parse_rsp_body(statement_body['fundMoveDetail'])

        if 'statementId' in statement_body:
            self.__statement_id = statement_body['statementId']


