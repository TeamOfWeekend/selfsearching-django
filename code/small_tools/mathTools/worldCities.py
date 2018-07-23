#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : worldCities.py
@Software: PyCharm Community Edition
@Time    : 2018/7/22 18:31
"""

import json

# {"country": "China", "geonameid": 1792520, "name": "Tongzhou", "subcountry": "Beijing"}
# {"country": "China", "geonameid": 1794035, "name": "Songjiang", "subcountry": "Shanghai Shi"}
# {"country": "China", "geonameid": 1794140, "name": "Sishui", "subcountry": "Shandong Sheng"}
# {"country": "China", "geonameid": 1794479, "name": "Laixi", "subcountry": "Shandong Sheng"}


filename = 'world-cities_json.json'
with open(filename) as f:
    pop_data = json.load(f)


for pop_dict in pop_data:
    if pop_dict['country'] == 'China' and pop_dict['subcountry'] == 'Henan Sheng':
        print(pop_dict['country'] + ' - ' + pop_dict['subcountry'] + ' - ' + pop_dict['name'] + ' - ' + str(pop_dict['geonameid']))

