import pandas as pd
import requests




url='http://eipapp.scmcc.com.cn:81/quicknotes/flow/note/todo2?hostport=81'
resp=requests.post(
    url=url,
    headers={"Host":"tooltt.com","Connection":"keep-alive","Cache-Control":"max-age=0","sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"macOS\"","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site":"none","Sec-Fetch-Mode":"navigate","Sec-Fetch-User":"?1","Sec-Fetch-Dest":"document","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Cookie":"Hm_lvt_8592dada379991cbb8c2d53677f43f61=1645757521,1645758555,1645758670,1645758705; Hm_lpvt_8592dada379991cbb8c2d53677f43f61=1645773036","If-None-Match":"W/\"62158cc9-2529a\"","If-Modified-Since":"Wed, 23 Feb 2022 01:24:25 GMT"}
 )

print(resp.status_code)
print(resp.status_code)
print(resp.headers)
print(resp.cookies)

str1 = resp.content.decode('utf-8')

print(str1)