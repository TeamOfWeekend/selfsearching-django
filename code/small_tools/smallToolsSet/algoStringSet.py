#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:Leo
@contact:lipf0627@163.com
@file:algo_binary_watch
@time:2018/6/4 10:41
@desc:
"""


def deleteRepeatedChars(strInput):
    """删除一个字符串中的重复字符"""
    strOutput = ''
    strOutput += strInput[0]
    for i in range(1, len(strInput)):
        if strOutput.find(strInput[i]) < 0:
            strOutput += strInput[i]
    return strOutput


def getCharRepeatCount(strInput):
    """计算一个字符串中每个字符重复出现的次数"""
    pass