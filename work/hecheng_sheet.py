from tkinter import filedialog

import pandas as pd
import os

path=r'C:\Users\Admin\Documents\全量运行电表清单.xlsx'
reader = pd.ExcelFile(r'C:\Users\Admin\Documents\全量运行电表清单.xlsx')
sheet_names = reader.sheet_names
# sheets = ['0415','0416']
D = []
for x in sheet_names:
		data = pd.read_excel(path, sheet_name=x)
		if data.empty is True :
			continue
		# data.rename(columns={'状态归类':'状态'},inplace=True)#状态归类和状态是同一个属性，所以我将状态归类替换成了状态
		data['date']= x
		D.append(data.loc[:, data.columns])
		# print(data)
		print(D)

num = pd.concat(D, axis=0)  # 合并list表D中的元素
print(num)
out_path=filedialog.askdirectory()
num.to_excel(out_path+'/结果.xlsx', index=False)