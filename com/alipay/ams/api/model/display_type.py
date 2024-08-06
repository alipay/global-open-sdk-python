#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class DisplayType(Enum):
    TEXT = "TEXT"
    MIDDLEIMAGE = "MIDDLEIMAGE"
    SMALLIMAGE = "SMALLIMAGE"
    BIGIMAGE = "BIGIMAGE"
    IMAGE = "IMAGE"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisplayType.TEXT.value == value:
            return DisplayType.TEXT
        elif DisplayType.MIDDLEIMAGE.value == value:
            return DisplayType.MIDDLEIMAGE
        elif DisplayType.SMALLIMAGE.value == value:
            return DisplayType.SMALLIMAGE
        elif DisplayType.BIGIMAGE.value == value:
            return DisplayType.BIGIMAGE
        elif DisplayType.IMAGE.value == value:
            return DisplayType.IMAGE
        else:
            return None
