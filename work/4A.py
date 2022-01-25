from idlelib import browser

import document as document
from selenium import webdriver
import pytesseract
import os,time
import requests

from selenium.webdriver.common.keys import Keys

'''
4A账号一键登录，需提前登录一点通保证流程自动进行。
:return:
'''
chromedriver = r"C:\Users\Admin\Desktop\chromedriver.exe"  # 这里写本地的chromedriver 的所在路径
os.environ["webdriver.Chrome.driver"] = chromedriver  # 调用chrome浏览器
driver = webdriver.Chrome(chromedriver)
driver.get("http://10.109.209.100:9083/uac/web3/jsp/local/sichuan/login.jsp")  # 该处为具体网址
driver.refresh()  # 刷新页面
driver.maximize_window()  # 浏览器最大化

time.sleep(1)

# 填充用户名 密码 验证码
driver.find_element_by_id("loginName").send_keys("huangwanqiang")
# 点击登录
driver.find_element_by_id("login_btn").click()

driver.find_element_by_id("face_login_btn").click()

time.sleep(15)
try:
    driver.find_element_by_id("saveDrsCfgBtn").click()
except Exception as e:
    print("刷脸太慢了")
    time.sleep(15)
    driver.find_element_by_id("saveDrsCfgBtn").click()

# browser.find_element_by_id('face_login_btn').send_keys(Keys.ENTER)

time.sleep(1)

driver.find_element_by_id("p1050000").click()

print('进入大数据个性化系统')
driver.switch_to.frame(driver.find_element_by_id("title4tab"))

driver.switch_to.default_content()








