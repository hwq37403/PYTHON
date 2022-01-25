import pandas as pd
import openpyxl

read_path = 'E:\\WORK\\202101网格承包\\网格承包202101 - 专业室 - 副本.xlsx'
sheetname = '分局汇总' #sheet表名
ID_COL = 2  #第三列为标识
ID_NAME = '区县' #第三列标识列名

def spilt(read_path,sheet_name,ID_COL):
    '''
    :DES:按ID_COL，拆分一个表的一个子表，到不同的ID_COL表里
    :param read_path: 文件读取路径
    :param sheet_name: sheet表名
    :param ID_COL: 标识
    :return: 标识列名
    '''
    file = pd.read_excel(read_path, sheet_name=sheet_name)
    menu = file.iloc[:, ID_COL].drop_duplicates()  ########2，选择以第ID_COL列为标识的所有行数据，并去除重复数据

    print(file)

    for name in menu:
        df1 = file[file[ID_NAME] == name]
        path = "C:\\Users\\Admin\\Desktop\\网络承包区县拆分\\" + name[0:2] + ".xlsx" #可修改输出路径
        with pd.ExcelWriter(path) as writer:
            df1.to_excel(writer, sheet_name=sheet_name, index=None)

spilt(read_path,sheetname,ID_COL)