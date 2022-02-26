import pandas as pd

df = pd.read_csv("/home/tianrking/t_ad_help_data/data/tx_ah_help_center_with_url_warning.csv",header=None, names=['0','Q_text','A','Ans','update'])
df = df[[ "Q_text", "Ans"]]
df.to_csv('final_with_url_safe.csv',index=False, header=False, mode='a+')