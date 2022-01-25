import pandas as pd
import os

import tkinter as tk
from tkinter import filedialog
import re
import time

path='/home/admin/image/skills/'

# path=r'C:\Users\abc\Desktop'
outpath='/home/admin/picname/skillname.txt'
# outpath=r'C:\Users\abc\Desktop\skillname.txt'
last= os.path.getmtime(path)
while(True):
    time.sleep(1)
    next= os.path.getmtime(path)
    if next-last > 0:#10分钟
        list=os.listdir(path)
        res=str(list)
        with open(outpath,"w") as f:
            f.write(res)  # 自带文件关闭功能，不需要再写f.close()
            print('已更新')
            last= os.path.getmtime(path)