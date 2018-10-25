#coding=utf-8

import re
import sys
import time
import json
import pymysql
from datetime import timedelta,datetime
import os


yesterday = datetime.today() + timedelta(-1)
yesterday_format = yesterday.strftime('%Y-%m-%d')
sdir = "/srv/log/somur_api/" + yesterday_format
filelist = os.listdir(sdir)


def conn():
  db = pymysql.connect('192.168.11.244','python_user','python','lagou')
  return db

def query(db,sql,id):
  if id == 'query':
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    db.commit()
    cursor.close()
    return result
  elif id == 'insert':
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def isdict(vdict):
 return (type(vdict).__name__ == 'dict')


def stdict(sdict,req_id,db):
  for key in sdict:
    if isdict(sdict[key]):
        stdict(sdict[key],req_id,db)
    else:
      if sdict[key] is not None:
        sql_Insert_2018 = "insert into log_para_2018(req_id,parameter,parameter_value) values('%s','%s','%s')" %(req_id,key,sdict[key])
        query(db,sql_Insert_2018,'insert')
        # print(sql_Insert_2018)


for filename in filelist:
  fileinput = sdir + '/' + filename
  try:
    file = open(fileinput,'r',encoding='utf-8')
  except IOError as e:
    print(e)
    sys.exit()

  strings = file.read()
  file.close()
  regex1 = r"\[INFO ] \[\d{1,4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}] .* - {.*}"
  context1 = re.compile(regex1)
  Info = context1.findall(strings)

  regex2 = r"{.*}"
  db = conn()

  for i in Info:
    context2 = re.compile(regex2)
    request = context2.findall(i)
    mdict = json.loads(request[0])
    logName = mdict.get('logName','Default')
    if logName == '调用service方法开始' or logName == '调用service方法结束' or logName == 'Default':
      continue
    url = mdict.get('url','')
    method = mdict.get('classAndMethod','')
    params = json.loads(mdict.get('params',''))
    ip = mdict.get('ip','')
    logId = mdict.get('logId','')
    req_time = mdict.get('time','')
    stype = mdict.get('type','')
    referer = mdict.get('refer','')
    querysql = "select * from log_url_config where url='%s'" %url
    print(params)
    result = query(db,querysql,'query')
    if result is None:
      insertsql = "insert into log_url_config(url) value('%s')" %url
      url_id = query(db,insertsql,'insert')
    else:
      url_id = result[0]
    sqllist = "insert into log_req_list_2018(client_ip,referer,url_id,req_time,method,source_pos) values('%s','%s','%s','%s','%s','%s')" %(ip,referer,url_id,req_time,stype,method)
    req_id = query(db,sqllist,'insert')
    # if req_id is None:
    #   print('req_id is none')
    # if db is None:
    #   print('db is none')
    stdict(params,req_id,db)
  db.close()