#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:Leo
@contact:lipf0627@163.com
@file:algo_binary_watch
@time:2018/7/19 10:41
@desc:
"""

import re


def findAllStringByRegix(reInput, strInput):
    strOutput = ''

    try:
        res = re.match(reInput, strInput)
        strOutput += ('字符串开头：%s  %s\n\n' % (strInput[:res.end()], str(res.span())))
    except AttributeError:
        strOutput += ('字符串开头：不匹配' + '\n\n')

    try:
        res = re.search(reInput, strInput)
        strOutput += ('第一次匹配：%s  %s\n\n' % (strInput[res.start():res.end()], str(res.span())))
    except AttributeError:
        strOutput += ('第一次匹配：无' + '\n\n')

    rels = re.findall(reInput, strInput)
    try:
        strOutput += ('所有匹配项：%d  %s' % (len(rels), str(rels)))
    except:
        strOutput += ('所有匹配项：无' + '\n')

    return strOutput

# print(findAllStringByRegix('ab', 'babaaaaabaabaaaabaaaa'))