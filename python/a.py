# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"\[INFO ] \[\d{1,2}:\d{1,2}:\d{1,2}] .* - {.*}"

test_str = ("[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.3.6-1366786, built on 07/29/2012 06:22 GMT\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:host.name=dev_web\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.version=1.8.0_101\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.home=/usr/local/java/jdk1.8.0_101/jre\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.class.path=/usr/local/tomcat-test/tomcat_somur/bin/bootstrap.jar:/usr/local/tomcat-test/tomcat_somur/bin/tomcat-juli.jar:/usr/local/tomcat-test/tomcat_somur/webapps/tingyun/tingyun-agent-java.jar\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/usr/local/tomcat-test/tomcat_somur/temp\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:os.name=Linux\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:os.arch=amd64\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:os.version=4.4.143-1.el6.elrepo.x86_64\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:user.name=setup\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:user.home=/home/setup\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Client environment:user.dir=/home/setup\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ZooKeeper - Initiating client connection, connectString=39.107.86.68:2181 sessionTimeout=10000 watcher=com.baidu.disconf.core.common.zookeeper.inner.ResilientActiveKeyValueStore@dc9e959\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ClientCnxn - Opening socket connection to server /39.107.86.68:2181\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ClientCnxn - Socket connection established to 39.107.86.68/39.107.86.68:2181, initiating session\n"
  "[INFO ] [11:11:38] org.apache.zookeeper.ClientCnxn - Session establishment complete on server 39.107.86.68/39.107.86.68:2181, sessionid = 0x10000148c080cfc, negotiated timeout = 10000\n"
  "[INFO ] [11:12:19] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.UserController.checkAutoMobile\",\"ip\":\"106.38.33.70\",\"logId\":\"185bf62665d441d4b7a68e67ca4b0cac\",\"logName\":\"请求开始\",\"params\":\"[\"\"13269236571\"\"]\",\"requestMap\":\"{mobile=[\"k2rV9Lm96jFeALhPykXrVA==\"]}\",\"sessionId\":\"61E4AE5FEC7C246F26FD6C3D2906E233\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:19\",\"type\":\"POST\",\"url\":\"https://dev.somur.com:8444/somur_api/user/checkAutoMobile.json\"}\n"
  "[INFO ] [11:12:19] com.somur.controller.UserController - #######checkAutoMobile.json#####\n"
  "[INFO ] [11:12:19] com.somur.controller.UserController - #######mobile=#####13269236571\n"
  "[INFO ] [11:12:19] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.service.impl.UserServiceImpl.checkAutoMobile\",\"logId\":\"185bf62665d441d4b7a68e67ca4b0cac\",\"logName\":\"调用service方法开始\",\"params\":\"[\"\"13269236571\"\"]\",\"resContent\":\"\",\"time\":\"2018-09-26 11:12:19\"}\n"
  "[INFO ] [11:12:19] com.somur.aspect.SystemOperationLogs - \"{\"classAndMethod\":\"com.somur.service.impl.UserServiceImpl.checkAutoMobile\",\"logId\":\"185bf62665d441d4b7a68e67ca4b0cac\",\"logName\":\"调用service方法结束\",\"params\":\"[\"\"13269236571\"\"]\",\"resContent\":\"{\"data\":\"YOUMIMA\",\"status\":200}\",\"time\":\"2018-09-26 11:12:19\"}\"\n"
  "[INFO ] [11:12:19] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.UserController.checkAutoMobile\",\"ip\":\"106.38.33.70\",\"logId\":\"185bf62665d441d4b7a68e67ca4b0cac\",\"logName\":\"请求结束\",\"params\":\"[\"\"13269236571\"\"]\",\"requestMap\":\"{mobile=[\"k2rV9Lm96jFeALhPykXrVA==\"]}\",\"sessionId\":\"61E4AE5FEC7C246F26FD6C3D2906E233\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:19\",\"type\":\"POST\",\"url\":\"https://dev.somur.com:8444/somur_api/user/checkAutoMobile.json\"}\n"
  "[INFO ] [11:12:24] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.UserController.login\",\"ip\":\"106.38.33.70\",\"logId\":\"ade32293ca324d96aab8468c77e33585\",\"logName\":\"请求开始\",\"params\":\"[\"\"13269236571\"\",\"\"e10adc3949ba59abbe56e057f20f883e\"\"]\",\"requestMap\":\"{password=[\"I9+ieWqd3tdkGNCpFp6WiKvtnQtGtgrBd6YdqNnZyqIEoBVogRfeLQ==\"], mobile=[\"k2rV9Lm96jFeALhPykXrVA==\"]}\",\"sessionId\":\"6B017B4B84142F45EA0A2AD88197E65B\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:24\",\"type\":\"POST\",\"url\":\"https://dev.somur.com:8444/somur_api/user/login.json\"}\n"
  "[INFO ] [11:12:24] com.somur.controller.UserController - #######login.json#####\n"
  "[INFO ] [11:12:24] com.somur.controller.UserController - #######mobile=#####13269236571\n"
  "[INFO ] [11:12:24] com.somur.controller.UserController - #######password=#####e10adc3949ba59abbe56e057f20f883e\n"
  "[INFO ] [11:12:24] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.service.impl.UserServiceImpl.login\",\"logId\":\"ade32293ca324d96aab8468c77e33585\",\"logName\":\"调用service方法开始\",\"params\":\"[\"\"13269236571\"\",\"\"e10adc3949ba59abbe56e057f20f883e\"\"]\",\"resContent\":\"\",\"time\":\"2018-09-26 11:12:24\"}\n"
  "[INFO ] [11:12:24] com.somur.aspect.SystemOperationLogs - \"{\"classAndMethod\":\"com.somur.service.impl.UserServiceImpl.login\",\"logId\":\"ade32293ca324d96aab8468c77e33585\",\"logName\":\"调用service方法结束\",\"params\":\"[\"\"13269236571\"\",\"\"e10adc3949ba59abbe56e057f20f883e\"\"]\",\"resContent\":\"{\"data\":{\"address\":\"\",\"age\":0,\"app_open_id\":\"oq_wo1bpquSMkkZ6qDQ6Dl2KTR_Y\",\"birthday\":\"1986-03-29\",\"company_id\":\"f6b2cb89348248348462ba2de3654356\",\"company_user_id\":0,\"company_user_name\":\"dev11609\",\"des\":\"bXkSIFxnuak=\",\"heal_corp_id\":16,\"hversion\":\"2.1\",\"icon\":\"http://somurappyun.oss-cn-beijing.aliyuncs.com/pics/icon/1537851154139/test.jpg\",\"isAgree\":0,\"is_star\":0,\"is_use_sample\":1,\"last_visit_time\":\"2018-09-25 12:52:34.0\",\"marital_status\":0,\"member_a_o_id\":0,\"member_id\":11609,\"mobile\":\"13269236571\",\"name\":\"刘佳佳\",\"nickname\":\"珍\",\"open_id\":\"oq_wo1bpquSMkkZ6qDQ6Dl2KTR_Y\",\"password\":\"123456\",\"real_card_no\":\"1234556789\",\"real_name\":\"刘佳102\",\"reserve_flag\":0,\"sample_id\":1,\"score\":0,\"sex\":2,\"state\":0,\"token\":\"e6b2db03cbb6e5057e3be81a686e1ae4.5987894\"},\"msg\":\"登陆成功!\",\"status\":200}\",\"time\":\"2018-09-26 11:12:24\"}\"\n"
  "[INFO ] [11:12:24] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.UserController.login\",\"ip\":\"106.38.33.70\",\"logId\":\"ade32293ca324d96aab8468c77e33585\",\"logName\":\"请求结束\",\"params\":\"[\"\"13269236571\"\",\"\"e10adc3949ba59abbe56e057f20f883e\"\"]\",\"requestMap\":\"{password=[\"I9+ieWqd3tdkGNCpFp6WiKvtnQtGtgrBd6YdqNnZyqIEoBVogRfeLQ==\"], mobile=[\"k2rV9Lm96jFeALhPykXrVA==\"]}\",\"sessionId\":\"6B017B4B84142F45EA0A2AD88197E65B\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:24\",\"type\":\"POST\",\"url\":\"https://dev.somur.com:8444/somur_api/user/login.json\"}\n"
  "[INFO ] [11:12:25] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.AppReportController.showServiceLoer\",\"ip\":\"106.38.33.70\",\"logId\":\"b754caf30a764be289b597bd113aee90\",\"logName\":\"请求开始\",\"params\":\"[\"11609\"]\",\"requestMap\":\"{member_id=[\"abAiScWbVxs=\"]}\",\"sessionId\":\"F1CC95F6980DECD9350570F900D95F4D\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:25\",\"type\":\"POST\",\"url\":\"https://dev.somur.com:8444/somur_api/app_report/showServiceLoer.json\"}\n"
  "[INFO ] [11:12:25] com.somur.aspect.SystemOperationLogs - {\"classAndMethod\":\"com.somur.controller.UserController.upVersion\",\"ip\":\"106.38.33.70\",\"logId\":\"bae3e606c92c49ff94a0af1a8d73445a\",\"logName\":\"请求开始\",\"params\":\"[\"\"11609\"\",\"\"1.6.4\"\"]\",\"requestMap\":\"{member_id=[\"abAiScWbVxs=\"], version=[\"WSE/De1p1Jo=\"]}\",\"sessionId\":\"3572E278B60773A5A88B7A799FF598A9\",\"sessionMap\":\"{}\",\"time\":\"2018-09-26 11:12:25\",\"type\":\"GET\",\"url\":\"https://dev.somur.com:8444/somur_api/user/upVersion.json\"}")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))