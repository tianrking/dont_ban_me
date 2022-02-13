from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.get("https://baidu.com/")

# email = chrome.find_element_by_id("email")
# password = chrome.find_element_by_id("pass")
 
# email.send_keys(config.email)
# password.send_keys(config.password)
# password.submit()
 
time.sleep(3)

print(driver.title)
driver.quit()