
import requests,json
from tqdm import tqdm # 进度条
import requests
from bs4 import BeautifulSoup

url = 'https://e.qq.com/portal/helper/contents?post_id=1712'
res = requests.get(url,cookies = {'nothing':'1'}) # 
Soup = BeautifulSoup(res.text,'html.parser')
JS = json.loads(res.text)
print(JS)
# print(Soup.title)
# print(Soup.title.text)