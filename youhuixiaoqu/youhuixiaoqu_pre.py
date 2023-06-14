import sys

import pandas as pd
import openpyxl

# 由于PD会覆盖重写sheet，为了保存一个EXCEL多个sheet，所有只能通过EXCELwriter使用一个句柄来写入多个sheet
import numpy  as np
import os
import pandas as pd
import mkdir
import time  # 引入time模块

<<<<<<< Updated upstream
<<<<<<< Updated upstream
# 自动化库
import pyautogui as pag
import webbrowser
import pyperclip as pyc
=======

>>>>>>> Stashed changes


=======



>>>>>>> Stashed changes
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d"):
    time_array = time.localtime(time_stamp/1000)
    other_style_time = time.strftime(format_string, time_array)
    print(other_style_time)
    return other_style_time

# 将今日的数据合并，放在一张表里


def pre(date, flag):
    path = r'E:\WORK\优惠小区\优惠小区\优惠小区导入' + date
    outpath = r'E:\WORK\优惠小区\优惠小区\优惠小区导入'+date+'\优惠小区导入' + date + '.xlsx'

    filenames = os.listdir(path)  # 获取path目录下的所有excel
    df_total = pd.DataFrame(
        columns=('基站名', '基站小区编号(10进制)', '基站小区编号(16进制)', '区县', '长度', '文件名', '备注'))
    for filename in filenames:
        print(filename)
        tmp_path = path + '\\' + filename
        df = pd.read_excel(tmp_path, sheet_name=None)
        print('sheet名为' + str(list(df)))
        # 循环sheet名，判断各种不规范表格，做数据清理
        for index in list(df):
            if index == 'Sheet1':
                try:
                    df = pd.read_excel(tmp_path, sheet_name=index)
                    df = df.loc[:, [
                        '基站名', '基站小区编号(10进制)', '基站小区编号(16进制)', '区县']]
                    break
                except ValueError:
                    flag = False
                    print('Sheet1表数据有问题，请手工清理，文件名为:' + filename)
                except KeyError:
                    flag = False
                    print('列名有问题,请检查')
                    input('输入任意键退出')
            elif index == '操作表':
                print(222)
                try:
                    df = pd.read_excel(tmp_path, sheet_name=index)
                    df = df.loc[:, [
                        '基站名', '基站小区编号(10进制)', '基站小区编号(16进制)', '区县']]
                    break
                except ValueError:
                    flag = False
                    print('操作表数据有问题,请手工清理,文件名为:' + filename)
            else:
                print('既不是Sheet1，也不是操作表,交的什么鬼数据')
                print('出错文件名:' + filename + ',sheet名为:' + index)
        col_count=0
        for i in range(0, len(df)):
            col_count+=1
            x = len(str(df.loc[i, ['基站小区编号(16进制)']].values[0]))
            # print('长度读取到没'+str(len(x)))
            if x == 4 or x == 7 or x == 9:
                df.loc[i, '长度'] = x
                df.loc[i, '文件名'] = filename
            else:
                print('长度有问题,问题长度:'+str(x)+'行数为：'+str(col_count)+'----文件名为:'+filename +
                      '---代码为'+str(df.loc[i, ['基站小区编号(16进制)']].values[0]))
                flag = False

        df_total = df_total.append(df)

        # print(df_total)

    print("----------------------合并后的df-----------------------")

    print(df_total)

    print('数据总长度为' + str(len(df_total['基站名'])))

    df_total.to_excel(outpath, index=False)
    #
    return flag


# 将表数据与代码表left join
def xiaoquyouhui(date):
    read_path = 'E:\\WORK\\优惠小区\\优惠小区\\优惠小区导入' + date + '\\优惠小区导入' + date + '.xlsx'
    out_path = 'E:\\WORK\\优惠小区\\优惠小区\\优惠小区导入' + date + '\\优惠小区导入' + date + '结果.xlsx'

    dm_path = r'E:\WORK\优惠小区\区县代码表\区县代码.xlsx'
    df2 = pd.read_excel(dm_path, 'Sheet1')
    with pd.ExcelFile(read_path) as xls:
        df1 = pd.read_excel(xls, 'Sheet1')
        # df2 = pd.read_excel(xls, 'Sheet2')

        df1['区县'] = df1['区县'].map(lambda 区县: 区县[0:2])
        df2['区县'] = df2['区县'].map(lambda 区县: 区县[0:2])

        print(df1['区县'])

    outer = pd.merge(df1, df2, on='区县')

    print(outer)

    outer = outer.loc[:, [
        '基站名', '基站小区编号(10进制)', '基站小区编号(16进制)', '区县', '类型', '代码']]
    #TODO 将outer转化为普通优惠配置模板数据格式

    outer2=outer.loc[:,['代码','基站小区编号(16进制)']]
    outer2['length'] = outer2['基站小区编号(16进制)'].astype(str).str.len()

    #case when
    outer2['网络制式'] = np.where(outer2['length']==4, '23G',
                      np.where(outer2['length']==7, '4G', 
                      np.where(outer2['length']==9, '5G', 'FALSE')))
    outer2.rename(columns={'代码':'小区优惠代码','基站小区编号(16进制)':'基站信息'},inplace=True) 

    outer2 = outer2.astype(str).drop(['length'], axis=1)  #删除a列

    outer2.to_excel(out_path, index=False, encoding='utf-8')
<<<<<<< Updated upstream

    # outer.to_excel(out_path, index=False, encoding='utf-8')

=======

    # outer.to_excel(out_path, index=False, encoding='utf-8')

>>>>>>> Stashed changes

# 逻辑流程
def controller():
    ticks = time.localtime()
    # date=timestamp_to_ydate(ticks)
    date = time.strftime("%Y%m%d", time.localtime())
    print(date)
    # date = input('请输入日期')
    file = r'E:\WORK\优惠小区\优惠小区\优惠小区导入' + date  # 结果日期
    tips = r'E:\WORK\优惠小区\操作手册.txt'  # 操作手册

    mkdir.mkdir(file)
    os.startfile(file)
    print("创建目录成功！")
    print("请将文件复制好，确认数据无误以后再确认Y")
    print("否则脚本报错，需重新运行")
    a = input("按Y/N")
    flag = True
    while (True):
        if a == "Y" or a == "y":
            print("执行成功！")
            flag = pre(date, flag)

            xiaoquyouhui(date)  # 执行脚本
            os.startfile(file+'\\优惠小区导入'+date+'.xlsx')
            os.startfile(file+'\\优惠小区导入'+date+'结果.xlsx')
            os.startfile(tips)
            print("源文件格式是否正确:", flag)
            a == input("已完成优惠小区处理，确认退出吗?（按任意键退出）")
            # 自动化填写表单
            if (a == 'N' or a == 'n'):
                exit(0)
            time.sleep(2)
            # autoWirteSheet()
            exit(0)
        elif a == "N" or a == "n":
            print("你已退出了该程序！")
            exit(0)
        else:
            print("你输入的内容有误，请重输入！")


def main():
    while (True):
        print("请确定今天是否需要处理优惠小区。按Y/N")
        in_content = input("请输入：")
        if in_content == "Y" or in_content == 'y':

            controller()  # 执行脚本
            exit(0)
        elif in_content == "N" or in_content == 'n':
            print("你已退出了该程序！")
            exit(0)
        else:
            print("你输入的内容有误，请重输入！")


if __name__ == '__main__':
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    main()
=======
    main()
>>>>>>> Stashed changes
=======
    main()
>>>>>>> Stashed changes
