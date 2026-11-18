import json
from com.alipay.ams.api.model.payment_method_category_type import PaymentMethodCategoryType
from com.alipay.ams.api.model.payment_option_detail import PaymentOptionDetail
from com.alipay.ams.api.model.logo import Logo
from com.alipay.ams.api.model.installment import Installment
from com.alipay.ams.api.model.promotion_info import PromotionInfo
from com.alipay.ams.api.model.interaction_type import InteractionType
from com.alipay.ams.api.model. amount_limit_info import AmountLimitInfo




class PaymentOption:
    def __init__(self):
        
        self.__payment_method_type = None  # type: str
        self.__payment_method_category = None  # type: PaymentMethodCategoryType
        self.__payment_method_region = None  # type: [str]
        self.__enabled = None  # type: bool
        self.__preferred = None  # type: bool
        self.__disable_reason = None  # type: str
        self.__supported_currencies = None  # type: [str]
        self.__payment_option_detail = None  # type: PaymentOptionDetail
        self.__extend_info = None  # type: str
        self.__logo = None  # type: Logo
        self.__promo_names = None  # type: [str]
        self.__installment = None  # type: Installment
        self.__promotion_infos = None  # type: [PromotionInfo]
        self.__interaction_type = None  # type: InteractionType
        self.__bank_identifier_code = None  # type: str
        self.__amount_limit_info_map = None  # type: {str: (AmountLimitInfo,)}
        

    @property
    def payment_method_type(self):
        """
        The payment method type. See Payment methods to check the valid values.    More information:  Maximum length: 64 characters
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def payment_method_category(self):
        """Gets the payment_method_category of this PaymentOption.
        
        """
        return self.__payment_method_category

    @payment_method_category.setter
    def payment_method_category(self, value):
        self.__payment_method_category = value
    @property
    def payment_method_region(self):
        """
        A list of region codes that represent the countries or regions of payment methods. The value of this parameter is a 2-letter ISO country code or GLOBAL.    More information:  Maximum length: 6 characters
        """
        return self.__payment_method_region

    @payment_method_region.setter
    def payment_method_region(self, value):
        self.__payment_method_region = value
    @property
    def enabled(self):
        """
        Indicates whether the payment method is available.
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value
    @property
    def preferred(self):
        """Gets the preferred of this PaymentOption.
        
        """
        return self.__preferred

    @preferred.setter
    def preferred(self, value):
        self.__preferred = value
    @property
    def disable_reason(self):
        """
        The reason why the payment method is not available. Valid values are:  PAYMENT_ACCOUNT_NOT_AVAILABLE EXCEED_CHANNEL_LIMIT_RULE SERVICE_DEGRADE CHANNEL_NOT_SUPPORT_CURRENCY CHANNEL_DISABLE CHANNEL_NOT_IN_SERVICE_TIME QUERY_IPP_INFO_FAILED LIMIT_CENTER_ACCESS_FAIL  CURRENT_CHANNEL_NOT_EXIST 
        """
        return self.__disable_reason

    @disable_reason.setter
    def disable_reason(self, value):
        self.__disable_reason = value
    @property
    def supported_currencies(self):
        """Gets the supported_currencies of this PaymentOption.
        
        """
        return self.__supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, value):
        self.__supported_currencies = value
    @property
    def payment_option_detail(self):
        """Gets the payment_option_detail of this PaymentOption.
        
        """
        return self.__payment_option_detail

    @payment_option_detail.setter
    def payment_option_detail(self, value):
        self.__payment_option_detail = value
    @property
    def extend_info(self):
        """Gets the extend_info of this PaymentOption.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def logo(self):
        """Gets the logo of this PaymentOption.
        
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value
    @property
    def promo_names(self):
        """
        The list of the promotion names. In JSON format. The keys are returned as a language and a country code, connected by an underscore, such as zh_CN, while the value is the promotion name, such as RM1 Voucher.    More information:  Maximum length: 512 characters
        """
        return self.__promo_names

    @promo_names.setter
    def promo_names(self, value):
        self.__promo_names = value
    @property
    def installment(self):
        """Gets the installment of this PaymentOption.
        
        """
        return self.__installment

    @installment.setter
    def installment(self, value):
        self.__installment = value
    @property
    def promotion_infos(self):
        """
        Promotion information.  This parameter is returned when the payment method offers a promotion to the buyer.
        """
        return self.__promotion_infos

    @promotion_infos.setter
    def promotion_infos(self, value):
        self.__promotion_infos = value
    @property
    def interaction_type(self):
        """Gets the interaction_type of this PaymentOption.
        
        """
        return self.__interaction_type

    @interaction_type.setter
    def interaction_type(self, value):
        self.__interaction_type = value
    @property
    def bank_identifier_code(self):
        """
        The bank identifier code for the payment method.
        """
        return self.__bank_identifier_code

    @bank_identifier_code.setter
    def bank_identifier_code(self, value):
        self.__bank_identifier_code = value
    @property
    def amount_limit_info_map(self):
        """Gets the amount_limit_info_map of this PaymentOption.
        
        """
        return self.__amount_limit_info_map

    @amount_limit_info_map.setter
    def amount_limit_info_map(self, value):
        self.__amount_limit_info_map = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "payment_method_category") and self.payment_method_category is not None:
            params['paymentMethodCategory'] = self.payment_method_category
        if hasattr(self, "payment_method_region") and self.payment_method_region is not None:
            params['paymentMethodRegion'] = self.payment_method_region
        if hasattr(self, "enabled") and self.enabled is not None:
            params['enabled'] = self.enabled
        if hasattr(self, "preferred") and self.preferred is not None:
            params['preferred'] = self.preferred
        if hasattr(self, "disable_reason") and self.disable_reason is not None:
            params['disableReason'] = self.disable_reason
        if hasattr(self, "supported_currencies") and self.supported_currencies is not None:
            params['supportedCurrencies'] = self.supported_currencies
        if hasattr(self, "payment_option_detail") and self.payment_option_detail is not None:
            params['paymentOptionDetail'] = self.payment_option_detail
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "logo") and self.logo is not None:
            params['logo'] = self.logo
        if hasattr(self, "promo_names") and self.promo_names is not None:
            params['promoNames'] = self.promo_names
        if hasattr(self, "installment") and self.installment is not None:
            params['installment'] = self.installment
        if hasattr(self, "promotion_infos") and self.promotion_infos is not None:
            params['promotionInfos'] = self.promotion_infos
        if hasattr(self, "interaction_type") and self.interaction_type is not None:
            params['interactionType'] = self.interaction_type
        if hasattr(self, "bank_identifier_code") and self.bank_identifier_code is not None:
            params['bankIdentifierCode'] = self.bank_identifier_code
        if hasattr(self, "amount_limit_info_map") and self.amount_limit_info_map is not None:
            params['amountLimitInfoMap'] = self.amount_limit_info_map
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'paymentMethodCategory' in response_body:
            payment_method_category_temp = PaymentMethodCategoryType.value_of(response_body['paymentMethodCategory'])
            self.__payment_method_category = payment_method_category_temp
        if 'paymentMethodRegion' in response_body:
            self.__payment_method_region = response_body['paymentMethodRegion']
        if 'enabled' in response_body:
            self.__enabled = response_body['enabled']
        if 'preferred' in response_body:
            self.__preferred = response_body['preferred']
        if 'disableReason' in response_body:
            self.__disable_reason = response_body['disableReason']
        if 'supportedCurrencies' in response_body:
            self.__supported_currencies = response_body['supportedCurrencies']
        if 'paymentOptionDetail' in response_body:
            self.__payment_option_detail = PaymentOptionDetail()
            self.__payment_option_detail.parse_rsp_body(response_body['paymentOptionDetail'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'logo' in response_body:
            self.__logo = Logo()
            self.__logo.parse_rsp_body(response_body['logo'])
        if 'promoNames' in response_body:
            self.__promo_names = response_body['promoNames']
        if 'installment' in response_body:
            self.__installment = Installment()
            self.__installment.parse_rsp_body(response_body['installment'])
        if 'promotionInfos' in response_body:
            self.__promotion_infos = []
            for item in response_body['promotionInfos']:
                obj = PromotionInfo()
                obj.parse_rsp_body(item)
                self.__promotion_infos.append(obj)
        if 'interactionType' in response_body:
            interaction_type_temp = InteractionType.value_of(response_body['interactionType'])
            self.__interaction_type = interaction_type_temp
        if 'bankIdentifierCode' in response_body:
            self.__bank_identifier_code = response_body['bankIdentifierCode']
        if 'amountLimitInfoMap' in response_body:
            self.__amount_limit_info_map = {}
            for key, value in response_body['amountLimitInfoMap'].items():
                self.__amount_limit_info_map[key] = value
