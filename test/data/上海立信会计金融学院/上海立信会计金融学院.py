# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver #抓取js加载的动态网页

def down_details(urls,filenames):
    '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'''
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    f = open(filenames,'w',encoding='utf-8')
#    opt = webdriver.ChromeOptions()
#    opt.add_argument('--headless')
#    drive = webdriver.Chrome(chrome_options=opt)
    for url in urls:
        detail = []
        #可以加上try
        try:
            res = requests.get(url)
#            drive.get(url)
#            res = drive.page_source
        except:
            print('the url was wrong: ' + url)
            continue
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'lxml') 
#        soup = BeautifulSoup(res,'lxml')   
        try:
            title = soup.select('.articleBox')[0].select('.title')[0]
            result = soup.select('.articleBox')[0].find_all('p')
#        r2 = soup.select('.tab-content')[0].find_all('')
        except:
            print('sth maybe wrong..' + url)
            continue
        detail.append(title.text.strip())
        for item in result:
            detail.append(item.text.strip().replace(r'\xa0',''))
#        for item in r2:
#            detail.append(item.text.strip())
        f.write(str(detail) + '\n\n')
        print('saving..')
    f.close()
    
def get_urls(urls,index_url):
    n_urls =[]
#    opt = webdriver.ChromeOptions()
#    opt.add_argument('--headless')
#    drive = webdriver.Chrome(chrome_options=opt)
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for url in urls:
        try:
            res = requests.get(url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text,'lxml')  
            result = soup.select('.listItemcon')[0].find_all('a')
#            drive.get(url)
#            data = drive.page_source
#            soup = BeautifulSoup(data,'lxml')
#            result = soup.select('.main-liebiao-con-box-right')[0].find_all('a')
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
                n_urls.append(index_url + item['href'])
    print('got urls..')
    return n_urls
urls = ['http://mksxy.lixin.edu.cn/info/iIndex.jsp?cat_id=13527','http://mksxy.lixin.edu.cn/info/iIndex.jsp?cat_id=13527&cur_page=2','http://mksxy.lixin.edu.cn/info/iIndex.jsp?cat_id=13527&cur_page=3']
urls = get_urls(urls,'http://mksxy.lixin.edu.cn') 
urls = list(set(urls))
#for item in urls:
#    print(item)
print('urls:' + str(len(urls)))
filename = '马克思主义学院.txt'
down_details(urls,filename) 