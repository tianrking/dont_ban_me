import pandas as pd
import json

with open("data_all.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

item = load_dict['data']['posts']['rows']

for i in range(0,len(item)):
    df = pd.DataFrame()
    Q = item[i]['post_title']
    A_text = item[i]['post_data']
    A_text = json.loads(A_text)
    A_text = A_text['content']
    A_url = "https://ad.weixin.qq.com/guide/%s"% str(item[i]['post_id'])
    
    df = pd.DataFrame(data=[
                    [Q,A_text,A_url]],
                    columns = ['Q','A_text','A_url'],
                    )
    df.to_csv('txggbzzx.csv', mode='a', header=False)
    print(i)
    