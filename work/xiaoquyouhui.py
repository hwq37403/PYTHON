import pandas as pd
import numpy as np

'''
优惠小区导入，修改读写路径，不包含校园小区，需单独添加
'''
read_path = 'E:\\WORK\\优惠小区\\优惠小区导入20210528\\优惠小区导入20210528补充.xlsx'
out_path = 'E:\\WORK\\优惠小区\\优惠小区导入20210528\\优惠小区导入20210528补充结果.xlsx'
with pd.ExcelFile(read_path) as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')

    df1['区县'] = df1['区县'].map(lambda 区县: 区县[0:2])
    df2['区县'] = df2['区县'].map(lambda 区县: 区县[0:2])

    print(df1['区县'])

outer = pd.merge(df1, df2, on='区县')

print(outer)

outer.to_excel(out_path, index=False, encoding='utf-8')





