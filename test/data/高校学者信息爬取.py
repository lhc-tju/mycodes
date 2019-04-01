# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver #抓取js加载的动态网页

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
#            title = soup.find('h1')
            result = soup.select('#vsb_content')[0].find_all('p')
#            r2 = soup.select('.entry')[0].find_all('p')
#            r2 = soup.find('tbody').find_all('p')
        except:
            print('sth maybe wrong..' + url)
            continue
#        detail.append(title.text.strip())
        for item in result:
            detail.append(item.text.strip().replace(r'\xa0',''))
#        for item in r2:
#            detail.append(item.text.strip())
        detail.append('网址：' + url + ' ')
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    drive = webdriver.Chrome(chrome_options=opt)
    
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for url in urls:
        try:
#        res = requests.get(url)
#        res.encoding = 'utf-8'
#        soup = BeautifulSoup(res.text,'lxml')   
            drive.get(url)
            data = drive.page_source
            soup = BeautifulSoup(data,'lxml')
            result = soup.select('#lm_right')[0].find_all('a')
#        result = soup.select('.col-news-list')[0].find_all('tbody')
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
            if item['href'].startswith('http'):
                n_urls.append(item['href'])
            else:
                n_urls.append(index_url + item['href'][2:])
    print('got urls..')
    return n_urls

urls = ['http://mc2014.ctbu.edu.cn/yjsjy/yjsds.htm']
urls = get_urls(urls,'http://mc2014.ctbu.edu.cn') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '管理学院.txt'
down_details(urls,filename) 