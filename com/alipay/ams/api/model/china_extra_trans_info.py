#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ChinaExtraTransInfo(object):
    def __init__(self):
        self.__business_type = None
        self.__flight_number = None
        self.__departure_time = None
        self.__hotel_name = None
        self.__checkin_time = None
        self.__checkout_time = None
        self.__admission_notice_url = None
        self.__total_quantity = None
        self.__goods_info = None
        self.__other_business_type = None

    @property
    def business_type(self):
        return self.__business_type

    @business_type.setter
    def business_type(self, value):
        self.__business_type = value

    @property
    def flight_number(self):
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value):
        self.__flight_number = value

    @property
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property
    def hotel_name(self):
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self.__hotel_name = value

    @property
    def checkin_time(self):
        return self.__checkin_time

    @checkin_time.setter
    def checkin_time(self, value):
        self.__checkin_time = value

    @property
    def checkout_time(self):
        return self.__checkout_time

    @checkout_time.setter
    def checkout_time(self, value):
        self.__checkout_time = value

    @property
    def admission_notice_url(self):
        return self.__admission_notice_url

    @admission_notice_url.setter
    def admission_notice_url(self, value):
        self.__admission_notice_url = value

    @property
    def total_quantity(self):
        return self.__total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self.__total_quantity = value

    @property
    def goods_info(self):
        return self.__goods_info

    @goods_info.setter
    def goods_info(self, value):
        self.__goods_info = value

    @property
    def other_business_type(self):
        return self.__other_business_type

    @other_business_type.setter
    def other_business_type(self, value):
        self.__other_business_type = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "business_type") and self.business_type:
            params["businessType"] = self.business_type

        if hasattr(self, "flight_number") and self.flight_number:
            params["flightNumber"] = self.flight_number

        if hasattr(self, "departure_time") and self.departure_time:
            params["departureTime"] = self.departure_time

        if hasattr(self, "hotel_name ") and self.hotel_name:
            params["hotelName"] = self.hotel_name

        if hasattr(self, "checkin_time") and self.checkin_time:
            params["checkinTime"] = self.checkin_time

        if hasattr(self, "checkout_time") and self.checkout_time:
            params["checkoutTime"] = self.checkout_time

        if hasattr(self, "admission_notice_url") and self.admission_notice_url:
            params["admissionNoticeUrl"] = self.admission_notice_url

        if hasattr(self, "total_quantity") and self.total_quantity:
            params["totalQuantity"] = self.total_quantity

        if hasattr(self, "goods_info") and self.goods_info:
            params["goodsInfo"] = self.goods_info

        if hasattr(self, "other_business_type") and self.other_business_type:
            params["otherBusinessType"] = self.other_business_type

        return params
