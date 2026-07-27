import json
from com.alipay.ams.api.model.billing_subscription_update_trial_settings_end_behavior import BillingSubscriptionUpdateTrialSettingsEndBehavior




class BillingSubscriptionUpdateTrialSettings:
    def __init__(self):
        
        self.__trial_end = None  # type: str
        self.__end_behavior = None  # type: BillingSubscriptionUpdateTrialSettingsEndBehavior
        

    @property
    def trial_end(self):
        """
        The trial end. Maximum length: 30 characters.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value
    @property
    def end_behavior(self):
        """Gets the end_behavior of this BillingSubscriptionUpdateTrialSettings.
        
        """
        return self.__end_behavior

    @end_behavior.setter
    def end_behavior(self, value):
        self.__end_behavior = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        if hasattr(self, "end_behavior") and self.end_behavior is not None:
            params['endBehavior'] = self.end_behavior
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
        if 'endBehavior' in response_body:
            self.__end_behavior = BillingSubscriptionUpdateTrialSettingsEndBehavior()
            self.__end_behavior.parse_rsp_body(response_body['endBehavior'])
