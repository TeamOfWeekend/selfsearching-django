#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imGrade.py
@site    : 
@Time    : 2018/7/25 10:09
@Software: PyCharm Community Edition
"""

import random

from .imTypes import CLASSS_IN_MAJOR_MIN, CLASSS_IN_MAJOR_MAX
from .imClass import ImClass

class ImGrade:
    """年级类"""
    def __init__(self, major, id):
        self.id = id
        self.classNum = 0
        self.classes = []
        # 所属专业
        self.major = major


    def createRandomAttrs(self):
        """创建随机属性"""
        self.classNum = random.randint(CLASSS_IN_MAJOR_MIN, CLASSS_IN_MAJOR_MAX)
        for i in range(0, self.classNum):
            classs = ImClass(self, i+1)
            classs.createRandomAttrs()
            self.classes.append(classs)
