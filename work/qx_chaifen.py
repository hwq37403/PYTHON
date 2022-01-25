import time  # 引入time模块

import pandas as pd

import work.mkdir as mkdir

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
date=int(date)
date=str(date)


path = 'E:\\WORK\\网格酬金核算\\'+date+'网格承包\\网格承包'+date+' - 专业室.xlsx'
# path = 'E:\\WORK\\网格酬金核算\\202104网格承包\\结果模板.xlsx'

file1 = pd.read_excel(path, sheet_name='服务中心汇总',skiprows=1)
# file2 = pd.read_excel('E:\\WORK\\网格酬金核算\\202103网格承包\\网格承包202103 - 专业室.xlsx', sheet_name='应知应会扣罚')
# file3 = pd.read_excel(path, sheet_name='服务负向动作扣罚（4月，5月）')
# # file3 = pd.read_excel('E:\\WORK\\网格酬金核算\\202104网格承包\\网格承包202104 - 专业室.xlsx', sheet_name='服务负向动作扣罚（4月）')
file2 = pd.read_excel(path, sheet_name='客户代表奖金明细')
file1.columns=file1.columns.str.strip()
file2.columns=file2.columns.str.strip()

# file5 = pd.read_excel(path, sheet_name='分局绩效跟踪表')
file1=file1.sort_values(by='区县')
file2=file2.sort_values(by='区县')

print(file1)
print(file2)






#区县列名
# menu1 = file1.iloc[:, 0].drop_duplicates()  ########2
# menu2 = file2.iloc[:, 0].drop_duplicates()  ########0
menu1 = file1.loc[:,'区县'].drop_duplicates()


menu2 = file2.loc[:, '区县'].drop_duplicates()
# menu4 = file4.loc[:, '区县'].drop_duplicates()
# menu5 = file5.loc[:, '区县'].drop_duplicates()
print(menu1)
print(menu2)



# print(file1)
# print(file2)
# print(file3)
# print(file4)


mkdir.mkdir("E:\\WORK\\网格酬金核算\\"+date+"网格承包\\区县拆分")

for name1,name2 in zip(menu1,menu2):
    df1 = file1[file1['区县'] == name1]
    df2 = file2[file2['区县'] == name2]
    # df3 = file3[file3['区县'] == name3]
    # df4 = file4[file4['区县'] == name4]
    # df5 = file5[file5['区县'] == name5]

    filename="E:\\WORK\\网格酬金核算\\"+date+"网格承包\\模板.xlsx"
    outpath = "E:\\WORK\\网格酬金核算\\"+date+"网格承包\\区县拆分\\网格承包"+date+"-" + name1[0:2] + ".xlsx"
    #复制模板到拆分

    shutil.copyfile(filename, outpath)

    # 读取被写入的Excel工作簿
    book = load_workbook(outpath)
    # 建立写入对象
    write = pd.ExcelWriter(outpath, engine='openpyxl')
    write.book = book
    write.sheets = {ws.title: ws for ws in book.worksheets}
    df1.to_excel(write, sheet_name='服务中心汇总', header=False, index=False, startrow=2, startcol=0)
    df2.to_excel(write, sheet_name='客户代表奖金明细', header=False, index=False, startrow=1, startcol=0)
    write.save()











