# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:36:16 2019

@author: mlin
"""
#南京审计大学
import requests 
from bs4 import BeautifulSoup


def down_details(urls,filenames):
    import requests
    from bs4 import BeautifulSoup
    f = open(filenames,'w',encoding='utf-8')
    for url in urls:
        detail = []
        #可以加上try
        try:
            res = requests.get(url)
        except:
            continue
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'lxml')
#        if '教授' not in res.text:
#            continue
        #针对性更改,可设置多个result
        result = soup.select('#displayinfo_content')[0].find_all('td')
        re2 = soup.select('#displayinfo_content')[0].find_all('p')
        for item in result:
            detail.append(item.text.strip())
        for item in re2:
            detail.append(item.text.strip())
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
def get_urls(urls,index_url):
    n_urls =[]
    for url in urls:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'lxml')      
        result = soup.select('#newslist')[0].find_all('a')
        for item in result:
            #temp = item.find_all('a')
            #for i in temp:
            n_urls.append(index_url + item['href'])
    print('got urls..')
    return n_urls

urls = ['http://sga.nau.edu.cn/2022/list.htm','http://sga.nau.edu.cn/2024/list.htm','http://sga.nau.edu.cn/2025/list.htm','http://sga.nau.edu.cn/2026/list.htm','http://sga.nau.edu.cn/2027/list.htm','http://sga.nau.edu.cn/2028/list.htm']
index_url = 'http://sga.nau.edu.cn'
urls = get_urls(urls,index_url)
down_details(urls,'政府审计学院.txt')