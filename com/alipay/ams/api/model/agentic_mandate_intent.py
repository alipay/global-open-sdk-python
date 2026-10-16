import json
from com.alipay.ams.api.model.agentic_decline_threshold import AgenticDeclineThreshold
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.merchant import Merchant




class AgenticMandateIntent:
    def __init__(self):
        
        self.__decline_threshold = None  # type: AgenticDeclineThreshold
        self.__effective_from_time = None  # type: str
        self.__effective_until_time = None  # type: str
        self.__preferred_merchant = None  # type: Merchant
        self.__allowed_merchant = None  # type: [Merchant]
        self.__consumer_prompt = None  # type: str
        self.__intent_desc = None  # type: str
        

    @property
    def decline_threshold(self):
        """Gets the decline_threshold of this AgenticMandateIntent.
        
        """
        return self.__decline_threshold

    @decline_threshold.setter
    def decline_threshold(self, value):
        self.__decline_threshold = value
    @property
    def effective_from_time(self):
        """
        Intent start time. Required for AUTONOMOUS authorization with recurrence or agent_recurrence time constraints. This does not imply support for purchaseType&#x3D;RECURRING. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object.
        """
        return self.__effective_from_time

    @effective_from_time.setter
    def effective_from_time(self, value):
        self.__effective_from_time = value
    @property
    def effective_until_time(self):
        """
        CreateBindingSession: Intent expiration time. Must be later than the current time. Required for applicable A+ mandate bind-and-authorize scenarios. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object. CreateAuthenticationSession: Intent expiration time. Must be later than the current time. Must also be later than effectiveFromTime. Required for applicable Visa and A+ mandate scenarios; for Mastercard recurrence it applies when the source authorization contains an end time. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object.
        """
        return self.__effective_until_time

    @effective_until_time.setter
    def effective_until_time(self, value):
        self.__effective_until_time = value
    @property
    def preferred_merchant(self):
        """Gets the preferred_merchant of this AgenticMandateIntent.
        
        """
        return self.__preferred_merchant

    @preferred_merchant.setter
    def preferred_merchant(self, value):
        self.__preferred_merchant = value
    @property
    def allowed_merchant(self):
        """
        Allowed merchants for autonomous authorization. Must not be an empty array when supplied. Deduplicate by referenceMerchantId or normalized domain. No separate item-count limit is specified; the total AMS message-size limit applies.
        """
        return self.__allowed_merchant

    @allowed_merchant.setter
    def allowed_merchant(self, value):
        self.__allowed_merchant = value
    @property
    def consumer_prompt(self):
        """
        Original user intent. Required for the applicable A+ mandate authorization scenario. The documented maximum length is 1M; the document does not define its exact numeric value or whether it counts characters or bytes. No numeric maxLength is imposed here.
        """
        return self.__consumer_prompt

    @consumer_prompt.setter
    def consumer_prompt(self, value):
        self.__consumer_prompt = value
    @property
    def intent_desc(self):
        """
        CreateBindingSession: Structured authorization summary produced by the caller. Required for applicable A+ mandate bind-and-authorize scenarios. CreateAuthenticationSession: Structured authorization summary produced by the caller. Required for Visa initiatePurchaseInstruction; optional for its composite path when the source authorization contains a description. For Mastercard, optional when the source intent has a description. Not consumed by A+, whose original expression uses consumerPrompt.
        """
        return self.__intent_desc

    @intent_desc.setter
    def intent_desc(self, value):
        self.__intent_desc = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "decline_threshold") and self.decline_threshold is not None:
            params['declineThreshold'] = self.decline_threshold
        if hasattr(self, "effective_from_time") and self.effective_from_time is not None:
            params['effectiveFromTime'] = self.effective_from_time
        if hasattr(self, "effective_until_time") and self.effective_until_time is not None:
            params['effectiveUntilTime'] = self.effective_until_time
        if hasattr(self, "preferred_merchant") and self.preferred_merchant is not None:
            params['preferredMerchant'] = self.preferred_merchant
        if hasattr(self, "allowed_merchant") and self.allowed_merchant is not None:
            params['allowedMerchant'] = self.allowed_merchant
        if hasattr(self, "consumer_prompt") and self.consumer_prompt is not None:
            params['consumerPrompt'] = self.consumer_prompt
        if hasattr(self, "intent_desc") and self.intent_desc is not None:
            params['intentDesc'] = self.intent_desc
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'declineThreshold' in response_body:
            self.__decline_threshold = AgenticDeclineThreshold()
            self.__decline_threshold.parse_rsp_body(response_body['declineThreshold'])
        if 'effectiveFromTime' in response_body:
            self.__effective_from_time = response_body['effectiveFromTime']
        if 'effectiveUntilTime' in response_body:
            self.__effective_until_time = response_body['effectiveUntilTime']
        if 'preferredMerchant' in response_body:
            self.__preferred_merchant = Merchant()
            self.__preferred_merchant.parse_rsp_body(response_body['preferredMerchant'])
        if 'allowedMerchant' in response_body:
            self.__allowed_merchant = []
            for item in response_body['allowedMerchant']:
                obj = Merchant()
                obj.parse_rsp_body(item)
                self.__allowed_merchant.append(obj)
        if 'consumerPrompt' in response_body:
            self.__consumer_prompt = response_body['consumerPrompt']
        if 'intentDesc' in response_body:
            self.__intent_desc = response_body['intentDesc']
