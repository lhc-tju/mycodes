# -*- coding: utf-8 -*-
import re
import pandas as pd

#find 硕导
	
def get_names(o_path,n_path,ftype):
    '''保存硕导名单，并以学院命名excel'''
    import os
    isExists = os.path.exists(n_path)
    if not isExists:
        os.makedirs(n_path) 
        print('目录创建成功')
    else:
        print('目录已存在')
    #获取目录下指定类型的文件名
    fnames = []
    for root, dirs, files in os.walk(o_path):
        for file in files:
            if ftype in file:
                fnames.append(file)
    writer = pd.ExcelWriter(n_path + '/硕导名单.xlsx')
    for name in fnames:
        try:
            df = pd.read_excel(name,usecols = 'B,J')
            s_name = []
            for index, row in df.iterrows():
                if type(row['职务']) == str:
                    if row['职务'].find('硕士生导师') > -1:
                        s_name.append(row['姓名'])
            df2 = pd.DataFrame({name[:-5]:s_name})
            df2.to_excel(writer,sheet_name=name[:-5])
            print('succeed...')
        except:
            print('failed...' + name)
    writer.save()
    

get_names('./','硕导名单','.xlsx')
