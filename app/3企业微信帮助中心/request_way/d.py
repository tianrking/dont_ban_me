import pandas as pd
from tqdm import tqdm 
import requests
from bs4 import BeautifulSoup

pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',200)

df=pd.read_csv('./awesome_link.csv')

df = df[['KEY','URL']]
# print(df)

for url in df['URL']:
    # print(url)
    res = requests.get(url,cookies = {'nothing':'1'}) # 
    Soup = BeautifulSoup(res.text,'html.parser')
    print(Soup.title.text.split("-帮助中心-企业微信")[0])
    print('\n')
    print(url)
    