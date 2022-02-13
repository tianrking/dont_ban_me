from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

# for i in range(106,3000):
#     url = "https://ad.weixin.qq.com/guide/" + 
#     driver.get("https://baidu.com/")
#     print(driver.title)
#     driver.quit()

# email = chrome.find_element_by_id("email")
# password = chrome.find_element_by_id("pass")
 
# email.send_keys(config.email)
# password.send_keys(config.password)
# password.submit()
 
url = "https://ad.weixin.qq.com/guide/" + "106"
driver.get(url)
print(driver.title)
driver.quit()

# print(driver.title)
# driver.quit()
