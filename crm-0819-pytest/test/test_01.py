#coding=utf8
import pytest
from logger import logger

# test_data=[{"username":"xiaoxuan003","pwd":"epipe123"}]
# @pytest.mark.parametrize("login",test_data,indirect=True)
# def test_getList(login):
#     logger.info("获取列表请求"+login)


def test_getList_01(start):
    logger.info("获取请求列表2"+start)

def test_getList_02(start):
    logger.info("获取请求列表3"+start)

if __name__ == '__main__':
    pytest.main(["-s","test_01.py"])

