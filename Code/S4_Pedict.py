# -*- coding:utf-8 -*-
'''
Created on 12 March 2018
@author: KEYS
说明：线性回归对数据进行预测
'''

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import json

FLAVOR_TIME_COUNT = 'Data/flavor_time_count.json'

# 读取文件
file=open(FLAVOR_TIME_COUNT,"r")
flavor_data = dict()
for line in file:  
    flavor_data=json.loads(line)

dta = flavor_data['flavor3']['time']
dta = pd.to_datetime(dta)
ts = dta['x']  # 生成pd.Series对象