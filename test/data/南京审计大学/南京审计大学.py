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
        try:
            re2 = soup.select('.wp_articlecontent')[0].find_all('td')
#            result = soup.select('.Article_Title')
        except:
            print('sth maybe wrong..')
            continue
#        for item in result:
#            detail.append(item.text.strip())
        for item in re2:
            detail.append(item.text.strip())
        
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
            result = soup.select('#wp_news_w4')[0].find_all('a')
        except:
            print('err')
            continue
        for item in result:
            #temp = item.find_all('a')
            #for i in temp:
            if item['href'].startswith('http'):
                n_urls.append(item['href'])
            else:
                n_urls.append(index_url + item['href'])
    print('got urls..')
    return n_urls



'''