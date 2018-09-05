#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imClass.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:16
"""

from vv_lib.vv_college.student import ImStudent
from vv_lib.vv_college.grade import ImGrade


class ImClass:
    """大学班级"""
    def __init__(self):
        self._id = id            # 编号
        self._students_num = 0   # 学生数量
        self._students = []      # 学生，需要排序
        self._grade = None       # 所属年级

    def to_dict(self):
        """
        将所有属性放在一个字典中
        :return:
        """
        attributes = {}
        attributes['id'] = self.id
        attributes['students_num'] = self.students_num
        attributes['students_info'] = []
        for student in self.students:
            student_info = []
            student_info.append(student.name)
            student_info.append(student.id)
            student_info.append(student.sex)
            attributes['students_info'].append(student_info)
        return attributes

    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 3
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.id = attributes['id']
        self.students_num = attributes['students_num']
        students_info = attributes['students_info']
        for student_info in students_info:
            student = ImStudent()
            student.name = student_info[0]
            student.id = student_info[1]
            student.sex = student_info[2]
            self.students.append(student)

    def update_student_id(self):
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

        for i in range(0, len(self.students)):
            self.students[i].id = i + 1
            self.students[i].createId()

    def add_student(self, student):
        if not isinstance(student, ImStudent):
            raise TypeError('student')
        self.students_num += 1
        student.id = self.students_num
        self.students.append(student)

    def del_student(self, student_id):
        if not isinstance(student_id, int):
            raise TypeError('student_id')
        for student in self.students:
            if student_id == student.id:
                self.students_num -= 1
                self.students.remove(student)

    def get_student(self, student_id):
        """
        根据学生学号获取学生对象
        :param student_id:
        :return:
        """
        if not isinstance(student_id, int):
            raise TypeError('student_id')
        for student in self.students:
            if student.id == student_id:
                return student
        else:
            return None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('val')
        self._id = val

    @property
    def students_num(self):
        return self._students_num

    @students_num.setter
    def students_num(self, students_num):
        if not isinstance(students_num, int):
            raise TypeError('students_num')
        self._students_num = students_num

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        if not isinstance(students, list):
            raise TypeError('students')
        self._students = students

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if not isinstance(grade, ImGrade):
            raise TypeError('grade')
        self._grade = grade
