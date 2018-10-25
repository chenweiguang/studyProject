#coding=utf-8

import re
import sys
import time
import json
import pymysql


fileinput = 'somur_api.info.log'
try:
  file = open(fileinput,'r',encoding='utf-8')
except IOError as e:
  print(e)
  sys.exit()
strings = file.read()
file.close()

def conn():
  db = pymysql.connect('localhost','python_user','python','lagou')
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

regex1 = r"\[INFO ] \[\d{1,4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}] .* - {.*}"
context1 = re.compile(regex1)
Info = context1.findall(strings)

regex2 = r"{.*}"
regex3 = r"\w*=\[\".*\"]"
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
  # params = mdict.getsparams','')
  ip = mdict.get('ip','')
  logId = mdict.get('logId','')
  req_time = mdict.get('time','')
  stype = mdict.get('type','')
  referer = mdict.get('refer','')
  params = mdict.get('requestMap')
  matches = re.findall(regex3,params)

  querysql = "select * from log_url_config where url='%s'" %url
  result = query(db,querysql,'query')
  if result is None:
    insertsql = "insert into log_url_config(url) value('%s')" %url
    url_id = query(db,insertsql,'insert')
  else:
    url_id = result[0]

  sqllist = "insert into log_req_list_2018(client_ip,referer,url_id,req_time,method,source_pos) values('%s','%s','%s','%s','%s','%s')" %(ip,referer,url_id,req_time,stype,method)
  req_id = query(db,sqllist,'insert')
  psql = ''
  log_para = ''
  if matches:
    for sr in matches[0].split(','):
      for sq in re.findall(regex3,sr):
        par = sq.split('=',1)[0]
        par_value = sq.split('=',1)[1].strip('[]"')
        par_list = "insert into log_para_2018(req_id,parameter,parameter_value)values('%s','%s','%s')" %(req_id,par,par_value)
        # print(par_list)
        query(db,par_list,'insert')
