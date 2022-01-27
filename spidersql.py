
import requests
import json
import csv
import jsonpath
import pandas as pd
import jsonpath
import tkinter as tk
from tkinter import filedialog

'''
1.首先登录进大数据系统，手工复制处理sql报文的请求头,包括url和header，在线转换网址:https://tooltt.com/header2json/
2.修改末尾main()函数里的url,注意url参数limit可自有调节
3.修改末尾main()函数header
'''


'''
工具类，用来处理数据，并保存爬虫结果.
data为数据，
outpath为选择保存结果的路径
'''
def savecsv(data,outpath):
            # 创建文件对象
    prepath=outpath
    f = open(prepath, 'w',encoding='utf-8')

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

    df=pd.read_csv(outpath,encoding='utf-8')


    df.dropna(axis=0)

    print(df)

    df.to_csv(outpath,encoding='utf-8',index=0)


'''
爬虫逻辑
'''
def spidersql(datapath,url,headers):
    resp=requests.get(
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
    outpath=datapath+"/data.csv"
    body_path ='data.csv'
    body_data = body[0]
    savecsv(body_data,outpath)

    
'''
主函数
'''
def main(url,headers):
    print('请选择结果存放位置……')
    df_mr=pd.DataFrame()
    root = tk.Tk()
    root.withdraw()

    datapath = filedialog.askdirectory()

    #执行爬虫
    spidersql(datapath,url,headers)


'''url和headers可修改'''
if __name__ == '__main__':

    url='http://10.113.221.244:8003/bas/Account/ashx/SysAshx/DataQuery.ashx?p=GetData&page=1&limit=1000&dbtype=EM_CN&sqlstr=select+*+from+yb_tmp_hwq_01&_=1643014284042'


    headers={"Host":"10.113.221.244:8003","Connection":"keep-alive","Accept":"application/json, text/javascript, */*; q=0.01","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","X-Requested-With":"XMLHttpRequest","Referer":"http://10.113.221.244:8003/bas/Account/SysFile/DataQuery?functionid=0CA6637E6B2CBE8D988863D689162306&r=0.8620768865661128","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Cookie":"ASP.NET_SessionId=ltfchzkglap4lnhcyd53im4c; EM_GX_COOKIE=USER_ID=4Auserid_rad_170171; cityID=12; CITY_COOKIE=cityID=12; userID=4Auserid_rad_170171; userCityID=12; is4AorBass=Bass; DATABASE_COOKIE=DATABASE_ID=9D835CA801CCB07D0890CC0ADED8C9C2; .ASPXAUTH=40A7AAD0A4C934187EE68591090B14C207E10A28591A39ACEDCFFBB89ED256AB93A2EED4372EA33C4C302688982A40EF58A0258C57975C8A2CE651CCF8824D3FAAD56C899E0BEE9511AB00F38ACAD666393F8E06DBE460931728B5559D38D9A67764CC4BAF53C039119B9A451FDB692B280695763E9245051A9887B501F65AF2B11C5AC9C220E4C2FF54B19AE0FFA4175C5B1501BFE95E1DE893E0D2AEFACCE6"}



    main(url,headers)
