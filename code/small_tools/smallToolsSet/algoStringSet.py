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
    #删除重复字符
    strInput_temp = deleteRepeatedChars(strInput)
    #进行排序，达到更友好的呈现效果
    strInput_temp = "".join((lambda x:(x.sort(), x)[1])(list(strInput_temp)))
    for i in range(len(strInput_temp)):
        cnt = strInput.count(strInput_temp[i])
        strOutput += (" ('" + strInput_temp[i] + "' : " + str(cnt) + ") ")
        if 0 == (i + 1)%16:
            strOutput += '\n'
    return strOutput