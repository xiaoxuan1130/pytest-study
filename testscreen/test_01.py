#codign:utf-8
from selenium import webdriver
import pytest
import time

@pytest.mark.webtest
def test_01(browser):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t=browser.title
    assert t=='上海悠悠'

def test_02(browser):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert '上海-悠悠' in t

if __name__ == '__main__':
    #pytest --html=report.html --self-contained-html
    pytest.main(["-m=webtest","--html=report.html"])