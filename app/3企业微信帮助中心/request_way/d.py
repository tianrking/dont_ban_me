import pandas as pd
from sqlalchemy import false, true
from tqdm import tqdm 
import requests
from bs4 import BeautifulSoup
import _thread 

pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',200)

df=pd.read_csv('./awesome_link.csv')

df = df[['KEY','URL']]
# print(df)

def download(threadName, start , end ):
    for i in tqdm(range(start,end)):
        _name='F'
        if i==0:
            continue
        url = df.loc[i,'URL']
        name = df.loc[i,'KEY']
        number = url.split('https://open.work.weixin.qq.com/help2/pc/')[1]
        number = number.split('?person_id=1')[0]
        # print(url,name,number)
        res = requests.get(url,cookies = {'dont ban me':'1'}) # 
        Soup = BeautifulSoup(res.text,'html.parser')
        dir = "all_in_one_html/"
        if len(name) > 4:
            _name=name[4]    
        dirname = dir + number+'__'+_name+'.html'  ## 此处两个_ 留着split用
        # print(res.text)
        # print(dirname)
        print(threadName)
        f = open(dirname,'w')
        f.write(res.text)
        f.close()


try:
    sum = 3500
    step = 3
    time = int(sum / step)
    _thread.start_new_thread(download, ("Thread-1", 0 , time) )
    _thread.start_new_thread(download, ("Thread-2", time , time*2) )
    _thread.start_new_thread(download, ("Thread-3", time*2 , 3418) )
    # _thread.start_new_thread(download, ("Thread-4", start , k , 3) )
    # _thread.start_new_thread(download, ("Thread-5", start , k , 3) )
except:
   print ("Error: 无法启动线程")


while 1:
    pass

