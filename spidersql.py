
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

    url='http://10.113.221.244:8002/bas/Account/ashx/SysAshx/DataQuery.ashx?p=GetData&page=1&limit=1000&dbtype=EM_CN&sqlstr=select+*+from+YB_TMP_HWQ_02&_=1657003062189'


    headers={"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"ASP.NET_SessionId=w2n5xnsythhr12qfwats1rw5; EM_GX_COOKIE=USER_ID=4Auserid_rad_170171; cityID=12; CITY_COOKIE=cityID=12; userID=4Auserid_rad_170171; userCityID=12; is4AorBass=Bass; DATABASE_COOKIE=DATABASE_ID=9D835CA801CCB07D0890CC0ADED8C9C2; .ASPXAUTH=28DC6BA2EB4F3BE34A339C576ACC142304961C1EFE3976BD6B1E1DEA99F586CC71D7B56B1E22B0EF6754E52B8F64AA143B4D0DD1497CE8032F32B35DA5B972A529A0850254F54EBB668FBFBA6DBFA6C6FC5B7BAA1E984B4506184C161781087C929F9C5BE363C64DEEF4387DAF35B168192BF84777B4AE7E965372BD765209BF6B8CFE8FD2C9DDE0D1A634816DE341CBBE7477A516CBB560830B7F65D581440E","Host":"10.113.221.244:8002","Referer":"http://10.113.221.244:8002/bas/Account/SysFile/DataQuery?functionid=0CA6637E6B2CBE8D988863D689162306&r=0.7607663894325467","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53","X-Requested-With":"XMLHttpRequest"}

    main(url,headers)
