#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:Leo
@contact:lipf0627@163.com
@file:algo_binary_watch
@time:2018/6/4 10:41
@desc:
"""


ALL_STRING_ALGOS = (
    '删除字符串中的重复字符',
)


def showAllStringAlgos():
    algoNames = ALL_STRING_ALGOS[:]
    return algoNames


def deleteRepeatedChars(strInput):
    strOutput = ''
    strOutput += strInput[0]
    for i in range(1, len(strInput)):
        if strOutput.find(strInput[i]) < 0:
            strOutput += strInput[i]
    return strOutput