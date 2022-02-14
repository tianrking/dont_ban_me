from pickle import NONE
import pandas as pd

read_file = pd.read_csv (r'/home/tianrking/pachong/app/ad_weixin_qq_com_guide_titile_clean.csv',engine = "python",header=None,
                 names=['KEY', 'URL'])
print(read_file.head())
