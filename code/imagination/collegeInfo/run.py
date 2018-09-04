#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/8 21:50
"""

import platform, socket

from .vv_lib.vv_ipc_msg.ipc_msg import IpcMsg, ModuleId, MSG_Type, MSG_SubType, IPC_Opcode
from .vv_lib.vv_college.college import ImCollege
from .vv_lib.vv_college.academy import ImAcademy
from .vv_lib.vv_college.major import ImMajor
from .vv_lib.vv_college.grade import ImGrade
from .vv_lib.vv_college.cclass import ImClass
from .vv_lib.vv_college.student import ImStudent
from .vv_lib.vv_college.teacher import ImTeacher


gCollege = None
gAcademy = None
gMajor = None
gGrade = None
gClass = None


server = None
os_sys = platform.system()

# 外部app作为服务器，实现本机进程间通信，为django提供数据
if 'Windows' == os_sys:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8003
elif 'Linux' == os_sys:
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
else:
    raise OSError('Other operate system')


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


def get_college_info(college_name):
    """
    通过socket ipc获取college数据
    :param college_name:
    :return:
    """
    # college = ImCollege()
    # server.send(collegeName.encode())
    # while server.recv(1024) < 1024:
    #     pass
    getSocketData(collegeName)


def send_ipc_wait_reply(module_id, msg_type, msg_subtype, opcode, data):
    """
    发送ipc消息，并等待应答
    :param ipc_msg_send:  待发送的ipc消息
    :param data: 要发送的数据
    :return:
    """
    global server
    ipc_msg_send = IpcMsg()
    ipc_msg_send.module_id = module_id
    ipc_msg_send.sender_id = ModuleId.Django
    ipc_msg_send.msg_type = msg_type
    ipc_msg_send.msg_subtype = msg_subtype
    ipc_msg_send.opcode = IPC_Opcode.Get
    ipc_msg_send.data = data

    server.connect((host, port))
    server.sendall(repr(ipc_msg_send.to_list()).encode())
    ipc_msg_recv = IpcMsg()
    ipc_msg_recv = eval(server.recv(1024).decode())
    server.shutdown(socket.SHUT_RDWR)
    server.close()

