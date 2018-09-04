#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imAcademy.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:29
"""

from vv_lib.vv_college.major import ImMajor
from vv_lib.vv_college.college import ImCollege


class ImAcademy:
    """学院"""
    def __init__(self, college=None, mid=0):
        self._name = ''             # 名称
        self._id = mid              # 编号
        self._description = ''      # 学院概述
        self._majors_num = 0        # 专业数量
        self._majors_name = []      # 专业名称
        self._majors = {}           # 专业
        self._students_num = 0      # 学生数量
        self._teachers_num = 0      # 教师数量
        self._college = college     # 所属学校

    def to_dict(self):
        """
        将所有属性放在一个字典中
        :return:
        """
        attributes_dict = {}
        attributes_dict['name'] = self.name
        attributes_dict['id'] = self.id
        attributes_dict['description'] = self.description
        attributes_dict['majors_num'] = self.majors_num
        attributes_dict['majors_name'] = self.majors_name
        return attributes_dict

    def add_major(self, major):
        if not isinstance(major, ImMajor):
            raise TypeError('major')
        if major.name not in self.majors.keys():
            self.majors[major.name] = major

    def del_major(self, major_name):
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if major_name in self.majors.keys():
            del self.majors[major_name]

    def get_major(self, major_name):
        """
        根据专业名获取专业对象
        :param major_name:
        :return:
        """
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if major_name in self.majors.keys():
            return self.majors[major_name]
        else:
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name')
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('id')
        self._id = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('description')
        self._description = description

    @property
    def majors_num(self):
        return self._majors_num

    @property
    def majors_name(self):
        return self._majors_name

    @property
    def majors(self):
        return self._majors

    @majors.setter
    def majors(self, majors):
        if not isinstance(majors, dict):
            raise TypeError('major_dict')
        self._majors = majors

    @property
    def students_num(self):
        return self._students_num

    @property
    def teachers_num(self):
        return self._teachers_num

    @property
    def college(self):
        return self._college

    @college.setter
    def college(self, college):
        if not isinstance(college, ImCollege):
            raise TypeError('college')
        self._college = college
