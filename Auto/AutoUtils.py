import pyautogui as pag
import webbrowser
import pyperclip as pyc

import time

'''
向下按n次
'''
def pressdown(n):
    time.sleep(0.5)
    for i in range(0,n):
        pag.hotkey('down') 
        
'''
将s字符串粘贴
'''    
def cv(s):
    pyc.copy(s)
    time.sleep(0.5) 
    pag.hotkey('ctrl', 'v') 
    time.sleep(1)