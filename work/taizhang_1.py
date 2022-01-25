import pandas as pd
import numpy as np
from pandas.core.frame import  DataFrame

read_path = 'D:\\财务数据\\填写台账.xlsx'
read_path_1 = 'D:\\财务数据\\财务数据\\总表.xlsx'

file1 = pd.read_excel(read_path, sheet_name='Sheet1')



file2 = pd.read_excel(read_path_1,sheet_name='居民')


menu1 = file1.iloc[:, 1].drop_duplicates()

j = 0
money_temp = 0  # 累加计数器
start = 0  # 本次累加起始位置
start_money = 0  # 本次累加起始位置
start_time = 1  # 本次累加起始时间
end = 9999  # 本次累加结束位置
n_get_money_time = []  # 保存未领钱的月份的位置
n_get_money = []  # 保存未领钱的金额
n_get_money_r_time = []  # 保存未领取的真实时间
# 用户按时间领钱，则状态置换为true,用户未领钱,则将状态置换为false，直到累加成功，再将state置换为true
name = ''  # 用户名字

i = 0

log_list = []

f_count = 0  # 错误计数器判断，当计数器>20，表示该列表循环出错，需特殊处理，回溯到之前第一次开始记为领钱时的位置，开始累加，直到核算到
# 成功后，再跳回继续的位置
flag = False  # 判断是否成功领钱
state = False  # 判断是否进入下一个用户
state_first = False  # 判断是否是第一次累加成功

s_temp = 0  # 特殊情况金钱计数器

name_temp = ''
start_time_temp = 0

for name1 in menu1:
    i=0
    j=0
    start = 0
    money_temp = 0  # 累加计数器
    f_count=0

    n_get_money_time.clear()
    n_get_money.clear()
    n_get_money_r_time.clear()


    df1 = file1[file1['名称'] == name1]
    print(df1)
    import pandas as pd
    import numpy as np
    from pandas.core.frame import DataFrame

    df2 = file2[file2['名称'] == name1]
    print(df2)

    # print(menu1)

    length = len(df1)
    length_1 = len(df2)

    while i < length and j<length_1:
        name = df1.iloc[i, 1]
        time = df1.iloc[i, 3]

        if name_temp != name and state == True:
            # 表明进入下一个用户，可以清楚这个用户的临时信息

            n_get_money_time.clear()
            n_get_money.clear()
            n_get_money_r_time.clear()
            name_temp = name
            state = False
        money = df1.iloc[i, 4]
        time = df1.iloc[i, 3]

        money_total = df2.iloc[j, 1]  # 总表第二列
        time_total = df2.iloc[j, 2]  # 总表第三列

        money_temp = money_temp + money

        print(money_temp)  # 处理为两位小数
        if round(money_temp, 2) < money_total and j < length_1:  # 累加中
            flag = False

            if start > length:
                break
            print(name_temp)
            print(money_total)
            print(money_temp)
            print(start)

        elif round(money_temp, 2) == money_total and j < length_1:  # 累加成功
            print("插入下一行")
            print("金钱为" + str(money_total))
            print("时间为" + str(time_total))
            money_temp = 0
            name_temp = df2.iloc[j, 0]

            if start > length:
                break

            flag = True
            # 输出n_Get_money列表
            if flag == True:
                start_money = money
                start_time = time
                j = j + 1
                start = i + 3  # 下一次累加的起始位置
            print(name_temp)
            print(n_get_money_time)
            print(n_get_money)

            print(money_temp)
            print(j)  # 总表位置
            print(start)  # 发行表起始位置
            print('#####')
            print('     ####   ')
            print('        ####')

        else:  # 累加失败,当累加出错对不上时，应该回退到这次累加的起始位置，然后从起始位置的下一行开始累加
            print("累加有错，对不上，有用户未来领钱")
            flag = False
            money_temp = 0  # 累加器清0
            start -= 1
            if start > length:
                break

            start_money = df1.iloc[start - 1, 4]
            start_time = df1.iloc[start - 1, 3]

            n_get_money_time.append(start + 1)  # 说明起始位置的月份是未领钱月份，保存起始位置月份
            n_get_money.append(start_money)  # 保存起始位置金钱
            n_get_money_r_time.append(start_time)  # 保存起始位置真实时间

            name_temp = df2.iloc[j, 0]

            start_time_temp = df1.iloc[i, 3]

            i = start - 1  # 将start回溯到起始位置的下一行

            print(name_temp)
            print(n_get_money_time)
            print(n_get_money)

            start = start + 2

            f_count += 1

            if  f_count > 10 or  j< len(df2):  # 表示在未领取月份，用户之后又来领钱了，所以需要回到为领钱月份里累加
                # 并且目标累加匹配成功后需回到财务数据下一个目标的起始位置,并在下一次循环，通过名字判断是否还是同一用户

                print('1111111')

                for k in range(0, len(n_get_money)):
                    s_temp += n_get_money[k]
                    if s_temp == money_total:
                        # 领钱成功，找到对应的df1里插入
                        print(n_get_money_time[k])  # n_get_m_time就是对应i的起始位置
                        # 插入,
                        print('插入成功')
                        # 回到i正常循环下的位置
                        i = n_get_money_time[-20]
                        # 思考什么时候情况n_get_money_time和n_get_money清零
                        # 保存这一次的用户名
                        name_temp = df2.iloc[j, 0]
            if name_temp != df2.iloc[j + 1, 0]:  # 判断是否需要清零信息
                state = True

            log_list.append(n_get_money)

        i += 1



    # 日志打印

    print(log_list)
    # f = open("D:\\财务数据\\错误日志.txt", "w")
    #
    # f.write(str(log_list))
    # f.close()

