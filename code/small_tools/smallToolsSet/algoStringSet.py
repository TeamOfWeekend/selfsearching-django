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
    strOutput = '%-10s ：%d\n'%('字符串长度',len(strInput))
    strOutput += '%-7s ：\n'%('重复字符统计')
    strInput_temp = deleteRepeatedChars(strInput)
    for i in range(len(strInput_temp)):
        cnt = strInput.count(strInput_temp[i])
        strOutput += ('(' + strInput_temp[i] + ' : ' + str(cnt) + ')')
    return strOutput