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
df1=pd.read_excel(datapath1,sheet_name='集团-我号异宽')
df2=pd.read_excel(datapath1,sheet_name='规则')



# %%
df_r1=df1.copy()

# %%
D=[]

# %%
print('正在拆分')
for index, row in df2.iterrows():

#   print(index, row)
  df_tmp=df1[df1['280编码']==row['集团代码']]
  paidan= row['派单量']
  df_tmp=df_tmp.head(paidan)
  df_tmp['接单人']=row['接单人']
  df1 = df1[~df1.手机号码.isin(df_tmp.手机号码)]
  D.append(df_tmp)


df_res1 = pd.concat(D, axis=0)
len(df_res1)

# %%
outpath=tk.filedialog.askdirectory()

# %%
df_res1.to_excel(outpath+'/集团.xlsx')
print('拆分完成')
# %%
