# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:36:52 2019

@author: mlin
"""
#首都经济贸易大学
import requests 
from bs4 import BeautifulSoup

def down_details(urls,filenames):
    f = open(filenames,'w',encoding='utf-8')
    for url in urls:
        detail = []
        #可以加上try
        try:
            res = requests.get(url)
        except:
            print('the url was wrong: ' + url)
            continue
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'lxml') 
#        if '教授' not in res.text:
#            continue
        #针对性更改,可设置多个result
        try:
#            title = soup.select('.box_lrt')[0]
            result = soup.select('.pic_tea')
            r2 = soup.select('.xxbox_tea')
#            re2 = soup.find('tbody').find_all('tr')
        except:
            print('sth maybe wrong..')
            continue
#        detail.append(title.text.strip())
        for item in result:
            detail.append(item.text.strip())
        for item in r2:
            detail.append(item.text.strip())
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
    for url in urls:
#        try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'lxml')     
#        result = soup.find('tbody')[0].find_all('tr')[-1].find_all('a')
        result = soup.select('.con01_tea')[0].find_all('a')
#        except:
#            print('err')
#            continue
        for item in result:
#            temp = item.find_all('a')
#            for i in temp:
#                if i['href'].startswith('http'):
#                    n_urls.append(i['href'])
#                else:
#                    n_urls.append(index_url + i['href'])
            try:
                if item['href'].startswith('http'):
                    n_urls.append(item['href'])
                else:
                    n_urls.append(url.replace('index.htm','') + item['href'])
            except:
                continue
    print('got urls..')
    return n_urls

urls = ['http://isem.cueb.edu.cn/xyry/index.htm']    
urls = get_urls(urls,'http://accdep.cueb.edu.cn/szdw/') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '国际经济管理学院.txt'
down_details(urls,filename) 