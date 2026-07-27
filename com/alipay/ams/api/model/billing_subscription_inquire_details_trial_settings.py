import json
from com.alipay.ams.api.model.billing_subscription_inquire_details_trial_settings_end_behavior import BillingSubscriptionInquireDetailsTrialSettingsEndBehavior




class BillingSubscriptionInquireDetailsTrialSettings:
    def __init__(self):
        
        self.__end_behavior = None  # type: BillingSubscriptionInquireDetailsTrialSettingsEndBehavior
        

    @property
    def end_behavior(self):
        """Gets the end_behavior of this BillingSubscriptionInquireDetailsTrialSettings.
        
        """
        return self.__end_behavior

    @end_behavior.setter
    def end_behavior(self, value):
        self.__end_behavior = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "end_behavior") and self.end_behavior is not None:
            params['endBehavior'] = self.end_behavior
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'endBehavior' in response_body:
            self.__end_behavior = BillingSubscriptionInquireDetailsTrialSettingsEndBehavior()
            self.__end_behavior.parse_rsp_body(response_body['endBehavior'])
