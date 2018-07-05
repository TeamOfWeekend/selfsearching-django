#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:Leo
@contact:lipf0627@163.com
@file:algo_binary_watch
@time:2018/6/4 10:41
@desc:
"""

from . import algoStringSet

ALL_STRING_ALGOS = {
    '删除字符串中的重复字符': algoStringSet.deleteRepeatedChars,
}


def getAllStringAlgos():
    return ALL_STRING_ALGOS


def processString(algoName, strInput):
    """根据算法名称调用对应的算法"""
    for k,v in ALL_STRING_ALGOS.items():
        if k == algoName:
            return v(strInput)


