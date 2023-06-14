
import requests
import json
import csv
import jsonpath
import pandas as pd
import jsonpath
import tkinter as tk
from tkinter import filedialog

'''
1.包括url和header，在线转换网址:https://tooltt.com/header2json/
2.修改末尾main()函数里的url,注意url参数limit可自有调节
3.修改末尾main()函数header
'''


'''
工具类，用来处理数据，并保存爬虫结果.
data为数据，
outpath为选择保存结果的路径
'''


def savecsv(data, outpath):
    # 创建文件对象
    prepath = outpath
    f = open(prepath, 'w', encoding='utf-8')

    # 通过文件创建csv对象
    csv_write = csv.writer(f)

    # writerow: 按行写入，　writerows: 是批量写入
    # 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
    csv_write.writerow(data[0])

    # 循环里面的字典，将value作为数据写入进去
    for row in data:
        print(row)
        csv_write.writerow(row.values())

    # 关闭打开的文件
    f.close()

    df = pd.read_csv(outpath, encoding='utf-8')

    df.dropna(axis=0)

    print(df)

    df.to_csv(outpath, encoding='utf-8', index=0)


'''
爬虫逻辑
'''


def spidersql(datapath, url, headers):
    resp = requests.get(
        url=url,
        headers=headers
    )
    print(resp.status_code)
    print(resp.status_code)
    print(resp.headers)
    print(resp.cookies)

    str1 = resp.content.decode('utf-8')

    print(str1)

    j = json.loads(str1)
    # print(j)
    # # col = jsonpath.jsonpath(j, '$..header')
    # # print(col)
    body = jsonpath.jsonpath(j, '$..data')

    print(body)
    outpath = datapath+"/data.csv"
    body_path = 'data.csv'
    body_data = body[0]
    savecsv(body_data, outpath)


'''
主函数
'''


def main(url, headers):
    print('请选择结果存放位置……')
    df_mr = pd.DataFrame()
    root = tk.Tk()
    root.withdraw()

    datapath = filedialog.askdirectory()

    # 执行爬虫
    spidersql(datapath, url, headers)


'''url和headers可修改'''
if __name__ == '__main__':

    url='http://10.113.221.244:8002/bas/Account/ashx/SysAshx/DataQuery.ashx?p=GetData&page=1&limit=1000&dbtype=EM_CN&sqlstr=select+*+from+YB_TMP_HWQ_02&_=1657003062189'

    headers ={}
    main(url, headers)
