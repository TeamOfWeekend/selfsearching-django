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
    strOutput += 'Match result'.center(50, '*')
    strOutput += '\n'
    try:
        res = re.match(reInput, strInput)
        strOutput += ('字符串开头匹配：%s  %s' % (str(res.span()), strInput[:res.end()]))
    except AttributeError:
        strOutput += ('字符串开头不匹配' + '\n')

    strOutput += 'Search result'.center(50, '*')
    strOutput += '\n'
    try:
        res = re.search(reInput, strInput)
        strOutput += ('第一次匹配：%s  %s\n' % (str(res.span()), strInput[res.start():res.end()]))
    except AttributeError:
        strOutput += ('没有匹配项' + '\n')

    strOutput += 'Findall result'.center(50, '*')
    strOutput += '\n'
    rels = re.findall(reInput, strInput)
    try:
        for rel in rels:
            strOutput += (rel + '\n')
    except:
        strOutput += ('没有匹配项' + '\n')

    return strOutput

print(findAllStringByRegix('ab', 'babaaaaabaabaaaabaaaa'))