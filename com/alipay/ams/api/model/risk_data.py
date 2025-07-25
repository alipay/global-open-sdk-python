import json
from com.alipay.ams.api.model.risk_order import RiskOrder
from com.alipay.ams.api.model.risk_buyer import RiskBuyer
from com.alipay.ams.api.model.risk_env import RiskEnv
from com.alipay.ams.api.model.risk_signal import RiskSignal
from com.alipay.ams.api.model.risk_address import RiskAddress
from com.alipay.ams.api.model.card_verification_result import CardVerificationResult




class RiskData:
    def __init__(self):
        
        self.__order = None  # type: RiskOrder
        self.__buyer = None  # type: RiskBuyer
        self.__env = None  # type: RiskEnv
        self.__risk_signal = None  # type: RiskSignal
        self.__address = None  # type: RiskAddress
        self.__card_verification_result = None  # type: CardVerificationResult
        

    @property
    def order(self):
        """Gets the order of this RiskData.
        
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
    @property
    def buyer(self):
        """Gets the buyer of this RiskData.
        
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value
    @property
    def env(self):
        """Gets the env of this RiskData.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def risk_signal(self):
        """Gets the risk_signal of this RiskData.
        
        """
        return self.__risk_signal

    @risk_signal.setter
    def risk_signal(self, value):
        self.__risk_signal = value
    @property
    def address(self):
        """Gets the address of this RiskData.
        
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    @property
    def card_verification_result(self):
        """Gets the card_verification_result of this RiskData.
        
        """
        return self.__card_verification_result

    @card_verification_result.setter
    def card_verification_result(self, value):
        self.__card_verification_result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "order") and self.order is not None:
            params['order'] = self.order
        if hasattr(self, "buyer") and self.buyer is not None:
            params['buyer'] = self.buyer
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "risk_signal") and self.risk_signal is not None:
            params['riskSignal'] = self.risk_signal
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        if hasattr(self, "card_verification_result") and self.card_verification_result is not None:
            params['cardVerificationResult'] = self.card_verification_result
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'order' in response_body:
            self.__order = RiskOrder()
            self.__order.parse_rsp_body(response_body['order'])
        if 'buyer' in response_body:
            self.__buyer = RiskBuyer()
            self.__buyer.parse_rsp_body(response_body['buyer'])
        if 'env' in response_body:
            self.__env = RiskEnv()
            self.__env.parse_rsp_body(response_body['env'])
        if 'riskSignal' in response_body:
            self.__risk_signal = RiskSignal()
            self.__risk_signal.parse_rsp_body(response_body['riskSignal'])
        if 'address' in response_body:
            self.__address = RiskAddress()
            self.__address.parse_rsp_body(response_body['address'])
        if 'cardVerificationResult' in response_body:
            self.__card_verification_result = CardVerificationResult()
            self.__card_verification_result.parse_rsp_body(response_body['cardVerificationResult'])
