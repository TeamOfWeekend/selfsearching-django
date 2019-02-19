#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : tasks.py
@Software: PyCharm Community Edition
@Time    : 2019/1/28 16:28
"""

from celery.task import task


# 自定义要执行的task任务
@task
def print_hello():
    return 'hello celery and diango...'
