#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/8 21:50
"""

import platform
import socket

from .vv_lib.vv_ipc_msg.ipc_msg import IpcMsg, ModuleId, MSG_Type, MSG_SubType, IPC_Opcode
from .vv_lib.vv_college.m_colleges import ImColleges
from .vv_lib.vv_college.m_college import ImCollege
from .vv_lib.vv_college.m_academy import ImAcademy
from .vv_lib.vv_college.m_major import ImMajor
from .vv_lib.vv_college.m_grade import ImGrade
from .vv_lib.vv_college.m_class import ImClass
from .vv_lib.vv_college.m_student import ImStudent
from .vv_lib.vv_college.m_teacher import ImTeacher


gAllColleges = ImColleges()
gCollege = ImCollege()
gAcademy = ImAcademy()
gMajor = ImMajor()
gGrade = ImGrade()
gClass = ImClass()
gStudent = ImStudent()
gTeacher = ImTeacher()


def get_all_colleges_info():
    """
    通过socket ipc获取所有college
    :return:
    """
    global gAllColleges
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.All_Colleges, MSG_SubType.Invalid, IPC_Opcode.Get, {})
    data_recv = msg_rcv.data
    gAllColleges.from_dict(data_recv)
    return data_recv


def get_college_info(college_name):
    """
    通过socket ipc获取college数据
    :param college_name:
    :return:
    """
    global gCollege
    data_send = {'college_name': college_name}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.College, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gCollege.from_dict(data_recv)
    return data_recv


def get_academy_info(academy_name):
    """
    通过socket ipc获取academy数据
    :param academy_name:
    :return:
    """
    global gCollege, gAcademy
    data_send = {'college_name': gCollege.name, 'academy_name': academy_name}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Academy, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gAcademy.from_dict(data_recv)
    return data_recv


def get_major_info(major_name):
    """
    通过socket ipc获取major数据
    :param major_name:
    :return:
    """
    global gCollege, gAcademy, gMajor
    data_send = {'college_name': gCollege.name, 'academy_name': gAcademy.name, 'major_name': major_name}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Major, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gMajor.from_dict(data_recv)
    return data_recv


def get_grade_info(grade_id):
    """
    通过socket ipc获取grade数据
    :param grade_id:
    :return:
    """
    global gCollege, gAcademy, gMajor, gGrade
    data_send = {'college_name': gCollege.name, 'academy_name': gAcademy.name, 'major_name': gMajor.name,
                 'grade_id': grade_id}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Grade, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gGrade.from_dict(data_recv)
    return data_recv


def get_class_info(class_id):
    """
    通过socket ipc获取class数据
    :param class_id:
    :return:
    """
    global gCollege, gAcademy, gMajor, gGrade, gClass
    data_send = {'college_name': gCollege.name, 'academy_name': gAcademy.name, 'major_name': gMajor.name,
                 'grade_id': gGrade.id, 'class_id': class_id}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Classs, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gClass.from_dict(data_recv)
    return data_recv


def get_student_info(student_id):
    """
    通过socket ipc获取student数据
    :param student_id:
    :return:
    """
    global gCollege, gAcademy, gMajor, gGrade, gClass, gStudent
    data_send = {'college_name': gCollege.name, 'academy_name': gAcademy.name, 'major_name': gMajor.name,
                 'grade_id': gGrade.id, 'class_id': gClass.id, 'student_id': student_id}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Student, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gStudent.from_dict(data_recv)
    return data_recv


def get_teacher_info(teacher_name):
    """
    通过socket ipc获取teacher数据
    :param teacher_name:
    :return:
    """
    global gCollege, gAcademy, gMajor, gTeacher
    data_send = {'college_name': gCollege.name, 'academy_name': gAcademy.name, 'major_name': gMajor.name,
                 'teacher_name': teacher_name}
    msg_rcv = send_ipc_wait_reply(ModuleId.College, MSG_Type.Teacher, MSG_SubType.Invalid, IPC_Opcode.Get, data_send)
    data_recv = msg_rcv.data
    gTeacher.from_dict(data_recv)
    return data_recv


def send_ipc_wait_reply(module_id, msg_type, msg_subtype, opcode, data):
    """
    发送ipc消息，并等待应答
    :param module_id:
    :param msg_type:
    :param msg_subtype:
    :param opcode:
    :param data:
    :return:
    """
    # server = None
    host = socket.gethostname()
    port = 8003
    os_sys = platform.system()

    # 外部app作为服务器，实现本机进程间通信，为django提供数据
    if 'Windows' == os_sys:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif 'Linux' == os_sys:
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        raise OSError('Other operate system')

    ipc_msg_send = IpcMsg()
    ipc_msg_send.module_id = module_id
    ipc_msg_send.sender_id = ModuleId.Django
    ipc_msg_send.msg_type = msg_type
    ipc_msg_send.msg_subtype = msg_subtype
    ipc_msg_send.opcode = opcode
    ipc_msg_send.data = data

    print('------------------------------------------------------')
    print(repr(ipc_msg_send.to_list()))
    print('------------------------------------------------------')

    server.connect((host, port))
    server.sendall(repr(ipc_msg_send.to_list()).encode())
    ipc_msg_recv = IpcMsg()
    data = eval(server.recv(1024).decode())
    print(data)
    ipc_msg_recv.from_list(data)
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    return ipc_msg_recv
