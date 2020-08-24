#codig:utf-8
import logging
import sys
import pytest
import requests,json,re

from testcrm.logger.Loggers import Loggers

log=Loggers(level=logging.INFO,className="conftest")
s=requests.session()

def getSessionId():
    url="http://192.168.3.171:8182/ucloud-crm/a/login"
    r=s.get(url)
    status=r.status_code
    # headers=r.headers
    # reg="[A-Za-z0-9]{32}"
    # pattern = re.compile(reg)  # 用于匹配至少一个数字
    # m=pattern.match(headers)
    return r.cookies


@pytest.fixture(scope="session")
def login(request):
    cookies=getSessionId()
    username=request.param["username"]
    password=request.param["password"]
    log.logger.info("用户名：%s,密码：%s"%(username,password))
    payload={"username":username,"password":password}
    url="http://192.168.3.171:8182/ucloud-crm/a/login"
    r=s.post(url,payload)
    status=r.status_code
    return s