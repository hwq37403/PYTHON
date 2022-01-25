import pandas as pd
import os
import sheet_name as sn
from fuzzywuzzy import fuzz

# file=os.listdir('D:/鑫速联翘状态表')[0]#读取指定文件夹下的第一个表名
#file='D:/鑫速联翘状态表.xlsx'#直接读取表名
# sheets=['1 (1)','1 (2)','1 (3)','1 (4)','1 (5)','1 (6)','1 (7)','1 (8)','1 (9)','1 (10)','1 (11)','1 (12)','1 (13)','1 (14)','1 (15)','1 (16)','1 (17)','1 (18)','1 (19)','1 (20)','1 (21)','1 (22)','1 (23)','1 (24)','1 (25)','1 (26)','1 (27)','1 (28)','1 (29)','1 (30)','1 (31)','1 (32)','1 (33)','1 (34)','1 (35)','1 (36)','1 (37)','1 (38)','1 (39)','1 (40)','1 (41)','1 (42)','1 (43)','1 (44)','1 (45)','1 (46)','1 (47)','1 (48)','1 (49)','1 (50)','1 (51)','1 (52)','1 (53)','1 (54)','1 (55)','1 (56)','1 (57)','1 (58)','1 (59)','1 (60)','1 (61)','1 (62)','1 (63)','1 (64)','1 (65)','1 (66)','1 (67)']
#----------------------------------------------------------------------读取所有sheet名-------
#--------------------------------------------------------------------------------------------
city_path=r'E:\WORK\大数据清理\202104\2021年03月数据下载明细-市州分公司.xls'

ALL_path=r'E:\WORK\大数据清理\test\总表.xlsx'

read_path = r'E:\WORK\大数据清理\test\表名.xlsx'

out_path=r'E:\WORK\大数据清理\202104\2021年03月数据下载明细-宜宾分公司.xlsx'
def hecheng(read_path):
    sheets = sn.sheet_name(read_path)
    D = []
    for x in sheets:
        data = pd.read_excel('E:/WORK/大数据清理/test/ ' + str(x) + '.xlsx', sheet_name='test')

        print(data)
        print('第几张表'+x)
        if data.empty is True:
            continue
        # data.rename(columns={'状态归类':'状态'},inplace=True)#状态归类和状态是同一个属性，所以我将状态归类替换成了状态
        D.append(data.loc[:, ['序号', '清理状态', '监督人', '清理时间']])
    num = pd.concat(D, axis=0)  # 合并list表D中的元素
    num.to_excel(ALL_path, index=False)

# hecheng(read_path)


df1 = pd.read_excel(city_path, sheet_name='SQL Results')
df2= pd.DataFrame(columns=['序号','下载人主帐号','下载人','手机号','下载人归属组织','文件名','申请时间','申请IP','清理状态','监督人','清理时间'])

menu1 = df1.iloc[:, 0].drop_duplicates()  ########2
# print(fuzz.ratio('阿坝',df1.iloc[0,4].replace('-','')))
print(fuzz.ratio('宜宾','四川省业务支撑平台-地市州分公司-宜宾分公司-翠屏分公司'))

for i in menu1:
      a=fuzz.ratio('宜宾',df1.iloc[i-1,4].replace('-',''))
      print(a)
      if a>0:
          df2=df2.append(df1.iloc[i-1,:])

df2.to_excel(out_path, index=False, encoding='utf-8')
df2 = pd.read_excel(out_path, sheet_name='Sheet1')
df3 = pd.read_excel(ALL_path, sheet_name='Sheet1')


print(df2.iloc[:,0])
print(df3)

for index in df2.index:
    print(index)
    for index1 in df3.index:
        if df2.iloc[index, 0] == df3.iloc[index1, 0]:
            df2.iloc[index, 8] = df3.iloc[index1, 1]
            df2.iloc[index, 9] = df3.iloc[index1, 2]
            df2.iloc[index, 10] = df3.iloc[index1, 3]

            print(df2.iloc[index,:])


df2.to_excel(r'E:\WORK\大数据清理\202104\2021年03月数据下载明细-宜宾分公司.xlsx', index=False, encoding='utf-8')