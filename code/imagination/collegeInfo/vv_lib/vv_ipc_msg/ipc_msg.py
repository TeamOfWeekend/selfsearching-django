#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : ipc_msg.py
@Software: PyCharm Community Edition
@Time    : 2018/8/22 22:16
"""

from enum import Enum, unique

@unique
class ModuleId(Enum):
    Django = 1
    College = 2
    Student = 3


@unique
class MSG_Type(Enum):
    All_Colleges = 1
    College = 2
    Academy = 3
    Major = 4
    Grade = 5
    Classs = 6
    Student = 7
    Teacher = 8


@unique
class MSG_SubType(Enum):    # 待扩展
    Invalid = 1


@unique
class IPC_Opcode(Enum):
    Add = 1         # 增加一项数据
    Del = 2         # 删除一项数据
    Update = 3      # 更新一项数据
    Get = 4         # 获取
    Getbulk = 5     # 批量获取
    Clear = 6       # 全部清空
    Enable = 7      # 使能
    Disable = 8     # 禁能
    Register = 9    # 注册
    UnRegister = 10 # 解注册
    Event = 11      # 事件
    Reply = 12      # 应答
    NoReply = 13    # 应答


@unique
class TLV_TAG(Enum):
    STR = 1
    INT = 2



class TLV():
    """tag、length、value数据结构"""
    def __init__(self, tag, length, value):
        """
        :param tag: 从枚举类TLV_TAG中选择
        :param length: >1
        :param value: 列表或字符串
        """
        if tag not in TLV_TAG.__members__.values():
            raise TypeError('tag must be a member of TLV_TAG')
        if length < 1:
            raise ValueError('length must be > 1')
        if not isinstance(value, str) or not isinstance(value, list):
            raise TypeError("value's type must be str or list")

        self.tag = tag
        self.length = length
        self.value = value


IPC_HDR_LEN = 5
IPC_MSG_LEN = 7

class IpcMsg:
    """添加类说明"""
    def __init__(self):
        self._module_id = 0
        self._sender_id = 0
        self._msg_type = 0
        self._msg_subtype = 0
        self._opcode = 0
        self._data_num = 0
        self._data = {}

    def __str__(self):
        return 'This is a ipc message'

    def data_add(self, key, value):
        """
        向IPC消息数据结构中增加一项数据
        :param key:
        :param value:
        :return:
        """
        if not isinstance(key, str):
            raise TypeError("key must be a str")
        self._data[key] = value
        self._data_num += 1

    def data_del(self, key, value):
        """
        从IPC消息数据结构中删除一项数据
        :param key:
        :param value:
        :return:
        """
        if not isinstance(key, str):
            raise TypeError("key must be a str")

        del self._data[key]

    def fill_hdr(self, hdr):
        """
        填充消息头
        :param hdr:长度为5的列表，且各项数据必须从上述枚举中取
        :return:
        """
        if not isinstance(hdr, list) or IPC_HDR_LEN != len(hdr):
            raise TypeError('hdr must be a list and length is %d' % IPC_HDR_LEN)
        self.module_id = hdr[0]
        self.sender_id = hdr[1]
        self.msg_type = hdr[2]
        self.msg_subtype = hdr[3]
        self.opcode = hdr[4]

    def fill_all(self, msg):
        """
        填充全部消息，包括消息头和数据
        :param msg: 列表，长度为7
        :return:
        """
        if not isinstance(msg, list) or IPC_MSG_LEN != len(msg):
            raise TypeError('msg must be a list and length is %d' % IPC_MSG_LEN)
        self.module_id = ModuleId(msg[0])
        self.sender_id = ModuleId(msg[1])
        self.msg_type = MSG_Type(msg[2])
        self.msg_subtype = MSG_SubType(msg[3])
        self.opcode = IPC_Opcode(msg[4])
        self.data_num = msg[5]
        self.data = msg[6]

    def to_list(self):
        """
        将消息的每个属性按顺序放置在列表中
        :return:
        """
        attrs_list = []
        attrs_list.append(self.module_id.value)
        attrs_list.append(self.sender_id.value)
        attrs_list.append(self.msg_type.value)
        attrs_list.append(self.msg_subtype.value)
        attrs_list.append(self.opcode.value)
        attrs_list.append(self.data_num)
        attrs_list.append(self.data)
        return attrs_list

    def from_list(self, data_list):
        """
        从list中获取各项数据
        :param data_list:
        :return:
        """
        if not isinstance(data_list, list):
            raise TypeError('data_list')
        if 7 != len(data_list):
            raise ValueError('data_list')
        self.module_id = ModuleId(data_list[0])
        self.sender_id = ModuleId(data_list[1])
        self.msg_type = MSG_Type(data_list[2])
        self.msg_subtype = MSG_SubType(data_list[3])
        self.opcode = IPC_Opcode(data_list[4])
        self.data_num = data_list[5]
        self.data = data_list[6]

    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        if module_id not in ModuleId.__members__.values():
            raise TypeError('module id must be member of ModuleId')
        self._module_id = module_id

    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        if sender_id not in ModuleId.__members__.values():
            raise TypeError('sender id must be member of ModuleId')
        self._sender_id = sender_id

    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        if msg_type not in MSG_Type.__members__.values():
            raise TypeError('message type must be member of MSG_Type')
        self._msg_type = msg_type

    @property
    def msg_subtype(self):
        return self._msg_subtype

    @msg_subtype.setter
    def msg_subtype(self, msg_subtype):
        if msg_subtype not in MSG_SubType.__members__.values():
            raise TypeError('message subtype must be member of MSG_SubType')
        self._msg_subtype = msg_subtype

    @property
    def opcode(self):
        return self._opcode

    @opcode.setter
    def opcode(self, opcode):
        if opcode not in IPC_Opcode.__members__.values():
            raise TypeError('opcode subtype must be member of IPC_Opcode')
        self._opcode = opcode

    @property
    def data_num(self):
        return self._data_num

    @data_num.setter
    def data_num(self, data_num):
        if not isinstance(data_num, int):
            raise TypeError('data_num must be type of int')
        self._data_num = data_num

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if not isinstance(data, dict):
            raise TypeError('data must be type of dict')
        self._data = data
        self.data_num = len(self.data)


# msg = IpcMsg()
# msg.data = {1:1}
# # list(msg)
# print(msg.data)
# # print(msg.to_list())
#
# b = {}
# a = {1:11, 2:22, 3:33}
# b = a
# print(b)