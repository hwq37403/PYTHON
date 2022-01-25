import pandas as pd
import numpy as np


df=pd.read_csv(r'E:\WORK\网格酬金核算\test.csv',encoding='ANSI')

print(df)
df_pivot = pd.pivot_table(df,index=['专业室18','科目14'], values=['得分16'],aggfunc=[len,np.sum],margins=True)
print(df_pivot)

df_pivot = df_pivot.reset_index()
df_pivot.to_csv(r'E:\WORK\网格酬金核算\透视表结果.csv', index=False,encoding='ANSI')
