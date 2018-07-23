#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : random_walk.py
@Software: PyCharm Community Edition
@Time    : 2018/7/19 22:51
"""

import os
import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """生成一个随机漫步数据的表"""
    def __init__(self, numPoints = 5000):
        """随机漫步的步数"""
        self.numPoints = numPoints
        #坐标初值(0,0)
        self.xValue = [0]
        self.yValue = [0]


    #填充所有点的坐标
    def fillWalk(self):
        self.xValue = [0]
        self.yValue = [0]
        while len(self.xValue) < self.numPoints:
            xDirection = choice([1, -1])
            xDistance  = choice(range(1,6))
            xStep = xDirection * xDistance

            yDirection = choice([1, -1])
            yDistance = choice(range(1, 6))
            yStep = yDirection * yDistance

            self.xValue.append(xStep + self.xValue[-1])
            self.yValue.append(yStep + self.yValue[-1])


    #绘制随机漫步图
    def drawWalkMap(self):
        """多次绘制漫步图"""
        while True:
            keepRunning = input("Make a new random walk? (y/n) :")
            if 'n' == keepRunning or 'N' == keepRunning:
                break
            numPoints = int(input("Input point number : "))
            self.numPoints = numPoints
            self.fillWalk()
            #设置绘图窗口的尺寸
            plt.figure(dpi=128, figsize=(10, 6))

            plt.scatter(self.xValue, self.yValue, c=range(self.numPoints), cmap=plt.cm.Blues,
                        edgecolor=None, s=15)
            # 突出起点和终点
            plt.scatter(0, 0, c='green', edgecolor=None, s=100)
            plt.scatter(self.xValue[-1], self.yValue[-1], c='red', edgecolor=None, s=100)
            #隐藏坐标轴
            plt.axes().get_xaxis().set_visible(False)
            plt.axes().get_yaxis().set_visible(False)
            #显示绘图结果
            # plt.show()
            plt.savefig(r'small_tools\mathTools\randomWalk.png')

