# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:11:00 2019
知网-财税相关文献分析

@author: mlin
"""
import pandas as pd
import numpy as np

def get_names(path,filetype):
    '''获取目录下所有指定文件类型的文件名'''
    import os
    name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if filetype in file:
                name.append(file)
    return name

path = 'D:\\codes\\GitProject\\mycodes\\test\\data\\new\\'
# 对作者字段进行 value_count 统计
# 对来源进行统计 对单位进行统计
df = pd.DataFrame()
names = get_names(path,'xlsx')
for item in names:
    fp = path + item
    print(fp)
    temp = pd.read_excel(fp)
    df.append(temp)
    


