# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:24:51 2019

@author: mlin
"""
import requests 
from bs4 import BeautifulSoup

def down_details(urls,filenames,i=1):
    import requests
    from bs4 import BeautifulSoup
    f = open(filenames,'w',encoding='utf-8')
    for url in urls:
        detail = []
        #可以加上try
        res = requests.get(url)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'lxml')
        if '教授' not in res.text:
            continue
        #针对性更改,可设置多个result
        result = soup.select('.wp_articlecontent')[0].find_all('td')
#        re2 = soup.select('.wp_articlecontent')[0].find_all('td')
        for item in result:
            detail.append(item.text.strip())
#        for item in re2:
#            detail.append(item.text.strip())
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
def get_urls(urls,index_url):
    n_urls =[]
    for url in urls:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'lxml')      
        result = soup.select('.wp_article_list')[0].find_all('a')[:-1]
        for item in result:
            #temp = item.find_all('a')
            #for i in temp:
            n_urls.append(index_url + item['href'])
    print('got urls..')
    return n_urls
# wp_articlecontent, 11p  工商管理学院
# 会计学院 抓取全部url 进入页面，只抓教授副教授

urls = ['http://iasfe.hbue.edu.cn/ab/f8/c7458a175096/page.htm','http://iasfe.hbue.edu.cn/a8/52/c7458a174162/page.htm','http://iasfe.hbue.edu.cn/ab/f9/c7458a175097/page.htm']
down_details(urls,'temp/财经高等研究院学院.txt')