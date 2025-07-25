import json
from com.alipay.ams.api.model.challenge_type import ChallengeType
from com.alipay.ams.api.model.challenge_trigger_source_type import ChallengeTriggerSourceType




class ChallengeActionForm:
    def __init__(self):
        
        self.__challenge_type = None  # type: ChallengeType
        self.__challenge_render_value = None  # type: str
        self.__trigger_source = None  # type: ChallengeTriggerSourceType
        self.__extend_info = None  # type: str
        

    @property
    def challenge_type(self):
        """Gets the challenge_type of this ChallengeActionForm.
        
        """
        return self.__challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self.__challenge_type = value
    @property
    def challenge_render_value(self):
        """Gets the challenge_render_value of this ChallengeActionForm.
        
        """
        return self.__challenge_render_value

    @challenge_render_value.setter
    def challenge_render_value(self, value):
        self.__challenge_render_value = value
    @property
    def trigger_source(self):
        """Gets the trigger_source of this ChallengeActionForm.
        
        """
        return self.__trigger_source

    @trigger_source.setter
    def trigger_source(self, value):
        self.__trigger_source = value
    @property
    def extend_info(self):
        """Gets the extend_info of this ChallengeActionForm.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "challenge_type") and self.challenge_type is not None:
            params['challengeType'] = self.challenge_type
        if hasattr(self, "challenge_render_value") and self.challenge_render_value is not None:
            params['challengeRenderValue'] = self.challenge_render_value
        if hasattr(self, "trigger_source") and self.trigger_source is not None:
            params['triggerSource'] = self.trigger_source
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'challengeType' in response_body:
            challenge_type_temp = ChallengeType.value_of(response_body['challengeType'])
            self.__challenge_type = challenge_type_temp
        if 'challengeRenderValue' in response_body:
            self.__challenge_render_value = response_body['challengeRenderValue']
        if 'triggerSource' in response_body:
            trigger_source_temp = ChallengeTriggerSourceType.value_of(response_body['triggerSource'])
            self.__trigger_source = trigger_source_temp
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
