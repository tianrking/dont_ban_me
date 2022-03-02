import pandas as pd
import os

c_dir = 'data_all_in_one_with_url'
files = os.listdir(c_dir)

print(files)

# exit()

df = pd.DataFrame()
for csv in files:
<<<<<<< HEAD
    df_temp = pd.read_csv(c_dir+"/"+csv)
    # df = pd.concat([df,df_temp])
    # df.append(df_temp)
    
    df_temp.to_csv('final_with_url.csv',index=False, header=False, mode='a+')
    df = pd.read_csv('final_with_url.csv')
    print(df.shape)
=======
    try:
        df_temp = pd.read_csv(c_dir+"/"+csv)
        # df = pd.concat([df,df_temp])
        # df.append(df_temp)
        
        df_temp.to_csv('final_with_url.csv',index=False, header=False, mode='a+')
        df = pd.read_csv('final_with_url.csv')
        print(df.shape)
    except:
        print(c_dir+"/"+csv+"  is wrong")
>>>>>>> e3746b0b247fcb6b33dafe3ec51dbd9b5a91b233
    

# df.to_csv('final.csv')
print(df.info)