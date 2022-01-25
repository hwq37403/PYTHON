import pandas as pd


import math

def taizhang():

    '''
    将财务数据里的总表，循环遍历，从发行数据台账进行累加核算，并将相应核算信息插入对应的下一行
    核心功能构成为拆表和插行，其中插行主要思维也是拆分DF，然后最后再合起来
    :return:
    '''
    count = 0

    index_total = 0
    money_total = 0
    time_total = 0

    F_start = 0
    F_end = 0
    F_count = 0

    n_get_money_index = []
    n_get_money = []
    n_get_money_time = []

    read_path = 'D:\\财务数据\\填写台账.xlsx'
    read_path_1 = 'D:\\财务数据\\财务数据\\总表.xlsx'
    file1 = pd.read_excel(read_path, sheet_name='Sheet1')
    file2 = pd.read_excel(read_path_1, sheet_name='居民')

    menu = file2.iloc[:, 0].drop_duplicates()

    for name in menu:

        i = 0
        j = 0

        print(j)
        money_temp = 0
        start = 0
        F_count = 0

        try:

            df1 = file1[file1['名称'] == name]
            df1['月份'] = None
            df1['钱'] = None
            df1['合并时间'] = None
            df1 = df1.reset_index(drop=True)
            print(df1)
        except IndexError as e:
            print(e)

        df2 = file2[file2['名称'] == name]
        df2 = df2.reset_index(drop=True)
        print(df2)

        length_1 = len(df2)
        while i < length_1:
            length = len(df1)
            money_total = df2.iloc[i, 1]
            time_total = df2.iloc[i, 2]

            try:

                money = df1.iloc[j, 4]
            except IndexError as e:
                print(e)
                break


            money_temp = money_temp + money

            if round(money_temp, 2) == money_total:
                # 匹配成功，应在第j行插入数据
                # i+1
                print('匹配成功')
                print("目标金钱" + str(money_temp))
                print(j)
                F_count = j - F_count + 1
                print(F_count)
                # 超过边界，回溯到上一行
                if F_count >= len(df1):
                    break
                if df1.iloc[F_count, 3] is None:
                    if j == 0:
                        F_start = df1.iloc[j, 3]  # 开始时间
                        F_end = df1.iloc[j, 3]  # 匹配成功，标记结束位置
                        df_1 = df1.loc[:j]
                        df_2 = df1.loc[j + 1:]
                    else:
                        F_start = df1.iloc[F_count+1, 3]
                        F_end = F_start  # 匹配成功，标记结束位置
                        print(F_start)
                        print(F_end)

                        ######

                        df_1 = df1.loc[:j + 2]
                        df_2 = df1.loc[j + 3:]

                else:

                    ######
                    if j == 0:
                        F_start = df1.iloc[j, 3]  # 开始时间
                        F_end = df1.iloc[j, 3]  # 匹配成功，标记结束位置
                        df_1 = df1.loc[:j]
                        df_2 = df1.loc[j + 1:]

                    else:
                        F_start = df1.iloc[F_count-1, 3]  # 开始时间



                        F_end = df1.iloc[j, 3]  # 匹配成功，标记结束位置
                        df_1 = df1.loc[:j]
                        df_2 = df1.loc[j + 1:]
                # if math.isnan(F_start) is True:
                #     F_count += 1
                #     F_start = df1.iloc[F_count, 3]
                if F_start is None:
                    F_start = df1.iloc[F_count, 3]

                print('df1 is:\n', df_1)
                print('df2 is:\n', df_2)
                print(df1.iloc[j, 0])
                print(df1.iloc[j, 1])
                print(df1.iloc[j, 2])
                print(df1.iloc[j, 3])
                print(df1.iloc[j, 4])
                df3 = pd.DataFrame({
                    '电厂（交易对象）编码': [df1.iloc[j, 0]],
                    '名称': [df1.iloc[j, 1]],
                    '动作标记': [' '],
                    '发行日期': [None],
                    '含税电费': [0],
                    '月份': [df2.iloc[i, 2]],
                    '钱': [money_temp],
                    '合并时间': [str(int(F_start)) + '—' + str(int(F_end))]
                })
                df1 = df_1.append(df3, ignore_index=True).append(df_2, ignore_index=True)

                if math.isnan(F_start) is True:
                    F_count += 1
                    F_start = df1.iloc[F_count, 3]

                F_count = 0

                print(F_start)
                print(F_end)

                print(df1)

                money_temp = 0
                i += 1
                j = 0



            elif round(money_temp, 2) < money_total:
                j += 1
                F_count += 1

                print("累加")
                print(j)
                if j >= length:
                    j = 0
                    money_temp = 0
                    start = 0
                    print(money_total)
                    # 需要从头遍历
                # 继续累加
            else:
                # 超过累加,从df1的第二行开始累加
                start += 1
                j = start
                money_temp = 0
                F_count = 0

                if j >= length:
                    j = 0
                    money_temp = 0
                    start = 0
                    print(money_total)
                    # 需要从头遍历

                print("超过累加,j=" + str(j))
                try:

                    print(df1.iloc[j, 4])
                except IndexError as e:
                    print(e)
        count += 1
        df1.to_excel('D:\\财务数据\\结果居民\\' + str(count) + '.xlsx', index=None)


