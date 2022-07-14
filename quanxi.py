# %%
import pandas as pd
import os

import tkinter as tk
from tkinter import filedialog
import re
import time

# %%
print('正在打开……')
df_mr=pd.DataFrame()
root = tk.Tk()
root.withdraw()
# path = filedialog.askopenfilename()
# path_out, temp = os.path.split(path)
# file_name, extension = os.path.splitext(temp)
# print('path:', path_out)
# print('file_name:', file_name)
# print('extension:', extension)

datapath1 = filedialog.askopenfilename()




# %%
df1=pd.read_excel(datapath1,sheet_name='三大家--权益包（引客到店）')
df2=pd.read_excel(datapath1,sheet_name='三大家-我号异宽（预约上门）')
df3=pd.read_excel(datapath1,sheet_name='三大家派单规则')
df4=pd.read_excel(datapath1,sheet_name='服务中心-我号异宽')
df5=pd.read_excel(datapath1,sheet_name='服务中心-扩群送泛智能')
df6=pd.read_excel(datapath1,sheet_name='服务中心派单规则')


# %%
df_r1=df1.copy()

# %%
D=[]

# %%
for index, row in df3.iterrows():

#   print(index, row)
  df_tmp=df1[df1['服务中心id']==row['服务中心编码']]
  df_tmp1=df2[df2['服务中心id']==row['服务中心编码']]

  ykdd_len= row['引客到店周工单量']
  yysm_len= row['总单量']

  if len(df_tmp)>=ykdd_len:
        df_tmp=df_tmp.head(ykdd_len)
        df1 = df1[~df1.号码.isin(df_tmp.号码)]
        df_tmp['打标']=row['渠道编码']
        re_len=  yysm_len-len(df_tmp)
        df_tmp1=df_tmp1.head(re_len)
        df_tmp1['打标']=row['渠道编码']
        df2=df2[~df2.号码.isin(df_tmp1.号码)]
        df_tmp=pd.concat([df_tmp, df_tmp1])
        
  else:
        
        df_tmp=df_tmp.head(len(df_tmp))
        re_len=  yysm_len-len(df_tmp)
        df1 = df1[~df1.号码.isin(df_tmp.号码)]
        df_tmp['打标']=row['渠道编码']
        df_tmp1=df_tmp1.head(re_len)
        df_tmp1['打标']=row['渠道编码']
        df2=df2[~df2.号码.isin(df_tmp1.号码)]
        df_tmp=pd.concat([df_tmp, df_tmp1])
  D.append(df_tmp)


df_res1 = pd.concat(D, axis=0)
len(df_res1)

# %%
outpath=tk.filedialog.askdirectory()

# %%
df_res1.to_excel(outpath+'/三大家.xlsx')

# %%
df4=df4[~df4.号码.isin(df_res1.号码)]

# %%
B=[]

# %%
for index, row in df6.iterrows():

#   print(index, row)网格分局ID
  fwzx_len=row['派单量']
  df_tmp=df5[df5['网格分局ID']==row['服务中心代码']]
  df_tmp1=df4[df4['服务中心id']==row['服务中心代码']]  
  if len(df_tmp)<fwzx_len:
    df_tmp=df_tmp.head(fwzx_len)
    df5 = df5[~df5.号码.isin(df_tmp.号码)]
    df_tmp['打标']=row['服务中心代码']
    re_len=fwzx_len-len(df_tmp)
    df_tmp1=df_tmp1.head(re_len)
    df4 = df4[~df4.号码.isin(df_tmp1.号码)]
    df_tmp1['打标']=row['服务中心代码']
    df_tmp=pd.concat([df_tmp, df_tmp1])
  else:
    df_tmp=df_tmp.head(fwzx_len)
    df_tmp['打标']=row['服务中心代码']
    df5 = df5[~df5.号码.isin(df_tmp.号码)]
  B.append(df_tmp)
df_res2 = pd.concat(B, axis=0)
len(df_res2)

# %%
df_res2.to_excel(outpath+'/服务中心.xlsx')


