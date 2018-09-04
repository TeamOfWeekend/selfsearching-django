#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : __init__.py.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 22:15
"""


class Default:
    """添加类说明"""

    # Constructor
    def __init__(self):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present"""
        pass

    # Accessor methods
    def isEmpty(self):
        """Return True if len(self) == 0, otherwise return False"""
        return True

    def __len__(self):
        """Return the numbers of items in self."""
        return 0

    def __str__(self):
        """Return the string representation of self."""
        return ''

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Return a new bag containing the contents of self and other."""
        return None

    def __eq__(self, other):
        """Return True if self == other."""
        return False

    def __ne__(self, other):
        """Return True if self != other."""
        return False

    def __lt__(self, other):
        """Return True if self < other."""
        return False

    def __le__(self, other):
        """Return True if self <= other."""
        return False

    def __gt__(self, other):
        """Return True if self > other."""
        return False

    def __ge__(self, other):
        """Return True if self >= other."""
        return False

    # Mutator methods
    def clear(self):
        """Make self become empty."""
        pass
