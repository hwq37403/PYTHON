# -*- coding: utf-8 -*-

import pandas as pd
import os


from pandas import DataFrame

path=r'E:\WORK\网格酬金核算\202106网格承包\6月市场掌控环比.xlsx'
log=r'E:\WORK\网格酬金核算\202106网格承包\6月市场掌控环比.txt'
# 打开文件
fd = os.open(log,os.O_RDWR|os.O_CREAT)

df = pd.read_excel(path, sheet_name='市场掌控环比',skiprows=1,usecols=[0,1,28,29,30,31,32,33,34,35,36,37,38]
                   )
df_total = pd.read_excel(path, sheet_name='市场掌控环比',skiprows=1,usecols=[0,1,28,29,30,31,32,33,34,35,36,37,38]
                   )
# df.columns = ['日均能力收入（万元）',	 '宽带净增（户）',	'个人客户净增（个）',	'三个升级',	'个人新动能（分）',	'家庭新动能（分）',	'5G终端（分）',	'5G资费（分）',	'企业微信（分）',	'分局关键过程项目综合积分（分）',	'服务负向动作扣罚'
# ]

sheet=df_total.columns.values
dist_down={}
dist_up={}
count=0

#降序
for i in sheet:
    if i=='区县' or i=='分局':
        continue
    i=i.replace(' ', '')
    # print(df_total[['区县','分局',i]])
    df=df_total[['区县','分局',i]]
    # print(df)
    df=df.sort_values(by=i,ascending=True)#升序
    df = df.reset_index(drop=True)

    dist_up[i]=str(df.loc[0,:].values)+'---'+str(df.loc[1,:].values)+'---'+str(df.loc[2,:].values)
    df = df.sort_values(by=i,ascending=False)  # 降序
    df = df.reset_index(drop=True)



    dist_down[i] = str(df.loc[0, :].values) + '---' + str(df.loc[1, :].values) + '---' + str(df.loc[2, :].values)
    t1= "------"+i+"中环比升序前三（最低）---\n"
    t2=dist_up[i]+"\n"
    t3="------"+i+"中环比降序前三（最高）---\n"
    t4= dist_down[i]+"\n"

    os.write(fd, t1.encode("utf-8"))
    os.write(fd, t2.encode("utf-8"))

    os.write(fd,t3.encode("utf-8") )
    os.write(fd, t4.encode("utf-8") )
    os.write(fd, "\n".encode("utf-8"))
    os.write(fd, "\n".encode("utf-8"))
    count+=1
os.close(fd)

print("写入完成")