# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:20:05 2019

@author: mlin
"""

#北京物质学院 数据清理
import re
import pandas as pd

with open('北京物质学院.txt',encoding='utf-8') as f:
    result = f.readlines()    
#name,gender,birth,xueli,xuewei,Graduated_school,college,jishuzhiwu,xingzhengzhiwu,
#email,phone

#检索，定位，正则匹配

#a = '永远年轻, 永远热泪盈眶'

def find(txt):
    m = re.search(r"('[\u4E00-\u9FA5]+')",txt)
    if m:
        return m.group(1).strip('\'')
    else:
        return ''


#df = pd.DataFrame(columns=['姓名','性别','出生年月','学历','学位','毕业学校','所属学院','专业技术职务','行政职务','电子邮件','电话'])
all_list = []
for item in result:
    #定位，正则匹配
    name = item[item.find('姓名')+4:item.find('姓名')+13].strip(',\'')
    name = find(name)
    gender = item[item.find('性别')+4:item.find('性别')+10]
    gender = find(gender)
    birth = item[item.find('出生年月')+6:item.find('出生年月')+ 18]
    birth = find(birth)
    xueli = item[item.find('学历')+4:item.find('学历')+13]
    xueli = find(xueli)
    xuewei =item[item.find('学位')+4:item.find('学位')+16]
    xuewei = find(xuewei)
    Graduated_school =item [item.find('毕业学校')+6:item.find('毕业学校')+23]
    Graduated_school = find(Graduated_school)
    college = item[item.find('所属学院')+6:item.find('所属学院')+16]
    college = find(college)
    jishuzhiwu = item[item.find('专业技术职务')+8:item.find('专业技术职务')+16]
    jishuzhiwu = find(jishuzhiwu)
    xingzhengzhiwu = item[item.find('行政职务')+6:item.find('行政职务')+20]
    xingzhengzhiwu = find(xingzhengzhiwu)
    
    email = item[item.find('电子邮件')+6:item.find('电子邮件')+40]
    email_m = re.search(r"('[a-zA-Z0-9_.\-@]+')",email)
    if email_m:
        email = email_m.group(1).strip('\'')
    else:
        email = ''
    phone = item[item.find('电话')+4:item.find('电话')+22]
    phone_m = re.search(r"('\d+')", phone)
    if phone_m:
        phone = phone_m.group(1).strip('\'')
    else:
        phone = ''
    #df.append([name,gender,birth,xueli,xuewei,Graduated_school,college,jishuzhiwu,xingzhengzhiwu,email,phone],)
    a = [name,gender,birth,xueli,xuewei,Graduated_school,college,jishuzhiwu,xingzhengzhiwu,email,phone]
    all_list.append(a)
df = pd.DataFrame(all_list,columns=['姓名','性别','出生年月','学历','学位','毕业学校','所属学院','专业技术职务','行政职务','电子邮件','电话'])
df.to_excel('北京电影物质学院.xlsx')
    

    