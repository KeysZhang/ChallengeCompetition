# -*- coding:utf-8 -*-
'''
Created on 12 March 2018
@author: KEYS
说明：提取训练集数据并转化为可数组的存储
'''

import numpy

# 文件路径
TRAINDATAPATH = 'Data/TrainData.txt'

# 存放训练集数据
machine_id = []
machine_type = []
machine_day = []
machine_second = []

# 读取训练集内容
with open(TRAINDATAPATH, 'r') as train_to_read:
    while True:
        lines = train_to_read.readline() # 整行读取数据
        if not lines:
            break
        data_id, data_type, data_day, data_second = [str(i) for i in lines.split()]
        machine_id.append(data_id)
        machine_type.append(data_type)
        machine_day.append(data_day)
        machine_second.append(data_second)

numpy.save('Data/train_machine_id.npy', machine_id)
numpy.save('Data/train_machine_type.npy', machine_type)
numpy.save('Data/train_machine_day.npy', machine_day)
numpy.save('Data/train_machine_second.npy', machine_second)