#coding=utf8
import pytest
from logger import logger

@pytest.mark.webtest
def test_01():
    logger.info("测试用例1")

def test_02():
    logger.info("测试用例2")

if __name__ == '__main__':
    pytest.main(["-s","test_mark.py","-m=webtest1"])