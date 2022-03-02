import json
import pandas as pd

df =  pd.read_csv("/home/tianrking/dont_ban_me/app/1微信广告帮助中心/awesome_version/txggbzzx.csv")

df.to_excel("txggbzzx.xlsx")