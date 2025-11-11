import json




class StockInfo:
    def __init__(self):
        
        self.__listed_region = None  # type: str
        self.__ticker_symbol = None  # type: str
        

    @property
    def listed_region(self):
        """
        The region or country where the company is listed.    More information:  Maximum length: 2 characters 
        """
        return self.__listed_region

    @listed_region.setter
    def listed_region(self, value):
        self.__listed_region = value
    @property
    def ticker_symbol(self):
        """
        The ticker symbol of the stock.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is US.    More information:  Maximum length: 32 characters
        """
        return self.__ticker_symbol

    @ticker_symbol.setter
    def ticker_symbol(self, value):
        self.__ticker_symbol = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "listed_region") and self.listed_region is not None:
            params['listedRegion'] = self.listed_region
        if hasattr(self, "ticker_symbol") and self.ticker_symbol is not None:
            params['tickerSymbol'] = self.ticker_symbol
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'listedRegion' in response_body:
            self.__listed_region = response_body['listedRegion']
        if 'tickerSymbol' in response_body:
            self.__ticker_symbol = response_body['tickerSymbol']
