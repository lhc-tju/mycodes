#selenium 批量导出参考文献 尝试
from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.common.keys import Keys
import time
#高级搜索页面，可以根据具体要求改变检索条件，当前为作者+机构（模糊）
scholars = ['丁芸','王少国'] # 学者名单列表
scho_institution = {'丁芸':'首都经济贸易大学','王少国':'首都经济贸易大学'} #机构对应表

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB&crossDbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD')
for scholar in scholars:
    try:
        name = driver.find_element_by_id('au_1_value1')#name.clear()
        name.clear()
        name.send_keys(scholar)
        institution = driver.find_element_by_id('au_1_value2') #institution.clear()
        institution.clear()
        institution.send_keys(scho_institution[scholar])
        institution.send_keys(Keys.ENTER) 
        time.sleep(1) 
        flag = True #用于定位iframe， 以及在首页时的下一页链接
        while True:
            if flag:
                driver.switch_to_frame('iframeResult')
                to_clear = driver.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[1]/div/span/a')
                to_clear.click()
            check_box = driver.find_element_by_id('selectCheckbox')
            check_box.click()  # 全选
            time.sleep(0.5)
            #n_next = driver.find_element_by_class_name('TitleLeftCell')
            try:
                next_page = driver.find_element_by_link_text(u'下一页')
            except:
                time.sleep(1)
                break #没有下一页
            next_page.click() #下一页
            flag = False
            time.sleep(1)        
        export = driver.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[1]/div/a[2]')
        export.click()
        driver.switch_to_window(driver.window_handles[1]) #可能要重新定位windows
        time.sleep(2)
        zidingyi = driver.find_element_by_xpath('//*[@id="SaveTypeList"]/li[10]/span[1]/a')
        zidingyi.click()
        time.sleep(0.5)
        select_all = driver.find_element_by_xpath('//*[@id="selfDefine"]/table/tbody/tr[4]/td/input[1]')
        select_all.click()
        time.sleep(2)
        download = driver.find_element_by_xpath('//*[@id="exportExcel"]')     #下载 excel
        download.click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        print(scholar + ' ' + '已完成')
        time.sleep(1.0) 
    except:
        print(scholar + ' ' + '数据导出失败')
print('ok')
