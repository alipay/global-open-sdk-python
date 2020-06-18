#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"
