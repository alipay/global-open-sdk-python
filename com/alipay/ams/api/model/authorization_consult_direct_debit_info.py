import json
from com.alipay.ams.api.model.authorization_access_params import AuthorizationAccessParams
from com.alipay.ams.api.model.period_rule_params import PeriodRuleParams
from com.alipay.ams.api.model.authorization_consult_pass_back_params import AuthorizationConsultPassBackParams
from com.alipay.ams.api.model.authorization_consult_subscription_params import AuthorizationConsultSubscriptionParams
from com.alipay.ams.api.model.authorization_consult_sub_merchant import AuthorizationConsultSubMerchant




class AuthorizationConsultDirectDebitInfo:
    def __init__(self):
        
        self.__channel_product_code = None  # type: str
        self.__personal_product_code = None  # type: str
        self.__sign_scene = None  # type: str
        self.__access_params = None  # type: AuthorizationAccessParams
        self.__period_rule_params = None  # type: PeriodRuleParams
        self.__pass_back_params = None  # type: AuthorizationConsultPassBackParams
        self.__subscription_params = None  # type: AuthorizationConsultSubscriptionParams
        self.__sub_merchant = None  # type: AuthorizationConsultSubMerchant
        self.__subscribe_type = None  # type: str
        self.__ori_agreement_no = None  # type: str
        

    @property
    def channel_product_code(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. Maximum length: 64 characters. Send CYCLE_PAY_AUTH; do not replace it with the channel product code. Allowed values: CYCLE_PAY_AUTH. The periodic-signing API product selector. The service maps it to the channel signing product GENERAL_WITHHOLDING.
        """
        return self.__channel_product_code

    @channel_product_code.setter
    def channel_product_code(self, value):
        self.__channel_product_code = value
    @property
    def personal_product_code(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. Maximum length: 64 characters. Allowed values: CYCLE_PAY_AUTH_P. The Alipay periodic-signing authorization product.
        """
        return self.__personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self.__personal_product_code = value
    @property
    def sign_scene(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. Production uses INDUSTRY|SUBSCRIPTION_DEFAULT_SCENE. Test environments use only explicitly configured test scenes; do not use a test scene in production.
        """
        return self.__sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self.__sign_scene = value
    @property
    def access_params(self):
        """Gets the access_params of this AuthorizationConsultDirectDebitInfo.
        
        """
        return self.__access_params

    @access_params.setter
    def access_params(self, value):
        self.__access_params = value
    @property
    def period_rule_params(self):
        """Gets the period_rule_params of this AuthorizationConsultDirectDebitInfo.
        
        """
        return self.__period_rule_params

    @period_rule_params.setter
    def period_rule_params(self, value):
        self.__period_rule_params = value
    @property
    def pass_back_params(self):
        """Gets the pass_back_params of this AuthorizationConsultDirectDebitInfo.
        
        """
        return self.__pass_back_params

    @pass_back_params.setter
    def pass_back_params(self, value):
        self.__pass_back_params = value
    @property
    def subscription_params(self):
        """Gets the subscription_params of this AuthorizationConsultDirectDebitInfo.
        
        """
        return self.__subscription_params

    @subscription_params.setter
    def subscription_params(self, value):
        self.__subscription_params = value
    @property
    def sub_merchant(self):
        """Gets the sub_merchant of this AuthorizationConsultDirectDebitInfo.
        
        """
        return self.__sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        self.__sub_merchant = value
    @property
    def subscribe_type(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. A signing action, distinct from the page template and not a passBackParams property. Allowed values: CREATE, TRIAL, UPDATE, DOWNGRADE, REVERT_CANCEL. The subscription signing action. Supported enum values do not imply that every action is enabled in production.
        """
        return self.__subscribe_type

    @subscribe_type.setter
    def subscribe_type(self, value):
        self.__subscribe_type = value
    @property
    def ori_agreement_no(self):
        """
        Required for UPDATE, DOWNGRADE and REVERT_CANCEL; omit for CREATE and TRIAL. Supply the original Antom Alipay authorization accessToken, not a raw channel agreement number. The service resolves it within the current merchant and maps it to the channel agreement. Do not log the token. Null and blank values are invalid.
        """
        return self.__ori_agreement_no

    @ori_agreement_no.setter
    def ori_agreement_no(self, value):
        self.__ori_agreement_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "channel_product_code") and self.channel_product_code is not None:
            params['channelProductCode'] = self.channel_product_code
        if hasattr(self, "personal_product_code") and self.personal_product_code is not None:
            params['personalProductCode'] = self.personal_product_code
        if hasattr(self, "sign_scene") and self.sign_scene is not None:
            params['signScene'] = self.sign_scene
        if hasattr(self, "access_params") and self.access_params is not None:
            params['accessParams'] = self.access_params
        if hasattr(self, "period_rule_params") and self.period_rule_params is not None:
            params['periodRuleParams'] = self.period_rule_params
        if hasattr(self, "pass_back_params") and self.pass_back_params is not None:
            params['passBackParams'] = self.pass_back_params
        if hasattr(self, "subscription_params") and self.subscription_params is not None:
            params['subscriptionParams'] = self.subscription_params
        if hasattr(self, "sub_merchant") and self.sub_merchant is not None:
            params['subMerchant'] = self.sub_merchant
        if hasattr(self, "subscribe_type") and self.subscribe_type is not None:
            params['subscribeType'] = self.subscribe_type
        if hasattr(self, "ori_agreement_no") and self.ori_agreement_no is not None:
            params['oriAgreementNo'] = self.ori_agreement_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'channelProductCode' in response_body:
            self.__channel_product_code = response_body['channelProductCode']
        if 'personalProductCode' in response_body:
            self.__personal_product_code = response_body['personalProductCode']
        if 'signScene' in response_body:
            self.__sign_scene = response_body['signScene']
        if 'accessParams' in response_body:
            self.__access_params = AuthorizationAccessParams()
            self.__access_params.parse_rsp_body(response_body['accessParams'])
        if 'periodRuleParams' in response_body:
            self.__period_rule_params = PeriodRuleParams()
            self.__period_rule_params.parse_rsp_body(response_body['periodRuleParams'])
        if 'passBackParams' in response_body:
            self.__pass_back_params = AuthorizationConsultPassBackParams()
            self.__pass_back_params.parse_rsp_body(response_body['passBackParams'])
        if 'subscriptionParams' in response_body:
            self.__subscription_params = AuthorizationConsultSubscriptionParams()
            self.__subscription_params.parse_rsp_body(response_body['subscriptionParams'])
        if 'subMerchant' in response_body:
            self.__sub_merchant = AuthorizationConsultSubMerchant()
            self.__sub_merchant.parse_rsp_body(response_body['subMerchant'])
        if 'subscribeType' in response_body:
            self.__subscribe_type = response_body['subscribeType']
        if 'oriAgreementNo' in response_body:
            self.__ori_agreement_no = response_body['oriAgreementNo']
