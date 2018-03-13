# -*- coding:utf-8 -*-
'''
Created on 12 March 2018
@author: KEYS
说明：线性回归对数据进行预测
'''

import json  
import time, datetime

# 对时间进行比较排序
def sort(day_list, count_list):
    for i in range(len(day_list)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(day_list)-i-1):  # ｊ为列表下标
            if datetime.datetime.strptime(day_list[j], '%Y-%m-%d') > datetime.datetime.strptime(day_list[j+1], '%Y-%m-%d'):
                day_list[j], day_list[j+1] = day_list[j+1], day_list[j]
                count_list[j], count_list[j+1] = count_list[j+1], count_list[j]

# 训练的数据
FLAVOR_CHARACTER = 'Data/flavor_character.json'
FLAVOR_TIME_COUNT = 'Data/flavor_time_count.json'

# 读取文件
file=open(FLAVOR_CHARACTER,"r")
flavor_data = dict()
for line in file:
    flavor_data=json.loads(line)

# 规范化数据
for type in flavor_data:
    cur_flavor = flavor_data[type]
    # 时间序列
    daystr_list = list(cur_flavor.keys())
    # 数量序列
    count_list = list()
    for i in range(len(daystr_list)):
        count_list.append(cur_flavor[daystr_list[i]])

    # 对时间进行比较排序
    sort(daystr_list, count_list)
    flavor_data[type] = dict()
    flavor_data[type]['time'] = daystr_list
    flavor_data[type]['count'] = count_list

# 将虚拟机特征数据保存到json文件中
with open(FLAVOR_TIME_COUNT,'w') as outfile:  
    json.dump(flavor_data,outfile,ensure_ascii=False)  
    outfile.write('\n')