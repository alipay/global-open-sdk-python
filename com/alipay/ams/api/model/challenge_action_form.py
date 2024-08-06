#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.challenge_trigger_source_type import ChallengeTriggerSourceType
from com.alipay.ams.api.model.challenge_type import ChallengeType


class ChallengeActionForm(object):
    def __init__(self):
        self.__challenge_type = None  # type:ChallengeType
        self.__challenge_render_value = None
        self.__trigger_source = None  # type:ChallengeTriggerSourceType
        self.__extend_info = None

    @property
    def challenge_type(self):
        return self.__challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self.__challenge_type = value

    @property
    def challenge_render_value(self):
        return self.__challenge_render_value

    @challenge_render_value.setter
    def challenge_render_value(self, value):
        self.__challenge_render_value = value

    @property
    def trigger_source(self):
        return self.__trigger_source

    @trigger_source.setter
    def trigger_source(self, value):
        self.__trigger_source = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def parse_rsp_body(self, challenge_action_form_body):
        if type(challenge_action_form_body) == str:
            challenge_action_form_body = json.loads(challenge_action_form_body)

        if 'challengeType' in challenge_action_form_body:
            self.__challenge_type = challenge_action_form_body['challengeType']

        if 'challengeRenderValue' in challenge_action_form_body:
            self.__challenge_render_value = challenge_action_form_body['challengeRenderValue']

        if 'triggerSource' in challenge_action_form_body:
            self.__trigger_source = challenge_action_form_body['triggerSource']

        if 'extendInfo' in challenge_action_form_body:
            self.__extend_info = challenge_action_form_body['extendInfo']
