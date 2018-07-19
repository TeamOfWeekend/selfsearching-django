#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : random_walk.py
@Software: PyCharm Community Edition
@Time    : 2018/7/19 22:51
"""

import os
import matplotlib.pyplot as plt

def drawRandomWalk():
    xVal = list(range(1, 1001))
    yVal = [x**2 for x in xVal]

    plt.scatter(xVal, yVal, c=yVal, cmap=plt.cm.Blues, edgecolor=None, s=10)
    dirCurr = os.getcwd()
    print(dirCurr)
    plt.savefig('randomWork.png')
    plt.show()