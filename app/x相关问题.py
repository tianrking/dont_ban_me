from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null
import pandas as pd
from lxml import etree

#导入 ActionChains 类 模拟点击事件
from selenium.webdriver import ActionChains

options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

read_file = pd.read_csv('/home/tianrking/pachong/app/相关问题.csv')
read_file = read_file[['KEY', 'URL']]
# print(read_file.head())
for index, row in read_file.iterrows():
    url = row['URL'] 
    driver.get(url)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    aa=soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
    html = etree.HTML(driver.page_source)
    # title = html.xpath("//div[@class='qa-list'][1]//h3[@class='qa-list__title']/a/text()")
    # result = etree.tostring(html)
    
    result = etree.tostring(html,encoding="unicode")
    
    print(result)
    # print(result.decode('utf-8'))
    
    # driver.get(url)
    # time.sleep(5)
    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # aa = soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
    # print(aa) # md-panel_expanded md-panel
# url = 'https://ad.weixin.qq.com/guide/term/186'
# driver.get("https://ad.weixin.qq.com/guide/1184")

# time.sleep(5)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# aa=soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
# print(aa)

# # 鼠标移动到 ac 位置
# ac = driver.find_element_by_xpath("//div[@class='md-panel__header-text']")
# ActionChains(driver).move_to_element(ac).perform()
# soup = BeautifulSoup(driver.page_source, 'lxml')
# print(soup)
# # print(soup.find(name='div'))


