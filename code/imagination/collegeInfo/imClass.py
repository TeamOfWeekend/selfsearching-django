#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imClass.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:16
"""

import random
from .imStudent import ImStudent
from .imTypes import STUDENTS_IN_CLASS_MAX, STUDENTS_IN_CLASS_MIN

class ImClass():
    """大学班级"""
    def __init__(self, grade, id):
        # 编号
        self.id = id
        # 学生数量
        self.studentNum = 0
        # 学生
        self.students = []
        # 所属年级
        self.grade = grade


    def createRandomAttrs(self):
        """生成随机属性"""
        self.studentNum = random.randint(STUDENTS_IN_CLASS_MIN, STUDENTS_IN_CLASS_MAX)
        for i in range(0, self.studentNum):
            stu = ImStudent(self)
            stu.createRandomAttrs()
            self.students.append(stu)
        self.sortStudentsIdByNamePinYin()


    def sortStudentsIdByNamePinYin(self):
        """按名字顺序对学生进行排序"""
        n = len(self.students)
        while n > 1:
            swapped = False
            i = 0
            while i < (n - 1):
                # print("%s  %s" %(self.students[i].name, self.students[i+1].name))
                # print(self.students[i].name < self.students[i+1].name)
                if self.students[i].namePinYin > self.students[i+1].namePinYin:
                    self.students[i], self.students[i+1] = self.students[i+1], self.students[i]
                    swapped = True
                i += 1
            if False == swapped:
                break
            n -= 1

        for i in range(0,len(self.students)):
            self.students[i].id = i + 1
            self.students[i].createId()





