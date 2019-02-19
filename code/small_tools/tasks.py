#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : tasks.py
@Software: PyCharm Community Edition
@Time    : 2019/2/13 22:03
"""


from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def test_add(x, y):
    print('tessssssssssssssssssst')
    return x+y