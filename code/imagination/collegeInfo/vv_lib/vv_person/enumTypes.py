#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : enumTypes.py
@site    : 
@Time    : 2018/7/26 14:45
@Software: PyCharm Community Edition
"""

from enum import Enum, unique


@unique
class SexEnum(Enum):
    男 = 1
    女 = 2

