#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : vprocess.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 20:55
"""

from multiprocessing import queues


class VQueue(queues.Queue):
    """添加类说明"""
    def __init__(self, qid, name, size, ctx):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present
        name : 进程名
        func : 进程代码入口
        queue : 进程通信队列"""
        super().__init__(maxsize=size, ctx=ctx)
        if not isinstance(qid, int):
            raise TypeError('Process id must be int type')
        if not isinstance(name, str):
            raise TypeError('Process name must be str type')
        self.qid = qid
        self.name = name

    # def __str__(self):
    #     """返回进程名字"""
    #     return self.name


