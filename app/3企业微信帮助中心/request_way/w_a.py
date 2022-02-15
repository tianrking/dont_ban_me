import pandas as pd


pd.set_option('display.max_columns',None)
#显示所有行
# pd.set_option('display.max_rows',None)
#设置数据的显示长度，默认为50

pd.set_option('max_colwidth',200)
df = pd.read_csv('./requests_url_thread.txt',header=None,names=['KEY','URL'])
# print(df.head())


## df.drop df[~df]
awesome = df[df['KEY']!='帮助中心-企业微信']

awesome['KEY']=awesome.KEY.map(lambda x: x.split("-帮助中心-企业微信")[0])
print(awesome)

awesome.to_csv('awesome_link.csv')