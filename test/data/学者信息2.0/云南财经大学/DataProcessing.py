# -*- coding: utf-8 -*-
import re
import pandas as pd

def clean_n(d_list):
    '''去除列表里面的\n 和空字符'''
    return [x.strip() for x in d_list if x.strip() != '']

def clean_null_list(d_list):
    '''去除里面的空列表'''
    return [x for x in d_list if len(x) > 0]

def clean_blank(d_list):
    '''去除\xa0'''
    return [x.replace(r'\xa0','') for x in d_list]

#def clear_dir_files(o_path,filetype):
#    '''获取目录下所有txt格式的文件'''
#    import os
#    names = []
#    for root, dirs, files in os.walk(o_path):
#        for file in files:
#            if filetype in file:
#                names.append(file)
#    for item in names:
##        try:
#        with open(o_path + item,encoding='utf-8') as f:
#            result = f.readlines()
#        result = clean_blank(result)
#        result = clean_n(result)
#        result = clean_null_list(result)
#        
#        n_path = 'clean/' + item
#        with open(n_path,'w',encoding='utf-8') as f:
#            for item in result:
#                f.write(item + '\n')
##            f.writelines(result)
##        except:
##            print('sth is wrong')
#            pass
#    print('finished cleaning..')
    

#clear_dir_files('raw/','.txt')
#with open('clean/安全与环境工程学院.txt','r',encoding='utf-8') as f:
#    result = f.readlines()
#print(result)
    
def find(data,item):
    '''返回找到的字段的下标'''
    return data.find(item)
    

    
    
def get_name(data):
    t_index = find(data,'姓名')
    if t_index > -1:
        txt = data[t_index+2: t_index+15]
        m = re.search(r'([\u4E00-\u9FA5]+)',txt)
        if m:
            return m.group(1)
    else:
        #要是没有找到，则在开头进行查找
        m = re.search(r'([\u4E00-\u9FA5]+)',data)
        if m:
            return m.group(1)
    return ''
def get_gender(data):
    t_index = find(data,'性别')
    if t_index > -1:
        txt = data[t_index+2: t_index+6]
        m = re.search(r'([\u7537|\u5973])',txt)
        if m:
            return m.group(1)
    index2 = find(data,'男')
    index3 = find(data,'女')
    if index2 > -1 and (data[index2 - 1] < u'\u4E00' or data[index2 + 1] > u'\u9FA5'):
        return '男'
    if index3 > -1 and (data[index3 - 1] < u'\u4E00' or data[index3 + 1] > u'\u9FA5'):
        return '女'
    return ''
def get_birth(data):
#    t_index = find(data,'出生年月')
#    if t_index > -1:
    return ''
def get_xueli(data):
    index1 = find(data,'硕士研究生')
    index2 = find(data,'博士研究生')
    i3 = find(data,'博士')
    i4 = find(data,'硕士')
    if index2 > -1:
        return '博士研究生'
    if index1 > -1:
        return '硕士研究生'
    if i3 > -1:
        return '博士'
    if i4 > -1:
        return '硕士'
    return ''
def get_xuewei(data):
    r1 = r'([\u4E00-\u9FA5]+学博士)'
    r2 = r'([\u4E00-\u9FA5]+学硕士)'
    m1 = re.findall(r1,data)
    m2 = re.findall(r2,data)
    i1 = find(data,'博士')
    i2 = find(data,'硕士')
    text = ''
    if len(m1) > 0:
        for item in m1:   
            if find(item,'得') > -1:  #去掉‘获得’ ‘获’
                item = item[find(item,'得') + 1:]
            if find(item,'获') > -1:
                item = item[find(item,'获') + 1:]
            text = text + item +' '
    if len(m2) > 0:
        for item in m2:   
            if find(item,'得') > -1:  #去掉‘获得’ ‘获’
                item = item[find(item,'得') + 1:]
            if find(item,'获') > -1:
                item = item[find(item,'获') + 1:]
            text = text + item +' '
    if len(text) == 0 and i1 > -1:
        return '博士'
    elif len(text) == 0 and i2 > -1:
        return '硕士'
    return text
def get_schools(data):
    return ''
def get_zhicheng(data):
    if find(data,'教授') > -1 and find(data,'副教授') == -1:
        return '教授'
    if find(data,'副教授') > -1:
        return '副教授'
    if find(data,'讲师') > -1:
        return '讲师'
def get_zhiwu(data):
    text = ''
    i1 = find(data,'是否博导：是')
    i4 = find(data,'是否博导： 是')
    i2 = find(data,'博士生导师')
    i3 = find(data,'博士研究生导师')
    if i1 > -1 or i2 > -1 or i3 > -1 or i4 > -1:
        text = text + '博士生导师'
    t1 = find(data,'是否硕导：是')
    t4 = find(data,'是否硕导： 是')
    t2 = find(data,'硕士生导师')
    t3 = find(data,'硕士研究生导师')
    if t1 > -1 or t2 > -1 or t3 > -1 or t4 > -1:
        text = text + ' ' + '硕士生导师'
    return text.strip()
#    t_index = find(data,'职务')
#    if t_index > -1:
#        txt = data[t_index+2: t_index+20]
#        m = re.search(r'([\u4E00-\u9FA5]+)',txt)
#        if m:
#            return m.group(1)
#    return '' 
def get_email(data):
#    邮箱、电子邮箱、email、Email、EMAIL
    m = re.search( r"([-_\w\.]{0,64}@([-\w]{1,63}\.)*[-\w]{1,63})",data)
    if m:
        return m.group(1)
    return ''
def get_phone(data):
    lists = ['电话','手机']
    for item in lists:
        i1 = find(data,item)
        if i1 > -1 :
            text = data[i1 + 2 : i1 + 20]
            m = re.search(r"(\d+)",text)
            if m:
                return m.group(1).strip('\'')
    return ''
def get_web(data):
    i1 = find(data,'网址：')
    if i1 == -1:
        return ''
    return data[i1+3:].strip()
    
    
def get_dir_filenames(path,ftype):
    '''获取目录下所有指定格式的文件名'''
    import os
    names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if ftype in file:
                names.append(file)
    return names

def final_cleaning(school, fpath,npath):
    '''输入学院的所有记录，进行清洗，并提取相应字段'''
    import os
    isExists = os.path.exists(npath)
    if not isExists:
        os.makedirs(npath) 
        print('目录创建成功')
    else:
        print('目录已存在')
    with open(fpath,'r',encoding='utf-8') as f:
        datas = f.readlines()
    datas = clean_null_list(clean_n(datas)) #初步清洗
#    new_datas = pd.DataFrame(columns=['性别'])
    new_datas = pd.DataFrame(columns=['姓名','性别','出生年月','学历','学位','毕业学校','所属学院','职称','职务','电子邮件','电话','工作单位（院校）','所有信息','网址'])
    for data in datas:
        data1 = data.replace('\xa0','')
        data2 = data1.replace(' ','')
        name = get_name(data2)
        gender = get_gender(data)
        birth = get_birth(data)
        xueli = get_xueli(data)
        xuewei = get_xuewei(data)
        Graduated_school = get_schools(data)
        college = fpath[:-4]
        zhicheng = get_zhicheng(data)
        zhiwu = get_zhiwu(data)
        email = get_email(data2)
        phone = get_phone(data)
        employer = school #学校
        web = get_web(data)
        all_message = data
        row = {'姓名':name,'性别':gender,'出生年月':birth,'学历':xueli,'学位':xuewei,'教育经历':Graduated_school,'所属学院':college,'职称':zhicheng,'职务':zhiwu,'电子邮件':email,'电话':phone,'工作单位（院校）':employer,'所有信息':all_message,'网址':web}
        new_datas = new_datas.append(row,ignore_index=True)
    new_datas.to_excel(npath + '/' + fpath[:-4] + '.xlsx')
    print('saving..' + fpath[:-4])


    
#fnames = get_dir_filenames('./','.txt')
#for item in fnames:
#    final_cleaning('首都经济贸易大学',item)
#final_cleaning('首都经济贸易大学','国际经济管理学院.txt')
fnames = get_dir_filenames('./','.txt')
for item in fnames:
    final_cleaning('云南财经大学',item,'清洗')
            