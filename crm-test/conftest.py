#codig:utf-8
import logging
import sys
import pytest

log=SelfLoggers(level=logging.INFO,className="conftest")

@pytest.fixture(scope="session")
def login(request):
    username=request.param["username"]
    password=request.param["password"]
    log.logger.info("用户名：%s,密码：%s"%(username,password))
