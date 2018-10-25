#coding=utf-8
import requests
import json
import pymysql
import time
import sys
from bs4 import BeautifulSoup

# #这里的header和上面的不同，大家试试看删掉一些还能不能获取数据
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#     "DNT": "1",
#     "Host": "www.lagou.com",
#     "Origin": "https://www.lagou.com",
#     "Referer": "https://www.lagou.com/jobs/list_",
#     "X-Anit-Forge-Code": "0",
#     "X-Anit-Forge-Token": None,
#     "X-Requested-With": "XMLHttpRequest" # 请求方式XHR
# }

# ajax_url = 'https://www.lagou.com/jobs/positionAjax.json'

# #first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
# post_param = {"first": "false", "pn": "1", "kd": "北京运维工程师"}

# # 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
# r = requests.post(ajax_url, headers=headers, data=post_param)

# result = json.loads(r.text)

# positionId = []
# for item in result["content"]["positionResult"]["result"]:
#     positionId.append(item['positionId'])

# print(positionId)

# for num in positionId:
#     jobs_url = 'https://www.lagou.com/jobs/' + str(num) + '.html'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#         'Host': 'www.lagou.com',
#         'Connection': 'keep-alive',
#         'Origin': 'http://www.lagou.com',
#         }
#     findpage = requests.get(jobs_url,headers=headers)
#     html = findpage.text
a = [{'a':1,'b':2},{'c':3}]
soup = BeautifulSoup(open('index.html', encoding="utf-8"),'html.parser')

for tag in soup.find_all("dd",'job_bt'):
    page = ''
    # print(tag)
    for strs in tag.div.stripped_strings:
      page = page + strs +  '\n'
print(page)





# db = pymysql.connect("192.168.11.244","python_user","python","lagou")
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database VERSION:%s" % data)
# db.close()