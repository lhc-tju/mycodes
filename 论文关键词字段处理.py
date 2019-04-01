import pandas as pd
import numpy as np
import re
'''
pandas.read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, parse_cols=None, parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, has_index_names=None, converters=None, dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)[source]
'''
file = pd.read_excel('mysamples/中央财大元数据2018.10.22原版.xlsx',usecols = 'I,T,W')

keywords = file['外文关键词']
newwords = []
for item in keywords:
    if item != item: #空值判断
        newwords.append(' ')
        continue
    temp = re.split(r'[，；、,;]|\s{3,5}',item)
    temp = [x.strip() for x in temp]
    newwords.append('||'.join(temp))

# 去掉|||| 
words = []
for item in newwords:
    temp = item.replace('|||||||||||','||')
    item = temp.replace('||||||||','||')
    temp = item.replace('||||||','||')
    item = temp.replace('||||','||')
    words.append(item)
    
file['外文关键词'] = words
file.to_excel('mysamples/林-清洁版7.0.xlsx')
print('ok')