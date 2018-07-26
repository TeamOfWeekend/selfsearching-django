#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imMajor.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:30
"""


from .imGrade import ImGrade

class ImMajor():
    """专业"""
    def __init__(self, academy, id):
        # 名称
        self.name = ''
        # 编号
        self.id = id
        # 年级数量
        self.gradeNum = 0
        # 年级
        self.grades = []
        # 所属学院
        self.academy = academy


    def createRandomAttrs(self):
        """创建随机属性"""
        # 四个年级，每个年级班级数目随机
        for i in range(1, 5):
            grade = ImGrade(self, i)
            grade.createRandomAttrs()
            self.grades.append(grade)
            self.gradeNum += 1
            # ranInt = random.randint(CLASSS_IN_MAJOR_MIN, CLASSS_IN_MAJOR_MAX)
            # for j in range(CLASSS_IN_MAJOR_MIN, ranInt + 1):
            #     classs = ImClass()
            #     classs.createRandomAttrs()
            #     self.grades[i].append(classs)


