from tkinter import filedialog

import pandas as pd
import os


def hecheng(read_path):
    '''
	合成多个子表，表名按1,2,3,4,5,6……的规则进行命名
	:return:
	'''
    sheets = os.listdir(read_path)
    # sheets = ['0415','0416']
    D = []
    for x in sheets:
        data = pd.read_csv(read_path + "\\" + x)
        # data = pd.read_excel(read_path + "\\" + x, sheet_name=0)

        if data.empty is True:
            continue
        # data.rename(columns={'状态归类':'状态'},inplace=True)#状态归类和状态是同一个属性，所以我将状态归类替换成了状态
        data['date'] = x
        D.append(data.loc[:, data.columns])
        # print(data)
        print(D)

    num = pd.concat(D, axis=0)  # 合并list表D中的元素
    print(num)
    out_path = filedialog.askdirectory()
    num.to_excel(out_path + '/结果.xlsx', index=False)


read_path = filedialog.askdirectory()

hecheng(read_path)
