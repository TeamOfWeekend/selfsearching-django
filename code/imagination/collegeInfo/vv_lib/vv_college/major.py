#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imMajor.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:30
"""


from vv_lib.vv_college.grade import ImGrade
from vv_lib.vv_college.academy import ImAcademy
from vv_lib.vv_college.teacher import ImTeacher


class ImMajor:
    """专业"""
    def __init__(self):
        self._name = ''             # 名称
        self._id = 0                # 编号
        self._teachers_num = 0      # 专业教师数量
        self._teachers_name = []    # 教师姓名列表
        self._teachers = {}         # 教师
        self._students_num = 0      # 学生数量
        self._grades_num = 0        # 年级数量
        self._grades = {}           # 年级对象字典
        self._academy = None        # 所属学院

    def to_dict(self):
        """
        将所有属性放在字典中
        :return:
        """
        attributes_dict = {}
        attributes_dict['name'] = self.name
        attributes_dict['id'] = self.id
        attributes_dict['teachers_num'] = self.teachers_num
        attributes_dict['teachers_name'] = self.teachers_name
        attributes_dict['grades_num'] = self.grades_num
        return attributes_dict

    def add_grade(self, grade):
        if not isinstance(grade, ImGrade):
            raise TypeError('grade')
        if grade.id not in self.grades.keys():
            self.grades[grade.id] = grade

    def del_grade(self, grade_id):
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if grade_id in self.grades.keys():
            del self.grades[grade_id]

    def get_grade(self, grade_id):
        """
        根据年级编号获取年级对象
        :param grade_id:
        :return:
        """
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if grade_id in self.grades.keys():
            return self.grades[grade_id]
        else:
            return None

    def add_teacher(self, teacher):
        if not isinstance(teacher, ImTeacher):
            raise TypeError('teacher')
        if teacher.name not in self.teachers.keys():
            self.teachers[teacher.name] = teacher

    def del_teacher(self, teacher_name):
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        if teacher_name in self.teachers.keys():
            del self.teachers[teacher_name]

    def get_teacher(self, teacher_name):
        """
        根据教师姓名获取教师对象
        :param teacher_name:
        :return:
        """
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        if teacher_name in self.teachers.keys():
            return self.teachers[teacher_name]
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
        if not isinstance(val, str):
            raise TypeError('name')
        self._id = val

    @property
    def teachers_num(self):
        return self._teachers_num

    @property
    def teachers_name(self):
        return self._teachers_name

    @property
    def teachers(self):
        return self._teachers

    @teachers.setter
    def teachers(self, teachers):
        if not isinstance(teachers, dict):
            raise TypeError('teachers')
        self._teachers = teachers

    @property
    def students_num(self):
        return self._students_num

    @property
    def grades_num(self):
        return self._grades_num

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise TypeError('grades')
        self._grades = grades

    @property
    def academy(self):
        return self._academy

    @academy.setter
    def academy(self, academy):
        if not isinstance(academy, ImAcademy):
            raise TypeError('academy')
        self._academy = academy
