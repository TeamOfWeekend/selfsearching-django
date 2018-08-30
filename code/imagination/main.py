#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/8 21:50
"""

import platform, socket, json

from .collegeInfo.imCollege import ImCollege
from .collegeInfo.imAcademy import ImAcademy
from .collegeInfo.imMajor import ImMajor
from .collegeInfo.imGrade import ImGrade
from .collegeInfo.imClass import ImClass
from .collegeInfo.imStudent import ImStudent


def getSocketData(collegeName):
    ossys = platform.system()

    college = ''
    # college 作为服务器，实现本机进程间通信，为django提供数据
    if 'Windows' == ossys:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8003
        server.connect((host, port))
        # server.send(collegeName.encode())

        # server.send(repr({'college_name': collegeName}).encode())
        # data = server.recv(1024)
        # print(eval(data.decode()))

        server.send(repr({'college_name': collegeName}).encode())
        data = eval(server.recv(1024).decode())
        print(data)
        # print(data[0], '-->', data[1])

        server.shutdown(socket.SHUT_RDWR)
        server.close()
    elif 'Linux' == ossys:
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        raise OSError('Other operate system')

    return college


def getCollege( collegeName):
    """
    通过socket ipc获取college数据
    :param server:
    :param collegeName:
    :return:
    """
    # college = ImCollege()
    # server.send(collegeName.encode())
    # while server.recv(1024) < 1024:
    #     pass
    getSocketData(collegeName)
