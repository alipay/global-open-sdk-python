import json
from com.alipay.ams.api.model.in_store_payment_scenario import InStorePaymentScenario
from com.alipay.ams.api.model.presentment_mode import PresentmentMode




class PaymentFactor:
    def __init__(self):
        
        self.__is_payment_evaluation = None  # type: bool
        self.__in_store_payment_scenario = None  # type: InStorePaymentScenario
        self.__presentment_mode = None  # type: PresentmentMode
        self.__capture_mode = None  # type: str
        self.__is_authorization = None  # type: bool
        

    @property
    def is_payment_evaluation(self):
        """Gets the is_payment_evaluation of this PaymentFactor.
        
        """
        return self.__is_payment_evaluation

    @is_payment_evaluation.setter
    def is_payment_evaluation(self, value):
        self.__is_payment_evaluation = value
    @property
    def in_store_payment_scenario(self):
        """Gets the in_store_payment_scenario of this PaymentFactor.
        
        """
        return self.__in_store_payment_scenario

    @in_store_payment_scenario.setter
    def in_store_payment_scenario(self, value):
        self.__in_store_payment_scenario = value
    @property
    def presentment_mode(self):
        """Gets the presentment_mode of this PaymentFactor.
        
        """
        return self.__presentment_mode

    @presentment_mode.setter
    def presentment_mode(self, value):
        self.__presentment_mode = value
    @property
    def capture_mode(self):
        """
        Indicates the method for capturing funds after the user authorizes the payment. Valid values are:  AUTOMATIC: indicates that Antom automatically captures the funds after the authorization. The same applies when the value is empty or you do not pass in this parameter. MANUAL: indicates that you manually capture the funds by calling the capture (Checkout Payment) API. Specify this parameter if you want to designate the capture mode of the payment.    More information:  Maximum length: 64 characters 
        """
        return self.__capture_mode

    @capture_mode.setter
    def capture_mode(self, value):
        self.__capture_mode = value
    @property
    def is_authorization(self):
        """
        Indicates whether the payment scenario is authorization. Specify this parameter when the value of paymentMethodType is CARD and you integrate the client-side SDK. Valid values of this parameter are:  true: indicates that the payment scenario is authorization. false: indicates that the payment scenario is a regular payment without authorization.   Under the authorization scenario, the payment funds are guaranteed and held on the payment method side. You can use the capture (Checkout Payment) API to deduct the payment funds. 
        """
        return self.__is_authorization

    @is_authorization.setter
    def is_authorization(self, value):
        self.__is_authorization = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "is_payment_evaluation") and self.is_payment_evaluation is not None:
            params['isPaymentEvaluation'] = self.is_payment_evaluation
        if hasattr(self, "in_store_payment_scenario") and self.in_store_payment_scenario is not None:
            params['inStorePaymentScenario'] = self.in_store_payment_scenario
        if hasattr(self, "presentment_mode") and self.presentment_mode is not None:
            params['presentmentMode'] = self.presentment_mode
        if hasattr(self, "capture_mode") and self.capture_mode is not None:
            params['captureMode'] = self.capture_mode
        if hasattr(self, "is_authorization") and self.is_authorization is not None:
            params['isAuthorization'] = self.is_authorization
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'isPaymentEvaluation' in response_body:
            self.__is_payment_evaluation = response_body['isPaymentEvaluation']
        if 'inStorePaymentScenario' in response_body:
            in_store_payment_scenario_temp = InStorePaymentScenario.value_of(response_body['inStorePaymentScenario'])
            self.__in_store_payment_scenario = in_store_payment_scenario_temp
        if 'presentmentMode' in response_body:
            presentment_mode_temp = PresentmentMode.value_of(response_body['presentmentMode'])
            self.__presentment_mode = presentment_mode_temp
        if 'captureMode' in response_body:
            self.__capture_mode = response_body['captureMode']
        if 'isAuthorization' in response_body:
            self.__is_authorization = response_body['isAuthorization']
