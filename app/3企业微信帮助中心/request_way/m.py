import _thread
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null

import requests  
from tqdm import tqdm # 进度条
import requests
from bs4 import BeautifulSoup
# url = "https://open.work.weixin.qq.com/help2/pc/14662?person_id=1"

# f = open("requests_url.txt",'a')
# for i in tqdm(range(3932,8000)): #3000
#     url = "https://open.work.weixin.qq.com/help2/pc/1%s?person_id=1"%str(i)
#     # url = "https://open.work.weixin.qq.com/help2/pc/13000?person_id=1"
#     res = requests.get(url,cookies = {'nothing':'1'}) # 
#     Soup = BeautifulSoup(res.text,'html.parser')
#     # print(Soup.title)
#     print(Soup.title.text)
#     # print(url)
#     # f.write(str(name))
#     f.write(Soup.title.text)
#     f.write(",")
#     f.write(url)
#     f.write('\n')
# f.close()


# 为线程定义一个函数
def get_url( threadName, start , k , point):
    count = 0
    
    for i in tqdm(range(start + k*(point-1),start + k*point)):
        url = "https://open.work.weixin.qq.com/help2/pc/1%s?person_id=1"%str(i)
        res = requests.get(url,cookies = {'nothing':'1'}) # 
        Soup = BeautifulSoup(res.text,'html.parser')
        # print(Soup.title)
        print(Soup.title.text)
        # print(url)
        # f.write(str(name))
        f = open("requests_url_thread.txt",'a')
        f.write(Soup.title.text)
        f.write(",")
        f.write(url)
        f.write('\n')
        f.close()
        
    # k= sum / point
    # print ("%s: %s" % ( threadName, k ,point ))



# 创建两个线程
try:
    end = 8000
    start = 3000
    point = 3
    sum=end-start
    k= int(sum / point)
    _thread.start_new_thread( get_url, ("Thread-1", start , k , 1) )
    _thread.start_new_thread( get_url, ("Thread-2", start , k , 2) )
    _thread.start_new_thread( get_url, ("Thread-3", start , k , 3) )
except:
   print ("Error: 无法启动线程")


while 1:
    pass