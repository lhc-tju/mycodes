# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver #抓取js加载的动态网页

def down_details(urls,filenames):
    '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'''
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    f = open(filenames,'w',encoding='utf-8')
    #针对采用了反爬措施的网站，启用selenium
#    opt = webdriver.ChromeOptions()
#    opt.add_argument('--headless')
#    drive = webdriver.Chrome(chrome_options=opt)
    for url in urls:
        detail = []
        #可以加上try
        try:
            res = requests.get(url)
            res.encoding='utf-8'
            soup = BeautifulSoup(res.text,'lxml')
#            drive.get(url)
#            data = drive.page_source
#            soup = BeautifulSoup(data,'lxml')
        except:
            print('the url was wrong: ' + url)
            continue
         
        #针对性更改,可设置多个result
        try:
            title = soup.find('h2')
            result = soup.select('.content')[0].find_all('p')
#            r2 = soup.select('.tab-content')[0].find_all('div')
#            r2 = soup.find('tbody').find_all('p')
        except:
            print('sth maybe wrong..' + url)
            continue
        try:
            detail.append(title.text.strip())
        except:
            pass
        for item in result:
            detail.append(item.text.strip())
#            try:
#                temp = item.select('.articleContent')[0]
#            f.write(item.text.strip().replace(r'\xa0','') + '网址：' + url + '\n')
#            except:
#                pass
##            for i in temp:
#        for item in r2:
#            detail.append(item.text.strip())
        detail.append('网址：' + url + ' ')
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
    #针对采用了反爬措施的网站，启用selenium
#    opt = webdriver.ChromeOptions()
#    opt.add_argument('--headless')
#    drive = webdriver.Chrome(chrome_options=opt)
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for url in urls:
#        try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'lxml')   
#            drive.get(url)
#            data = drive.page_source
#            soup = BeautifulSoup(data,'lxml')
        result = soup.select('#mylist')[0].find_all('a')
#            result = soup.find_all('table')[2].find_all('a')
#        except:
#            print('err')
#            continue
        for item in result:
#            temp = item.find_all('a')
#            if temp['href'].startswith('http'):
#                n_urls.append(temp['href'])
#            else:
#                n_urls.append(index_url + temp['href'].replace(r'../',''))
#            for i in temp:
#                if i['href'].startswith('http'):
#                    n_urls.append(i['href'])
#                else:
#                    n_urls.append(index_url + i['href'])
            if item['href'].startswith('http'):
                n_urls.append(item['href'])
            else:
                n_urls.append(index_url.replace('index.htm','') + item['href'].replace(r'../',''))
    print('got urls..')
    return n_urls
#u1 = 'http://xinxi.xaufe.edu.cn/teacher.asp?page='
#urls = []
#for i in range(6):
#    i += 1
#    urls.append(u1 + str(i) )
urls = ['http://www.ynufe.edu.cn/pub/lfxy/xyjs/szdw/index.htm']

urls = get_urls(urls,'http://www.ynufe.edu.cn/pub/lfxy/xyjs/szdw/') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '旅游与酒店管理学院.txt'
down_details(urls,filename) 