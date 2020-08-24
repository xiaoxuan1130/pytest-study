#coding=utf8
import pytest
from logger import logger

test_data=[{"username":"test003","pwd":"epipe123"}]
@pytest.fixture(scope="module",autouse=False)
def login(request):
    username=request.param["username"]
    pwd=request.param["pwd"]
    logger.info("用户名为：%s,密码为:%s" % (username,pwd))
    return "1"

@pytest.fixture(scope="module",autouse=False)
def start(request):
    logger.info("---------------开始测试")
    logger.info("module     :%s" % request.module.__name__)
    username=test_data[0]["username"]
    pwd=test_data[0]["pwd"]
    logger.info("用户名为：%s,密码为:%s" % (username, pwd))
    yield("haha")
    logger.info("---------------结束测试")

