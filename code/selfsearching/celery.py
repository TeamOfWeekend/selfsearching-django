#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : celery.py
@Software: PyCharm Community Edition
@Time    : 2019/1/28 14:18
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selfsearching.settings')

# 注册Celery的APP
app = Celery('selfsearching')
# 绑定配置文件
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')

# 自动发现各个app下的tasks.py文件
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))
