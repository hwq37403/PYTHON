import time  # 引入time模块

import pandas as pd

import os

import openpyxl

import shutil

from openpyxl import load_workbook

###由于PD会覆盖重写sheet，为了保存一个EXCEL多个sheet，所有只能通过EXCELwriter使用一个句柄来写入多个sheet

'''
区县分局承包拆分表格，拆分时需对四个子表的区县字段进行升序排序，保证顺序一致，否则每个区县的子表顺序不一致。
'''


ticks = time.localtime()
    # date=timestamp_to_ydate(ticks)
date = time.strftime("%Y%m", time.localtime())
# date=int(date)-1 #上个月YYYYMM
date=int(date) #YYYYMM
date=str(date)

date='202212'

path = 'E:\\WORK\\网格酬金核算\\'+date+'网格承包\\网格承包'+date+' - 专业室.xlsx'


file0 = pd.read_excel(path, sheet_name='服务中心汇总')
file0=file0[file0['区县'].notnull()]
file1 = pd.read_excel(path, sheet_name='城市')
file1=file1[file1['区县'].notnull()]
file2 = pd.read_excel(path, sheet_name='绝地反击型')
file2=file2[file2['区县'].notnull()]
file3 = pd.read_excel(path, sheet_name='强力进攻型')
file3=file3[file3['区县'].notnull()]
file4 = pd.read_excel(path, sheet_name='提值进攻型')
file4=file4[file4['区县'].notnull()]
file5 = pd.read_excel(path, sheet_name='稳存进攻型')
file5=file5[file5['区县'].notnull()]
# file2 = pd.read_excel('E:\\WORK\\网格酬金核算\\202103网格承包\\网格承包202103 - 专业室.xlsx', sheet_name='应知应会扣罚')
# file3 = pd.read_excel(path, sheet_name='服务负向动作扣罚（4月，5月）')
# # file3 = pd.read_excel('E:\\WORK\\网格酬金核算\\202104网格承包\\网格承包202104 - 专业室.xlsx', sheet_name='服务负向动作扣罚（4月）')
file0.columns=file0.columns.str.strip()
file1.columns=file1.columns.str.strip()
file2.columns=file2.columns.str.strip()
file3.columns=file3.columns.str.strip()
file4.columns=file4.columns.str.strip()
file5.columns=file5.columns.str.strip()

# file5 = pd.read_excel(path, sheet_name='分局绩效跟踪表')
file0=file0.sort_values(by='区县')
file1=file1.sort_values(by='区县')
file2=file2.sort_values(by='区县')
file3=file3.sort_values(by='区县')
file4=file4.sort_values(by='区县')
file5=file5.sort_values(by='区县')








#区县列名
# menu1 = file1.iloc[:, 0].drop_duplicates()  ########2
# menu2 = file2.iloc[:, 0].drop_duplicates()  ########0
menu0 = file0.loc[:,'区县'].drop_duplicates()
menu1 = file1.loc[:,'区县'].drop_duplicates()


menu2 = file2.loc[:, '区县'].drop_duplicates()
menu3 = file3.loc[:, '区县'].drop_duplicates()
menu4 = file4.loc[:, '区县'].drop_duplicates()
menu5 = file5.loc[:, '区县'].drop_duplicates()




# print(file1)
# print(file2)
# print(file3)
# print(file4)
fname="E:\\WORK\\网格酬金核算\\"+date+"网格承包\\区县拆分"

if os.path.exists(fname)==False:
    os.mkdir("E:\\WORK\\网格酬金核算\\"+date+"网格承包\\区县拆分")

for name1 in menu1:
    df0 = file0[file0['区县'] == name1]
    df1 = file1[file1['区县'] == name1]
    df2 = file2[file2['区县'] == name1]
    df3 = file3[file3['区县'] == name1]
    df4 = file4[file4['区县'] == name1]
    df5 = file5[file5['区县'] == name1]
    

    #TODO 自助创建模板
    filename="E:\\WORK\\网格酬金核算\\模板.xlsx"
    outpath = "E:\\WORK\\网格酬金核算\\"+date+"网格承包\\区县拆分\\网格承包"+date+"-" + name1[0:2] + ".xlsx"
    #复制模板到拆分

    shutil.copyfile(filename, outpath)

    # 读取被写入的Excel工作簿
    book = load_workbook(outpath)
    # 建立写入对象
    write = pd.ExcelWriter(outpath, engine='openpyxl')
    write.book = book
    write.sheets = {ws.title: ws for ws in book.worksheets}
    df0.to_excel(write, sheet_name='服务中心汇总', header=False, index=False, startrow=3, startcol=0)
    df1.to_excel(write, sheet_name='城市', header=False, index=False, startrow=3, startcol=0)
    df2.to_excel(write, sheet_name='绝地反击型', header=False, index=False, startrow=3, startcol=0)
    df3.to_excel(write, sheet_name='强力进攻型', header=False, index=False, startrow=3, startcol=0)
    df4.to_excel(write, sheet_name='提值进攻型', header=False, index=False, startrow=3, startcol=0)
    df5.to_excel(write, sheet_name='稳存进攻型', header=False, index=False, startrow=3, startcol=0)
    
    write.save()



print('拆分完成')







