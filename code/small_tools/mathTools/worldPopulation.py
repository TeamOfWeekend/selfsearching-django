#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : worldPopulation.py
@Software: PyCharm Community Edition
@Time    : 2018/7/22 18:17
"""

import json, os
import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle
from pygal_maps_world.i18n import COUNTRIES

POPULATION_DATA_FILE = 'small_tools\mathTools\population_json.json'

class WorldPopulationMap():
    """世界人口地图"""
    def __init__(self, year = 2016):
        # 年份
        self.pop_year = year
        # 某一年人口数据
        self.pop_data = {}


    def load_population_data(self):
        """从文件中导入某年的人口数据"""
        with open(POPULATION_DATA_FILE) as f:
            datas_load = json.load(f)
        for data_load in datas_load:
            if self.pop_year == int(data_load['Year']):
                country_name = data_load['Country Name']
                population = int(float(data_load['Value']))
                country_code = self.get_country_code(country_name)
                if country_code:
                    self.pop_data[country_code] = population


    def get_country_code(self, country_name):
        """根据国家名字，获取国别码"""
        for code, name in COUNTRIES.items():
            if name == country_name:
                return code
        #如果未找到，返回None
        return None


    def draw_population_map(self):
        """绘制世界人口地图"""
        self.load_population_data()
        # 根据人口数量将所有国家分为三组
        pop_data1, pop_data2, pop_data3 = {}, {}, {}
        for cc, pop in self.pop_data.items():
            if pop < 10000000:
                pop_data1[cc] = pop
            elif pop < 1000000000:
                pop_data2[cc] = pop
            else:
                pop_data3[cc] = pop

        world_map_style = RotateStyle('#3399AA', base_style=LightColorizedStyle)
        world_map = pygal.maps.world.World(style = world_map_style)
        world_map.title = 'World population in %d, by Country' % self.pop_year
        world_map.add('0-10m', pop_data1)
        world_map.add('10m-1bm', pop_data2)
        world_map.add('>1bm', pop_data3)
        world_map.render_to_file('small_tools\mathTools\world_population.svg')