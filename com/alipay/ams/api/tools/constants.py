#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

IS_PYTHON_VERSION_3 = True
if sys.version_info < (3, 0):
    IS_PYTHON_VERSION_3 = False

IS_PYTHON_VERSION_cryptography = True
if sys.version_info < (2.7, 0):
    IS_PYTHON_VERSION_3 = False

DEFAULT_KEY_VERSION = "1"

DEFAULT_CHARSET = "UTF-8"

DEFAULT_TIMEOUT = 15
