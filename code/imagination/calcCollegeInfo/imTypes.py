#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imTypes.py
@site    : 
@Time    : 2018/7/25 11:19
@Software: PyCharm Community Edition
"""

from enum import Enum, unique


@unique
class CollegeEnum(Enum):
    北京大学 = 1
    清华大学 = 2
    中国人民大学 = 3
    中国航空航天大学 = 4
    郑州大学 = 5


@unique
class AcademyEnum(Enum):
    计算机学院 = 1
    信息工程学院 = 2
    电气工程学院 = 3
    医学院 = 4
    土木工程学院 = 5
    机械工程学院 = 6
    理学院 = 7
    文学院 = 8
    历史学院 = 9



ACADEMY_MAJOR_DIR = {'计算机学院' : ['软件工程', '计算机科学与技术', '计算机软件'],
                     '信息工程学院' : ['信息工程', '通信工程', '电子信息工程'],
                     '电气工程学院' : ['电气工程及其自动化', '自动化', '生物医学工程'],
                     '医学院' : ['基础医学', '预防医学', '临床医学', '麻醉学', '医学影像'],
                     '土木工程学院' : ['土木工程', '水务工程'],
                     '机械工程学院' : ['机械设计制造及自动化', '材料成型机控制工程', '工业设计'],
                     '理学院' : ['数学与应用数学', '信息与计算科学', '数理基础科学'],
                     '文学院' : ['图书馆学', '档案学', '汉语言文学'],
                     '历史学院' : ['历史学', '考古学', '世界历史', '民族学'],}


# 每个专业每级班级数的最大最小值
CLASSS_IN_MAJOR_MIN = 1
CLASSS_IN_MAJOR_MAX = 5

# 每个班学生数量的最大最小值
STUDENTS_IN_CLASS_MAX = 50
STUDENTS_IN_CLASS_MIN = 5