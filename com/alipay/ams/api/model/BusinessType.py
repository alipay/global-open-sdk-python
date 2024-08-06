#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BusinessType(object):
    HOTEL = "1"
    AIR_FLIGHT = "2"
    STUDAY_ABROAD = "3"
    TRADE = "4"
    OTHER = "5"

    def to_ams_dict(self):
        return self.name
