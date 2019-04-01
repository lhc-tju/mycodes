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
    '''处理情况：
    出生年月 xxxx/   xxx 出生 / xxx生  / 大牛（1950- —） / 出生日期：\nxxx
    '''
    r1 = r'出生年月[:：][\s\d\u4E00-\u9FA5]+'
    r2 = r'[\d\u4E00-\u9FA5]+出生'
    r3 = r'[\d\u4E00-\u9FA5]+生于'
    #r4 = r'（\d+[-—]+.*?）'
    r5 = r'出生日期[:：][\s\d\u4E00-\u9FA5]+'
    m1 = re.findall(r1,data)
    m2 = re.findall(r2,data)
    m3 = re.findall(r3,data)
    #m4 = re.findall(r4,data)
    m5 = re.findall(r5,data.replace(r'\n',''))
    def find_birth(text):
        data = re.findall(r'\d+',text)
        if len(data) > 0:  #在符合条件的匹配中检索数字
            year = data[0]
            if len(year) != 4:
                return ''
            if len(data) > 1:
                month = data[1]
                birth = str(year[:4]) + '年' + str(month) + '月' #预防199608的情况
            else:
                birth = str(year) + '年'
            return birth
        return ''    
    if len(m1) > 0:  
        birth = find_birth(m1[0])
        if len(birth) > 0:
            return birth
    if len(m2) > 0:
        birth = find_birth(m2[0])
        if len(birth) > 0:
            return birth
    if len(m3) > 0:
        birth = find_birth(m3[0])
        if len(birth) > 0:
            return birth 
    if len(m5) > 0:
        birth = find_birth(m5[0])
        if len(birth) > 0:
            return birth
    return ''
    
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
    if i3 > -1:
        return '博士研究生'
    if index1 > -1:
        return '硕士研究生'
    if i4 > -1:
        return '硕士研究生'
    return ''
def get_xuewei(data):
    r1 = r'([\u4E00-\u9FA5]+学博士)'
    r2 = r'([\u4E00-\u9FA5]+学硕士)'
    m1 = re.findall(r1,data)
    m2 = re.findall(r2,data)
    i1 = find(data,'博士')
    i2 = find(data,'硕士')
#    text = ''
    text = []
    if len(m1) > 0:
        for item in m1:   
            if find(item,'得') > -1:  #去掉‘获得’ ‘获’
                item = item[find(item,'得') + 1:]
            if find(item,'获') > -1:
                item = item[find(item,'获') + 1:]
            text.append(item)
    if len(m2) > 0:
        for item in m2:   
            if find(item,'得') > -1:  #去掉‘获得’ ‘获’
                item = item[find(item,'得') + 1:]
            if find(item,'获') > -1:
                item = item[find(item,'获') + 1:]
            text.append(item)
    text = list(set(text)) #去重
    if len(text) == 0 and i1 > -1:
        return '博士'
    elif len(text) == 0 and i2 > -1:
        return '硕士'
    return '||'.join(text).strip('|')
def get_schools(data):
    return ''
def get_zhicheng(data):
    if find(data,'教授') > -1 and find(data,'副教授') == -1:
        return '教授'
    if find(data,'副教授') > -1:
        return '副教授'
    if find(data,'讲师') > -1:
        return '讲师'
def get_xiaonei_zhiwu(data):
    text = []
    i1 = find(data,'是否博导：是')
    i4 = find(data,'是否博导： 是')
    i2 = find(data,'博士生导师')
    i3 = find(data,'博士研究生导师')
    if i1 > -1 or i2 > -1 or i3 > -1 or i4 > -1:
        text.append('博士生导师')
    t1 = find(data,'是否硕导：是')
    t4 = find(data,'是否硕导： 是')
    t2 = find(data,'硕士生导师')
    t3 = find(data,'硕士研究生导师')
    if t1 > -1 or t2 > -1 or t3 > -1 or t4 > -1:
        text.append('硕士生导师')
    return '||'.join(text).strip('|')
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
    
def get_qita_zhiwu(data):
    '''获取职务'''
    r0 = r'[\u4e00-\u9fa5]+'
    the_list = ['书记','院长','顾问','理事','会长','主任','主席']
    content = []
    for item in the_list:
        r1 = r0 + item
        match = re.findall(r1,data)
        for i in match:
            if i.find('任') > -1:
                i = i[i.find('任')+1:]
            if i.find('为') > -1:
                i = i[i.find('为')+1:]   # 是否加入这个指标待定
            content.append(i.strip('\' ， ；。'))
    #去重
    content = list(set(content))
    return '||'.join(content).strip('|')

def get_education(data):
    '''获取教育背景'''
    r0 = r'[\d\u4e00-\u9fa5]+'
    the_list = ['学士','硕士','博士，','博士后','硕导','博导','硕士生导师','博士生导师','教授']
    content = []
    for item in the_list:
        r1 = r0 + item
        match = re.findall(r1,data)
        for i in match:
            if i.find('学') == -1:  #过滤
                continue
            if i.find('得') > -1:
                i = i[i.find('得')+1:]
            if i.find('获') > -1:
                i = i[i.find('获')+1:]
            if i.find('为') > -1:
                i = i[i.find('为')+1:]
            content.append(i.strip('\' ；，。'))
    #去重
    content = list(set(content))
    return '||'.join(content).strip('|')

def get_field(data):
    '''获取研究方向
    处理情况：主要研究方向：|| 主要研究方向为 || 研究方向 xx || 研究领域：
    只接受中文和中文顿号 去掉最后的 等'''
    temp_list = re.findall('研究方向：[：、\s\u4e00-\u9fa5]+',data)
    if len(temp_list) > 0:
        temp = re.sub(r'\s+','',temp_list[0][5:]) #去空格、去定位项
        if temp[-1] == '等':
            temp = temp[:-1]
        content = temp.split('、')
        content = list(set(content))  #去重
        return '||'.join(content).strip('|')
    temp_list = re.findall('研究方向为[：\s\u4e00-\u9fa5、]+',data)
    if len(temp_list) > 0:
        temp = re.sub(r'\s+','',temp_list[0][5:]) #去空格、去定位项
        if temp[-1] == '等':
            temp = temp[:-1]
        content = temp.split('、')
        content = list(set(content))  #去重
        return '||'.join(content).strip('|')
    temp_list = re.findall('研究领域：[\s\u4e00-\u9fa5、]+',data)
    if len(temp_list) > 0:
        temp = re.sub(r'\s+','',temp_list[0][5:]) #去空格、去定位项
        if temp[-1] == '等':
            temp = temp[:-1]
        content = temp.split('、')
        content = list(set(content))  #去重
        return '||'.join(content).strip('|')
    return ''
def get_chengguo(data):
    '''获取科研成果
    处理情况：主持xxx 直到句号、分号'''
    temp_list = re.findall('主持.*?[。；]',data)
    content = []
    if len(temp_list) > 0:
        for temp in temp_list:
            content.append(temp.strip('。 ；：'))
        content = list(set(content))  #去重
        return '||'.join(content).strip('|')
    return ''

def get_timeline(data):
    '''获取时间轴（出生/学习/工作
    xx年xxxx  去掉过短的'''
    temp_list = re.findall('\d{4}年.*?[。；\s]',data)
    content = []
    my_filter = ['获','任','参加','在','入选','学习','毕业','访','为'] #用于过滤匹配结果
    if len(temp_list) > 0:
        for temp in temp_list:
            flag = True #用于标志过滤器	
            if len(temp) < 9: #去掉过短
                continue
            for item in my_filter:
                if temp.find(item) > -1:
                    flag = False
                    break
            if flag:  #如果数据中不包含过滤器中的值，则跳过
                continue
            content.append(temp.strip('。；： '))
        content = list(set(content))  #去重
        return '||'.join(content).strip('|')
    return '' 
    
   
def get_dir_filenames(path,ftype):
    '''获取目录下所有指定格式的文件名'''
    import os
    names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if ftype in file:
                names.append(file)
    return names

def final_cleaning():
    '''对汇总的财税学者信息进行进一步提取'''
    df = pd.read_excel('财税学者信息汇总1.0.xls',sheet_name='概览')
    new_datas = pd.DataFrame(columns=['姓名','性别','出生年月','学历','学位','职称','校内职务','其他职务','电子邮件','工作单位（院校）','学院','网址','教育背景','研究方向','成果','时间轴','所有信息'])
    for index,row in df.iterrows():
        if type(row['姓名']) == float:
            continue
        name = row['姓名'].strip()
        employer = row['工作单位（高校）'].strip() if type(row['工作单位（高校）']) == str else ''
        college = row['所属学院'] if type(row['所属学院'])   == str else ''
        if type(row['个人简介'])  == float:
            print(name + ' 没有学者信息详情，请详细比对')
            continue
        data = row['个人简介'].replace('\xa0','')
        data1 = data.replace(' ','')
        gender = get_gender(data)
        birth = get_birth(data)
        xueli = get_xueli(data)
        xuewei = get_xuewei(data)
        zhicheng = get_zhicheng(data)
        xiaonei_zhiwu = get_xiaonei_zhiwu(data)
        email = get_email(data1)
        web = get_web(data)
        zhicheng = get_zhicheng(data)
        qita_zhiwu = get_qita_zhiwu(data)
        education = get_education(data)
        field = get_field(data)
        chengguo = get_chengguo(data)
        timeline = get_timeline(data)
        all_message = data
        row = {'姓名':name,'性别':gender,'出生年月':birth,'学历':xueli,'学位':xuewei,'教育背景':education,'所属学院':college,'职称':zhicheng,'校内职务':xiaonei_zhiwu,'电子邮件':email,'工作单位（院校）':employer,'网址':web,'其他职务':qita_zhiwu,'研究方向':field,'成果':chengguo,'时间轴':timeline,'所有信息':all_message}
        new_datas = new_datas.append(row,ignore_index=True)
    new_datas.to_excel('财税学者信息深度.xlsx')
    print('finish..')

#注意： 博士后、博士 信息会重叠
final_cleaning()
            