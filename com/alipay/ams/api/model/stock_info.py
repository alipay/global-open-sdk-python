
class StockInfo:
    def __init__(self):
        self.__listed_region = None
        self.__ticker_symbol = None

    def get_listed_region(self):
        return self.__listed_region

    def set_listed_region(self, listed_region):
        self.__listed_region = listed_region

    def get_ticker_symbol(self):
        return self.__ticker_symbol

    def set_ticker_symbol(self, ticker_symbol):
        self.__ticker_symbol = ticker_symbol


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'listed_region') and self.listed_region:
            params['listedRegion'] = self.listed_region
        if hasattr(self, 'ticker_symbol') and self.ticker_symbol:
            params['tickerSymbol'] = self.ticker_symbol
        return params