#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/8 21:50
"""

from .imCollege import ImCollege
from .imTypes import CollegeEnum, AcademyEnum

collegeList = []

if __name__ == '__main__':
      college = ImCollege()
      collegeList.append(college)


def getCollege(collegeName):
    for college in collegeList:
        if college.name == collegeName:
            return college
    return None


