#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imAcademy.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:29
"""

from .imTypes import ACADEMY_MAJOR_DIR, AcademyEnum
from .imMajor import ImMajor


class ImAcademy():
    """学院"""
    def __init__(self, college, id):
        # 名称
        self.name = ''
        # 编号
        self.id = id
        # 专业数量
        self.majorNum = 0
        # 专业
        self.majors = {}
        # 所属学校
        self.college = college


    def fillMajors(self):
        # try:
        self.name = AcademyEnum(self.id).name
        for id in range(0, len(ACADEMY_MAJOR_DIR[self.name])):
            major = ImMajor(self, id+1)
            major.createRandomAttrs()
            self.majors[ACADEMY_MAJOR_DIR[self.name][id]] = major
            self.majorNum += 1
        # except:
        #     print('选择的院系名称有误')