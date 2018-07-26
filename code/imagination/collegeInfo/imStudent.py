#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imStudent.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:28
"""

import random, datetime
from pypinyin import pinyin, NORMAL

from enum import Enum, unique

from .vvlib import baijiaxing, person


@unique
class ImSex(Enum):
    male = 1
    female = 2


@unique
class MaleHobbies(Enum):
    篮球 = 1
    足球 = 2
    网球 = 3
    排球 = 4
    羽毛球 = 5
    台球 = 6
    玩游戏 = 7
    看书 = 8
    写代码 = 9
    看电影 = 10
    旅游 = 11

@unique
class FemaleHobbies(Enum):
    逛街 = 1
    买买买 = 2
    看书 = 3
    看电影 = 4
    旅游 = 5
    化妆 = 6


class ImStudent(person.Person):
    """大学生"""
    def __init__(self, classs):
        # 继承父类的构造方法，两种方式
        # person.Person.__init__()
        super(ImStudent, self).__init__()

        # 学号
        self.id = 0
        # 名字拼音
        self.namePinYin = ''
        # 入学年份
        self.year_in_college = 0
        # 所属班级
        self.classs = classs
        # 爱好
        self.hobbies = []


    def createRandomName(self):
        """随机获取一个名字"""
        self.name = baijiaxing.getRandomName()
        # 将汉字转换为拼音，pinyin()转换后是列表，不加style转换后带声调
        pos = 1
        for piny in pinyin(self.name, style=NORMAL):
            piny = ''.join(piny)
            if (1 == pos) or (2 == pos):
                piny = piny.capitalize()
            self.namePinYin += piny
            pos += 1
        # print(self.namePinYin)


    def createRandomSex(self):
        """随机获取性别"""
        ranInt = random.randint(1, len(ImSex))
        self.sex = ImSex(ranInt)


    def createRandomHobbies(self):
        """获取随机爱好"""
        ranInt = random.randint(1,5)
        if ImSex.male == self.sex:
            while ranInt:
                self.hobbies.append(MaleHobbies(random.randint(1, len(MaleHobbies))))
                ranInt -= 1
        else:
            while ranInt:
                self.hobbies.append(FemaleHobbies(random.randint(1, len(FemaleHobbies))))
                ranInt -= 1



    def createId(self):
        """根据入学年份、学校、院系、专业，生成学号，如 2018 000011 002 03 05"""
        self.id = self.year_in_college * 10**13\
                  + self.classs.grade.major.academy.college.id * 10**7\
                  + self.classs.grade.major.academy.id * 10**4\
                  + self.classs.grade.major.id * 10**2\
                  + self.id
        # print('%6s --> %d' % (self.name, self.id))


    def createRandomAttrs(self):
        """创建随机属性"""
        if datetime.datetime.now().month < 6:
            self.year_in_college = datetime.datetime.now().year - self.classs.grade.id
        else:
            self.year_in_college = datetime.datetime.now().year - self.classs.grade.id + 1

        self.createRandomName()
        self.createRandomSex()
        self.age = (datetime.datetime.now().year - self.year_in_college + 17)
        self.height = random.randint(130, 200)
        self.weight = random.random() + random.randint(30, 100)
        self.hobbies = []


    def getStudentAllInfo(self):
        """"""
        info = {}
