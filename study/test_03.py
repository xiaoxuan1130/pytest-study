#coding:utf-8
import pytest
#mark  pytest.ini文件中配置
@pytest.mark.webtest
def test_send_http():
    print("发送http请求")
    pass

class TestClass:
    def test_method(self):
        pass

if __name__ == '__main__':
    #pytest -s -v -m webtest
    pytest.main(["-s","test_03.py","-m=webtest"])

