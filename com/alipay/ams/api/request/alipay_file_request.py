#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.exception.exception import AlipayApiException

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)


class AlipayFileRequest(object):
    """Base request accepted only by DefaultAlipayClient.upload_file()."""

    def __init__(self):
        self.__file = None
        self.__filename = None
        self.__key_version = None

    def set_file(self, file_object, filename=None):
        if file_object is None or not hasattr(file_object, "read"):
            raise AlipayApiException("file must be a readable binary file object")
        resolved_name = filename
        if not resolved_name:
            resolved_name = getattr(file_object, "name", None)
        if not isinstance(resolved_name, string_types) or not resolved_name.strip():
            raise AlipayApiException("filename is required for an anonymous file object")
        resolved_name = resolved_name.replace("\\", "/").rsplit("/", 1)[-1]
        resolved_name = "".join(
            "_" if character == '"' or ord(character) < 0x20 or ord(character) == 0x7F
            else character
            for character in resolved_name
        )
        if not resolved_name:
            raise AlipayApiException("filename cannot be empty")
        self.__file = file_object
        self.__filename = resolved_name
        return self

    @property
    def file(self):
        return self.__file

    @property
    def filename(self):
        return self.__filename

    @property
    def key_version(self):
        return self.__key_version

    @key_version.setter
    def key_version(self, value):
        self.__key_version = value
