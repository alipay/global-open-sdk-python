#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

'''
python3.2前版本中需要，时区支持
'''
try:
    import pytz
except ImportError:
    pass

from com.alipay.ams.api.tools.constants import *
from datetime import datetime

'''
python version > 3.2有timezone模块
'''
try:
    from datetime import timezone
except ImportError:
    pass


def get_cur_iso8601_time():
    if not IS_PYTHON_VERSION_3:
        return datetime.fromtimestamp(int(time.time()), tz=pytz.timezone('UTC')).isoformat()
    else:
        return datetime.fromtimestamp(int(time.time()), tz=timezone.utc).isoformat()
