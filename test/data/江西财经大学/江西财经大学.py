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
#            result = soup.select('.word')[0].find_all('p')
            result = soup.find_all('tbody')[-1].find_all('tr')
#            r2 = soup.select('.word')[0].find_all('div')
#            re2 = soup.find('tbody').find_all('tr')
        except:
            print('sth maybe wrong..')
            continue
#        detail.append(title.text.strip())
        for item in result:
#            detail.append(item.find_all('td')[-1].text.strip())
#        for item in r2:
#            detail.append(item.text.strip())
            f.write(item.find_all('td')[-1].text.strip() + '\n\n')
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
        result = soup.find_all('tbody')[-1].find_all('tr')
#        except:
#            print('err')
#            continue
        for item in result:
            temp = item.find_all('td')[-1]
#            for i in temp:
            if temp['href'].startswith('http'):
                n_urls.append(temp['href'])
            else:
                n_urls.append(index_url + i['href'])
#            try:
#                if item['href'].startswith('http'):
#                    n_urls.append(item['href'])
#                else:
#                    n_urls.append(url.replace('index.htm','') + item['href'])
#            except:
#                continue
    print('got urls..')
    return n_urls

urls = ['http://econ.jxufe.cn/news-show-3285.html']    
#u1 = 'http://gmxy.jxufe.cn/news-list-jiaoshiminglu-'
#for i in range(5):
#    i += 1
#    urls.append(u1 + str(i) +'.html')
#urls = get_urls(urls,'http://accdep.cueb.edu.cn/szdw/') 
#urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '经济学院.txt'
down_details(urls,filename) 