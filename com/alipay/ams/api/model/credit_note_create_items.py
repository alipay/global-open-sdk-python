import json
from com.alipay.ams.api.model.line_item import LineItem




class CreditNoteCreateItems:
    def __init__(self):
        
        self.__data = None  # type: [LineItem]
        self.__has_more = None  # type: bool
        

    @property
    def data(self):
        """
        The data. Maximum length: 100 characters.
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
    @property
    def has_more(self):
        """
        The has more.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "data") and self.data is not None:
            params['data'] = self.data
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'data' in response_body:
            self.__data = []
            for item in response_body['data']:
                obj = LineItem()
                obj.parse_rsp_body(item)
                self.__data.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
