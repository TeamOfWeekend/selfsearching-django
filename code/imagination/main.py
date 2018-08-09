#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/8 21:50
"""

from .collegeInfo.imCollege import ImCollege
from .collegeInfo.imTypes import CollegeEnum


collegeList = []

gCollegeList = []


def main():
    collegeInfoMain()


def collegeInfoMain():
    for collegeE in CollegeEnum:
        college = ImCollege()
        college.name = collegeE.name
        college.id = collegeE.value
        college.createRandomAttrs()
        print("%s %d" % (college.name, college.getStudentNum()))
        gCollegeList.append(college)


def getCollege(collegeName):
    for college in gCollegeList:
        print("%s vs %s" % (college.name, collegeName))
        if college.name == collegeName:
            return college
    return None


