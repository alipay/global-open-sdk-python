#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.request.alipay_file_request import AlipayFileRequest


class AlipayProductUploadImageRequest(AlipayFileRequest):
    """Request for uploading an image that can later be associated with a product."""

    def __init__(self):
        super(AlipayProductUploadImageRequest, self).__init__()
        self.__product_id = None

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
