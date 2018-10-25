#coding=utf-8

import fileinput
import time
import sys
import re
import pymysql



#数据库插入函数
def conn(sql,value):
  db = pymysql.connect('192.168.11.244','python_user','python','lagou')
  cursor = db.cursor()
  cursor.execute(sql,value)
  db.commit()
  cursor.close


file = '../../localhost_access_log.2018-09-17.txt'

regex = r"(?P<ip>.*?) (?P<remote_log_name>.*?) (?P<userid>.*?) \[(?P<date>.*?)(?= ) (?P<timezone>.*?)\] \"(?P<request_method>.*?) (?P<path>.*?)(?P<request_version> HTTP/.*)?\" (?P<status>.*?) (?P<size>.*?)$"

list = []
for line in fileinput.input(file):
  matches = re.findall(regex,line)
  matches.append(matches[0][6].split('?')[0])
  try:
    matches.append(matches[0][6].split('?')[1])
  except IndexError as  e:
    # print(e)
    matches.append('')
  list.append(matches)

#数据库插入函数
def conn(sql,value):
  db = pymysql.connect('192.168.11.244','python_user','python','lagou')
  cursor = db.cursor()
  cursor.execute(sql,value)
  db.commit()
  cursor.close

sql = "insert into czg(ip,time,method,status,url,parameter) values(%(ip)s,%(time)s,%(method)s,%(status)s,%(url)s,%(parameter)s)"
for str in list:
    value = {'ip':str[0][0],'time':str[0][3],'method':str[0][5],'status':str[0][8],'url':str[1],'parameter':str[2]}
    conn(sql,value)
