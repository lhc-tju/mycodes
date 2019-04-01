# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:25:13 2019

@author: mlin
"""
import requests 
from bs4 import BeautifulSoup

def down_details(urls,filenames):
    '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    f = open(filenames,'w',encoding='utf-8')
    for url in urls:
        detail = []
        #可以加上try
        try:
            res = requests.get(url,headers=headers)
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
            result = soup.select('.read')[0].find_all('p')
#            r2 = soup.select('.xxbox_tea')
#            re2 = soup.find('tbody').find_all('tr')
        except:
            print('sth maybe wrong..')
            continue
#        detail.append(title.text.strip())
        for item in result:
            detail.append(item.text.strip())
#        for item in r2:
#            detail.append(item.text.strip())
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
    for url in urls:
        try:
            res = requests.get(url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text,'lxml')     
    #        result = soup.find('tbody')[0].find_all('tr')[-1].find_all('a')
            result = soup.select('#wp_news_w35')[0].find_all('a')
        except:
            print('err')
            continue
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
                    n_urls.append(url[:-10] + item['href'])
            except:
                continue
    print('got urls..')
    return n_urls

u1 = 'http://www.suibe.edu.cn/7386/list'  
urls = []
for i in range(12):
    i += 1
    urls.append(u1 + str(i) + '.htm')
urls = get_urls(urls,'http://www.suibe.edu.cn') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '上海对外经贸大学.txt'
down_details(urls,filename) 