# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver #抓取js加载的动态网页

def down_details(urls,filenames):
    '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'''
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    f = open(filenames,'w',encoding='utf-8')
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    drive = webdriver.Chrome(chrome_options=opt)
    for url in urls:
        detail = []
        #可以加上try
        try:
#            res = requests.get(url)
            drive.get(url)
            data = drive.page_source
            soup = BeautifulSoup(data,'lxml')
        except:
            print('the url was wrong: ' + url)
            continue
#        res.encoding='utf-8'
#        soup = BeautifulSoup(res.text,'lxml') 
        #针对性更改,可设置多个result
        try: #有三种不同的导师显示方式
#            title = soup.find('h1')
            result = soup.select('.left')[0].find_all('div')
#            r2 = soup.select('.top22')[0].find_all('div')
#            r2 = soup.find('tbody').find_all('p')
        except:
            try:
                result = soup.select('.left')[0].find_all('div')
                r2 = soup.select('.news_list')[0].find_all('li')
#                result = soup.select('.wp_articlecontent')[0].find_all('p')
#                title = soup.find('h1')
            except:
                try:
                    title = soup.find('h1')
                    result = soup.select('.news_list')[0].find_all('p')
                except:
                    print('sth maybe wrong..' + url)
                    continue
#            print('sth maybe wrong..' + url)
#            continue
        try:
            detail.append(title.text.strip())
        except:
            pass
        for item in result:
            detail.append(item.text.strip())
#            temp = item.find_all('td')[-1]
##            for i in temp:
#            f.write(temp.text.strip().replace(r'\xa0','') + '网址：' + url + '\n')
        try:
            for item in r2:
                detail.append(item.text.strip())
        except:
            pass
        detail.append('网址：' + url + ' ')
        f.write(str(detail) + '\n\n')
        print('saving..')
        sleep(2)
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    drive = webdriver.Chrome(chrome_options=opt)
    
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for url in urls:
#        try:
#        res = requests.get(url)
#        res.encoding = 'utf-8'
#        soup = BeautifulSoup(res.text,'lxml')   
        drive.get(url)
        sleep(2)
        data = drive.page_source
        soup = BeautifulSoup(data,'lxml')
        result = soup.select('#wp_news_w6')[0].find_all('a')
#        result = soup.find('article').find_all('ul')
#            result = soup.find_all('div')[30].find_all('a')
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
                n_urls.append(index_url + item['href'].replace(r'../',''))
        sleep(2)
    print('got urls..')
    return n_urls
urls = ['http://tsxy.zuel.edu.cn/4833/list.htm',
'http://tsxy.zuel.edu.cn/4834/list.htm','http://tsxy.zuel.edu.cn/4835/list.htm','http://tsxy.zuel.edu.cn/4836/list.htm',
'http://tsxy.zuel.edu.cn/sltjx/list.htm','http://tsxy.zuel.edu.cn/4837/list.htm','http://tsxy.zuel.edu.cn/4838/list.htm','http://tsxy.zuel.edu.cn/yytjzyssdsjdsz/list.htm']
urls = get_urls(urls,'http://tsxy.zuel.edu.cn') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '统计与数学学院硕导.txt'
down_details(urls,filename) 

#def get_url(url,index_url):
#    '''selenium获取链接'''
#    n_urls = []
#    opt = webdriver.ChromeOptions()
#    opt.add_argument('--headless')
#    driver = webdriver.Chrome(chrome_options=opt)
#    driver.get(url)
#    data = driver.page_source
#    soup = BeautifulSoup(data,'lxml')
#    result = soup.select('#list_content')[0].find_all('a')
#    for item in result:
#        if item['href'].startswith('http'):
#            n_urls.append(item['href'])
#        else:
#            n_urls.append(index_url + item['href'].replace(r'../',''))
#    for i in range(9):
#        c_next = driver.find_element_by_class_name('next')
#        c_next.click()
#        data = driver.page_source
#        soup = BeautifulSoup(data,'lxml')
#        result = soup.select('#list_content')[0].find_all('a')
#        for item in result:
#            if item['href'].startswith('http'):
#                n_urls.append(item['href'])
#            else:
#                n_urls.append(index_url + item['href'].replace(r'../',''))
#    return n_urls