class CurrencyPair(object):
    def __init__(self):
        self.__sell_currency = None
        self.__buy_currency = None


    @property
    def sell_currency(self):
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value

    @property
    def buy_currency(self):
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value


    def to_ams_dict(self):
        params = dict()

        if hasattr(self, "sell_currency") and self.sell_currency:
            params['sellCurrency'] = self.sell_currency

        if hasattr(self, "buy_currency") and self.buy_currency:
            params['buyCurrency'] = self.buy_currency

        return params
