from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null


#导入 ActionChains 类 模拟点击事件
from selenium.webdriver import ActionChains

options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

url = 'https://ad.weixin.qq.com/guide/term/186'
driver.get(url)

# 鼠标移动到 ac 位置
ac = driver.find_element_by_xpath("//div[@class='md-panel__header-text']")
ActionChains(driver).move_to_element(ac).perform()
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup)
# print(soup.find(name='div'))

