#coding=utf-8
import sys
import requests
import time
import pymysql
from urllib.parse import quote
from bs4 import BeautifulSoup

#获取拉勾网的Ajax data

city = '北京'
url = 'https://www.lagou.com/jobs/positionAjax.json?city=' + city + '&needAddtionalResult=false'
# first: true
# pn: 1
# kd: 系统运维工程师

headers = {
  'Host':'www.lagou.com',
  'Origin':'http://www.lagou.com',
  'X-Anit-Forge-Code':'0',
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
  'Accept':'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With':'XMLHttpRequest',
  'X-Anit-Forge-Token':None,
  'Referer':'https://www.lagou.com/jobs/list_',
  'Cookie':'user_trace_token=20180905105011-2dca8b7f-78f1-47f3-b08d-af4409857318; _ga=GA1.2.1803439144.1536115812; LGUID=20180905105012-68ced9c3-b0b6-11e8-85e7-525400f775ce; _gid=GA1.2.407729677.1536645942; LG_LOGIN_USER_ID=e93971278d2311d26b62adeb11ffc1e096041f7455cf8965c510619c1e703039; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=154; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAFCAAEG5FDC012FD87FF113E66936AA56A94C39; _putrc=5802AA2461D682E7123F89F2B170EADC; login=true; unick=%E9%99%88%E4%BC%9F%E5%85%89; LGSID=20180912165232-3011a893-b669-11e8-959c-525400f775ce; PRE_UTM=; PRE_HOST=www.google.co.jp; PRE_SITE=https%3A%2F%2Fwww.google.co.jp%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536645944,1536645996,1536737462,1536742354; gate_login_token=62b8beb2e5e5a7c547fbfa82bb87a5cf8b9b51a6191f6550983a3579f14e7b3e; _gat=1; LGRID=20180912171332-1ee5edbb-b66c-11e8-959e-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536743613; SEARCH_ID=c3b324538f514e54af2a74f3ab4b3551',
}

data = {'first':'true','pn':5,'kd':'系统运维工程师'}

Info = requests.post(url,data=data,headers=headers)
Info = Info.json()
menu = []
for pstr in Info["content"]["positionResult"]["result"]:
    jobs = {'positionId':pstr['positionId'],'positionAdvantage':pstr['positionAdvantage'],'salary':pstr['salary'],'workYear':pstr['workYear'],'companyShortName':pstr['companyShortName']}
    menu.append(jobs)

#通过positionId 获取职业详情数据
for page in menu:
    # time.sleep(1)
    positionId = page['positionId']
    details = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'
    position = requests.get(details,headers=headers)
    html = position.text
    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    for tag in soup.find_all("dd",'job_bt'):
        content = ''
        for strs in tag.div.stripped_strings:
            content = content + strs +  '\n'
    page['content'] = content
# print(menu)
# sys.exit()


#数据库插入函数
def conn(sql):
  db = pymysql.connect('192.168.11.244','python_user','python','lagou')
  cursor = db.cursor()
  cursor.execute(sql)
  db.commit()
  cursor.close

def get_i_sql(table, dict):
    '''
    生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''
    sql = 'insert into %s set ' % table
    sql += dict_2_str(dict)
    return sql

def dict_2_str(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)

tmplist = []
for value in menu:
    sql = get_i_sql('plan',value)
    conn(sql)
