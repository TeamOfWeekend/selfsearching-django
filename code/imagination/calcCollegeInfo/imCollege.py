#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imCollege.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:07
"""


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
        self.academies = []
