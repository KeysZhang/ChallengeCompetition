# -*- coding:utf-8 -*-
'''
Created on 12 March 2018
@author: KEYS
说明：将训练集数据分类，提取时间和统计数量
'''

import numpy, json, datetime

# 文件路径
TRAIN_MACHINE_ID = 'Data/train_machine_id.npy'
TRAIN_MACHINE_TYPE = 'Data/train_machine_type.npy'
TRAIN_MACHINE_DAY = 'Data/train_machine_day.npy'
FLAVOR_CHARACTER = 'Data/flavor_character.json'

# 导入训练集变量
train_machine_id = numpy.load(TRAIN_MACHINE_ID)
train_machine_type = numpy.load(TRAIN_MACHINE_TYPE)
train_machine_day = numpy.load(TRAIN_MACHINE_DAY)

# 要求的虚拟机规格
require_type = ['flavor1', 'flavor2', 'flavor3', 'flavor4', 'flavor5',
                'flavor6', 'flavor7', 'flavor8', 'flavor9', 'flavor10',
                'flavor11', 'flavor12', 'flavor13', 'flavor14', 'flavor15']

# 记录训练集开始和结束的时间
start_day = datetime.datetime.now()
end_day = datetime.datetime.strptime("1997-12-31", "%Y-%m-%d")
for day_str in train_machine_day:
    day = datetime.datetime.strptime(day_str, "%Y-%m-%d")
    start_day = min(start_day, day)
    end_day = max(end_day, day)


# 数据分类：根据规格分类，提取时间和统计对应的数量
flavor_data = dict()
for i in range(len(train_machine_type)):
    # 判断当前类型是为要求的规格且是否在字典中
    cur_type = train_machine_type[i]
    if cur_type not in require_type:
        continue
    if  cur_type not in flavor_data:
        flavor_data[cur_type] = dict()
    # 判断当前时间是否在对应类型的时间序列中
    cur_day = train_machine_day[i]
    if cur_day not in flavor_data[cur_type]:
        flavor_data[cur_type][cur_day] = 1
    else:
        flavor_data[cur_type][cur_day] += 1


# 对于每个规格的虚拟机，将不访问的时间下数量设置为0
for flavor in flavor_data.values():
    date = start_day
    while(date <= end_day):
        day_str = date.strftime("%Y-%m-%d")
        if day_str not in flavor.keys():
            flavor[day_str] = 0
        date = date + datetime.timedelta(days=1)

# 将虚拟机特征数据保存到json文件中
with open(FLAVOR_CHARACTER,'w') as outfile:  
    json.dump(flavor_data,outfile,ensure_ascii=False)  
    outfile.write('\n')