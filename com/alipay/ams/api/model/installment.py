import json
from com.alipay.ams.api.model.support_card_brand import SupportCardBrand
from com.alipay.ams.api.model.plan import Plan




class Installment:
    def __init__(self):
        
        self.__support_card_brands = None  # type: [SupportCardBrand]
        self.__plans = None  # type: [Plan]
        

    @property
    def support_card_brands(self):
        """
        The list of card brands that support the installment plans.    This parameter is returned when the value of paymentMethodType is CARD. 
        """
        return self.__support_card_brands

    @support_card_brands.setter
    def support_card_brands(self, value):
        self.__support_card_brands = value
    @property
    def plans(self):
        """
        The list of installment plans for payment methods that support installments. 
        """
        return self.__plans

    @plans.setter
    def plans(self, value):
        self.__plans = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "support_card_brands") and self.support_card_brands is not None:
            params['supportCardBrands'] = self.support_card_brands
        if hasattr(self, "plans") and self.plans is not None:
            params['plans'] = self.plans
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'supportCardBrands' in response_body:
            self.__support_card_brands = []
            for item in response_body['supportCardBrands']:
                obj = SupportCardBrand()
                obj.parse_rsp_body(item)
                self.__support_card_brands.append(obj)
        if 'plans' in response_body:
            self.__plans = []
            for item in response_body['plans']:
                obj = Plan()
                obj.parse_rsp_body(item)
                self.__plans.append(obj)
