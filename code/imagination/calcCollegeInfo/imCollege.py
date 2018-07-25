#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imCollege.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:07
"""

import random
from .imTypes import CollegeEnum, AcademyEnum
from .imAcademy import ImAcademy


class ImCollege():
    """大学"""
    def __init__(self):
        """学校属性"""
        # 学校名称
        self.name = None
        # 学校编号
        self.id = 0
        # 学校地址
        self.address = ''
        # 学校级别
        self.level = None
        # 校园面积
        self.area = 0
        # 学院
        self.academies = {}


    def createRandomAttrs(self):
        """生成随机属性"""
        self.id = random.randint(1, len(CollegeEnum))
        self.name = CollegeEnum(self.id).name
        for academyE in AcademyEnum:
            academy = ImAcademy(self, academyE.value)
            academy.fillMajors()
            self.academies[academyE.name] = academy
        # print('--------------------------------------')
        # for key, val in self.academies.items():
        #     print(key)
        #     print(val.majors.keys())
        print(self.getStudentNum())


    def getStudentNum(self):
        """获取全校学生数量"""
        stuNum = 0
        for academy in self.academies.values():
            for major in academy.majors.values():
                for grade in major.grades:
                    for classs in grade.classes:
                        stuNum += len(classs.students)
        return stuNum




