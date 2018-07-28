#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : person.py
@site    : 
@Time    : 2018/7/26 14:42
@Software: PyCharm Community Edition
"""

from .enumTypes import SexEnum


AGE_MIN = 0
AGE_MAX = 170

# 身高最大最小值，单位cm
HEIGHT_MIN = 0
HEIGHT_MAX = 300

# 体重最大最小值，单位kg
WEIGHT_MIN = 0
WEIGHT_MAX = 300


class Person:
    """自然人的类"""

    # Constructor
    def __init__(self, name='', age=0, sex=SexEnum.male):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present"""

        # 名字、身份证号、年龄、性别、身高、体重
        self._name = name
        self._idCardNum = 0
        self._sex = sex
        self._age = age
        self._height = 0
        self._weight = 0
        # 胸围、腰围、臀围
        self._bust = 0
        self._waist = 0
        self._hips = 0
        # 是否结婚
        self._married = False



    def __str__(self):
        """Return the string representation of self."""
        msg = ''
        msg += ("%-10s : %s\n" % ('name', self._name))
        msg += ("%-10s : %s\n" % ('age', str(self._age)))
        msg += ("%-10s : %s\n" % ('sex', self._sex.name))
        return msg


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('人的名字必须是字符串')
        self._name = name

    @property
    def idCardNum(self):
        return self._idCardNum

    @idCardNum.setter
    def idCardNum(self, id):
        if not isinstance(id, int):
            raise ValueError('人的身份证号必须是数字')
        self._idCardNum = id

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        if sex not in SexEnum:
            raise ValueError('人的性别必须从SexEnum中选择')
        self._idCardNum = id

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('人的年龄必须是数字')
        if age < AGE_MIN or age > AGE_MAX:
            raise ValueError('人的年龄范围<%d, %d>', (AGE_MIN, AGE_MAX))
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, float) and not isinstance(height, int):
            raise ValueError('人的身高必须是数字')
        if height < HEIGHT_MIN or height > HEIGHT_MAX:
            raise ValueError('人的身高范围<%d, %d>', (HEIGHT_MIN, HEIGHT_MAX))
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, float) and not isinstance(weight, int):
            raise ValueError('人的体重必须是数字')
        if weight < WEIGHT_MIN or weight > WEIGHT_MAX:
            raise ValueError('人的体重范围<%d, %d>', (WEIGHT_MIN, WEIGHT_MAX))
        self._weight = weight

    @property
    def married(self):
        return self._married

    @married.setter
    def married(self, val):
        if not isinstance(val, bool):
            raise ValueError('人的婚姻状况必须是Ture或False')
        self._married = val
