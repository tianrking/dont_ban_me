import json
import pandas as pd

df =  pd.read_csv("/home/tianrking/dont_ban_me/app/2腾讯广告帮助中心/final_with_url.csv")

print(df.describe)

df.to_excel("final_with_url.xlsx")