# ***PYTHON***
## ***work***
- 自动化
  - 4A.py 实现网页自动化脚本，4A账号一键登录，需提前登录一点通保证流程自动进行。
- 数据清理
  - dataclear.py 通过合成基础表，利用fuzzywuzzy库模糊匹配功能，搜索符合条件关键字并实现vlookup
  - hecheng.py 合成基础表xlsx（可修改为合成csv,但合成csv文件使用CMD命令 COPY *.CSV ALL.CSV）
  - hecheng_sheet.py 合成一个excel中的所有子表
  - Pivot_table.py 实现数据透视表
  - qx_chaifen.py 根据某列列表进行文件拆分
  - sheet_name.py 返回excel所有子表名称
- 通过pandas针对特殊场景实现的数据清理
  - taizhang2.py
- 工具类
  -TXT_EXCEL.py 
## ***youhuixiaoqu***
- youhuixiaoqu.py 自动化完成每日优惠小区基站清理
- ~~mkdir.py~~ 生成文件，不过OS库自带mkdir API，~~所以废弃~~
## ***other***
- picutil.py 图片处理工具，通过运维思想实现自动化
- spidersql.py 爬虫工具，抓取表格数据